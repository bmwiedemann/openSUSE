#
# spec file for package gtkpod
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gtkpod
Summary:        A platform independent GUI for the Apple iPod
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Version:        2.1.5
Release:        0
URL:            http://gtkpod.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/gtkpod/gtkpod/gtkpod-2.1.5/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE gtkpod-pref.patch -- Preferences to mountpoint and some tag preferences
Patch0:         gtkpod-pref.patch
# PATCH-FEATURE-UPSTREAM use-python3.patch -- Use python3
Patch1:         use-python3.patch
# PATCH-FIX-UPSTREAM xml-inc.patch -- Add missing include
Patch2:         xml-inc.patch
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libdiscid-devel
BuildRequires:  libgpod-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.2
BuildRequires:  pkgconfig(flac) >= 1.2.1
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(id3tag) >= 0.15
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libanjuta-3.0)
BuildRequires:  pkgconfig(libbrasero-media3) >= 3.0
BuildRequires:  pkgconfig(libcurl) >= 7.10.0
BuildRequires:  pkgconfig(libdiscid) >= 0.2.2
BuildRequires:  pkgconfig(libmusicbrainz5) >= 5.0.1
BuildRequires:  pkgconfig(vorbisfile) >= 1.3.1
%glib2_gsettings_schema_requires

%description
gtkpod is a Platform-Independent GUI for the Apple iPod using GTK2. It
allows you to upload songs and play lists to your iPod. It supports ID3
tag editing with multiple charsets for ID3 tags, detects duplicate
songs, allows offline modification of the database with later
synchronization, and more.

%package devel
Summary:        Development files for gtkpod, a GUI for Apple iPods
Group:          Development/Libraries/C and C++
Requires:       libatomicparsley0 = %{version}
Requires:       libgtkpod1 = %{version}

%description devel
This package contains development headers for libgtkpod

gtkpod is a Platform-Independent GUI for the Apple iPod using GTK2. It
allows you to upload songs and play lists to your iPod. It supports ID3
tag editing with multiple charsets for ID3 tags, detects duplicate
songs, allows offline modification of the database with later
synchronization, and more.

%package -n libgtkpod1
Summary:        A platform independent GUI for the Apple® iPod® - System Library
Group:          System/Libraries

%description -n libgtkpod1
gtkpod is a Platform-Independent GUI for the Apple iPod using GTK2. It
allows you to upload songs and play lists to your iPod. It supports ID3
tag editing with multiple charsets for ID3 tags, detects duplicate
songs, allows offline modification of the database with later
synchronization, and more.

Shared Library, to be installed by package dependencies.

%package -n libatomicparsley0
Summary:        Atomic parsley in gtkpod
Group:          System/Libraries

%description -n libatomicparsley0
This is the core library for atomic parsley of mp4 files in gtkpod.
Library including read/write lyric support for the first time and
write metadata function.

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fcommon"
%configure --disable-static
make V=1

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
%suse_update_desktop_file %name Utility SyncUtility
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} > 1130

%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post
%endif

%if 0%{?suse_version} > 1130

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%post -n libgtkpod1 -p /sbin/ldconfig

%postun -n libgtkpod1 -p /sbin/ldconfig

%post -n libatomicparsley0 -p /sbin/ldconfig

%postun -n libatomicparsley0 -p /sbin/ldconfig

%files
%doc README NEWS INSTALL ChangeLog AUTHORS
%license COPYING
%{_bindir}/gtkpod
%{_datadir}/gtkpod/
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/%{name}.svg
%{_datadir}/applications/gtkpod.desktop
%{_datadir}/glib-2.0/schemas/org.gtkpod.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtkpod.sjcd.gschema.xml
%{_libdir}/gtkpod/
%{_mandir}/*/%{name}.*

%files -n libgtkpod1
%{_libdir}/libgtkpod.so.*

%files -n libatomicparsley0
%{_libdir}/libatomicparsley.so.*

%files lang -f %{name}.lang

%files devel
%{_includedir}/gtkpod/
%{_libdir}/libatomicparsley.so
%{_libdir}/libgtkpod.so
%{_libdir}/pkgconfig/libgtkpod-1.1.0.pc

%changelog
