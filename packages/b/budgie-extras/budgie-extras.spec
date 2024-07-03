#
# spec file for package budgie-extras
#
# Copyright (c) 2023 SUSE LLC
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

%if %{pkg_vcmp budgie-desktop-devel >= 10.8}
%bcond_without budgie_10_8
%else
%bcond_with budgie_10_8
%endif
%if %{undefined _distconfdir}
%define _distconfdir %{_sysconfdir}
%endif
Name:           budgie-extras
Version:        1.7.1
Release:        0
Summary:        Additional Budgie Desktop enhancements for user experience
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/UbuntuBudgie/%{name}
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(budgie-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(plank)
# All applets
Recommends:     budgie-app-launcher-applet
Recommends:     budgie-brightness-controller-applet
Recommends:     budgie-clockworks-applet
Recommends:     budgie-countdown-applet
Recommends:     budgie-dropby-applet
Recommends:     budgie-fuzzyclock-applet
Recommends:     budgie-hotcorners-applet
Recommends:     budgie-kangaroo-applet
Recommends:     budgie-keyboard-autoswitch-applet
Recommends:     budgie-network-manager-applet
Recommends:     budgie-previews
Recommends:     budgie-quickchar
Recommends:     budgie-quicknote-applet
Recommends:     budgie-recentlyused-applet
Recommends:     budgie-rotation-lock-applet
Recommends:     budgie-showtime-applet
Recommends:     budgie-takeabreak-applet
Recommends:     budgie-trash-applet
Recommends:     budgie-visualspace-applet
Recommends:     budgie-wallstreet
Recommends:     budgie-weathershow-applet
Recommends:     budgie-window-shuffler
Recommends:     budgie-workspace-stopwatch-applet
Recommends:     budgie-workspace-wallpaper-applet

%description
Additional Budgie Desktop enhancements for the user experience

%package -n budgie-app-launcher-applet
Summary:        App Launcher applet
Group:          System/GUI/Other
Requires:       python3-gobject-Gdk

%description -n budgie-app-launcher-applet
App Launcher is a Budgie Desktop applet for productivity. This applet lists your favourite apps.

%package -n budgie-applications-menu-applet
Summary:        Stylish Applications Menu for Budgie-Desktop
Group:          System/GUI/Other
Requires:       budgie-extras-lang
Requires:       gnome-menus

%description -n budgie-applications-menu-applet
The application-menu is a stylish panel applet that displays applications
in different views - grid and list. Weblinks typed into the search bar
can be opened in your default browser. Applications that have additional
desktop options show via a right-click menu. Applications with associated
actions show those actions are additional searchable entries.

%package -n budgie-brightness-controller-applet
Summary:        Brightness controller applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang

%description -n budgie-brightness-controller-applet
Brightness Controller is a Budgie Desktop applet for productivity.

%package -n budgie-clockworks-applet
Summary:        Clockworks applet
Group:          System/GUI/Other
Requires:       python3-CairoSVG
Requires:       python3-Pillow
Requires:       python3-gobject-Gdk
Requires:       python3-svgwrite

%description -n budgie-clockworks-applet
A multi-clock applet to show the time across multiple timezones.
Clocks can be created and deleted in a single click, and easily be (re-) named.
Timezones can be looked up from the applet's popup menu.

%package -n budgie-countdown-applet
Summary:        Countdown applet
Group:          System/GUI/Other
Requires:       python3-gobject-Gdk
Requires:       python3-psutil
Requires:       sound-theme-freedesktop
Requires:       vorbis-tools
Requires:       zenity

%description -n budgie-countdown-applet
A count down applet with the following options: ring a bell, flash the (panel) icon, display a message window or run a (any) command.
The applet also offers the option to overrule possible user settings on suspend, to keep the clock going while time is running.

%package -n budgie-dropby-applet
Summary:        DropBy applet
Group:          System/GUI/Other
Requires:       python3-gobject-Gdk
Requires:       python3-psutil
Requires:       python3-pyudev
Requires:       util-linux
Requires:       wmctrl
Requires:       zenity

%description -n budgie-dropby-applet
The DropBy applet pops up on the occasion of connecting a usb device.
The applet subsequently offers the option(s) to mount, unmount/eject, and, in case of a flash drive, to make a local copy of the drive's content.
The info shows the free space on the volume.

%package daemon
Summary:        Daemon for Budgie Extras
Group:          System/GUI/Other

%description daemon
This on logon process manages keyboard shortcuts delivered via .bde files for various extras-plugins.

%package -n budgie-fuzzyclock-applet
Summary:        Fuzzyclock Applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang

%description -n budgie-fuzzyclock-applet
This applet shows the time in a Fuzzy Way.

%package -n budgie-hotcorners-applet
Summary:        Hotcorners applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang
Requires:       budgie-screensaver
Requires:       dconf
Requires:       libnotify-tools
Requires:       xdotool

%description -n budgie-hotcorners-applet
Hotcorners offers the option to set corner actions, both from preset and custom commands.
Pressure can be set from Budgie Settings.
This is the new Vala-based hotcorners applet.

%package -n budgie-kangaroo-applet
Summary:        Kangaroo applet
Group:          System/GUI/Other
Requires:       python3-gobject-Gdk
Requires:       python3-psutil
Requires:       xdg-utils
Requires:       zenity

%description -n budgie-kangaroo-applet
Kangaroo is an applet for quick & easy browsing, across (possibly) many directory layers, without having to do a single mouse click.

%package -n budgie-keyboard-autoswitch-applet
Summary:        Keyboard autoswitch applet
Group:          System/GUI/Other
Requires:       python3-gobject-Gdk
Requires:       python3-psutil
Requires:       wmctrl
Requires:       xdpyinfo
Requires:       xev
Requires:       xlsatoms
Requires:       xlsclients
Requires:       xlsfonts
Requires:       xprop
Requires:       xvinfo
Requires:       xwininfo

%description -n budgie-keyboard-autoswitch-applet
Keyboard Auto Switch is an applet to use a different input keyboard layout per application.
Simply set a default layout to be used in general.
Subsequently, simply set a different layout, with the application's window in front, and an exception for that specific application is remembered.

%package -n budgie-network-manager-applet
Summary:        Network manager applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang

%description -n budgie-network-manager-applet
This is a fork of Wingpanel Network Indicator, ported to budgie desktop

%package -n budgie-previews
Summary:        Previews applet
Group:          System/GUI/Other
Requires:       budgie-extras-daemon
Requires:       xinput
Requires:       xprintidle

%description -n budgie-previews
Provides window previews capabilities for the Budgie Desktop

%package -n budgie-quickchar
Summary:        Quickchar applet
Group:          System/GUI/Other
Requires:       budgie-extras-daemon
Requires:       python3-gobject-Gdk
Requires:       python3-pyperclip
Requires:       python3-python-xlib
Requires:       wmctrl
Requires:       xdpyinfo
Requires:       xev
Requires:       xlsatoms
Requires:       xlsclients
Requires:       xlsfonts
Requires:       xprop
Requires:       xvinfo
Requires:       xwininfo

%description -n budgie-quickchar
QuickChar is a mini-app to quickly choose and insert equivalents of ascii characters.
QuickChar is activated via the Budgie Menu.

%package -n budgie-quicknote-applet
Summary:        Quicknote applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang

%description -n budgie-quicknote-applet
Quicknote is an applet to provide the easiest possible way to make small notes.
Just click the icon and write down your notes.
QuickNote autosaves the text while writing, and comes with a ten- level undo/redo function.

%package -n budgie-recentlyused-applet
Summary:        Recently Used applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang
Requires:       xdg-utils

%description -n budgie-recentlyused-applet
Show (Gtk applications') recently used items in a menu.

%package -n budgie-rotation-lock-applet
Summary:        Rotationlock applet
Group:          System/GUI/Other
Requires:       python3-gobject-Gdk

%description -n budgie-rotation-lock-applet
RotationLock is a simple applet that lets you toggle the "Rotation Lock" feature for Budgie.

%package -n budgie-showtime-applet
Summary:        Showtime applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang
Requires:       dconf

%description -n budgie-showtime-applet
Budgie Showtime is a digital desktop clock, showing time, and optionally, date.
Textcolor of both can be set separately from the applet's menu.

%package -n budgie-takeabreak-applet
Summary:        Takeabreak applet
Group:          System/GUI/Other
Requires:       iceauth
Requires:       python3-gobject-Gdk
Requires:       rgb
Requires:       sessreg
Requires:       xcmsdb
Requires:       xgamma
Requires:       xhost
Requires:       xmodmap
Requires:       xrandr
Requires:       xrdb
Requires:       xrefresh
Requires:       xset
Requires:       xsetmode
Requires:       xsetpointer
Requires:       xsetroot
Requires:       xstdcmap
Requires:       xvidtune

%description -n budgie-takeabreak-applet
Budgie TakeaBreak is a pomodoro- like applet, to make sure to take regular breaks from working.
Options from Budgie Settings include turning the screen upside down, dim the screen, lock screen or show a countdown message on break time.
The applet can be accessed quickly from the panel to temporarily switch it off.

%if %{without budgie_10_8}
%package -n budgie-trash-applet
Summary:        Trash applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang

%description -n budgie-trash-applet
Trash is a Budgie Desktop applet for productivity.
%endif

%package -n budgie-visualspace-applet
Summary:        Visualspace applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang

%description -n budgie-visualspace-applet
Budgie VisualSpace shows the current workspace(s), as bullet(s).
The applet includes a menu to navigate to either one of the windows or their corresponding workspace.

%package -n budgie-wallstreet
Summary:        Wallstreet applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang

%description -n budgie-wallstreet
Budgie WallStreet is a mini-app to switch wallpapers on regular intervalls.

%package -n budgie-weathershow-applet
Summary:        Weathershow applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang
Requires:       dconf
Requires:       procps

%description -n budgie-weathershow-applet
WeatherShowII is a completely rewritten version of the existing python WeatherShow applet.

%package -n budgie-window-shuffler
Summary:        Window shuffler applet
Group:          System/GUI/Other
Requires:       budgie-extras-daemon
Requires:       budgie-extras-lang
Requires:       xdpyinfo
Requires:       xev
Requires:       xlsatoms
Requires:       xlsclients
Requires:       xlsfonts
Requires:       xprop
Requires:       xvinfo
Requires:       xwininfo

%description -n budgie-window-shuffler
GUI and keyboard friendly window arranger for the budgie desktop

%package -n budgie-workspace-stopwatch-applet
Summary:        Workspace stopwatch applet
Group:          System/GUI/Other
Requires:       python3-gobject-Gdk

%description -n budgie-workspace-stopwatch-applet
Workspace Timer Applet is an applet to keep track of usage per workspace, e.g. to find out how much minutes/hours were actually spent on a job.
Workspaces can be freely named, custom names and all data are rmembered, also after logout/restart, until the RESET button is pressed.

%package -n budgie-workspace-wallpaper-applet
Summary:        Workspace Wallpaper applet
Group:          System/GUI/Other
Requires:       budgie-extras-lang

%description -n budgie-workspace-wallpaper-applet
Budgie Wallpaper Workspace Switcher is an application (applet) to show a different wallpaper on each of the workspaces.

%lang_package

%prep
%autosetup -p1

%build
# Handle poor vala code
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson \
  -Dxdg-appdir=%{_distconfdir}/xdg/autostart \
  -Dwith-zeitgeist=false \
  -Dbuild-recommended=true \
  -Dwith-default-schema=false \
%if %{without budgie_10_8}
  -Dbuild-trash=true \
%endif
  %{nil}

%meson_build

%install
%meson_install
find %{buildroot} -name '*.py' -type f -print -exec chmod 755 {} \;
find %{buildroot} -type f -exec sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|g' {} \;
chmod 0644 LICENSE
%find_lang %{name}
%fdupes -s %{buildroot}

%files
%license LICENSE
%doc README.md

%files daemon
%{_datadir}/budgie-desktop
%{_libdir}/budgie-extras-daemon
%{_datadir}/budgie-extras-daemon
%{_bindir}/budgie-extras-daemon
%{_mandir}/man1/budgie-extras-daemon.1%{?ext_man}
%{_distconfdir}/xdg/autostart/budgie-extras-daemon.desktop

%files -n budgie-app-launcher-applet
%{_libdir}/budgie-desktop/plugins/budgie-app-launcher
%{_datadir}/pixmaps/budgie-app-launcher-applet-symbolic.svg
%{_datadir}/pixmaps/budgie-app-launcher-edit-symbolic.svg

%files -n budgie-applications-menu-applet
%{_libdir}/budgie-desktop/plugins/applications-menu
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-appmenu.gschema.xml

%files -n budgie-brightness-controller-applet
%{_libdir}/budgie-desktop/plugins/budgie-brightness-controller
%{_datadir}/pixmaps/budgie-brightness-controller-1-symbolic.svg

%files -n budgie-clockworks-applet
%{_libdir}/budgie-desktop/plugins/budgie-clockworks
%{_datadir}/pixmaps/budgie-clockworks-symbolic.svg
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-clockworks.gschema.xml

%files -n budgie-countdown-applet
%{_datadir}/pixmaps/cr*.png
%{_datadir}/pixmaps/budgie-countdown-symbolic.svg
%{_libdir}/budgie-desktop/plugins/budgie-countdown
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-countdown.gschema.xml

%files -n budgie-dropby-applet
%{_datadir}/pixmaps/budgie-dropby*.svg
%{_libdir}/budgie-desktop/plugins/budgie-dropby
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-dropby.gschema.xml

%files -n budgie-fuzzyclock-applet
%{_libdir}/budgie-desktop/plugins/budgie-fuzzyclock

%files -n budgie-hotcorners-applet
%{_libexecdir}/budgie-hotcorners
%{_datadir}/budgie-hotcorners
%{_distconfdir}/xdg/autostart/org.ubuntubudgie.budgie-extras.HotCorners-autostart.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.ubuntubudgie.budgie-extras.hotcorners.svg
%{_datadir}/applications/org.ubuntubudgie.budgie-extras.HotCorners.desktop
%{_datadir}/pixmaps/budgie-hotcorners-symbolic.svg
%{_datadir}/pixmaps/budgie-hotcgui*.svg
%{_libdir}/budgie-desktop/plugins/budgie-hotcorners
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.budgie-extras.HotCorners.gschema.xml

%files -n budgie-kangaroo-applet
%{_datadir}/pixmaps/budgie-foldertrack-symbolic.svg
%{_libdir}/budgie-desktop/plugins/budgie-kangaroo

%files -n budgie-keyboard-autoswitch-applet
%{_datadir}/pixmaps/budgie-keyboard-autoswitch-symbolic.svg
%{_libdir}/budgie-desktop/plugins/budgie-keyboard-autoswitch

%files -n budgie-network-manager-applet
%{_libdir}/budgie-desktop/plugins/budgie-network-manager

%files -n budgie-previews
%{_libdir}/budgie-previews
%{_datadir}/pixmaps/budgie_wpreviews_*.png
%{_datadir}/applications/org.ubuntubudgie.previewscontrols.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.ubuntubudgie.budgiewpreviews.svg
%{_datadir}/metainfo/org.ubuntubudgie.previewscontrols.metainfo.xml
%{_distconfdir}/xdg/autostart/previews-creator-autostart.desktop
%{_distconfdir}/xdg/autostart/previews-daemon-autostart.desktop
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.budgie-wpreviews.gschema.xml

%files -n budgie-quickchar
%{_bindir}/quickchar
%{_libdir}/quickchar
%{_datadir}/quickchar
%{_datadir}/applications/org.ubuntubudgie.quickchar.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.ubuntubudgie.quickchar.svg
%{_datadir}/metainfo/org.ubuntubudgie.quickchar.metainfo.xml
%{_distconfdir}/xdg/autostart/quickchar-autostart.desktop
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.quickchar.gschema.xml
%{_mandir}/man1/quickchar.1%{?ext_man}

%files -n budgie-quicknote-applet
%{_datadir}/pixmaps/budgie-quicknote-symbolic.svg
%{_libdir}/budgie-desktop/plugins/budgie-quicknote
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.quicknote.gschema.xml

%files -n budgie-recentlyused-applet
%{_libdir}/budgie-desktop/plugins/budgie-recentlyused
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-recentlyused.gschema.xml

%files -n budgie-rotation-lock-applet
%{_datadir}/pixmaps/budgie-rotation-*.svg
%{_libdir}/budgie-desktop/plugins/budgie-rotation-lock

%files -n budgie-showtime-applet
%{_datadir}/pixmaps/showtimenew-symbolic.svg
%{_libdir}/budgie-desktop/plugins/budgie-showtime
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-showtime.gschema.xml

%files -n budgie-takeabreak-applet
%{_datadir}/pixmaps/takeabreak*.svg
%{_libdir}/budgie-desktop/plugins/budgie-takeabreak
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.takeabreak.gschema.xml

%if %{without budgie_10_8}
%files -n budgie-trash-applet
%{_libdir}/budgie-desktop/plugins/budgie-trash
%endif

%files -n budgie-visualspace-applet
%{_datadir}/pixmaps/visualspace-symbolic.svg
%{_libdir}/budgie-desktop/plugins/budgie-visualspace
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-visualspace.gschema.xml
%{_distconfdir}/xdg/autostart/visualspace-autostart.desktop

%files -n budgie-wallstreet
%{_libdir}/budgie-wallstreet
%{_datadir}/applications/org.ubuntubudgie.wallstreetcontrol.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.ubuntubudgie.wallstreet-control.svg
%{_datadir}/metainfo/org.ubuntubudgie.wallstreetcontrol.metainfo.xml
%{_distconfdir}/xdg/autostart/wallstreet-autostart.desktop
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.budgie-wallstreet.gschema.xml

%files -n budgie-weathershow-applet
%{_libdir}/budgie-desktop/plugins/budgie-weathershow
%{_datadir}/pixmaps/budgie-wticon-symbolic.svg
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.weathershow.gschema.xml

%files -n budgie-window-shuffler
%{_libdir}/budgie-window-shuffler
%{_libdir}/budgie-desktop/plugins/budgie-window-shuffler
%{_datadir}/applications/org.ubuntubudgie.shufflercontrol.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.ubuntubudgie.shuffler-control.svg
%{_datadir}/metainfo/org.ubuntubudgie.shufflercontrol.metainfo.xml
%{_datadir}/pixmaps/shuffler*.svg
%{_datadir}/pixmaps/dragsnapimg*.svg
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.windowshuffler.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-shufflerapplet.gschema.xml
%{_distconfdir}/xdg/autostart/shufflerdaemon-autostart.desktop
%{_distconfdir}/xdg/autostart/shufflergui-autostart.desktop
%{_distconfdir}/xdg/autostart/layoutspopup-autostart.desktop
%{_distconfdir}/xdg/autostart/dragsnap-autostart.desktop

%files -n budgie-workspace-stopwatch-applet
%{_datadir}/pixmaps/budgie-wstopwatch-symbolic.svg
%{_libdir}/budgie-desktop/plugins/budgie-workspace-stopwatch

%files -n budgie-workspace-wallpaper-applet
%{_datadir}/pixmaps/budgie-wsw-symbolic.svg
%{_libdir}/budgie-desktop/plugins/budgie-wswitcher
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-wswitcher.gschema.xml

%files lang -f %{name}.lang

%changelog
