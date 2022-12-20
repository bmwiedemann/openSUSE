#
# spec file for package xfce4-notifyd
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


Name:           xfce4-notifyd
Version:        0.6.5
Release:        0
Summary:        Simple Notification Daemon for Xfce
License:        GPL-2.0-only
Group:          System/Daemons
URL:            https://docs.xfce.org/apps/notifyd/start
Source:         https://archive.xfce.org/src/apps/xfce4-notifyd/0.6/%{name}-%{version}.tar.bz2
Source1:        %{name}.xml
Source100:      %{name}-rpmlintrc
BuildRequires:  exo-tools
BuildRequires:  intltool
BuildRequires:  update-desktop-files
# BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.10.0
Requires:       libnotify-tools
Requires:       xfce4-notifyd-branding = %{version}-%{release}
Recommends:     %{name}-lang = %{version}-%{release}
Provides:       notification-daemon-xfce = %{version}-%{release}
Obsoletes:      notification-daemon-xfce < %{version}-%{release}

%description
Xfce4-notifyd is a simple, visually-appealing notification daemon for Xfce that
implements the Freedesktop.org Desktop Notifications Specification.

%package branding-upstream
Summary:        Upstream Branding of xfce4-notifyd
# BRAND: xfce4-notifyd.xml: Controls the appearance of notifications.
Group:          System/GUI/XFCE
Conflicts:      otherproviders(xfce4-notifyd-branding)
Provides:       xfce4-notifyd-branding = %{version}-%{release}
Supplements:    packageand(xfce4-notifyd:branding-upstream)
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for the Xfce Notification Daemon.

%lang_package

%prep
%setup -q

%build
# xdt-autogen
%configure \
    --with-helper-path-prefix=%{_libexecdir} \
    --enable-maintainer-mode
%make_build

%install
%make_install

install -D -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-notifyd.xml

%suse_update_desktop_file -i xfce4-notifyd-config
rm %{buildroot}%{_libdir}/xfce4/panel/plugins/*.la

%find_lang %{name} %{?no_lang_C}

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_bindir}/xfce4-notifyd-config
%{_datadir}/applications/xfce4-notifyd-config.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.notification.*
%{_datadir}/icons/hicolor/scalable/status/notification-*symbolic.svg
%dir %{_datadir}/themes/*
%dir %{_datadir}/themes/*/xfce-notify-4.0
%{_datadir}/themes/*/xfce-notify-4.0/gtk.css
%dir %{_libexecdir}/xfce4
%dir %{_libexecdir}/xfce4/notifyd
%{_libexecdir}/xfce4/notifyd/xfce4-notifyd
%{_libdir}/xfce4/panel/plugins/libnotification-plugin.so
%{_datadir}/xfce4/panel/plugins/notification-plugin.desktop
%{_sysconfdir}/xdg/autostart/xfce4-notifyd.desktop
%doc %{_mandir}/man1/xfce4-notifyd-config.1*

%files lang -f %{name}.lang

%files branding-upstream
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-notifyd.xml

%changelog
