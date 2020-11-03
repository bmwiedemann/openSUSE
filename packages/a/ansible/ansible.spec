#
# spec file for package ansible
#
# Copyright (c) 2020 SUSE LLC
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


%global __brp_mangle_shebangs_exclude_from %{_prefix}/lib/python[0-9]+\.[0-9]+/site-packages/ansible_test/_data/.*
%if 0%{?rhel} || 0%{?fedora}
# RHEL and Fedora add -s to the shebang line.  We do *not* use -s -E -S or -I
# with ansible because it has many optional features which users need to
# install libraries on their own to use.  For instance, paramiko for the
# network connection plugins or winrm to talk to windows hosts.
# Set this to nil to remove -s
%define py_shbang_opts %{nil}
%define py2_shbang_opts %{nil}
%define py3_shbang_opts %{nil}
%endif
# While Windows Powershell meanwhile exists, it is not in Factory/Leap for now.
# So let's exclude /usr/bin/pwsh from the dependencies
%define __requires_exclude ^%{_bindir}/pwsh$
# Python 2 or Python 3?
%if 0%{?suse_version} >= 1315
%bcond_without  python3
%else
%bcond_with     python3
%endif
# Disable/Enable tests only on newer distributions, which have the
# needed dependencies.
%define with_tests 0
#
# Fedora
#
%if 0%{?fedora} >= 18
%global         with_python2 0
%global         with_python3 1
%define         __python python2
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-straight-plugin
Requires:       PyYAML
Requires:       python-httplib2
Requires:       python-jinja2
Requires:       python-keyczar
Requires:       python-paramiko
Requires:       python-setuptools
Requires:       python-six
Requires:       sshpass
# Bundled provides
Provides:       bundled(python-backports-ssl_match_hostname) = 3.7.0.1
Provides:       bundled(python-distro) = 1.4.0
Provides:       bundled(python-ipaddress) = 1.0.22
Provides:       bundled(python-selectors2) = 1.1.1
Provides:       bundled(python-six) = 1.12.0
%endif
#
# RHEL
#
%if 0%{?rhel}
%if 0%{?rhel} >= 8
%global         with_python2 0
%global         with_python3 1
BuildRequires:  %{py3_dist coverage}
BuildRequires:  git-core
BuildRequires:  python3-PyYAML
BuildRequires:  python3-cryptography
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-jinja2
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-systemd
Requires:       python3-PyYAML
Requires:       python3-cryptography
Requires:       python3-jinja2
Requires:       python3-six
Requires:       sshpass
%else
%if 0%{?rhel} >= 7
%global         with_python2 1
%global         with_python3 0
BuildRequires:  PyYAML
BuildRequires:  git
BuildRequires:  pytest
BuildRequires:  python-boto3
BuildRequires:  python-coverage
BuildRequires:  python-jinja2
BuildRequires:  python-jmespath
BuildRequires:  python-mock
BuildRequires:  python-paramiko
BuildRequires:  python-passlib
BuildRequires:  python-requests
BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  python-sphinx
BuildRequires:  python2-cryptography
BuildRequires:  python2-devel
Requires:       PyYAML
Requires:       python-jinja2
Requires:       python-paramiko
Requires:       python-six
Requires:       python2-cryptography
Requires:       sshpass
# end of Requires for RHEL 7
%endif
# end of Requires for RHEL 8
%endif
# Bundled provides
Provides:       bundled(python-backports-ssl_match_hostname) = 3.7.0.1
Provides:       bundled(python-distro) = 1.4.0
Provides:       bundled(python-ipaddress) = 1.0.22
Provides:       bundled(python-selectors2) = 1.1.1
Provides:       bundled(python-six) = 1.12.0
%endif
%if %{with python3}
%define __python python3
%define python python3
%else
%define python python
%endif
#
# SUSE/openSUSE
#
%if 0%{?suse_version}
# Enable WinRM (Run tasks over Microsoft's WinRM)
# by setting the following definition to 1
%define with_winrm 0
# Enable Gitlab support (runner, project, hook, deploy)
# by setting this definition to 1
%define with_gitlab 0
# openSUSE has currently not good enough python3 sphinx (sub-)packages
# disable building extensive docs per default:
%define with_docs 0
# Distribution version dependend stuff
%if 0%{?suse_version} >= 1500
# Enable VMWare support for newer openSUSE distributions here
# otherwise disable this by setting the value below to 0
%define with_vmware 1
# Enable Amazon EC2 support (modules) dependencies
# by setting the following definition to 1
%define with_amazon 1
%else
%define with_amazon 0
%define with_vmware 0
%define with_tests  0
%endif
%if ! %{with python3}
Requires:       %{python}-xml
%endif
%if 0%{?with_amazon}
BuildRequires:  %{python}-boto3
BuildRequires:  %{python}-botocore
%endif
%if 0%{?with_gitlab}
BuildRequires:  %{python}-gitlab
BuildRequires:  %{python}-httmock
Recommends:     %{python}-gitlab
Recommends:     %{python}-httmock
%endif
%if 0%{?with_tests}
BuildRequires:  %{python}-pbkdf2
BuildRequires:  %{python}-pytest
BuildRequires:  %{python}-python-memcached
BuildRequires:  %{python}-redis
BuildRequires:  %{python}-requests
%endif
%if 0%{?with_vmware}
BuildRequires:  %{python}-pyvmomi
Recommends:     %{python}-pyvmomi
%endif
%if 0%{?with_winrm}
BuildRequires:  %{python}-pexpect
BuildRequires:  %{python}-pywinrm
Recommends:     %{python}-pywinrm
%endif
BuildRequires:  %{python}-Jinja2
BuildRequires:  %{python}-PyYAML
BuildRequires:  %{python}-coverage
BuildRequires:  %{python}-devel
BuildRequires:  %{python}-jmespath
BuildRequires:  %{python}-paramiko
BuildRequires:  %{python}-pycrypto >= 2.6
BuildRequires:  %{python}-setuptools > 0.6
BuildRequires:  %{python}-straight-plugin
BuildRequires:  fdupes
Requires:       %{python}-Jinja2
Requires:       %{python}-PyYAML
Requires:       %{python}-coverage
Requires:       %{python}-jmespath
Requires:       %{python}-paramiko
Requires:       %{python}-passlib
Requires:       %{python}-pycrypto >= 2.6
Requires:       %{python}-setuptools > 0.6
Recommends:     %{python}-boto3
Recommends:     %{python}-botocore
Recommends:     %{python}-dnspython
Recommends:     %{python}-dopy
Recommends:     %{python}-httplib2
Recommends:     %{python}-keyczar
Recommends:     %{python}-pbkdf2
Recommends:     %{python}-python-memcached
Recommends:     %{python}-pywinrm
Recommends:     %{python}-redis
Recommends:     %{python}-requests
Recommends:     %{python}-six
Recommends:     sshpass
%endif
Name:           ansible
Version:        2.9.15
Release:        0
Summary:        SSH-based configuration management, deployment, and task execution system
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://ansible.com/
Source:         https://releases.ansible.com/ansible/ansible-%{version}.tar.gz
Source1:        https://releases.ansible.com/ansible/ansible-%{version}.tar.gz.sha
Source99:       ansible-rpmlintrc
BuildArch:      noarch
# extented documentation
%if 0%{?with_docs}
BuildRequires:  asciidoc
BuildRequires:  python-sphinx
BuildRequires:  python-sphinx-notfound-page
BuildRequires:  python-sphinx-theme-alabaster
%endif

