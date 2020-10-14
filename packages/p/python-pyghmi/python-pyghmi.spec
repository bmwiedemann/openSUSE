#
# spec file for package python-pyghmi
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


Name:           python-pyghmi
Version:        1.5.18
Release:        0
Summary:        General Hardware Management Initiative (IPMI and others)
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/pyghmi
Source0:        https://files.pythonhosted.org/packages/source/p/pyghmi/pyghmi-1.5.18.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-cryptography >= 2.1
BuildRequires:  python3-devel
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslotest
BuildRequires:  python3-python-dateutil >= 2.8.1
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
This is a pure python implementation of IPMI protocol.

pyghmicons and pyghmiutil are example scripts to show how one may incorporate
this library into python code

%package -n python3-pyghmi
Summary:        General Hardware Management Initiative (IPMI and others)
Group:          Development/Languages/Python
Requires:       python3-cryptography >= 2.1
Requires:       python3-python-dateutil >= 2.8.1
Requires:       python3-six >= 1.10.0
%if 0%{?suse_version}
Obsoletes:      python2-pyghmi < 1.6.0
%endif

%description -n python3-pyghmi
This is a pure python implementation of IPMI protocol.

pyghmicons and pyghmiutil are example scripts to show how one may incorporate
this library into python code

This package contains the Python 3.x module.

%package -n python-pyghmi-doc
Summary:        General Hardware Management Initiative (IPMI and others) -- Documentation
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx

%description -n python-pyghmi-doc
This is a pure python implementation of IPMI protocol.

pyghmicons and pyghmiutil are example scripts to show how one may incorporate
this library into python code

%prep
%autosetup -p1 -n pyghmi-%{version}
%py_req_cleanup

%build
%{py3_build}
PYTHONPATH=. PBR_VERSION=1.5.18 %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-pyghmi
%doc README.md ChangeLog
%license LICENSE
%{_bindir}/pyghmicons
%{_bindir}/pyghmiutil
%{_bindir}/virshbmc
%{_bindir}/fakebmc
%{python3_sitelib}/pyghmi*
%{python3_sitelib}/*.egg-info

%files -n python-pyghmi-doc
%doc doc/build/html
%license LICENSE

%changelog
