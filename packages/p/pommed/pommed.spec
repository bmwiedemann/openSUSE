#
# spec file for package pommed
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


Name:           pommed
Version:        1.39
Release:        0
Summary:        Apple laptops hotkeys event handler
License:        GPL-2.0-only
Group:          Hardware/Mobile
URL:            https://launchpad.net/pommed
Source0:        %{name}-%{version}.tar.bz2
Source1:        pommed.service
Source2:        gpomme.desktop
Source3:        gpommerc
Source5:        pommed.conf
# PATCH-FIX-UPSTREAM pommed-desktop.patch idoenmez@suse.de -- Update desktop categories
Patch1:         pommed-desktop.patch
# PATCH-FIX-OPENSUSE pommed-1.38-cflags.patch idoenmez@suse.de -- Respect our cflags
Patch2:         pommed-1.38-cflags.patch
# PATCH-FIX-OPENSUSE pommed-1.38-hardcoded-libpci.patch idoenmez@suse.de -- Remove hardcoded static pci library
Patch3:         pommed-1.38-hardcoded-libpci.patch
# PATCH-FIX-UPSTREAM pommed-dbus_policy.patch ro@novell.com -- bnc#469771
Patch4:         pommed-dbus_policy.patch
Patch5:         pommed-1.39-multiple-def-lcd_bck_info.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(audiofile)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
Requires:       eject
Requires(post): update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64
%{?systemd_requires}

%description
pommed handles the hotkeys found on the Apple MacBook Pro, MacBook and
PowerBook laptops and adjusts the LCD backlight, sound volume, keyboard
backlight or ejects the CD-ROM drive accordingly.

pommed also monitors the ambient light sensors to automatically light
up the keyboard backlight on the MacBook Pro and PowerBook.

Optional support for the Apple Remote control is available.

%package -n gpomme
Summary:        Graphical client for pommed
Group:          Hardware/Mobile
Requires:       dbus-1
Requires:       pommed

%description -n gpomme
pommed handles the hotkeys found on the Apple MacBook Pro, MacBook and
PowerBook laptops and adjusts the LCD backlight, sound volume, keyboard
backlight or ejects the CD-ROM drive accordingly.

gpomme is a graphical client for pommed. It listens for signals sent by
pommed on DBus and displays the action taken by pommed along with the
current state associated to this action.

%package -n wmpomme
Summary:        WindowMaker dockapp client for pommed
Group:          Hardware/Mobile
Requires:       dbus-1
Requires:       pommed

%description -n wmpomme
pommed handles the hotkeys found on the Apple MacBook Pro, MacBook and
PowerBook laptops and adjusts the LCD backlight, sound volume, keyboard
backlight or ejects the CD-ROM drive accordingly.

wmpomme is a dockapp client for pommed. It displays the current level
of each item controlled by pommed.

%prep
%setup -q
%patch1
%patch2 -p1
%patch3 -p1
%patch4
%patch5 -p1

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_sbindir} %{buildroot}/%{_sysconfdir}/dbus-1/system.d
mkdir -p %{buildroot}/%{_unitdir} %{buildroot}/%{_unitdir}/multi-user.target.wants
mkdir -p %{buildroot}/%{_datadir}/{applications,autostart,icons,pixmaps,gpomme,locale}
mkdir -p %{buildroot}/%{_mandir}/man1 %{buildroot}/%{_datadir}/kde4/config
install -m 755 pommed/pommed          %{buildroot}/%{_sbindir}
install -m 644 dbus-policy.conf   %{buildroot}/%{_sysconfdir}/dbus-1/system.d/pommed.conf
install -m 644 %{SOURCE5}    %{buildroot}/%{_sysconfdir}/pommed.conf
install -m 644 %{SOURCE1}      %{buildroot}%{_unitdir}/pommed.service
ln -s service %{buildroot}/%{_sbindir}/rcpommed
install -m 644 pommed.1               %{buildroot}/%{_mandir}/man1
# gpomme
install -m 755 gpomme/gpomme          %{buildroot}/%{_bindir}
install -m 644 gpomme/gpomme.1        %{buildroot}/%{_mandir}/man1
install -m 644 gpomme/*.desktop       %{buildroot}/%{_datadir}/applications
install -m 644 icons/gpomme*          %{buildroot}/%{_datadir}/icons
install -m 644 icons/gpomme_32x32.xpm %{buildroot}/%{_datadir}/pixmaps/gpomme.xpm
cp -a gpomme/themes                   %{buildroot}/%{_datadir}/gpomme
rm -rfv %{buildroot}/%{_datadir}/gpomme/themes/src
for mo in gpomme/po/*.mo ; do
    lang=`basename $mo .mo`
    filename="gpomme.mo"
    install -d %{buildroot}/%{_datadir}/locale/$lang/LC_MESSAGES
    install -m 644 $mo %{buildroot}/%{_datadir}/locale/$lang/LC_MESSAGES/$filename
done
install -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/autostart
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/kde4/config
# wmpomme
install -m 755 wmpomme/wmpomme        %{buildroot}/%{_bindir}
install -m 644 wmpomme/wmpomme.1      %{buildroot}/%{_mandir}/man1
%suse_update_desktop_file %{buildroot}/%{_datadir}/applications/gpomme-c.desktop
%suse_update_desktop_file %{buildroot}/%{_datadir}/applications/gpomme.desktop
# enable videoswitch
mkdir -p %{buildroot}/%{_sysconfdir}/pommed
install -m 644 icons/gpomme_32x32.xpm %{buildroot}/%{_datadir}/icons/wmpomme.xpm
install -m 644 icons/gpomme_32x32.xpm %{buildroot}/%{_datadir}/pixmaps/gpomme.xpm

%fdupes -s %{buildroot}
%find_lang gpomme

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%post -n gpomme
%desktop_database_post
%icon_theme_cache_post

%postun -n gpomme
%icon_theme_cache_postun
%desktop_database_postun

%post -n wmpomme
%icon_theme_cache_post

%postun -n wmpomme
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS README TODO COPYING
%config(noreplace) %{_sysconfdir}/pommed.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/pommed.conf
%{_sbindir}/pommed
%{_sbindir}/rcpommed
%{_mandir}/man1/po*
%{_unitdir}/%{name}.service

%files -n gpomme -f gpomme.lang
%defattr(-,root,root)
%{_bindir}/gpomme
%{_datadir}/applications/*.desktop
%{_datadir}/icons/gp*
%{_datadir}/pixmaps/gp*
%{_datadir}/gpomme
%{_datadir}/autostart
%dir %{_datadir}/kde4
%{_datadir}/kde4/config
%{_mandir}/man1/gpo*

%files -n wmpomme
%defattr(-,root,root)
%{_bindir}/wmpomme
%{_datadir}/icons/wm*
%{_mandir}/man1/wmpo*

%changelog
