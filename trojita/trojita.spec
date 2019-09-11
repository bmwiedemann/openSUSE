#
# spec file for package trojita
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define         X_display         ":98"
Name:           trojita
Version:        0.7
Release:        0
Summary:        Qt5 IMAP e-mail client
License:        (GPL-2.0 or GPL-3.0) and BSD-3-Clause and LGPL-2.0 and (LGPL-2.1 or GPL-3.0) and LGPL-2.1+ and GPL-2.0
Group:          Productivity/Networking/Email/Clients
# Almost everything: dual-licensed under the GPLv2 or GPLv3
# (with KDE e.V. provision for relicensing)
# src/XtConnect: BSD
# src/Imap/Parser/3rdparty/kcodecs.*: LGPLv2
# Nokia imports: LGPLv2.1 or GPLv3
# src/Imap/Parser/3rdparty/rfccodecs.cpp: LGPLv2+
# src/qwwsmtpclient/: GPLv2
Url:            http://trojita.flaska.net/
Source:         http://sourceforge.net/projects/trojita/files/src/%{name}-%{version}.tar.xz
Source1:        http://sourceforge.net/projects/trojita/files/src/%{name}-%{version}.tar.xz.asc
# PATCH-FIX-OPENSUSE
Patch:          Skip-QtWebKit-tests.patch
# PATCH-FIX-UPSTREAM
Patch1:         tests-Fix-build-with-Qt-5.13.patch
BuildRequires:  cmake >= 2.8.7
BuildRequires:  git
BuildRequires:  gpgmepp5-devel
BuildRequires:  libqt5-linguist-devel >= 5.2.0
BuildRequires:  libqt5-sql-sqlite
BuildRequires:  pkgconfig
BuildRequires:  qtkeychain-qt5-devel
BuildRequires:  ragel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Trojita is a Qt IMAP e-mail client which:
  * Enables you to access your mail anytime, anywhere.
  * Does not slow you down. If we can improve the productivity of an e-mail user, we better do.
  * Respects open standards and facilitates modern technologies. We value the vendor-neutrality that IMAP provides and are committed to be as interoperable as possible.
  * Is efficient — be it at conserving the network bandwidth, keeping memory use at a reasonable level or not hogging the system's CPU.
  * Can be used on many platforms. One UI is not enough for everyone, but our IMAP core works fine on anything from desktop computers to cell phones and big ERP systems.
  * Plays well with the rest of the ecosystem. We don't like reinventing wheels, but when the existing wheels quite don't fit the tracks, we're not afraid of making them work.

%prep
%setup -q
%autopatch -p1

%build
export CXXFLAGS="%{optflags} -fPIC"
export LDFLAGS="-pie"
%cmake \
	-DWITH_TESTS=ON \
	-DWITH_QT5=ON \
	-DWITH_ZLIB=ON \
	-DWITH_RAGEL=OFF \
	-DWITH_SHARED_PLUGINS=ON
make %{?_smp_mflags}

%install
cd build
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%suse_update_desktop_file %{buildroot}/%{_datadir}/applications/trojita.desktop

%check
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}${LD_LIBRARY_PATH:+:}%{buildroot}%{_libdir}"
export DISPLAY=%{X_display}
Xvfb %{X_display} &
trap "kill $! || true" EXIT
cd build
ctest --output-on-failure

%files
%defattr(-,root,root)
%doc LICENSE README
%{_libdir}/libtrojita_plugins.so
%dir %{_libdir}/trojita
%{_libdir}/trojita/trojita_plugin_QtKeychainPasswordPlugin.so
%{_bindir}/trojita
%{_bindir}/be.contacts
%{_datadir}/applications/trojita.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/32x32/apps/trojita.png
%{_datadir}/icons/hicolor/scalable/apps/trojita.svg
%dir %{_datadir}/trojita
%dir %{_datadir}/trojita/locale
%{_datadir}/trojita/locale/trojita_common_*.qm
%dir %{_datadir}/appdata
%{_datadir}/appdata/trojita.appdata.xml

%changelog
