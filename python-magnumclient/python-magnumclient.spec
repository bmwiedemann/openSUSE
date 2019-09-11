#
# spec file for package python-magnumclient
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


Name:           python-magnumclient
Version:        2.12.0
Release:        0
Summary:        Python API and CLI for OpenStack Magnum
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-magnumclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-magnumclient/python-magnumclient-2.12.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PrettyTable >= 0.7.2
BuildRequires:  python2-cryptography >= 2.1
BuildRequires:  python2-decorator >= 3.4.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-keystoneauth1 >= 3.4.0
BuildRequires:  python2-mock
BuildRequires:  python2-openstackclient
BuildRequires:  python2-os-client-config >= 1.28.0
BuildRequires:  python2-osc-lib >= 1.8.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-osprofiler
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-cryptography >= 2.1
BuildRequires:  python3-decorator >= 3.4.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-mock
BuildRequires:  python3-openstackclient
BuildRequires:  python3-os-client-config >= 1.28.0
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-osprofiler
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-cryptography >= 2.1
Requires:       python-decorator >= 3.4.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-os-client-config >= 1.28.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
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
Client library for Magnum built on the Magnum API. It provides a Python API
(the magnumclient module) and a command-line tool (magnum).

%package -n python-magnumclient-doc
Summary:        Documentation for OpenStack Magnum API client libary
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-magnumclient-doc
Client library for Magnum built on the Magnum API. It provides a Python API
(the magnumclient module) and a command-line tool (magnum).
This package contains the documentation.

%prep
%autosetup -p1 -n python-magnumclient-2.12.0
%py_req_cleanup

%build
%{python_build}

# Build HTML docs and man page
PBR_VERSION=2.12.0 sphinx-build -b html doc/source doc/build/html
PBR_VERSION=2.12.0 sphinx-build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
# man page
install -p -D -m 644 doc/build/man/python-magnumclient.1 %{buildroot}%{_mandir}/man1/magnum.1
# Install bash completion
install -p -D -m 644 tools/magnum.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/magnum.bash_completion
%python_clone -a %{buildroot}%{_bindir}/magnum
%python_clone -a %{buildroot}%{_mandir}/man1/magnum.1
%python_clone -a %{buildroot}%{_sysconfdir}/bash_completion.d/magnum.bash_completion

%post
%{python_install_alternative magnum magnum.1 %{_sysconfdir}/bash_completion.d/magnum.bash_completion}

%postun
%python_uninstall_alternative magnum

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%{python_sitelib}/magnumclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/magnum
%python_alternative %{_mandir}/man1/magnum.1
%python_alternative %{_sysconfdir}/bash_completion.d/magnum.bash_completion

%files -n python-magnumclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
