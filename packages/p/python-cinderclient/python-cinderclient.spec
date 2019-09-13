#
# spec file for package python-cinderclient
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-cinderclient
Version:        4.2.0
Release:        0
Summary:        Python API and CLI for OpenStack Cinder
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-cinderclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-cinderclient/python-cinderclient-4.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PrettyTable >= 0.7.1
BuildRequires:  python2-ddt
BuildRequires:  python2-fixtures
BuildRequires:  python2-keystoneauth1 >= 3.4.0
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.serialization
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-requests >= 2.14.2
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PrettyTable >= 0.7.1
BuildRequires:  python3-ddt
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.serialization
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.1
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-simplejson >= 3.5.1
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
This is a client for the OpenStack Cinder API (Block Storage. There's a
Python API (the cinderclient module), and a command-line script (cinder).
Each implements 100% of the OpenStack Cinder API.

%package -n python-cinderclient-doc
Summary:        Documentation for OpenStack Cinder API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

%description -n python-cinderclient-doc
This is a client for the OpenStack Cinder API (Block Storage. There's a
Python API (the cinderclient module), and a command-line script (cinder).
Each implements 100% of the OpenStack Cinder API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-cinderclient-4.2.0
%py_req_cleanup

%build
%{python_build}

PBR_VERSION=4.2.0 sphinx-build -b html doc/source doc/build/html
PBR_VERSION=4.2.0 sphinx-build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
# man page
install -p -D -m 644 doc/build/man/cinder.1 %{buildroot}%{_mandir}/man1/cinder.1
# bash completion
install -p -D -m 644 tools/cinder.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/cinder.bash_completion
%python_clone -a %{buildroot}%{_bindir}/cinder
%python_clone -a %{buildroot}%{_mandir}/man1/cinder.1
%python_clone -a %{buildroot}%{_sysconfdir}/bash_completion.d/cinder.bash_completion

%post
%{python_install_alternative cinder cinder.1 %{_sysconfdir}/bash_completion.d/cinder.bash_completion}

%postun
%python_uninstall_alternative cinder

%check
rm cinderclient/tests/unit/test_shell.py
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/cinderclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/cinder
%python_alternative %{_mandir}/man1/cinder.1
%python_alternative %{_sysconfdir}/bash_completion.d/cinder.bash_completion

%files -n python-cinderclient-doc
%license LICENSE
%doc doc/build/html

%changelog
