#
# spec file for package libgnome
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


Name:           libgnome
Version:        2.32.2+20180228.6a7dbfb9
Release:        0
Summary:        The GNOME 2.x Desktop Base Libraries
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://www.gnome.org/

# Source based on tar_scm _service
Source:         %{name}-%{version}.tar.xz
Source99:       baselibs.conf

# PATCH-FIX-OPENSUSE libgnome-sounds-default.diff -- Set default sounds for events
Patch0:         libgnome-sounds-default.patch
# PATCH-FIX-UPSTREAM libgnome-uninitialized-vars.patch bgo543570
Patch1:         libgnome-uninitialized-vars.patch
# PATCH-FIX-UPSTREAM libgnome-va_list-empty.patch bgo543570 -- This fixes the same as libgnome-uninitialized-vars.patch, so both can go away when upstream accepts patc
Patch2:         libgnome-va_list-empty.patch
# PATCH-FIX-OPENSUSE libgnome-help-bundles.patch
Patch3:         libgnome-help-bundles.patch

BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-vfs-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libbonobo-2.0)
Recommends:     %{name}-lang = %{version}
#
# A bunch of legacy gnome apps relies more or less on yelp for a working help system (it can be reconfigured). Thus we recommend yelp from here, as low in the stack as it makes sense.
Recommends:     yelp
%{gconf_schemas_prereq}

%description
This package contains the basic libraries for the GNOME 2.x Desktop
platform. GNOME has no specific window manager. You are totally free in
your choice. Many GNOME users like Sawfish, Enlightenment, or IceWM as
a window manager for GNOME (see those packages).

%package devel
Summary:        Development files for libgnome
#FIXME: major bloat, should be only
#Requires: libbonobo-devel
#
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Provides:       libgnome-doc = %{version}
Obsoletes:      libgnome-doc < %{version}

%description devel
This subpackage contains the header files for developing
applications that want to make use of libgnome.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-esd \
	--enable-canberra=no \
	--enable-gtk-doc \
	--disable-static \
	%{nil}
%make_build

%install
%make_install

mkdir -p %{buildroot}/%{_datadir}/gnome/help %{buildroot}/%{_datadir}/gnome/autostart
%find_lang %{name}-2.0
%find_gconf_schemas
cat %{name}.schemas_list >%{name}.lst
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_prefix}

%pre -f %{name}.schemas_pre
%post -p /sbin/ldconfig
%posttrans -f %{name}.schemas_posttrans
%preun -f %{name}.schemas_preun
%postun -p /sbin/ldconfig

%files -f %{name}.lst
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_bindir}/*
%dir %{_datadir}/gnome
# generic directory for help files
%dir %{_datadir}/gnome/help
# generic directory for autostart desktop files
# NOTE: This directory is referenced by (and technically belongs to)
# gnome-session. But libgnome provides complete support for such
# binaries so these binaries don't need gnome-session.
%dir %{_datadir}/gnome/autostart
%{_datadir}/gnome-background-properties/*.xml
%{_datadir}/pixmaps/backgrounds/gnome/*.*
%{_libdir}/*.*so.*
%{_libdir}/bonobo/monikers/*.so
%{_libdir}/bonobo/servers/*
%{_mandir}/man7/gnome-options.7%{?ext_man}
# generic directory for sound events
%dir %{_sysconfdir}/sound
%dir %{_sysconfdir}/sound/events
%config %{_sysconfdir}/sound/events/*.soundlist
# own directory to break build loop libgnome->gnome-themes->librsvg->libgnomeprintui->...->libgnome:
%dir %{_datadir}/gnome-background-properties
%dir %{_datadir}/pixmaps/backgrounds
%dir %{_datadir}/pixmaps/backgrounds/gnome

%files lang -f %{name}-2.0.lang

%files devel
%{_includedir}/libgnome-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgnome-2.0.pc
%{_datadir}/gtk-doc/html/libgnome

%changelog
