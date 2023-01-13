#
# spec file for package python-qt3d-qt5
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


# This definition is for projects which include the PyQt5 packages in recent
# versions but use default (old) Qt libraries e.g. from Leap, which does not
# have Qt >= 5.10. In that case, no Qt3DAnimation module will be built per
# sip %%If directives in the sip/Qt3DAnimation/*.sip files
%if %{pkg_vcmp libQt53DAnimation-devel >= 5.10}
%define have_qt3danimation 1
%endif

%define plainpython python
%define mname qt3d-qt5

%define skip_python2 1
Name:           python-%{mname}
Version:        5.15.5
Release:        0
Summary:        Python bindings for the Qt5 3D framework
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqtchart/intro
Source:         https://files.pythonhosted.org/packages/source/P/PyQt3D/PyQt3D-%{version}.tar.gz
Patch0:         qt3d-geometry-equals.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyqt-builder >= 1.9}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module sip-devel >= 5.3}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt53DAnimation)
BuildRequires:  pkgconfig(Qt53DCore)
BuildRequires:  pkgconfig(Qt53DExtras)
BuildRequires:  pkgconfig(Qt53DInput)
BuildRequires:  pkgconfig(Qt53DLogic)
BuildRequires:  pkgconfig(Qt53DRender)
Provides:       python-PyQt3D = %{version}-%{release}
Requires:       python-qt5 >= %{version}
Requires:       python-qt5-sip

%python_subpackages

%description
PyQt3D is a set of Python bindings for the Qt 3D framework.

%package devel
Summary:        Development files for %{name}
Group:          Development/Tools/IDE
Requires:       python-qt5-devel
Requires:       %{plainpython}(abi) = %python_version
Supplements:    (eric and python-%{mname})
Supplements:    (python-qt5-devel and python-%{mname})
Provides:       python-%{mname}-sip = %{version}-%{release}
Obsoletes:      python-%{mname}-sip < %{version}-%{release}
Provides:       python-%{mname}-api = %{version}-%{release}
Obsoletes:      python-%{mname}-api < %{version}-%{release}
Provides:       %{plainpython}-%{mname}-sip = %{version}-%{release}
Obsoletes:      %{plainpython}-%{mname}-sip < %{version}-%{release}
Provides:       %{plainpython}-%{mname}-api = %{version}-%{release}
Obsoletes:      %{plainpython}-%{mname}-api < %{version}-%{release}

%description devel
This package provides the SIP files used to generate the Python bindings
and the Qt5 3D framework API files for the Eric IDE for %{name}

%package doc
Summary:        Examples for %{name}
Group:          Documentation/Other
Provides:       %{python_module %{mname}-examples = %{version}-%{release}}
BuildArch:      noarch

%description doc
This package provides %{name} examples.

%prep
%autosetup -p1 -n PyQt3D-%{version}

%build
%pyqt_build

%install
%pyqt_install
# replace CRLF line endings in example resources in order to make rpmlint happy.
find examples/assets -type f -print0 | xargs -0 dos2unix 
%pyqt_install_examples %mname

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt5/
%{?have_qt3danimation:%{python_sitearch}/PyQt5/Qt3DAnimation.*}
%{python_sitearch}/PyQt5/Qt3DCore.*
%{python_sitearch}/PyQt5/Qt3DExtras.*
%{python_sitearch}/PyQt5/Qt3DInput.*
%{python_sitearch}/PyQt5/Qt3DLogic.*
%{python_sitearch}/PyQt5/Qt3DRender.*
%{python_sitearch}/PyQt3D-%{version}.dist-info/

%files %{python_files devel}
%license LICENSE
%dir %{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/
%{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/PyQt3D.api
%{?have_qt3danimation:%{pyqt5_sipdir}/Qt3DAnimation/}
%{pyqt5_sipdir}/Qt3DCore/
%{pyqt5_sipdir}/Qt3DExtras/
%{pyqt5_sipdir}/Qt3DInput/
%{pyqt5_sipdir}/Qt3DLogic/
%{pyqt5_sipdir}/Qt3DRender/

%files %{python_files doc}
%license LICENSE
%{_docdir}/%{python_prefix}-%{mname}
%exclude %{_docdir}/%{python_prefix}-%{mname}/NEWS
%exclude %{_docdir}/%{python_prefix}-%{mname}/README

%changelog
