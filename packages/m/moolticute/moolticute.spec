#
# spec file for package moolticute
#
# Copyright (c) 2022 SUSE LLC
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


%global UDEVDIR %{_udevrulesdir}
%global QMAKE_BIN qmake-qt5
Name:           moolticute
Version:        1.00.1.r0.gf211d93
Release:        0
Summary:        Companion GUI application for Mooltipass password manager devices
License:        GPL-3.0-only
URL:            https://github.com/mooltipass/moolticute
Source0:        %{name}-%{version}.tar.gz
Source1:        69-mooltipass.rules
Source2:        README.SUSE
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libudev)
Conflicts:      moolticute-testing

%description
This project aims to be an easy to use companion to your Mooltipass device and extend the power of the device to more platform/tools. With it you can manage your Mooltipass with a cross-platform app, as well as provide a daemon service that handles all USB communication with the device. This tool comes with a daemon that runs in background, and a user interface app to control your Mooltipass. Other clients can also connect and talk to the daemon (it uses a websocket connection and simple JSON messages). It is completely cross platform, and runs on Linux (using native hidraw API), OS X (native IOKit API), and Windows (native HID API).

%prep
%autosetup

%build
%{QMAKE_BIN} PREFIX=%{_prefix} DESTDIR= Moolticute.pro
%make_build sub-daemon-pro-all sub-gui-pro-all

%install
install -d 555 %{buildroot}%{_sbindir}
install -d 555 %{buildroot}%{_bindir}
install -d 755 %{buildroot}%{UDEVDIR}
install -m 644 %{_sourcedir}/69-mooltipass.rules %{buildroot}%{UDEVDIR}/.

%make_install PREFIX=%{_prefix} INSTALL_ROOT=%{buildroot}

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcmoolticuted

install -m 644 -D %{SOURCE2} %{buildroot}%{_docdir}/%{name}/README.SUSE

%files
%license LICENSE
%{_bindir}/moolticute
%{_bindir}/moolticuted
%{UDEVDIR}/69-mooltipass.rules
%{_sbindir}/rcmoolticuted
%{_prefix}/lib/systemd/system/moolticuted.service
%{_datadir}/applications/moolticute.desktop
%{_datadir}/icons/hicolor/128x128/apps/moolticute.png
%{_datadir}/icons/hicolor/32x32/apps/moolticute.png
%{_datadir}/icons/hicolor/scalable/apps/moolticute.svg
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%dir %{_docdir}/moolticute
%{_docdir}/moolticute/README.SUSE

%pre
%service_add_pre moolticuted.service

%post
%service_add_post moolticuted.service

%preun
%service_del_preun moolticuted.service

%postun
%service_del_postun moolticuted.service

%changelog
