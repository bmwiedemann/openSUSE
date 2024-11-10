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


%define plainpython python
%define mname PyQt6
%define pyqt_build_for_qt6 1
%define pep440version 6.8.0.dev2410061818
%{?sle15_python_module_pythons}
Name:           python-%{mname}
Version:        6.8.0~dev2410061818
Release:        0
Summary:        Python bindings for Qt 6
License:        GPL-3.0-only OR SUSE-GPL-2.0-with-FLOSS-exception OR NonFree
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqt
#Source:         https://files.pythonhosted.org/packages/source/P/PyQt6/PyQt6-%%{version}.tar.gz
# The URL will be dead soon, don't bother including it
# https://www.riverbankcomputing.com/pypi/packages/PyQt6/PyQt6-%{version}.tar.gz
Source:         PyQt6-%{pep440version}.tar.gz
# PATCH-FIX-OPENSUSE - disable-rpaths.diff - Disable RPATH when building PyQt6.
Patch0:         disable-rpaths.diff
# PATCH-FIX-OPENSUSE - install binary dbus mainloop integration in arch dependent directory
Patch1:         0001-Use-a-noarch-wrapper-for-dbus-mainloop-integration.patch
BuildRequires:  %{python_module PyQt6-sip >= 13.8}
BuildRequires:  %{python_module dbus-python-devel >= 0.8}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pyqt-builder >= 1.15}
BuildRequires:  %{python_module sip-devel >= 6.8}
BuildRequires:  dbus-1-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gdb
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Bluetooth)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Nfc)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
%if %{?suse_version} >= 1550
# no pdf headers in 15.X
%ifarch aarch64 x86_64 riscv64
# qt6-pdf-devel is built in qt6-webengine with ExclusiveArch
BuildRequires:  cmake(Qt6Pdf)
BuildRequires:  cmake(Qt6PdfWidgets)
%endif
%endif
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
%if %{?suse_version} >= 1550
BuildRequires:  cmake(Qt6Quick3D)
BuildRequires:  cmake(Qt6Quick3DRuntimeRender)
%endif
BuildRequires:  cmake(Qt6RemoteObjects)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6SerialPort)
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 155000
BuildRequires:  cmake(Qt6SpatialAudio)
%endif
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
%if %{?suse_version} >= 1550
BuildRequires:  cmake(Qt6TextToSpeech)
%endif
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
Requires:       python-PyQt6-sip >= %(rpm -q --whatprovides python-PyQt6-sip --qf "%%{version}")
Requires:       python-dbus-python >= %(rpm -q --whatprovides python-dbus-python --qf "%%{version}")
Provides:       python-qt6 = %{version}-%{release}
%python_subpackages

%description
PyQt is a set of Python bindings for the Qt framework.

%package devel
Summary:        PyQt - devel part of python bindings for Qt 6
Group:          Development/Libraries/Python
Requires:       python-%{mname} = %{version}
Requires:       python-dbus-python-devel >= 0.8
Requires:       python-devel
Requires:       qt6-base-devel
Requires:       qt6-macros
Requires:       cmake(Qt6Bluetooth)
Requires:       cmake(Qt6Designer)
Requires:       cmake(Qt6DBus)
Requires:       cmake(Qt6Help)
Requires:       cmake(Qt6Multimedia)
Requires:       cmake(Qt6MultimediaWidgets)
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Nfc)
Requires:       cmake(Qt6OpenGL)
Requires:       cmake(Qt6OpenGLWidgets)
%if %{?suse_version} >= 1550
# no pdf headers in 15.X
%ifarch aarch64 x86_64 riscv64
# qt6-pdf-devel is built in qt6-webengine with ExclusiveArch
Requires:       cmake(Qt6Pdf)
Requires:       cmake(Qt6PdfWidgets)
%endif
%endif
Requires:       cmake(Qt6Positioning)
Requires:       cmake(Qt6PrintSupport)
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Quick)
Requires:       cmake(Qt6QuickWidgets)
%if %{?suse_version} >= 1550
Requires:       cmake(Qt6Quick3D)
Requires:       cmake(Qt6Quick3DRuntimeRender)
%endif
Requires:       cmake(Qt6RemoteObjects)
Requires:       cmake(Qt6Sensors)
Requires:       cmake(Qt6SerialPort)
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 155000
Requires:       cmake(Qt6SpatialAudio)
%endif
Requires:       cmake(Qt6Sql)
Requires:       cmake(Qt6Svg)
Requires:       cmake(Qt6SvgWidgets)
Requires:       cmake(Qt6Test)
%if %{?suse_version} >= 1550
Requires:       cmake(Qt6TextToSpeech)
%endif
Requires:       cmake(Qt6WebChannel)
Requires:       cmake(Qt6WebSockets)
Requires:       cmake(Qt6Widgets)
Requires:       cmake(Qt6Xml)
Requires:       %plainpython(abi) = %{python_version}
Requires(post): update-alternatives
Requires(postun):update-alternatives
# If and which version of sip is required depends on the project trying
# to build against PyQt6.
Recommends:     python-sip-devel
Recommends:     python-qscintilla-qt6
Provides:       python-qt6-devel = %{version}-%{release}