%description
Ansible is a radically simple model-driven configuration management, multi-node
deployment, and remote task execution system. Ansible works over SSH and does
not require any software or daemons to be installed on remote nodes. Extension
modules can be written in any language and are transferred to managed machines
automatically.

%package doc
Summary:        Documentation for Ansible
Recommends:     %{name} = %{version}

%description doc
This package contains extensive documentation for ansible.

Ansible is a radically simple model-driven configuration management, multi-node
deployment, and remote task execution system. Ansible works over SSH and does
not require any software or daemons to be installed on remote nodes. Extension
modules can be written in any language and are transferred to managed machines
automatically.

%package test
Summary:        Tool for testing ansible plugin and module code
Requires:       %{name} = %{version}
#
# RHEL
#
%if 0%{?rhel} >= 7
BuildRequires:  python-virtualenv
Requires:       python-virtualenv
%endif
#
# SUSE/openSUSE
#
%if 0%{?suse_version} >= 1500
BuildRequires:  %{python}-virtualenv
Requires:       %{python}-virtualenv
%endif

%description test
This package installs the ansible-test command for testing modules and plugins
developed for ansible.

Ansible is a radically simple model-driven configuration management, multi-node
deployment, and remote task execution system. Ansible works over SSH and does
not require any software or daemons to be installed on remote nodes. Extension
modules can be written in any language and are transferred to managed machines
automatically.

