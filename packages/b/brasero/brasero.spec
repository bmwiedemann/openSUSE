#
# spec file for package brasero
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


Name:           brasero
Version:        3.12.2+20200906.5945fdff
Release:        0
Summary:        CD/DVD burning application for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/CD/Record
URL:            http://gnome.org/projects/brasero
# Service generated tarball
Source:         %{name}-%{version}.tar.xz
#Source:         http://download.gnome.org/sources/brasero/3.12/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
# Needed, as we provide a git snapshot
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.29.14
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libburn-1) >= 0.4.0
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libisofs-1) >= 0.6.4
BuildRequires:  pkgconfig(libnautilus-extension)
BuildRequires:  pkgconfig(libnotify) >= 0.6.1
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(totem-plparser) >= 2.29.1
# cdrkit-cdrtools-compat or cdrtools provide cdda2wav
Requires:       %{_bindir}/cdda2wav
# We need cdrecord to burn CDs (bnc#729984) This can be provided by either wodim or cdrtools
Requires:       %{_bindir}/cdrecord
Requires:       %{_bindir}/mkisofs
Requires:       %{_bindir}/readcd
# We need cdrdao to be able to extract audio tracks from disks
Requires:       cdrdao
# The gstreamer Requires are versioned as gstreamer010 packages had virtual provides.
Requires:       gstreamer >= 0.11.02
Requires:       gstreamer-plugins-base >= 0.11.92
Requires:       gstreamer-plugins-good >= 0.11.92
Provides:       brasero-doc = 0.9.1
Obsoletes:      brasero-doc < 0.9.1
Provides:       gnomebaker = 0.6.1
Obsoletes:      gnomebaker < 0.6.1
%glib2_gsettings_schema_requires

%description
Brasero is an application for the GNOME Desktop to write to CD/DVDs.

For data CDs/DVDs, Brasero supports multisession, Joliet extensions
and on-the-fly image generation. The file manager can automatically
ignore unwanted files.

For Red Book audio CDs, Brasero supports CD-TEXT, on-the-fly transcoding from
Ogg/FLAC/etc., and intra-track silence configuration.

Brasero is capable of copying CDs/DVDs to an image file on disk and
vice-versa. BIN/CUE is supported.

%package devel
Summary:        Development files for Brasero, a CD/DVD burning application for GNOME
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       libbrasero-burn3-1 = %{version}
Requires:       libbrasero-media3-1 = %{version}
Requires:       libbrasero-utils3-1 = %{version}
Requires:       typelib-1_0-BraseroBurn-3_2_0 = %{version}
Requires:       typelib-1_0-BraseroMedia-3_2_0 = %{version}

%description devel
Brasero is an application for the GNOME Desktop to write CD/DVDs.

%package -n libbrasero-burn3-1
Summary:        Brasero composition utility function library
# The obsoletes IS technically wrong. But as libbrasero-utils was
# not split from the main package, is required to have a smooth
# upgrade possibility.
Group:          System/Libraries
Obsoletes:      libbrasero-burn1 < %{version}

%description -n libbrasero-burn3-1
Brasero is an application for the GNOME Desktop to write CD/DVDs.

This subpackage contains a library of Brasero with utility functions related to
abstract disc image composition (files and audio tracks).

%package -n typelib-1_0-BraseroBurn-3_2_0
Summary:        Introspection bindings for libbrasero-burn
Group:          System/Libraries

%description -n typelib-1_0-BraseroBurn-3_2_0
Brasero is an application for the GNOME Desktop to write CD/DVDs.

This package provides the GObject Introspection bindings for the
libbrasero-burn library.

%package -n libbrasero-media3-1
Summary:        Brasero media utility function library
Group:          System/Libraries

%description -n libbrasero-media3-1
Brasero is an application for the GNOME Desktop to write CD/DVDs.

This subpackage contains a library of Brasero with utility functions
related to disc image creation and extraction, and drive handling.

%package -n typelib-1_0-BraseroMedia-3_2_0
Summary:        GObject introspection bindings for libbrasero-media
Group:          System/Libraries

%description -n typelib-1_0-BraseroMedia-3_2_0
Brasero is an application for the GNOME Desktop to write CD/DVDs.

This package provides the GObject Introspection bindings for the
libbrasero-media library.

%package -n libbrasero-utils3-1
Summary:        Brasero miscellaneous utility function library
Group:          System/Libraries

%description -n libbrasero-utils3-1
Brasero is an application to burn CD/DVDs for the GNOME Desktop. It is

This subpackage contains a library of Brasero with utility functions
that did not fit in the other two categories (brasero-burn,
brasero-media).

%package nautilus
Summary:        Brasero CD/DVD burning extension for Nautilus
Group:          Productivity/Multimedia/CD/Record
Supplements:    packageand(brasero:nautilus)

%description nautilus
This package provides the Brasero extension for Nautilus.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
        --disable-static \
        --disable-gtk-doc \
        --disable-search \
        --enable-playlist \
        --enable-nautilus \
        --enable-introspection \
        --enable-libburnia
make %{?_smp_mflags} V=1

%install
%make_install
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{name}
%suse_update_desktop_file brasero-nautilus
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%post
/sbin/ldconfig
%glib2_gsettings_schema_post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%post -n libbrasero-burn3-1 -p /sbin/ldconfig
%post -n libbrasero-media3-1 -p /sbin/ldconfig
%post -n libbrasero-utils3-1 -p /sbin/ldconfig
%post nautilus
%desktop_database_post

%postun
/sbin/ldconfig
%glib2_gsettings_schema_postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%postun -n libbrasero-burn3-1 -p /sbin/ldconfig
%postun -n libbrasero-media3-1 -p /sbin/ldconfig
%postun -n libbrasero-utils3-1 -p /sbin/ldconfig
%postun nautilus
%desktop_database_postun

%files
%license COPYING
%doc NEWS AUTHORS README
%doc %{_datadir}/help/C/%{name}/
%{_datadir}/metainfo/brasero.appdata.xml
%{_datadir}/brasero/
%{_libdir}/brasero3/
%{_bindir}/brasero
%{_datadir}/applications/brasero.desktop
%{_datadir}/icons/hicolor/*/apps/brasero*.*
%{_datadir}/mime/packages/brasero.xml
%{_datadir}/GConf/gsettings/brasero.convert
%{_datadir}/glib-2.0/schemas/org.gnome.brasero.gschema.xml
%{_mandir}/man?/*%{ext_man}

%files -n libbrasero-burn3-1
%{_libdir}/libbrasero-burn3.so.1*

%files -n typelib-1_0-BraseroBurn-3_2_0
%{_libdir}/girepository-1.0/BraseroBurn-*.typelib

%files -n libbrasero-media3-1
%{_libdir}/libbrasero-media3.so.1*

%files -n typelib-1_0-BraseroMedia-3_2_0
%{_libdir}/girepository-1.0/BraseroMedia-*.typelib

%files -n libbrasero-utils3-1
# Even though there is no need to split according to upstream, we follow the
# openSUSE policy, as not splitting can cause upgrade trouble.
%{_libdir}/libbrasero-utils3.so.1*

%files devel
%{_includedir}/brasero3/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libbrasero-media3.pc
%{_libdir}/pkgconfig/libbrasero-burn3.pc
%{_datadir}/gir-1.0/BraseroBurn-*.gir
%{_datadir}/gir-1.0/BraseroMedia-*.gir

%files nautilus
%{_libdir}/nautilus/extensions-3.0/*.so
%{_datadir}/applications/brasero-nautilus.desktop

%files lang -f %{name}.lang

%changelog
