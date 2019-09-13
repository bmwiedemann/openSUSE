#
# spec file for package ansible
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2013 by Lars Vogdt
# Copyright 2014 by Boris Manojlovic
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%if 0%{?suse_version} && 0%{?suse_version} >= 1500
%bcond_without python3
%else
%bcond_with    python3
%endif
%if %{with python3}
%define __python %{__python3}
%define python python3
%else
%define python python
%endif

%if 0%{?suse_version} && 0%{?suse_version} <= 1110 || 0%{?rhel} == 5
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif
Name:           ansible
Version:        2.8.3
Release:        0
Summary:        Software automation engine
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://ansible.com/
Source:         https://releases.ansible.com/ansible/ansible-%{version}.tar.gz
Source99:       ansible-rpmlintrc
# SuSE/openSuSE
%if 0%{?suse_version}
%if %{with python3}
BuildRequires:  python3-devel >= 3.5
%else
BuildRequires:  python-devel
%endif
BuildRequires:  %{python}-setuptools
Recommends:     %{python}-dnspython
Recommends:     %{python}-dopy
Recommends:     %{python}-pywinrm
Recommends:     sshpass
Recommends:     %{python}-httplib2
Recommends:     %{python}-keyczar
Recommends:     %{python}-six
Requires:       %{python}-setuptools
%if 0%{?suse_version} >= 01130
BuildRequires:  %{python}-Jinja2
BuildRequires:  %{python}-PyYAML
BuildRequires:  %{python}-paramiko
BuildRequires:  %{python}-pycrypto >= 2.6
BuildRequires:  fdupes
Requires:       %{python}-Jinja2
Requires:       %{python}-PyYAML
Requires:       %{python}-paramiko
Requires:       %{python}-passlib
Requires:       %{python}-pycrypto >= 2.6
%else
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
%endif
# RHEL <=5
%if 0%{?rhel} && 0%{?rhel} <= 5
BuildRequires:  python26-devel
BuildRequires:  python26-setuptools
Requires:       python26-PyYAML
Requires:       python26-httplib2
Requires:       python26-jinja2
Requires:       python26-keyczar
Requires:       python26-paramiko
Requires:       python26-setuptools
Requires:       python26-six
Requires:       sshpass
%endif
# RHEL > 5
%if 0%{?rhel} && 0%{?rhel} >= 5
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
Requires:       PyYAML
Requires:       python-jinja2
Requires:       python-paramiko
Requires:       python-setuptools
Requires:       python-six
Requires:       sshpass
%endif
# RHEL == 6
%if 0%{?rhel} == 6
Requires:       python-crypto
%endif
# RHEL >=7
%if 0%{?rhel} >= 7
Requires:       python2-cryptography
BuildRequires:  perl(Exporter)
%endif
%if 0%{?fedora} >= 18
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       PyYAML
Requires:       python-httplib2
Requires:       python-jinja2
Requires:       python-keyczar
Requires:       python-paramiko
Requires:       python-setuptools
Requires:       python-six
Requires:       sshpass
%define         __python %{__python2}
%endif

%description
Ansible is an IT automation system. It handles
configuration-management, application deployment, cloud provisioning, ad-hoc
task-execution, and multinode orchestration - including trivializing things
like zero downtime rolling updates with load balancers.

%prep
%setup -q -n ansible-%{version}
find . -name .git_keep -delete
find contrib/ -type f -exec chmod 644 {} +

%build
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/ansible/
cp examples/hosts %{buildroot}%{_sysconfdir}/ansible/
cp examples/ansible.cfg %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_datadir}/ansible
%if 0%{?suse_version} >= 01130
%fdupes %{buildroot}/%{python_sitelib}/ansible/
%endif

%files
%defattr(-,root,root,-)
%if 0%{?suse_version} >= 1200
%license COPYING
%else
%doc COPYING
%endif
%doc *.rst contrib examples changelogs
%{_bindir}/ansible
%{_bindir}/ansible-config
%{_bindir}/ansible-connection
%{_bindir}/ansible-console
%{_bindir}/ansible-doc
%{_bindir}/ansible-galaxy
%{_bindir}/ansible-inventory
%{_bindir}/ansible-playbook
%{_bindir}/ansible-pull
%{_bindir}/ansible-vault
%if %{with python3}
%{python3_sitelib}/*
%else
%{python_sitelib}/*
%endif
%{_mandir}/man1/ansible.1%{?ext_man}*
%{_mandir}/man1/ansible-config.1%{?ext_man}*
%{_mandir}/man1/ansible-console.1%{?ext_man}*
%{_mandir}/man1/ansible-doc.1%{?ext_man}*
%{_mandir}/man1/ansible-galaxy.1%{?ext_man}*
%{_mandir}/man1/ansible-inventory.1%{?ext_man}*
%{_mandir}/man1/ansible-playbook.1%{?ext_man}*
%{_mandir}/man1/ansible-pull.1%{?ext_man}*
%{_mandir}/man1/ansible-vault.1%{?ext_man}*
%dir %{_sysconfdir}/ansible
%config(noreplace) %{_sysconfdir}/ansible/ansible.cfg
%config(noreplace) %{_sysconfdir}/ansible/hosts

%changelog
