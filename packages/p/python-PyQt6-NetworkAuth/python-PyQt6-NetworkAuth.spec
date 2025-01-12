#
# spec file for package python-PyQt6-NetworkAuth
#
# Copyright (c) 2025 SUSE LLC
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


%define qtlib NetworkAuth
%define pyqt_build_for_qt6 1
%define plainpython python
%{?sle15_python_module_pythons}
Name:           python-PyQt6-%{qtlib}
Version:        6.8.0
Release:        0
Summary:        Python bindings for the Qt Network Authorization library
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqtnetworkauth
Source:         https://files.pythonhosted.org/packages/source/P/PyQt6-%{qtlib}/PyQt6_%{qtlib}-%{version}.tar.gz
BuildRequires:  %{python_module PyQt6-devel >= 6.2}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyqt-builder >= 1.17 with %python-pyqt-builder < 2}
BuildRequires:  %{python_module sip-devel >= 6.9 with %python-sip-devel < 7}
BuildRequires:  fdupes
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  cmake(Qt6%{qtlib})
Requires:       python-PyQt6 >= %(rpm -q --whatprovides python-PyQt6 --qf "%%{version}")
Requires:       python-PyQt6-sip >= %(rpm -q --whatprovides python-PyQt6-sip --qf "%%{version}")
Provides:       python-qtnetworkauth-qt6 = %{version}-%{release}
%python_subpackages

%description
PyQt6-NetworkAuth is a set of Python bindings for The Qt Company's Qt Network
Authorisation library. The bindings sit on top of PyQt6 and are implemented as
a single module.

%package devel
Summary:        Devel files for %{name}
Group:          Development/Tools/IDE
Requires:       python-PyQt6-devel
Requires:       %plainpython(abi) = %{python_version}
Supplements:    (eric and python-PyQt6-%{qtlib})
Supplements:    (python-PyQt6-devel and python-PyQt6-%{qtlib})

%description devel
This package provides Qt6 API files for the Eric IDE and the SIP files
used to generate the Python bindings for %{name}

%prep
%autosetup -p1 -n PyQt6_%{qtlib}-%{version}

%build
%pyqt_build

%install
%pyqt_install

%check
export PYTHONDONTWRITEBYTECODE=1 # boo#1047218
%{python_expand # there is no test suite. If it compiles and imports, it should be okay.
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c 'from PyQt6 import Qt%{qtlib}; assert Qt%{qtlib}.PYQT_NETWORKAUTH_VERSION_STR == "%{version}"'
}

%files %{python_files}
%license LICENSE
%doc NEWS README.md
%dir %{python_sitearch}/PyQt6/
%{python_sitearch}/PyQt6/Qt%{qtlib}.*
%{python_sitearch}/PyQt6_%{qtlib}-%{version}.dist-info/
%exclude %{pyqt6_sipdir}

%files %{python_files devel}
%license LICENSE
%dir %{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/
%{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/PyQt6-%{qtlib}.api
%dir %{pyqt6_sipdir}
%{pyqt6_sipdir}/Qt%{qtlib}/

%changelog
