#
# spec file for package ART
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} && 0%{?suse_version} < 1590
%global force_gcc_version 12
%endif

%if (0%{?suse_version} >= 1590) || ("%{_project}" == "graphics")
%bcond_without art_ctl
%else
%bcone_with    art_ctl
%endif

Name:           ART
Version:        1.25.3.1
Release:        0
Summary:        Rawtherapee fork with masks and simplified UI
License:        GPL-3.0-only
URL:            http://art.pixls.us/
Source:         https://github.com/artpixls/ART/releases/download/%{version}/%{name}-%{version}.tar.xz
# No signed tarball quite yet. See gh#artpixls/ART#341 for open issue
# Source1:         https://github.com/artpixls/ART/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
# https://keys.openpgp.org/vks/v1/by-fingerprint/942FCFB1CBE1E38928A1A6BEA94D951156835A5D
Source2:        %{name}.keyring
Patch0:         fix-missing-lm.patch
BuildRequires:  OpenColorIO-devel
%if %{with art_ctl}
BuildRequires:  ctl-devel
%endif
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 12
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

%if 0%{?force_gcc_version}
export CC=gcc-%{?force_gcc_version}
export CXX=gcc-%{?force_gcc_version}
%else
export CC=gcc
export CXX=gcc
%endif

%cmake \
%if 0%{?force_gcc_version}
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++-%{?force_gcc_version} \
%endif
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
    -DCMAKE_C_FLAGS="$CFLAGS" \
    -DCACHE_NAME_SUFFIX="" \
    -DENABLE_LIBRAW="ON" \
%if %{with art_ctl}
    -DENABLE_CTL="ON" \
    -DCTL_INCLUDE_DIR="%{_includedir}/CTL" \
%endif
    -DENABLE_OCIO="ON"
%cmake_build

%install
%cmake_install
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}

%fdupes %{buildroot}/%{_prefix}

%files
%{_bindir}/ART
%{_bindir}/ART-cli
%{_libdir}/librtengine.so
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/*/%{name}*
%{_docdir}/%{name}

%changelog
