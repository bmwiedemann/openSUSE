#
# spec file for package python
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

# define a default so that quilt does not fail
%define pyname python

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "python3" || "%{flavor}" == "python3_quick3d"
%define skip_python2 1
%define pyname python3
%endif

%if "%{flavor}" == "python2" || "%{flavor}" == "python2_quick3d"
%define skip_python3 1
%define pyname python2
%if 0%{?suse_version} > 1500
ExclusiveArch:  do_not_build
%endif
%endif

%if "%{flavor}" == "python3"
%define build_examples 1
%define build_sipfiles 1
%endif

%if "%{flavor}" == "python3_quick3d" || "%{flavor}" == "python2_quick3d"
%if 0%{?_with_ringdisabled}
ExclusiveArch:  do_not_build
%else
%define build_quick3d 1
%endif
%endif

%define bname python-qt5
%define pname %{pyname}-qt5

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           %{pname}
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
BuildRequires:  %{python_module sip-devel >= 4.19.19}
BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  gdb
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
%if !0%{?skip_python2}
BuildRequires:  python2-enum34
%endif
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
Requires:       %{pyname}-sip(api) = %{python_sip_api_ver}
%requires_ge    libqt5-x11
%requires_ge    %{pyname}-dbus-python
Provides:       %{pyname}-PyQt5 = %{version}
%ifpython2
Requires:       %{pyname}-enum34
%endif
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
%ifpython2
%requires_ge    dbus-1-python
%endif
%ifpython3
%requires_ge    dbus-1-python3
%endif
%python_subpackages

%description
PyQt is a set of Python bindings for the Qt framework.

%package devel
Summary:        PyQt - devel part of python bindings for Qt 5
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       %{pyname}-devel
Requires:       %{pyname}-sip-devel >= 4.19.11
Requires:       libqt5-qtbase-devel
Requires:       python-qt5-common-devel
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
Recommends:     %{pyname}-qscintilla-qt5
Recommends:     pkgconfig(Qt5Quick3D)
Provides:       %{pyname}-PyQt5-devel = %{version}
%ifpython2
Requires:       %{pyname}-enum34
%endif
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
%ifpython2
Requires:       dbus-1-python-devel
%endif
%ifpython3
Requires:       dbus-1-python3-devel
%endif

%description devel
PyQt is a set of Python bindings for the Qt framework.

This package contains all the developer tools you need to create your
own PyQt applications.

%package -n %{bname}-common-devel
Summary:        Common files for PyQt5 for python2 and python3
Group:          Development/Libraries/Python
Obsoletes:      %{bname}-utils < %{version}-%{release}
Provides:       %{bname}-utils = %{version}-%{release}
BuildArch:      noarch

%description -n %{bname}-common-devel
PyQt is a set of Python bindings for the Qt framework.

This package contains the SIP definitions shared between python2
and python3 versions of PyQt5.

%package -n %{bname}-doc
Summary:        Examples for %{bname}
Group:          Documentation/Other
Provides:       %{python_module PyQt5-doc = %{version}}
Provides:       %{python_module qt5-doc = %{version}}
BuildArch:      noarch

%description -n %{bname}-doc
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

# Fix wrong-script-interpreter
%if 0%{?build_examples}
find examples -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%__python3|" {} \;
%endif

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"

%{python_expand mkdir build_%{$python_bin_suffix}

pushd build_%{$python_bin_suffix}

ln -s ../config-tests .
$python ../configure.py --verbose  \
                        --confirm-license \
                        --assume-shared \
                        --qmake=%{_libqt5_qmake} \
                        --sip=%{_bindir}/sip-%{$python_bin_suffix} \
                        --qsci-api \
                        --qsci-api-destdir=%{_libqt5_datadir}/qsci \
                        QMAKE_CFLAGS+="${CFLAGS} ${CPPFLAGS}" \
                        QMAKE_CXXFLAGS+="${CXXFLAGS} ${CPPFLAGS}" \
                        %{?build_quick3d:--enable}%{!?build_quick3d:--disable} QtQuick3D

make %{?_smp_mflags}

popd

}

