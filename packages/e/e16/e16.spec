#
# spec file for package e16
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


%define enable_sound       0
%define enable_hints_gnome 0
%define enable_zoom        1
%define enable_xrandr      1
%define enable_composite   1
%define enable_pango       1
Name:           e16
Version:        1.0.19
Release:        0
Summary:        A Window Manager for the X Window System
License:        MIT-advertising AND GPL-2.0-or-later
Group:          System/GUI/Other
Url:            http://www.enlightenment.org
Source:         e16-%{version}.tar.xz
Patch0:         fix-compile-gtk.patch
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.7
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(imlib2) >= 1.2.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
Requires:       imlib2-loaders
#conflict with the old enlightenment package
Conflicts:      enlightenment >= 1.0.0
Provides:       windowmanager
Obsoletes:      enlight < %{version}
Provides:       enlight = %{version}
# don't use provides as that will cause issues with the new enlightenment (e18) package
Obsoletes:      enlightenment >= 1.0.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{enable_sound}
BuildRequires:  pkgconfig(libpulse)
%endif
%if %{enable_pango}
BuildRequires:  pkgconfig(pango)
%endif
BuildRequires:  fdupes
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

%description
Enlightenment is a window manager for the X Window System that is
extensible and configurable looking. It is one of the more
graphically intense window managers.

Enlightenment goes beyond managing windows by providing a graphical
shell from which to work. It allows the user to define their own
policy down to every last detail.

%prep
%setup -q
%autopatch -p1

%build
%if 0%{?sles_version} != 10
autoreconf -fi
%endif
%configure \
        --disable-roothacklib \
%if %{enable_sound}
	--enable-sound \
%else
	--disable-sound \
%endif
%if %{enable_hints_gnome}
	--enable-hints-gnome \
%else
	--disable-hints-gnome \
%endif
%if %{enable_zoom}
	--enable-zoom \
%else
	--disable-zoom \
%endif
%if %{enable_xrandr}
	--enable-xrandr \
%else
	--disable-xrandr \
%endif
%if %{enable_composite}
	--enable-composite \
%else
	--disable-composite \
%endif
%if %{enable_pango}
	--enable-pango
%else
	--disable-pango
%endif
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} \
     localedir=%{_datadir}/locale \
     gnulocaledir=%{_datadir}/locale \
     install
find %{buildroot}%{_datadir}/e16/themes -type d | xargs chmod 755
find %{buildroot}%{_datadir}/e16/themes -type f | xargs chmod 644
rm %{buildroot}%{_datadir}/applications/e16.desktop
rm %{buildroot}%{_datadir}/xsessions/e16-{gnome2,gnome3,kde}-session.desktop
rm -rf %{buildroot}%{_datadir}/gnome-session
rm -rf %{buildroot}%{_datadir}/e16/fonts
%if 0%{?suse_version} >= 1100
%fdupes -s %{buildroot}%{_datadir}/e16/themes/winter
%endif
%find_lang e16

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f e16.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_bindir}/*
%{_bindir}/starte16
%{_libdir}/e16/
%{_datadir}/e16
%{_datadir}/doc/e16
%{_mandir}/man1/*
%{_datadir}/xsessions/*

%changelog
