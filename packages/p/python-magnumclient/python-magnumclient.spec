#
# spec file for package python-magnumclient
#
# Copyright (c) 2024 SUSE LLC
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
Version:        4.5.0
Release:        0
Summary:        Python API and CLI for OpenStack Magnum
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-magnumclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-magnumclient/python-magnumclient-4.5.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-cryptography >= 3.0
BuildRequires:  python3-decorator >= 3.4.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.4.0
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
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Client library for Magnum built on the Magnum API. It provides a Python API
(the magnumclient module) and a command-line tool (magnum).

%package -n python3-magnumclient
Summary:        Python API and CLI for OpenStack Magnum
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-cryptography >= 3.0
Requires:       python3-decorator >= 3.4.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-os-client-config >= 1.28.0
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-stevedore >= 1.20.0
%if 0%{?suse_version}
Obsoletes:      python2-magnumclient < 2.17.0
%endif

%description -n python3-magnumclient
Client library for Magnum built on the Magnum API. It provides a Python API
(the magnumclient module) and a command-line tool (magnum).

This package contains the Python 3.x module.

%package -n python-magnumclient-doc
Summary:        Documentation for OpenStack Magnum API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-magnumclient-doc
Client library for Magnum built on the Magnum API. It provides a Python API
(the magnumclient module) and a command-line tool (magnum).
This package contains the documentation.

%prep
%autosetup -p1 -n python-magnumclient-4.5.0
%py_req_cleanup

%build
%{py3_build}

# Build HTML docs and man page
PBR_VERSION=4.5.0 %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=4.5.0 %sphinx_build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}
# man page
install -p -D -m 644 doc/build/man/python-magnumclient.1 %{buildroot}%{_mandir}/man1/magnum.1
# Install bash completion
install -p -D -m 644 tools/magnum.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/magnum.bash_completion

%check
%{openstack_stestr_run}

%files -n python3-magnumclient
%license LICENSE
%{python3_sitelib}/magnumclient
%{python3_sitelib}/*.egg-info
%{_bindir}/magnum
%{_mandir}/man1/magnum.1.*
%{_sysconfdir}/bash_completion.d/magnum.bash_completion

%files -n python-magnumclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