%install
# sip4 uses an extra target for the python3 only PEP484 pyi stub files
%define python2_pep484target %{nil}
%define python3_pep484target install_pep484_stubs
%{python_expand pushd build_%{$python_bin_suffix}

%if ! 0%{?build_quick3d}
%make_install INSTALL_ROOT=%{buildroot}

mv %{buildroot}%{_libqt5_plugindir}/designer/libpyqt5.so %{buildroot}%{_libqt5_plugindir}/designer/libpy%{$python_bin_suffix}qt5.so
mv %{buildroot}%{_libqt5_plugindir}/PyQt5/libpyqt5qmlplugin.so %{buildroot}%{_libqt5_plugindir}/PyQt5/libpy%{$python_bin_suffix}qt5qmlplugin.so
mv -T %{buildroot}%{_datadir}/qt5/qsci/api/python %{buildroot}%{_datadir}/qt5/qsci/api/python_%{$python_bin_suffix}
%else
%__make sub-QtQuick3D-install_subtargets-ordered \
        %{$python_pep484target} \
        INSTALL="%__install -p" INSTALL_ROOT=%{buildroot}
%endif

# Point to the correct location for the documentation files
cp ../README ./
sed -i 's/The "doc" directory/The "doc" directory of package %{$python_prefix}-qt5-devel/' README

popd
}

%if !0%{?build_quick3d}
%python_clone -a %{buildroot}%{_bindir}/pyuic5
%python_clone -a %{buildroot}%{_bindir}/pylupdate5
%python_clone -a %{buildroot}%{_bindir}/pyrcc5
%endif

%if 0%{?build_examples}
mkdir -p %{buildroot}%{_docdir}/%{bname}
cp -r examples %{buildroot}%{_docdir}/%{bname}/
%fdupes %{buildroot}%{_docdir}/%{bname}/
%endif

%if !0%{?build_sipfiles}
rm -Rf %{buildroot}%{_datadir}/sip/PyQt5/
%endif

%if ! 0%{?build_quick3d}
%post devel
%python_install_alternative pyuic5 pylupdate5 pyrcc5

%postun devel
%python_uninstall_alternative pyuic5

%files %{python_files}
%license LICENSE
%doc build_%{python_bin_suffix}/README
%doc NEWS ChangeLog
%{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5-%{version}.dist-info/
%dir %{python_sitelib}/dbus
%dir %{python_sitelib}/dbus/mainloop
%{python_sitelib}/dbus/mainloop/pyqt5.py
%dir %{_libqt5_plugindir}/PyQt5/
%{_libqt5_plugindir}/PyQt5/libpy%{python_bin_suffix}qt5qmlplugin.so
%exclude %{_docdir}/%{bname}/examples/

%files %{python_files devel}
%python_alternative %{_bindir}/pyuic5
%python_alternative %{_bindir}/pylupdate5
%python_alternative %{_bindir}/pyrcc5
%dir %{_libqt5_plugindir}/designer/
%{_libqt5_plugindir}/designer/libpy%{python_bin_suffix}qt5.so
%dir %{_datadir}/qt5/qsci/
%dir %{_datadir}/qt5/qsci/api/
%dir %{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/
%{_datadir}/qt5/qsci/api/python_%{python_bin_suffix}/PyQt5.api

%else

%files %{python_files quick3d}
%license LICENSE
%doc build_%{python_bin_suffix}/README
%doc NEWS ChangeLog
%{python_sitearch}/PyQt5/QtQuick3D*
%endif

%if 0%{?build_sipfiles}
%files -n %{bname}-common-devel
%{_datadir}/sip/PyQt5/
%endif

%if 0%{?build_examples}
%files -n %{bname}-doc
%license LICENSE
%dir %{_docdir}/%{bname}
%{_docdir}/%{bname}/examples/
%endif

%changelog
