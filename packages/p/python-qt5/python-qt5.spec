#
# spec file for package python-qt5
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "quick3d"
%if 0%{?_with_ringdisabled}
ExclusiveArch:  do_not_build
%else
%define build_quick3d 1
%endif
%endif

%if 0%{suse_version} < 1550
%{?!use_sip4:%define use_sip4 1}
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
%define mname qt5
Name:           python-%{mname}
Version:        5.15.1
Release:        0
Summary:        Python bindings for Qt 5
License:        SUSE-GPL-2.0-with-FLOSS-exception OR GPL-3.0-only OR NonFree
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqt
Source:         https://files.pythonhosted.org/packages/source/P/PyQt5/PyQt5-%{version}.tar.gz
Source99:       python-qt5-rpmlintrc
# PATCH-FIX-UPSTREAM - allow hashable signals - https://www.riverbankcomputing.com/pipermail/pyqt/2020-September/043160.html
Patch0:         pyqt5-signals-hashable.patch
# PATCH-FIX-UPSTREAM - QCustomAudioRoleControl for Qt5 5.11 and later only - https://www.riverbankcomputing.com/pipermail/pyqt/2020-September/043241.html
Patch1:         pyqt5-customaudio-qt511.patch
# PATCH-FIX-OPENSUSE - disable-rpaths.diff - Disable RPATH when building PyQt5.
Patch2:         disable-rpaths.diff
# PATCH-FIX-OPENSUSE - install binary dbus mainloop integration in arch dependent directory
Patch3:         0001-Use-a-noarch-wrapper-for-dbus-mainloop-integration.patch
BuildRequires:  %{python_module dbus-python-devel}
BuildRequires:  %{python_module devel}
BuildRequires:  dbus-1-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gdb
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5Bluetooth)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Nfc)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
%{?build_quick3d:BuildRequires: pkgconfig(Qt5Quick3D)}
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
# Do not build WebKit support from SLE15
%if 0%{?is_opensuse} || 0%{?suse_version} < 1500
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
%endif
# Do not build WebEngine support from SLE15
%if 0%{?is_opensuse} && 0%{?suse_version} >= 1320
%ifnarch ppc ppc64 ppc64le s390 s390x riscv64
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebEngineCore)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
%endif
%endif
# Do not build Qt5NetworkAuth support in SLE
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(Qt5NetworkAuth)
%endif
# Use sip4 for non tumbleweed distros -- supports python2
%if 0%{?use_sip4}
BuildRequires:  %{python_module sip4-devel >= 4.19.23}
BuildRequires:  python2-enum34
Requires:       python-sip(api) = %{python_sip_api_ver}
%else
BuildRequires:  %{python_module pyqt-builder}
BuildRequires:  %{python_module sip-devel >= 5.3}
%requires_eq    python-qt5-sip
%endif
%requires_ge    libqt5-x11
%requires_ge    python-dbus-python
%ifpython2
Requires:       %{oldpython}-enum34
%endif
Provides:       python-PyQt5 = %{version}-%{release}
Suggests:       python-%{mname}-quick3d

%python_subpackages

%description
PyQt is a set of Python bindings for the Qt framework.

