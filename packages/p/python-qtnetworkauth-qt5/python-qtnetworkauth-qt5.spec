#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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


%define mname qtnetworkauth-qt5
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define plainpython python
Name:           python-%{mname}
Version:        5.15.5
Release:        0
Summary:        Python bindings for the Qt Network Authorization library
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqtnetworkauth
Source:         https://files.pythonhosted.org/packages/source/P/PyQtNetworkAuth/PyQtNetworkAuth-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyqt-builder >= 1.9}
BuildRequires:  %{python_module qt5-devel >= %{version}}
BuildRequires:  %{python_module sip-devel >= 5.3}
BuildRequires:  fdupes
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5NetworkAuth) >= 5.15
Requires:       python-qt5 >= %{version}
Requires:       python-qt5-sip
Provides:       python-PyQtNetworkAuth = %{version}-%{release}
%python_subpackages

%description
PyQtNetworkAuth is a set of Python bindings for The Qt Company’s Qt Network
Authorization library. The bindings sit on top of PyQt5 and are implemented
as a single module.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Tools/IDE
Requires:       python-%{mname}
Requires:       python-qt5-devel
Requires:       %{plainpython}(abi) = %{python_version}
Supplements:    (eric and python-%{mname})
Supplements:    (python-qt5-devel and python-%{mname})

%description    devel
This package provides Qt5 Network Authorization library API files
and the SIP files used to generate the Python bindings for %{name}.

%prep
%setup -q -n PyQtNetworkAuth-%{version}

%build
%pyqt_build

%install
%pyqt_install

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5/QtNetworkAuth.*
%{python_sitearch}/PyQtNetworkAuth-%{version}.dist-info

%files %{python_files devel}
%license LICENSE
%dir %{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/
%{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/PyQtNetworkAuth.api
%dir %{pyqt5_sipdir}
%{pyqt5_sipdir}/QtNetworkAuth/

%changelog