%description devel
PyQt is a set of Python bindings for the Qt framework.

This package contains all the developer tools you need to create your
own PyQt applications

%package doc
Summary:        Examples for %{name}
Group:          Documentation/Other
Provides:       python-qt6-doc = %{version}
BuildArch:      noarch

%description doc
PyQt is a set of Python bindings for the Qt framework.

This package contains programming examples for PyQt6.

%prep
%autosetup -p1 -n PyQt6-%{pep440version}
dos2unix examples/quick/models/*/view.qml
dos2unix examples/multimedia*/*/*.ui

%build

# -DQT_NO_INT128 is required to build with Qt 6.6.0.
%{pyqt_build -v \
    -s %{quote:--pep484-pyi \
               --confirm-license \
               --qt-shared \
               --qmake-setting 'QMAKE_CXXFLAGS_RELEASE=%{optflags} -DQT_NO_INT128'}}

%install
%pyqt_install
%pyqt_install_examples %mname

%python_clone -a %{buildroot}%{_bindir}/pyuic6
%python_clone -a %{buildroot}%{_bindir}/pylupdate6

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1 # boo#1047218
%{python_expand # there is no test suite. If it compiles and imports, it should be okay.
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c 'from PyQt6 import QtCore; assert QtCore.PYQT_VERSION_STR == "%{pep440version}"'
}

%post devel
%python_install_alternative pyuic6 pylupdate6

%postun devel
%python_uninstall_alternative pyuic6

%files %{python_files}
%license LICENSE
%doc README.md NEWS ChangeLog
%{python_sitearch}/PyQt6/
%{python_sitearch}/PyQt6-%{pep440version}.dist-info/
%dir %{python_sitelib}/dbus
%dir %{python_sitelib}/dbus/mainloop
%{python_sitelib}/dbus/mainloop/pyqt6.py
%dir %{_qt6_pluginsdir}/PyQt6/
%{_qt6_pluginsdir}/PyQt6/libpy%{python_bin_suffix}qt6qmlplugin.so
%exclude %pyqt6_sipdir

%files %{python_files devel}
%license LICENSE
%python_alternative %{_bindir}/pyuic6
%python_alternative %{_bindir}/pylupdate6
%dir %{_qt6_pluginsdir}/designer/
%{_qt6_pluginsdir}/designer/libpy%{python_bin_suffix}qt6.so
%dir %{_qt6_datadir}/qsci/
%dir %{_qt6_datadir}/qsci/api/
%dir %{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/
%{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/PyQt6.api
%pyqt6_sipdir

%files %{python_files doc}
%license LICENSE
%{_docdir}/%{python_prefix}-%{mname}
%exclude %{_docdir}/%{python_prefix}-%{mname}/README.md
%exclude %{_docdir}/%{python_prefix}-%{mname}/NEWS
%exclude %{_docdir}/%{python_prefix}-%{mname}/ChangeLog

%changelog
