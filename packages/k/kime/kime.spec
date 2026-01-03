#
# spec file for package kime
#
# Copyright (c) 2025 SUSE LLC
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

Name:           kime
Version:        3.1.1
Release:        1
Summary:        Korean IME
License:        GPL-3.0-or-later
Group:          System/I18n/Korean
URL:            https://github.com/Riey/kime
Source:         https://github.com/Riey/kime/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz

BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-base-private-devel
BuildRequires:  update-desktop-files

%description
Kime is a fast Korean Input Method Engine for Linux.
Supports GTK3/4, Qt5/6, XIM and Wayland.

%package devel
Summary:        Development files for kime
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files (headers and library) for kime Korean Input Method Engine.

%package gtk3
Summary:        GTK3 input module for kime
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Supplements:    (%{name} and gtk3)

%description gtk3
GTK3 input module for kime Korean Input Method Engine.

%package gtk4
Summary:        GTK4 input module for kime
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Supplements:    (%{name} and gtk4)

%description gtk4
GTK4 input module for kime Korean Input Method Engine.

%package qt5
Summary:        Qt5 input module for kime
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Supplements:    (%{name} and libQt5Gui5)

%description qt5
Qt5 input module for kime Korean Input Method Engine.

%package qt6
Summary:        Qt6 input module for kime
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Supplements:    (%{name} and qt6-gui)

%description qt6
Qt6 input module for kime Korean Input Method Engine.

%prep
%autosetup -a1

mkdir -p src/frontends/qt6/src
cp src/frontends/qt5/src/{*.cc,*.hpp,kime.json} src/frontends/qt6/src/
mv src/frontends/qt6/src/kime-qt5.hpp src/frontends/qt6/src/kime-qt6.hpp

sed -i 's/kime-qt5\.hpp/kime-qt6.hpp/g' src/frontends/qt6/src/*.cc src/frontends/qt6/src/*.hpp
sed -i 's/QPlatformInputContextFactoryInterface_iid/"org.qt-project.Qt.QPlatformInputContextFactoryInterface"/g' src/frontends/qt6/src/plugin.hpp
sed -i 's|../qt5/src/plugin.cc ../qt5/src/input_context.cc|src/plugin.cc src/input_context.cc|g' src/frontends/qt6/CMakeLists.txt
sed -i 's|target_include_directories(kime-qt6 PRIVATE ${Qt6Gui_PRIVATE_INCLUDE_DIRS}|target_include_directories(kime-qt6 PRIVATE ${Qt6Gui_PRIVATE_INCLUDE_DIRS} ${Qt6Core_PRIVATE_INCLUDE_DIRS} ${Qt6_DIR}/../../../include/qt6/QtGui/${Qt6_VERSION} ${Qt6_DIR}/../../../include/qt6/QtGui/${Qt6_VERSION}/QtGui ${Qt6_DIR}/../../../include/qt6/QtCore/${Qt6_VERSION} ${Qt6_DIR}/../../../include/qt6/QtCore/${Qt6_VERSION}/QtCore|g' src/frontends/qt6/CMakeLists.txt

sed -i 's|#!/usr/bin/env sh|#!/bin/sh|g' res/kime-xdg-autostart

%build
export LIBCLANG_PATH=$(llvm-config --libdir)

cargo build --release --locked -p kime-engine-capi -p kime-engine-cffi
export LIBRARY_PATH="$PWD/target/release:$LIBRARY_PATH"

cargo build --release --locked \
    -p kime -p kime-check -p kime-indicator \
    -p kime-candidate-window -p kime-xim -p kime-wayland

mkdir -p build && cd build
cmake ../src \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DENABLE_GTK3=ON -DENABLE_GTK4=ON \
    -DENABLE_QT5=ON -DENABLE_QT6=ON
%make_build

%install
for bin in kime kime-check kime-indicator kime-candidate-window kime-xim kime-wayland; do
    install -Dm755 target/release/$bin %{buildroot}%{_bindir}/$bin
done
install -Dm755 res/kime-xdg-autostart %{buildroot}%{_bindir}/kime-xdg-autostart

install -Dm755 target/release/libkime_engine.so %{buildroot}%{_libdir}/libkime_engine.so
install -Dm644 src/engine/cffi/kime_engine.h %{buildroot}%{_includedir}/kime_engine.h
install -Dm644 src/engine/cffi/kime_engine.hpp %{buildroot}%{_includedir}/kime_engine.hpp

install -Dm644 res/kime.desktop %{buildroot}%{_datadir}/applications/kime.desktop
install -Dm644 res/kime.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/kime.desktop
install -Dm644 res/icons/64x64/*.png -t %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/kime.desktop

install -Dm755 build/lib/libkime-gtk3.so %{buildroot}%{_libdir}/gtk-3.0/3.0.0/immodules/im-kime.so
install -Dm755 build/lib/libkime-gtk4.so %{buildroot}%{_libdir}/gtk-4.0/4.0.0/immodules/libkime-gtk4.so
install -Dm755 build/lib/libkime-qt5.so %{buildroot}%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
install -Dm755 build/lib/libkime-qt6.so %{buildroot}%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md README.ko.md NOTICE.md docs/CHANGELOG.md docs/CONFIGURATION.md docs/CONFIGURATION.ko.md res/default_config.yaml
%{_bindir}/kime*
%{_libdir}/libkime_engine.so
%{_datadir}/applications/kime.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/kime.desktop
%{_datadir}/icons/hicolor/64x64/apps/kime-*.png

%files devel
%{_includedir}/kime_engine.h
%{_includedir}/kime_engine.hpp

%files gtk3
%dir %{_libdir}/gtk-3.0
%dir %{_libdir}/gtk-3.0/3.0.0
%dir %{_libdir}/gtk-3.0/3.0.0/immodules
%{_libdir}/gtk-3.0/3.0.0/immodules/im-kime.so

%files gtk4
%dir %{_libdir}/gtk-4.0
%dir %{_libdir}/gtk-4.0/4.0.0
%dir %{_libdir}/gtk-4.0/4.0.0/immodules
%{_libdir}/gtk-4.0/4.0.0/immodules/libkime-gtk4.so

%files qt5
%dir %{_libdir}/qt5
%dir %{_libdir}/qt5/plugins
%dir %{_libdir}/qt5/plugins/platforminputcontexts
%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

%files qt6
%dir %{_libdir}/qt6
%dir %{_libdir}/qt6/plugins
%dir %{_libdir}/qt6/plugins/platforminputcontexts
%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

%changelog
