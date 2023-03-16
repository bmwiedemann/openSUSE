#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define qtlib DataVisualization
%define mname PyQt6-%{qtlib}
%define pyqt_build_for_qt6 1
%define plainpython python
Name:           python-%{mname}
Version:        6.4.0
Release:        0
Summary:        Python bindings for the Qt Data Visualization library
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqtdatavisualization
Source:         https://files.pythonhosted.org/packages/source/P/%{mname}/PyQt6_%{qtlib}-%{version}.tar.gz
Patch0:         support-python3.6.patch
BuildRequires:  %{python_module PyQt6-devel >= 6.2}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module pyqt-builder >= 1.10}
BuildRequires:  %{python_module sip-devel >= 6}
BuildRequires:  fdupes
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  cmake(Qt6%{qtlib})
%requires_ge    python-PyQt6
Provides:       python-qtdatavisualization-qt6 = %{version}-%{release}
%python_subpackages

%description
%{mname} is a set of Python bindings for The Qt Company’s Qt %{qtlib} framework.
The bindings sit on top of PyQt6 and are implemented as a single module.

%package devel
Summary:        Devel files for %{name}
Group:          Development/Tools/IDE
Requires:       python-PyQt6-devel
Requires:       %plainpython(abi) = %{python_version}
Supplements:    (eric and python-%{mname})
Supplements:    (python-PyQt6-devel and python-%{mname})

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
$python -c 'from PyQt6 import Qt%{qtlib}; assert Qt%{qtlib}.PYQT_DATAVISUALIZATION_VERSION_STR == "%{version}"'
}

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt6/
%{python_sitearch}/PyQt6/Qt%{qtlib}.*
%{python_sitearch}/PyQt6_%{qtlib}-%{version}*-info/
%exclude %{pyqt6_sipdir}

%files %{python_files devel}
%license LICENSE
%dir %{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/
%{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/PyQt6-%{qtlib}.api
%dir %{pyqt6_sipdir}
%{pyqt6_sipdir}/Qt%{qtlib}/

%changelog
