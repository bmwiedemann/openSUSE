#
# spec file for package python-freezerclient
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


Name:           python-freezerclient
Version:        4.0.0
Release:        0
Summary:        Python API and CLI for OpenStack Freezer
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-freezerclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-freezerclient/python-freezerclient-4.0.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.serialization >= 2.25.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Client library for Freezer built on the Freezer API. It provides a Python API
(the freezerclient module) and a command-line tool (freezer).

%package -n python3-freezerclient
Summary:        Python API and CLI for OpenStack Freezer
Group:          Development/Languages/Python
Requires:       python3-cliff >= 2.8.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-oslo.serialization >= 2.25.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-six
%if 0%{?suse_version}
Obsoletes:      python2-freezerclient < 3.0.0
%endif

%description -n python3-freezerclient
Client library for Freezer built on the Freezer API. It provides a Python API
(the freezerclient module) and a command-line tool (freezer).

This package contains the Python 3.x module.

%package -n python-freezerclient-doc
Summary:        Documentation for OpenStack Freezer API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-freezerclient-doc
Client library for Freezer built on the Freezer API. It provides a Python API
(the freezerclient module) and a command-line tool (freezer).
This package contains the documentation.

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%{py3_build}

# Build HTML docs and man page
PBR_VERSION=4.0.0 %sphinx_build -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-freezerclient
%doc README.rst
%license LICENSE
%{python3_sitelib}/freezerclient
%{python3_sitelib}/*.egg-info
%{_bindir}/freezer

%files -n python-freezerclient-doc
%doc doc/build/html
%license LICENSE

%changelog
