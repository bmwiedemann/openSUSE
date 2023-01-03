#
# spec file for package ART
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


Name:           ART
Version:        1.18.0
Release:        0
Summary:        Rawtherapee fork with masks and simplified UI
License:        GPL-3.0-only
URL:            https://bitbucket.org/agriggio/art/wiki/Home
Source:         https://bitbucket.org/agriggio/art/downloads/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibmm2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libraw-devel
BuildRequires:  mimalloc-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(fftw3l)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-broadway-3.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gdkmm-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-broadway-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libprofiler)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libtcmalloc_debug)
BuildRequires:  pkgconfig(libtcmalloc_minimal)
BuildRequires:  pkgconfig(libtcmalloc_minimal_debug)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)

%description
A free, open-source, cross-platform raw image processing program. ART is a derivative of the popular RawTherapee, trading a bit of customization and control over various processing parameters for a simpler and (hopefully) easier to use interface, while still maintaining the power and quality of RawTherapee.

%prep
%autosetup -p1

%build
# Upstream recommended '-O3' optimisation, do not change
export CFLAGS="%(echo %{optflags} | sed 's/-O2/-O3/' | sed 's/-D_FORTIFY_SOURCE=2/-D_FORTIFY_SOURCE=3/')"
export CXXFLAGS="$CFLAGS"

%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
    -DCMAKE_C_FLAGS="$CFLAGS" \
    -DCACHE_NAME_SUFFIX="" \
    -DENABLE_LIBRAW="ON"
%cmake_build

%install
%cmake_install
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}

%fdupes %{buildroot}/%{_prefix}

%files
%{_bindir}/*
%{_libdir}/librtengine.so
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/*/%{name}*
%{_docdir}/%{name}

%changelog
