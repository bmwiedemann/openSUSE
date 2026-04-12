#
# spec file for package rawtherapee
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2022 Marcin Bajor
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


%define __builder ninja
Name:           rawtherapee
Version:        5.12
Release:        0
Summary:        Cross-platform raw image processing program
License:        GPL-3.0-only
URL:            https://rawtherapee.com
Source0:        https://rawtherapee.com/shared/source/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM -- Fixes crash on application startup -- https://github.com/RawTherapee/RawTherapee/issues/7642
Patch0:         https://raw.githubusercontent.com/digitalcarp/RawTherapee/refs/heads/meyer-5.12/patch/0001-Fix-static-init-order-fiasco-crashes.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gtk3-devel >= 3.24.3
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2) >= 0.24
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libraw) >= 0.21
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.52
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(zlib)
Conflicts:      rawtherapee-gtk2
Conflicts:      rawtherapee-gtk2-nosse
Conflicts:      rawtherapee-gtk2-nosse-unstable
Conflicts:      rawtherapee-gtk2-unstable
Conflicts:      rawtherapee-gtk3
Conflicts:      rawtherapee-gtk3-nosse
Conflicts:      rawtherapee-nosse
Conflicts:      rawtherapee-nosse-unstable
Conflicts:      rawtherapee-stable-3.x
Conflicts:      rawtherapee-unstable
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif

%description
RawTherapee is a cross platform image processing software equipped with the essential tools for high quality and efficient RAW photo development.
%ifarch i386 i486 i586 i686
Latest stable build from "releases" branch with SSE2 support.
%else
Latest stable build from "releases" branch.
%endif

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif

export CFLAGS="%(echo %{optflags} | sed 's/-O2/-O3/' | sed 's/-D_FORTIFY_SOURCE=2/-D_FORTIFY_SOURCE=3/')"
export CXXFLAGS="$CFLAGS"

%ifarch i386 i486 i586 i686
export CFLAGS+=" -msse2"
export CXXFLAGS+=" -msse2"
%endif

echo "CFLAGS: "$CFLAGS
echo "CXXFLAGS= "$CXXFLAGS

# Because CMake variables have no implicit meaning and this project has a very
# liberal interpretation of “shared library”, BUILD_SHARED_LIBS will install a
# *static* library instead. Without headers.
%cmake \
    -DWITH_SYSTEM_LIBRAW=ON \
    -DENABLE_TCMALLOC=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=OFF \
    -DDOCDIR=%{_docdir}/%{name} \
    -DCREDITSDIR=%{_docdir}/%{name} \
    -DLICENCEDIR=%{_datadir}/licenses/%{name} \
    -DCACHE_NAME_SUFFIX=""

%cmake_build

%install
%cmake_install

# create symlinks for man pages
%fdupes -s %{buildroot}/%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}/%{_prefix}

%files
%dir %{_datadir}/licenses/%{name}
%license %{_datadir}/licenses/%{name}/*
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/com.rawtherapee.RawTherapee.appdata.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
