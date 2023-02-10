#
# spec file for package python-qt5
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "nonring-extras"
# These modules are not in staging
%if 0%{?_with_ringdisabled}
ExclusiveArch:  do_not_build
%else
%define build_nonring 1
%endif
%endif

%define oldpython python
%define mname qt5
Name:           python-%{mname}
Version:        5.15.9
Release:        0
Summary:        Python bindings for Qt 5
License:        SUSE-GPL-2.0-with-FLOSS-exception OR GPL-3.0-only OR NonFree
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqt
Source:         https://files.pythonhosted.org/packages/source/P/PyQt5/PyQt5-%{version}.tar.gz
Source99:       python-qt5-rpmlintrc
# PATCH-FIX-OPENSUSE - disable-rpaths.diff - Disable RPATH when building PyQt5.
Patch0:         disable-rpaths.diff
# PATCH-FIX-OPENSUSE - install binary dbus mainloop integration in arch dependent directory
Patch1:         0001-Use-a-noarch-wrapper-for-dbus-mainloop-integration.patch
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
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
%if 0%{?build_nonring}
BuildRequires:  pkgconfig(Qt5Quick3D)
BuildRequires:  pkgconfig(Qt5RemoteObjects)
%endif
BuildRequires:  %{python_module pyqt-builder >= 1.14.1}
BuildRequires:  %{python_module qt5-sip >= 12.11}
BuildRequires:  %{python_module sip-devel >= 6.6.2}
Requires:       python-qt5-sip >= 12.11
%requires_ge    python-dbus-python
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
# silence rpmlint
Requires:       %{oldpython}(abi) = %{python_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
# If and which version of sip is required depends on the project trying
# to build against PyQt5.
Recommends:     python-sip-devel
Recommends:     python-qscintilla-qt5
Recommends:     pkgconfig(Qt5Quick3D)
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
Requires:       %{oldpython}(abi) = %{python_version}

%description quick3d-devel
PyQt is a set of Python bindings for the Qt framework.

This package contains all the developer tools you need to create your
own PyQt applications with QtQuick3D

%package remoteobjects-devel
Summary:        PyQt - devel part of python bindings for QtRemoteObjects
Group:          Development/Libraries/Python
Requires:       python-%{mname}-devel = %{version}
Requires:       pkgconfig(Qt5RemoteObjects)
Requires:       %{oldpython}(abi) = %{python_version}

%description remoteobjects-devel
PyQt is a set of Python bindings for the Qt framework.

This package contains all the developer tools you need to create your
own PyQt applications with QtRemoteObjects

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
Requires:       python-qt5 = %{version}

%description quick3d
PyQt is a set of Python bindings for the Qt framework.

This package contains the extension for QtQuick3D.

%package remoteobjects
Summary:        Python bindings for QtRemoteObjects
Group:          Development/Libraries/Python
Requires:       python-qt5 = %{version}

%description remoteobjects
PyQt is a set of Python bindings for the Qt framework.

This package contains the extension for QtRemoteObjects.

%prep
%autosetup -p1 -n PyQt5-%{version}
chmod -x examples/activeqt/webbrowser/webbrowser.py
dos2unix examples/tools/codecs/encodedfiles/iso-8859-1.txt
dos2unix examples/tools/codecs/encodedfiles/iso-8859-15.txt

# remove argument to `#define PY_SSIZE_T_CLEAN`
# before any `#include <Python.h>` which was introduced by SIP 6.4
# for Python 3.10 builds but prevents downstream packages stuck on
# SIP v4 or SIP v5 (qgis) from building -- boo#1192300
# https://docs.python.org/3/c-api/arg.html#arg-parsing
  sed -e 's/, py_ssize_t_clean=True//' \
      -i sip/QtCore/QtCoremod.sip

%build
# sip-build requires QtCore as target, even if we want a nonring module only
%{pyqt_build -v \
    -s %{quote:--pep484-pyi \
               --confirm-license \
               --qt-shared \
               %{!?build_nonring: --disable QtQuick3D --disable QtRemoteObjects} \
               %{?build_nonring: --enable QtQuick3D --enable QtRemoteObjects \
               --enable QtCore \
               --no-dbus-python \
               --no-designer-plugin \
               --no-qml-plugin \
               --no-tools}}}

%install
%if ! 0%{?build_nonring}
%pyqt_install
%pyqt_install_examples %mname

%python_clone -a %{buildroot}%{_bindir}/pyuic5
%python_clone -a %{buildroot}%{_bindir}/pylupdate5
%python_clone -a %{buildroot}%{_bindir}/pyrcc5

# Provide the legacy path to the SIP files for packages stuck on sip4
mkdir -p %{buildroot}%{_datadir}/sip/
%{python_expand ln -sr \
  %{buildroot}%{$python_sitearch}/PyQt5/bindings \
  %{buildroot}%{_datadir}/pyqt5-sip-%{$python_bin_suffix}
}
%prepare_alternative -t %{_datadir}/sip/PyQt5 pyqt5-sip
%else
%{python_expand pushd build
%__make sub-QtQuick3D-install_subtargets-ordered \
        sub-QtRemoteObjects-install_subtargets-ordered \
        INSTALL="%__install -p" INSTALL_ROOT=%{buildroot}
popd
}
%endif

%{python_expand %fdupes %{buildroot}%{$python_sitearch}}

%if ! 0%{?build_nonring}
%pre devel
# boo#1178814 -- migration to update-alternatives, part 1
# If it exists but is not a link yet, move existing old directory before cpio
# starts to unpack the archive and tries to create the update-alternatives link
if [ -d %{_datadir}/sip/PyQt5 -a ! -L %{_datadir}/sip/PyQt5 ]; then
  mv %{_datadir}/sip/PyQt5 %{_datadir}/sip/PyQt5~
fi

%post devel
%{python_install_alternative pyuic5 pylupdate5 pyrcc5} \
   --slave %{_datadir}/sip/PyQt5 pyqt5-sip %{_datadir}/pyqt5-sip-%{python_bin_suffix}
# boo#1178814 -- migration to update-alternatives, part 2
# temporaryily disable the u-a slave link again so that package removals later
# in the same transaction, e.g. obsoleted python-qt5-devel-common don't remove
# the freshly installed binding files
if [ -d %{_datadir}/sip/PyQt5~ ]; then
  mv %{_datadir}/sip/PyQt5 %{_datadir}/sip/PyQt5.u-a-link
  mv %{_datadir}/sip/PyQt5~ %{_datadir}/sip/PyQt5
fi

%postun devel
%python_uninstall_alternative pyuic5

%posttrans devel
# boo#1178814 -- migration to update-alternatives, part 3
if [ ! -L  %{_datadir}/sip/PyQt5 ]; then
  # move remaining files from foreign packages, if any, into new 
  # bindings dir
  find %{_datadir}/sip/PyQt5/ -mindepth 1 -maxdepth 1 -exec \
    mv '{}' %{_datadir}/pyqt5-sip-%{python_bin_suffix}/ \;
  rmdir %{_datadir}/sip/PyQt5
  # restore the u-a link after all old packages have been removed
  mv %{_datadir}/sip/PyQt5.u-a-link %{_datadir}/sip/PyQt5
fi

%files %{python_files}
%license LICENSE
%doc README NEWS ChangeLog
%{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5-%{version}.dist-info/
%exclude %pyqt5_sipdir
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
%doc README
%dir %{python_sitearch}/PyQt5
%{python_sitearch}/PyQt5/QtQuick3D*
%sip5_only %exclude %{python_sitearch}/PyQt5/QtCore*
%sip5_only %exclude %pyqt5_sipdir

%files %{python_files quick3d-devel}
%license LICENSE
%dir %pyqt5_sipdir
%pyqt5_sipdir/QtQuick3D
%exclude %pyqt5_sipdir/QtCore

%files %{python_files remoteobjects}
%license LICENSE
%doc README
%dir %{python_sitearch}/PyQt5
%{python_sitearch}/PyQt5/QtRemoteObjects*
%exclude %{python_sitearch}/PyQt5/QtCore*
%exclude %pyqt5_sipdir

%files %{python_files remoteobjects-devel}
%license LICENSE
# sip v4 builds have the sip files in the regular devel package
%dir %pyqt5_sipdir
%pyqt5_sipdir/QtRemoteObjects
%exclude %pyqt5_sipdir/QtCore

%endif

%changelog
