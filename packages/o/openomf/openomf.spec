#
# spec file for package openomf
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%define sover   0_0_0-suse
Name:           openomf
Version:        0.6.5+git.20190205
Release:        0
Summary:        Open Source remake of "One Must Fall 2097"
License:        MIT
Group:          Amusements/Games/Action/Arcade
URL:            http://www.openomf.org
#Git-Clone:     https://github.com/omf2097/openomf.git
Source:         %{name}-%{version}.tar.xz
Source2:        %{name}.README.SUSE
Patch0:         libshadowdive-soversion.patch
Patch1:         openomf-set-cflags.patch
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  enet-devel
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng16-compat-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(argtable2)
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)

%description
OpenOMF is a open source remake of "One Must Fall 2097".

OMF is a fighting game featuring two robot fighters who fight in a
single arena. Eleven robots and ten customizable pilots are available
for play, along with five arenas and four tournaments. The pilots
vary in strength, speed and endurance.

%package -n libshadowdive%{sover}
Summary:        A library for reading and writing One Must Fall 2097 datafiles
Group:          System/Libraries

%description -n libshadowdive%{sover}
libShadowDive is a library for reading and writing One Must Fall 2097 datafiles.
The library can deal with the following files:

  * HAR Data files (*.AF)
  * Arena/background data files (*.BK)
  * Language files (ENGLISH.DAT,GERMAN.DAT)
  * Sound data file (SOUNDS.DAT)
  * Characters for both big and small fonts (GRAPHCHR.DAT, CHARSMAL.DAT)
  * Score file (SCORES.DAT)
  * Pilot image files (*.PIC)
  * Tournament data files (*.TRN)
  * Character save files (*.CHR)
  * Match record files (*.REC)
  * Alternate palette file (ALTPALS.DAT)

%package -n shadowdive-devel
Summary:        Header files for libShadowDive
Group:          Development/Libraries/C and C++
Requires:       libpng16-compat-devel
Requires:       libshadowdive%{sover} = %{version}

%description -n shadowdive-devel
Development and header files for libShadowDive.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake \
    -DUSE_OGGVORBIS=ON \
    -DUSE_XMP=ON \
    -DUSE_OPENAL=ON \
    -DUSE_PNG=ON \
    -DUSE_TESTS=ON
make %{?_smp_mflags}

%install
%cmake_install
# Install icons and desktop file
for size in 256 128 96 64 48 32 16; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps"
    convert -strip resources/openomf_icon.png -resize "$size"x"$size" %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps/%{name}.png"
done
%suse_update_desktop_file -c %{name} 'Remake of "One Must Fall 2097"' "A fighting video game" %{name} %{name} Game ArcadeGame
install -m0644 %{SOURCE2} README.SUSE

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%check
export LD_LIBRARY_PATH=$(pwd)/build/external/libShadowDive
cd build/
./openomf_test_main

%post   -n libshadowdive%{sover} -p /sbin/ldconfig
%postun -n libshadowdive%{sover} -p /sbin/ldconfig

%files
%doc README.md README.SUSE
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/openomf.bk
%{_datadir}/games/%{name}/openomf_icon.png

%files -n libshadowdive%{sover}
%doc external/libShadowDive/README.md
%license external/libShadowDive/LICENSE
%{_libdir}/libshadowdive.so.0*

%files -n shadowdive-devel
%dir %{_includedir}/shadowdive
%{_includedir}/shadowdive/*.h
%{_libdir}/libshadowdive.so

%changelog
