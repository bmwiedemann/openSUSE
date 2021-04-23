#
# spec file for package python-masakariclient
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


%global oldpython python
Name:           python-masakariclient
Version:        6.1.1
Release:        0
Summary:        Python API and CLI for OpenStack Masakari
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-masakariclient/python-masakariclient-6.1.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable
BuildRequires:  python3-ddt
BuildRequires:  python3-openstacksdk >= 0.13.0
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils
BuildRequires:  python3-oslotest
BuildRequires:  python3-python-subunit
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).

%package -n python3-masakariclient
Summary:        Python API and CLI for OpenStack Masakari
Group:          Development/Languages/Python
Requires:       python3-openstacksdk >= 0.13.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils
Requires:       python3-pbr >= 2.0.0
Conflicts:      %oldpython-masakariclient < %version

%description -n python3-masakariclient
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).

This package contains the Python 3.x module.

%package -n python-masakariclient-doc
Summary:        Documentation for OpenStack Masakari API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
%if 0%{?suse_version}
Obsoletes:      %oldpython-masakariclient < %version
%endif

%description -n python-masakariclient-doc
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).
This package contains the documentation.

%prep
%autosetup -p1 -n python-masakariclient-%{version}
%py_req_cleanup

%build
%{py3_build}

# Build HTML docs and man page
PBR_VERSION=6.1.1 %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=6.1.1 %sphinx_build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}
# man pages
install -p -D -m 644 doc/build/man/python-masakariclient.1 %{buildroot}%{_mandir}/man1/python-masakariclient.1

%check
python3 -m stestr.cli run

%files -n python3-masakariclient
%license LICENSE
%{python3_sitelib}/masakariclient
%{python3_sitelib}/*.egg-info
%{_bindir}/masakari

%files -n python-masakariclient-doc
%license LICENSE
%doc doc/build/html
%{_mandir}/man1/python-masakariclient.1.*

%changelog
