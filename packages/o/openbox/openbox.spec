#
# spec file for package openbox
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           openbox
Provides:       windowmanager
Version:        3.6.1
Release:        0
Summary:        ICCCM and EWMH Compliant Window Manager with Very Few Dependencies
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            http://openbox.org/
Source:         http://openbox.org/dist/openbox/openbox-%{version}.tar.xz
Source1:        %name-README.SuSE
Source2:        %name.desktop
Source3:        %name-pipemenu
Source4:        menu.xml
Source5:        xcompmgr-autostart
Patch1:         %name-3.6.1-return.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
# only for ownership of datadir/share/gnome-sessions/
BuildRequires:  gnome-session-core
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoxft)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
Requires:       xdg-menu
# /usr/bin/openbox-pipemenu launches xsltproc to build up the menu
Requires:       xsltproc
Recommends:     obconf

%description
Openbox is a window manager for the X Window System. It currently runs
on a large list of platforms. It was originally based on Blackbox, but
is, since version 3.0, a complete reimplementation with these features,
among others:

o ICCCM and EWMH compliance o Chainable key bindings o Customizable
mouse actions o Window resistance o Multihead Xinerama support o Pipe
menus

The configuration tool "obconf" is recommended along with this package.

%package -n libobrender32
Summary:        Openbox Render Library
Group:          System/Libraries

%description -n libobrender32
This subpackage contains a utility function library used by Openbox
for theme rendering.

%package -n libobt2
Summary:        Openbox Toolkit Library
Group:          System/Libraries

%description -n libobt2
This subpackage contains a utility function library used by Openbox
to load and parse configuration and theme files of Openbox.

%package gnome
Summary:        Openbox GNOME integration
Group:          System/GUI/Other
Requires:       %{name} = %{version}

%description gnome
This package provides openbox GNOME integration and tools

%package kde
Summary:        Openbox KDE integration
Group:          System/GUI/Other
Requires:       %{name} = %{version}

%description kde
This package provides openbox KDE integration and tools

%package devel
Summary:        Includes and static libraries for openbox
Group:          Development/Libraries/X11
Requires:       libobrender32 = %version
Requires:       libobt2 = %version
Requires:       pkgconfig(ice)
Requires:       pkgconfig(sm)
Requires:       pkgconfig(x11)

%description devel
Development Includes and static libraries for openbox.

%prep
%setup -q
cp %{S:1} ./README.SUSE
%patch1 -p1
mv po/no.po po/nb.po
mv po/no.gmo po/nb.gmo
%__perl -p -i -e 's/^no$/nb/' po/LINGUAS

%build
#autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-static --with-pic
%__make clean
%__make %{?_smp_mflags} V=1

%install
%makeinstall
# we dont want static libs
rm $RPM_BUILD_ROOT%_libdir/*.la
# we dont want the stupid docdir
rm -rf $RPM_BUILD_ROOT%_datadir/doc/%name
# we dont want invalid locales
rm -rf %buildroot/%_datadir/locale/en@boldquot
rm -rf %buildroot/%_datadir/locale/en@quot
# install kdm/gdm entry
install -m 0755 -d $RPM_BUILD_ROOT/%_datadir/xsessions/
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT/%_datadir/xsessions/
install -m 0755 %SOURCE3 $RPM_BUILD_ROOT/%_bindir/%name-pipemenu
install -m 0644 %SOURCE4 $RPM_BUILD_ROOT/%_sysconfdir/xdg/openbox/menu.xml
install -m 0755 %SOURCE5 $RPM_BUILD_ROOT/%_bindir/xcompmgr-autostart
%suse_update_desktop_file $RPM_BUILD_ROOT/%_datadir/applications/%name.desktop
%suse_update_desktop_file $RPM_BUILD_ROOT/%_datadir/xsessions/%name.desktop
%suse_update_desktop_file $RPM_BUILD_ROOT/%_datadir/xsessions/%name-gnome.desktop
%suse_update_desktop_file $RPM_BUILD_ROOT/%_datadir/xsessions/%name-kde.desktop
%suse_update_desktop_file $RPM_BUILD_ROOT/%_datadir/gnome/wm-properties/%name.desktop
%find_lang %name
%fdupes %buildroot/%_prefix
%fdupes -s %buildroot

%post
%desktop_database_post

%postun
%desktop_database_postun

%post   -n libobrender32 -p /sbin/ldconfig
%postun -n libobrender32 -p /sbin/ldconfig
%post   -n libobt2 -p /sbin/ldconfig
%postun -n libobt2 -p /sbin/ldconfig

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING COMPLIANCE README README.SUSE
%doc data/xbm data/menu.xsd doc/rc-mouse-focus.xml data/rc.xsd
%dir %_sysconfdir/xdg/%name
%config(noreplace) %_sysconfdir/xdg/openbox/menu.xml
%config(noreplace) %_sysconfdir/xdg/openbox/rc.xml
%config(noreplace) %_sysconfdir/xdg/openbox/autostart
%config(noreplace) %_sysconfdir/xdg/openbox/environment
%_bindir/obxprop
%_bindir/openbox
%_bindir/openbox-pipemenu
%_bindir/openbox-session
%_bindir/xcompmgr-autostart
%_libexecdir/openbox-autostart
%_libexecdir/openbox-xdg-autostart
%_datadir/xsessions/openbox.desktop
%doc %_mandir/man1/obxprop.1*
%doc %_mandir/man1/openbox-session.1*
%doc %_mandir/man1/openbox.1*
%_datadir/themes/*
%_datadir/pixmaps/openbox.png
%_datadir/applications/openbox.desktop

%files -n libobrender32
%defattr(-,root,root)
%_libdir/libobrender.so.*

%files -n libobt2
%defattr(-,root,root)
%_libdir/libobt.so.*

%files gnome
%defattr(-,root,root)
%_bindir/gdm-control
%_bindir/gnome-panel-control
%_bindir/openbox-gnome-session
%_datadir/xsessions/openbox-gnome.desktop
%dir %_datadir/gnome
%dir %_datadir/gnome/wm-properties
%_datadir/gnome/wm-properties/openbox.desktop
%doc %_mandir/man1/openbox-gnome-session.1*
%_datadir/gnome-session/sessions/openbox-gnome.session
%_datadir/gnome-session/sessions/openbox-gnome-fallback.session

%files kde
%defattr(-,root,root)
%_bindir/openbox-kde-session
%_datadir/xsessions/openbox-kde.desktop
%doc %_mandir/man1/openbox-kde-session.1*

%files devel
%defattr(-,root,root)
%_includedir/%name
%_libdir/pkgconfig/obt-*.pc
%_libdir/pkgconfig/obrender-*.pc
%_libdir/libobt.so
%_libdir/libobrender.so

%changelog
