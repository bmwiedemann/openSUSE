#
# spec file for package gnome-desktop
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


Name:           gnome-desktop
Version:        3.36.6
Release:        0
Summary:        The GNOME Desktop API Library
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-desktop/3.36/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

# PATCH-FIX-OPENSUSE gnome-desktop-switch-Japanese-default-input-to-mozc.patch bnc#1029083 boo#1056289 qzhao@suse.com -- Switch new user's default input engine from "anthy" to "mozc" in gnome-desktop with Japanese language and ibus input frame-work condition.
Patch1:         gnome-desktop-switch-Japanese-default-input-to-mozc.patch
# PATCH-FIX-UPSTREAM gnome-desktop-invalid-size-crash.patch bsc#1176596 mgorse@suse.com -- fix a crash caused by a mal-formed background xml file.
Patch2:         gnome-desktop-invalid-size-crash.patch

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.36.5
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.53.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.31.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.3.6
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)

%description
This package contains the desktop-wide files.

%package -n gnome-version
Summary:        GNOME version
Group:          System/GUI/GNOME

%description -n gnome-version
This package contains information on the version of GNOME that is installed.

%package -n libgnome-desktop-3_0-common
Summary:        Common data files for the GNOME Desktop API library
Group:          System/Libraries

%description -n libgnome-desktop-3_0-common
The libgnome-desktop library provides API shared by several applications
on the desktop, but that cannot live in the platform for various
reasons.

This package contains data files used by libgnome-dekstop.

%package -n libgnome-desktop-3-19
Summary:        The GNOME Desktop API Library
# the library calls out to bwrap in order to fire up thumbnailers in a secure container
Group:          System/Libraries
Requires:       bubblewrap
Requires:       gsettings-desktop-schemas
# Data files for libgnome-desktop, split in an own package for SLPP compliancy
Requires:       libgnome-desktop-3_0-common >= %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libgnome-desktop-3-19
The libgnome-desktop library provides API shared by several applications
on the desktop, but that cannot live in the platform for various
reasons.

%package -n typelib-1_0-GnomeDesktop-3_0
Summary:        Introspection bindings for the GNOME Desktop API library
Group:          System/Libraries

%description -n typelib-1_0-GnomeDesktop-3_0
The libgnome-desktop library provides API shared by several applications
on the desktop, but that cannot live in the platform for various
reasons.

This package provides the GObject Introspection bindings for
libgnome-desktop.

%package -n libgnome-desktop-3-devel
Summary:        Development files for the GNOME Desktop API library
Group:          Development/Libraries/GNOME
Requires:       libgnome-desktop-3-19 = %{version}
# Needed as /usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-xkb-info.h includes X11/extensions/XKBrules.h
Requires:       libxkbfile-devel
Requires:       typelib-1_0-GnomeDesktop-3_0 = %{version}
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description -n libgnome-desktop-3-devel
The libgnome-desktop library provides API shared by several applications
on the desktop, but that cannot live in the platform for various
reasons.

%lang_package

%prep
%autosetup -p1
translation-update-upstream po gnome-desktop

%build
%meson \
	-Dgnome_distributor=openSUSE \
	-Ddate_in_gnome_version=false \
	-Ddesktop_docs=true \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{name}-3.0 %{?no_lang_C}
%find_lang fdl %{?no_lang_C} %{name}-3.0.lang
%find_lang gpl %{?no_lang_C} %{name}-3.0.lang
%find_lang lgpl %{?no_lang_C} %{name}-3.0.lang

%fdupes %{buildroot}/%{_prefix}

%post -n libgnome-desktop-3-19 -p /sbin/ldconfig
%postun -n libgnome-desktop-3-19 -p /sbin/ldconfig

%files -n libgnome-desktop-3-19
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/libgnome-desktop-3.so.*

%files -n libgnome-desktop-3_0-common
%doc %{_datadir}/help/C/fdl/
%doc %{_datadir}/help/C/gpl/
%doc %{_datadir}/help/C/lgpl/
%{_datadir}/locale/en/
%{_libexecdir}/gnome-rr-debug

%files -n typelib-1_0-GnomeDesktop-3_0
%{_libdir}/girepository-1.0/GnomeDesktop-3.0.typelib

%files -n libgnome-desktop-3-devel
%{_includedir}/gnome-desktop-3.0/
%{_libdir}/libgnome-desktop-3.so
%{_libdir}/pkgconfig/gnome-desktop-3.0.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/gnome-desktop3/

%files lang -f %{name}-3.0.lang
# english locale should be in the main package
%exclude %{_datadir}/locale/en

%files -n gnome-version
%dir %{_datadir}/gnome
%{_datadir}/gnome/gnome-version.xml

%changelog