%package devel
Summary:        PyQt - devel part of python bindings for Qt 5
Group:          Development/Libraries/Python
Requires:       libqt5-qtbase-devel
Requires:       python-%{mname} = %{version}
Requires:       python-dbus-python-devel
Requires:       python-devel
Requires:       python-sip-devel >= 4.19.23
Requires:       pkgconfig(Qt5Bluetooth)
Requires:       pkgconfig(Qt5Designer)
Requires:       pkgconfig(Qt5Help)
Requires:       pkgconfig(Qt5Location)
Requires:       pkgconfig(Qt5Multimedia)
Requires:       pkgconfig(Qt5MultimediaWidgets)
Requires:       pkgconfig(Qt5Nfc)
Requires:       pkgconfig(Qt5Positioning)
Requires:       pkgconfig(Qt5Qml)
Requires:       pkgconfig(Qt5Quick)
Requires:       pkgconfig(Qt5QuickWidgets)
Requires:       pkgconfig(Qt5SerialPort)
Requires:       pkgconfig(Qt5Svg)
Requires:       pkgconfig(Qt5TextToSpeech)
Requires:       pkgconfig(Qt5UiTools)
Requires:       pkgconfig(Qt5WebChannel)
Requires:       pkgconfig(Qt5WebSockets)
Requires:       pkgconfig(Qt5X11Extras)
Requires:       pkgconfig(Qt5XmlPatterns)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-qscintilla-qt5
Recommends:     pkgconfig(Qt5Quick3D)
# Do not build WebKit support from SLE15
%if 0%{?is_opensuse} || 0%{?suse_version} < 1500
Requires:       pkgconfig(Qt5WebKit)
Requires:       pkgconfig(Qt5WebKitWidgets)
%endif
# Do not build WebEngine support from SLE15
%if 0%{?is_opensuse} && 0%{?suse_version} >= 1320
%ifnarch ppc ppc64 ppc64le s390 s390x riscv64
Requires:       pkgconfig(Qt5WebEngine)
Requires:       pkgconfig(Qt5WebEngineCore)
Requires:       pkgconfig(Qt5WebEngineWidgets)
%endif
%endif
Provides:       python-PyQt5-devel = %{version}-%{release}
Obsoletes:      python-PyQt5-devel < %{version}-%{release}
Provides:       %{oldpython}-%{mname}-common-devel = %{version}-%{release}
Provides:       %{oldpython}-%{mname}-utils = %{version}-%{release}
Obsoletes:      %{oldpython}-%{mname}-common-devel < %{version}-%{release}
Obsoletes:      %{oldpython}-%{mname}-utils < %{version}-%{release}

%description devel
PyQt is a set of Python bindings for the Qt framework.

This package contains all the developer tools you need to create your
own PyQt applications

%package quick3d-devel
Summary:        PyQt - devel part of python bindings for QtQuick3D
Group:          Development/Libraries/Python
Requires:       python-%{mname}-devel = %{version}
Requires:       pkgconfig(Qt5Quick3D)

%description quick3d-devel
PyQt is a set of Python bindings for the Qt framework.

This package contains all the developer tools you need to create your
own PyQt applications with QtQuick3D

%package doc
Summary:        Examples for %{name}
Group:          Documentation/Other
Provides:       python-PyQt5-doc = %{version}
BuildArch:      noarch

%description doc
PyQt is a set of Python bindings for the Qt framework.

This package contains programming examples for PyQt5.

%package quick3d
Summary:        Python bindings for QtQuick3D
Group:          Development/Libraries/Python
Requires:       %{python_module qt5 = %{version}}

%description quick3d
PyQt is a set of Python bindings for the Qt framework.

This package contains the extension for QtQuick3D


%prep
%autosetup -p1 -n PyQt5-%{version}

%build
# sip-build requires QtCore as target, even if we want QtQuick3D only
%{pyqt_build -v \
    -c %{quote:--confirm-license \
               --assume-shared \
               %{!?build_quick3d: --disable QtQuick3D \
               --qsci-api \
               --qsci-api-destdir %{_libqt5_datadir}/qsci} \
               %{?build_quick3d: --enable QtQuick3D \
               --no-python-dbus \
               --no-designer-plugin \
               --no-qml-plugin \
               --no-qsci-api \
               --no-tools}}
    -s %{quote:--pep484-pyi \
               --confirm-license \
               --qt-shared \
               %{!?build_quick3d: --disable QtQuick3D} \
               %{?build_quick3d: --enable QtQuick3D \
               --enable QtCore \
               --no-dbus-python \
               --no-designer-plugin \
               --no-qml-plugin \
               --no-tools}}              
}