%prep
%setup -q -n ansible-%{version}

for file in .git_keep .travis.yml ; do
  find . -name "$file" -delete
done
find contrib/ -type f -exec chmod 644 {} +

# Replace all #!/usr/bin/env lines to use #!/usr/bin/$1 directly.
find ./ -type f -exec \
    sed -i '1s|^#!%{_bindir}/env |#!%{_bindir}/|' {} \;

%build
%{python} setup.py build
%if 0%{?with_docs}
  %make_build PYTHON=%{_bindir}/%{python} SPHINXBUILD=sphinx-build webdocs
%else
  %make_build PYTHON=%{_bindir}/%{python} -Cdocs/docsite config cli keywords modules plugins testing
%endif

%install
%{python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/ansible/
cp examples/hosts %{buildroot}%{_sysconfdir}/ansible/
cp examples/ansible.cfg %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_datadir}/ansible
%if 0%{?suse_version} >= 01130
%fdupes %{buildroot}/%{python_sitelib}/ansible/
%endif

# Create system directories that Ansible defines as default locations in
# ansible/config/base.yml
DATADIR_LOCATIONS='%{_datadir}/ansible/collections
%{_datadir}/ansible/plugins/doc_fragments
%{_datadir}/ansible/plugins/action
%{_datadir}/ansible/plugins/become
%{_datadir}/ansible/plugins/cache
%{_datadir}/ansible/plugins/callback
%{_datadir}/ansible/plugins/cliconf
%{_datadir}/ansible/plugins/connection
%{_datadir}/ansible/plugins/filter
%{_datadir}/ansible/plugins/httpapi
%{_datadir}/ansible/plugins/inventory
%{_datadir}/ansible/plugins/lookup
%{_datadir}/ansible/plugins/modules
%{_datadir}/ansible/plugins/module_utils
%{_datadir}/ansible/plugins/netconf
%{_datadir}/ansible/roles
%{_datadir}/ansible/plugins/strategy
%{_datadir}/ansible/plugins/terminal
%{_datadir}/ansible/plugins/test
%{_datadir}/ansible/plugins/vars'

UPSTREAM_DATADIR_LOCATIONS=$(grep -ri default lib/ansible/config/base.yml| tr ':' '\n' | grep '%{_datadir}/ansible')

if [ "$SYSTEM_LOCATIONS" != "$UPSTREAM_SYSTEM_LOCATIONS" ] ; then
    echo "The upstream Ansible datadir locations have changed.  Spec file needs to be updated"
    exit 1
fi

mkdir -p %{buildroot}%{_datadir}/ansible/plugins/
for location in $DATADIR_LOCATIONS ; do
    mkdir %{buildroot}"$location"
done
mkdir -p %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}%{_sysconfdir}/ansible/roles/
# fix for https://github.com/ansible/ansible/pull/24381
# resp. https://bugzilla.opensuse.org/show_bug.cgi?id=1137479
mkdir -p %{buildroot}%{python3_sitelib}/ansible/galaxy/data/default/role/{files,templates}

cp examples/hosts %{buildroot}%{_sysconfdir}/ansible/
cp examples/ansible.cfg %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/

cp -pr docs/docsite/rst .
%if 0%{?with_docs}
  cp -pr docs/docsite/_build/html %{_builddir}/%{name}-%{version}/html
%endif

%if 0%{?with_tests} &&  0%{with python3}
%check
python3 bin/ansible-test units -v --python %{python3_version}
%endif


%files
%license COPYING
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
%exclude %{python3_sitelib}/ansible_test
%else
%{python_sitelib}/*
%exclude %{python_sitelib}/ansible_test
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
%{_datadir}/ansible/

%files doc
%doc changelogs contrib examples rst
%if 0%{?with_docs}
%doc html
%endif

%files test
%{_bindir}/ansible-test
%if %{with python3}
%{python3_sitelib}/ansible_test
%attr(0755,root,root) %{python3_sitelib}/ansible_test/_data/injector/*.sh
%attr(0755,root,root) %{python3_sitelib}/ansible_test/_data/setup/*.sh
%else
%{python2_sitelib}/ansible_test
%attr(0755,root,root) %{python2_sitelib}/ansible_test/_data/injector/*.sh
%attr(0755,root,root) %{python2_sitelib}/ansible_test/_data/setup/*.sh
%endif

%changelog
