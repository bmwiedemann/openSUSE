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
%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "qt6pdf"
%define pkg_suffix -qt6pdf
%bcond_without qt6pdf

%if (0%{?suse_version} == 1600 && !0%{?is_opensuse}) || 0%{?suse_version} < 1600
# SLFO and SLE15 don't have cmake(Qt6Pdf)
ExclusiveArch:  do_not_build
%endif
%ifnarch aarch64 x86_64 riscv64
# qt6-pdf-devel is built in qt6-webengine with ExclusiveArch
ExclusiveArch:  do_not_build
%endif

%else
%bcond_with qt6pdf
%endif

%{?sle15_python_module_pythons}
Name:           python-%{mname}%{?pkg_suffix}
Version:        6.9.1
Release:        0
Summary:        Python bindings for Qt 6
License:        GPL-3.0-only OR SUSE-GPL-2.0-with-FLOSS-exception OR NonFree
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqt
Source:         https://files.pythonhosted.org/packages/source/P/PyQt6/pyqt6-%{version}.tar.gz
# PATCH-FIX-OPENSUSE - disable-rpaths.diff - Disable RPATH when building PyQt6.
Patch0:         disable-rpaths.diff
# PATCH-FIX-OPENSUSE - install binary dbus mainloop integration in arch dependent directory
Patch1:         0001-Use-a-noarch-wrapper-for-dbus-mainloop-integration.patch
# PATCH-FIX-UPSTREAM fix-build-without-qtcore.patch -- Allow building only the Qt6Pdf bindings
Patch3:         fix-build-without-qtcore.patch
BuildRequires:  %{python_module PyQt6-sip >= 13.8}
BuildRequires:  %{python_module dbus-python-devel >= 0.8}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module pyqt-builder >= 1.17}
BuildRequires:  %{python_module sip-devel >= 6.12}
BuildRequires:  dbus-1-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gdb
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-macros
%if %{with qt6pdf}
BuildRequires:  cmake(Qt6Pdf)
BuildRequires:  cmake(Qt6PdfWidgets)
BuildRequires:  %{python_module PyQt6-devel}
%else
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
BuildRequires:  cmake(Qt6StateMachine)
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
%endif
Requires:       python-PyQt6-sip >= %(rpm -q --whatprovides python-PyQt6-sip --qf "%%{version}")
Requires:       python-dbus-python >= %(rpm -q --whatprovides python-dbus-python --qf "%%{version}")
%if %{with qt6pdf}
Requires:       python-PyQt6
%else
Recommends:     python-PyQt6-qt6pdf
Provides:       python-qt6 = %{version}-%{release}
%endif
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
%if %{with qt6pdf}
Requires:       cmake(Qt6Pdf)
Requires:       cmake(Qt6PdfWidgets)
%else
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
%endif
Requires:       %plainpython(abi) = %{python_version}
Requires(post): update-alternatives
Requires(postun):update-alternatives
# If and which version of sip is required depends on the project trying
# to build against PyQt6.
%if %{with qt6pdf}
Requires:       python-PyQt6-devel
%else
Recommends:     python-sip-devel
Recommends:     python-qscintilla-qt6
Provides:       python-qt6-devel = %{version}-%{release}
%endif

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
%autosetup -p1 -n pyqt6-%{version}
dos2unix examples/quick/models/*/view.qml
dos2unix examples/multimedia*/*/*.ui

%build

# -DQT_NO_INT128 is required to build with Qt 6.6.0.
%{pyqt_build -v \
    -s %{quote:--pep484-pyi \
               --confirm-license \
               --qt-shared \
               --qmake-setting 'QMAKE_CXXFLAGS_RELEASE=%{optflags} -DQT_NO_INT128'\
%if %{with qt6pdf}
               --enable QtPdf \
%endif
               %{nil}
}}

%install
%pyqt_install
%if %{without qt6pdf}
%pyqt_install_examples %mname

%python_clone -a %{buildroot}%{_bindir}/pyuic6
%python_clone -a %{buildroot}%{_bindir}/pylupdate6
%else
# We have to remove installed files that aren't part of qt6pdf
rm %{buildroot}%{_bindir}/pyuic6 \
   %{buildroot}%{_bindir}/pylupdate6
rm -Rf %{buildroot}%{_qt6_datadir}/qsci
%{python_expand 
rm -Rf %{buildroot}%{$python_sitelib}/dbus \
   %{buildroot}%{$python_sitearch}/PyQt6/uic \
   %{buildroot}%{$python_sitearch}/PyQt6/lupdate \
   %{buildroot}%{$python_sitearch}/[Pp]y[Qq]t6-%{version}.dist-info
rm %{buildroot}%{$python_sitearch}/PyQt6/__init__.py \
   %{buildroot}%{$python_sitearch}/PyQt6/dbus_mainloop.abi3.so \
   %{buildroot}%{$python_sitearch}/PyQt6/py.typed \
   %{buildroot}%{$python_sitearch}/PyQt6/sip.pyi
}
%endif

%python_expand %fdupes %{buildroot}%{$python_sitearch}


%if %{without qt6pdf}

%check
export PYTHONDONTWRITEBYTECODE=1 # boo#1047218
%{python_expand # there is no test suite. If it compiles and imports, it should be okay.
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c 'from PyQt6 import QtCore; assert QtCore.PYQT_VERSION_STR == "%{version}"'
}

%post devel
%python_install_alternative pyuic6 pylupdate6

%postun devel
%python_uninstall_alternative pyuic6

%endif

%files %{python_files}
%license LICENSE
%if %{without qt6pdf}
%doc README.md NEWS ChangeLog
%{python_sitearch}/PyQt6/
%{python_sitearch}/[Pp]y[Qq]t6-%{version}.dist-info/
%dir %{python_sitelib}/dbus
%dir %{python_sitelib}/dbus/mainloop
%{python_sitelib}/dbus/mainloop/pyqt6.py
%dir %{_qt6_pluginsdir}/PyQt6/
%{_qt6_pluginsdir}/PyQt6/libpy%{python_bin_suffix}qt6qmlplugin.so
%exclude %pyqt6_sipdir
%exclude %{python_sitearch}/PyQt6/QtPdf.*
%else
%{python_sitearch}/PyQt6/QtPdf.*
%endif

%files %{python_files devel}
%license LICENSE
%pyqt6_sipdir
%if %{without qt6pdf}
%python_alternative %{_bindir}/pyuic6
%python_alternative %{_bindir}/pylupdate6
%dir %{_qt6_pluginsdir}/designer/
%{_qt6_pluginsdir}/designer/libpy%{python_bin_suffix}qt6.so
%dir %{_qt6_datadir}/qsci/
%dir %{_qt6_datadir}/qsci/api/
%dir %{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/
%{_qt6_datadir}/qsci/api/python_%{python_bin_suffix}/PyQt6.api

%files %{python_files doc}
%license LICENSE
%{_docdir}/%{python_prefix}-%{mname}
%exclude %{_docdir}/%{python_prefix}-%{mname}/README.md
%exclude %{_docdir}/%{python_prefix}-%{mname}/NEWS
%exclude %{_docdir}/%{python_prefix}-%{mname}/ChangeLog
%endif

%changelog
