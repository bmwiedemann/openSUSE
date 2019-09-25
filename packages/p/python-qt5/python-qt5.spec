#
# spec file for package python-qt5
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-qt5
Version:        5.13.1
Release:        0
Summary:        Python bindings for Qt 5
License:        SUSE-GPL-2.0-with-FLOSS-exception OR GPL-3.0-only OR NonFree
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqt
Source:         https://www.riverbankcomputing.com/static/Downloads/PyQt5/%{version}/PyQt5_gpl-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE - disable-rpaths.diff - Disable RPATH when building PyQt5.
Patch1:         disable-rpaths.diff
# PATCH-FIX-UPSTREAM
Patch2:         update-timeline.patch
# PATCH-FIX-UPSTREAM - add-qkeysequenceedit-to-uic.patch
Patch3:         add-qkeysequenceedit-to-uic.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module sip-devel >= 4.19.19}
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-python-devel
BuildRequires:  dbus-1-python3-devel
BuildRequires:  fdupes
BuildRequires:  gdb
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  python-enum34
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
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
Requires:       %{name}-utils
Requires:       python-sip(api) = %{python_sip_api_ver}
%requires_ge    libqt5-x11
%requires_ge    python-dbus-python
Provides:       python-PyQt5 = %{version}
%ifpython2
Requires:       python-enum34
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
PyQt is a set of Python bindings for Trolltech's Qt application
framework. The qt4 and qt5 bindings can be co-installed.

%package devel
Summary:        PyQt - devel part of python bindings for Qt 5
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       libqt5-qtbase-devel
Requires:       python-devel
Requires:       python-qt5-utils
Requires:       python-sip-devel >= 4.19.11
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
Requires:       pkgconfig(Qt5UiTools)
Requires:       pkgconfig(Qt5WebChannel)
Requires:       pkgconfig(Qt5WebSockets)
Requires:       pkgconfig(Qt5X11Extras)
Requires:       pkgconfig(Qt5XmlPatterns)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-qscintilla-qt5
Provides:       python-PyQt5-devel = %{version}
%ifpython2
Requires:       python-enum34
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
PyQt is a set of Python bindings for Trolltech's Qt application
framework. The qt4 and qt5 bindings can be co-installed.

This package contains all the developer tools you need to create your
own PyQt applications.

%package -n %{name}-utils
Summary:        Common files for PyQt5 for python2 and python3
Group:          Development/Libraries/Python
Provides:       %{python_module PyQt5-utils = %{version}}
Provides:       %{python_module qt5-utils = %{version}}

%description -n %{name}-utils
PyQt is a set of Python bindings for Trolltech's Qt application
framework. The qt4 and qt5 bindings can be co-installed.

This package contains common files shared between python2 and python3
versions of PyQt5.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module PyQt5-doc = %{version}}
Provides:       %{python_module qt5-doc = %{version}}

%description -n %{name}-doc
PyQt is a set of Python bindings for Trolltech's Qt application
framework. The qt4 and qt5 bindings can be co-installed.

This package contains documentation and examples for PyQt5.

%prep
%autosetup -p1 -n PyQt5_gpl-%{version}

# Fix wrong-script-interpreter
find examples -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%__python3|" {} \;

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"

%{python_expand mkdir build_%{$python_bin_suffix}

pushd build_%{$python_bin_suffix}

ln -s ../config-tests .
$python ../configure.py --verbose  \
                        --confirm-license \
                        --assume-shared \
                        --debug \
                        --qmake=%{_libqt5_qmake} \
                        --sip=%{_bindir}/sip-%{$python_bin_suffix} \
                        --qsci-api \
                        --qsci-api-destdir=%{_libqt5_datadir}/qsci \
                        QMAKE_CFLAGS+="${CFLAGS} ${CPPFLAGS}" \
                        QMAKE_CXXFLAGS+="${CXXFLAGS} ${CPPFLAGS}" \

make %{?_smp_mflags}

popd

}

%install
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
%{python_expand pushd build_%{$python_bin_suffix}

%make_install INSTALL_ROOT=%{buildroot}

# Point to the correct location for the documentation files
cp ../README ./
sed -i 's/The "doc" directory/The "doc" directory of package %{$python_prefix}-qt5-devel/' README

popd

# Prepare for update-alternatives usage
for p in pyuic5 pylupdate5 pyrcc5 ; do
    mv %{buildroot}%{_bindir}/$p %{buildroot}%{_bindir}/$p-%{$python_bin_suffix}
done

mv %{buildroot}%{_libqt5_plugindir}/designer/libpyqt5.so %{buildroot}%{_libqt5_plugindir}/designer/libpy%{$python_bin_suffix}qt5.so
mv %{buildroot}%{_libqt5_plugindir}/PyQt5/libpyqt5qmlplugin.so %{buildroot}%{_libqt5_plugindir}/PyQt5/libpy%{$python_bin_suffix}qt5qmlplugin.so
mv -T %{buildroot}%{_datadir}/qt5/qsci/api/python %{buildroot}%{_datadir}/qt5/qsci/api/python_%{$python_bin_suffix}
}

for p in pyuic5 pylupdate5 pyrcc5 ; do
    %prepare_alternative $p
done

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r examples %{buildroot}%{_docdir}/%{name}/
%fdupes %{buildroot}%{_docdir}/%{name}/

%post devel
%{python_install_alternative pyuic5} \
   --slave %{_bindir}/pylupdate5 pylupdate5 %{_bindir}/pylupdate5-%{python_bin_suffix} \
   --slave %{_bindir}/pyrcc5 pyrcc5 %{_bindir}/pyrcc5-%{python_bin_suffix}

%postun devel
%python_uninstall_alternative pyuic5

%files %{python_files}
%license LICENSE
%doc build_%{python_bin_suffix}/README
%doc NEWS ChangeLog
%{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5-%{version}.dist-info/
%{python_sitelib}/dbus/mainloop/pyqt5.so
%dir %{_libqt5_plugindir}/PyQt5/
%{_libqt5_plugindir}/PyQt5/libpy%{python_bin_suffix}qt5qmlplugin.so
%exclude %{_docdir}/%{name}/examples/

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

%files -n %{name}-utils
%{_datadir}/sip/PyQt5/

%files -n %{name}-doc
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/examples/

%changelog
