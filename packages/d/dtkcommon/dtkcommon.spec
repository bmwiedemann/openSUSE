#
# spec file for package dtkcommon
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
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

Name:           dtkcommon
Version:        5.5.2
Release:        0
Summary:        The DTK Tools
License:        GPL-3.0+
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dtkcommon
Source0:        https://github.com/linuxdeepin/dtkcommon/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  glib2-tools 
BuildRequires:  libQt5Core-private-headers-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A public project for building DTK Library

%prep
%setup -q
sed -i 's|$$PREFIX/lib|$$LIB_INSTALL_DIR|g' dtkcommon.pro
sed -i 's|lrelease|lrelease-qt5|g' features/dtk_translation.prf

%build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%qmake5_install

# workaroud boo#1181642
rm %{buildroot}%{_sysconfdir}/dbus-1/system.d/com.deepin.dtk.FileDrag.conf

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
# %config %{_sysconfdir}/dbus-1/system.d/com.deepin.dtk.FileDrag.conf
%dir %{_libdir}/cmake/Dtk
%{_libdir}/cmake/Dtk/DtkConfig.cmake
%{_libdir}/qt5/mkspecs/features/*.prf
%{_libdir}/qt5/mkspecs/modules/qt_lib_dtkcommon.pri
%{_datadir}/glib-2.0/schemas/com.deepin.dtk.gschema.xml

%changelog
