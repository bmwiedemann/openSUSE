#
# spec file for package python-oslo.rootwrap
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


Name:           python-oslo.rootwrap
Version:        6.2.0
Release:        0
Summary:        Filtering shell commands to run as root from OpenStack services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.rootwrap
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.rootwrap/oslo.rootwrap-6.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-eventlet
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  iproute2
%else
BuildRequires:  iproute
%endif

%description
oslo.rootwrap allows fine-grained filtering of shell commands to run as root
from OpenStack services.

%package -n python3-oslo.rootwrap
Summary:        Filtering shell commands to run as root from OpenStack services
Group:          Development/Languages/Python
Requires:       python3-six >= 1.10.0
%if 0%{?suse_version}
Obsoletes:      python2-oslo.rootwrap < 6.0.1
%endif

%description -n python3-oslo.rootwrap
oslo.rootwrap allows fine-grained filtering of shell commands to run as root
from OpenStack services.

This package contains the Python 3.x module.

%package -n python-oslo.rootwrap-doc
Summary:        Documentation for OpenStack oslo.rootwrap
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.rootwrap-doc
Documentation for the OpenStack oslo.rootwrap library.

%prep
%autosetup -p1 -n oslo.rootwrap-6.2.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=6.2.0 %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
export PYTHONPATH=.
python3 -m stestr.cli run

%files -n python3-oslo.rootwrap
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/oslo_rootwrap
%{python3_sitelib}/*.egg-info
%{_bindir}/oslo-rootwrap
%{_bindir}/oslo-rootwrap-daemon

%files -n python-oslo.rootwrap-doc
%license LICENSE
%doc doc/build/html

%changelog