%install
%if ! 0%{?build_quick3d}
%pyqt_install
%pyqt_install_examples %mname

%python_clone -a %{buildroot}%{_bindir}/pyuic5
%python_clone -a %{buildroot}%{_bindir}/pylupdate5
%python_clone -a %{buildroot}%{_bindir}/pyrcc5

# Provide the legacy path to the SIP files for packages stuck on sip4
mkdir -p %{buildroot}%{_datadir}/sip/
%{python_expand ln -sr \
  %if 0%{?use_sip4}
    %{buildroot}%{_datadir}/sip/PyQt5-%{$python_bin_suffix} \
  %else
    %{buildroot}%{$python_sitearch}/PyQt5/bindings \
  %endif
  %{buildroot}%{_datadir}/pyqt5-sip-%{$python_bin_suffix}
}
%prepare_alternative -t %{_datadir}/sip/PyQt5 pyqt5-sip
%else
# sip4 uses an extra target for the python3 only PEP484 pyi stub files
%define python2_pep484target %{nil}
%define python3_pep484target install_pep484_stubs
%{python_expand pushd build
%__make sub-QtQuick3D-install_subtargets-ordered \
        %{?use_sip4:%{$python_pep484target}} \
        INSTALL="%__install -p" INSTALL_ROOT=%{buildroot}
popd
}
%endif

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if ! 0%{?build_quick3d}
%post devel
%{python_install_alternative pyuic5 pylupdate5 pyrcc5} \
   --slave %{_datadir}/sip/PyQt5 pyqt5-sip %{_datadir}/pyqt5-sip-%{python_bin_suffix}

%postun devel
%python_uninstall_alternative pyuic5

%files %{python_files}
%license LICENSE
%doc README NEWS ChangeLog
%{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5-%{version}.dist-info/
%sip5_only %exclude %pyqt5_sipdir
%dir %{python_sitelib}/dbus
%dir %{python_sitelib}/dbus/mainloop
%{python_sitelib}/dbus/mainloop/pyqt5.py
%dir %{_libqt5_plugindir}/PyQt5/
%{_libqt5_plugindir}/PyQt5/libpy%{python_bin_suffix}qt5qmlplugin.so

%files %{python_files devel}
%license LICENSE
%python_alternative %{_bindir}/pyuic5
%python_alternative %{_bindir}/pylupdate5
%python_alternative %{_bindir}/pyrcc5
%dir %{_libqt5_plugindir}/designer/
%{_libqt5_plugindir}/designer/libpy%{python_bin_suffix}qt5.so
%dir %{_datadir}/qt5/qsci/
%dir %{_datadir}/qt5/qsci/api/
%dir %{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/
%{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/PyQt5.api
%dir %_datadir/sip
%ghost %{_sysconfdir}/alternatives/pyqt5-sip
%{_datadir}/sip/PyQt5
%{_datadir}/pyqt5-sip-%{python_bin_suffix}
%pyqt5_sipdir

%files %{python_files doc}
%license LICENSE
%{_docdir}/%{python_prefix}-%{mname}
%exclude %{_docdir}/%{python_prefix}-%{mname}/README
%exclude %{_docdir}/%{python_prefix}-%{mname}/NEWS
%exclude %{_docdir}/%{python_prefix}-%{mname}/ChangeLog

%else

%files %{python_files quick3d}
%license LICENSE
%doc README NEWS ChangeLog
%{python_sitearch}/PyQt5/QtQuick3D*
%sip5_only %exclude %{python_sitearch}/PyQt5/QtCore*
%sip5_only %exclude %pyqt5_sipdir

%files %{python_files quick3d-devel}
%license LICENSE
# sip4 has the sip files in the regular devel package
%sip5_only %dir %pyqt5_sipdir
%sip5_only %pyqt5_sipdir/QtQuick3D
%sip5_only %exclude %pyqt5_sipdir/QtCore

%endif

%changelog
