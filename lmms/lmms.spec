#
# spec file for package lmms
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Since 42.2 RPM creates a hard requirement on a build time library (libvstbase), the requirement is unnecessary and bad
%global __requires_exclude_from ^%{_libdir}/lmms/.*\\.so$
%bcond_without  carla
%bcond_without  crippled_stk
Name:           lmms
Version:        1.2.0rc7+git20180925.a2685c1cc
Release:        0
Summary:        Linux MultiMedia Studio
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://lmms.io/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE Patch for providing proper return code in a function
Patch0:         lmms-1.1.0-return.patch
# PATCH-FIX-OPENSUSE Some parts cannot be build because stk misses some files due to legal issues (bnc#761147)
Patch1:         lmms-1.2.0-crippled_stk.patch
# PATCH-FIX-UPSTREAM Fix fluidsynth sf2 player compilation, backport from git (gh#LMMS/lmms#4678)
Patch2:         lmms-fluidsynth.patch
# PATCH-FIX-UPSTREAM Fix plugin library search path, testing an upstream proposal
Patch3:         lmms-1.2.0-libdir.patch

BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  fltk-devel
BuildRequires:  fluidsynth
BuildRequires:  gcc-c++-32bit
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  libqt5-qttools
BuildRequires:  libstk-devel
BuildRequires:  pkgconfig
BuildRequires:  sndio-devel
BuildRequires:  wine
BuildRequires:  wine-devel
BuildRequires:  wine-devel-32bit
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3f) >= 3.0.0
BuildRequires:  pkgconfig(fluidsynth) >= 1.0.7
BuildRequires:  pkgconfig(gig)
BuildRequires:  pkgconfig(jack) >= 0.77
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(samplerate) >= 0.1.8
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sndfile) >= 1.0.11
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(zlib)
Recommends:     wine
ExclusiveArch:  x86_64
%if %{with carla}
# also needed (contains libcarla_standalone2 library)
BuildRequires:  carla
# to enable internal Carla plugin host
BuildRequires:  pkgconfig(carla-standalone)
%endif

%description
LMMS is a free cross-platform music studio which allows you to produce music
with your computer. This includes the creation of melodies and beats, the
synthesis and mixing of sounds, and arranging of samples.

%package devel
Summary:        Headers to create LMMS plugins
Group:          Development/Libraries/C and C++

%description devel
Headers that provide access to the LMMS features. Install it if you plan to
create a LMMS plugin.

%prep
%setup -q
%patch0 -p1
%if %{with crippled_stk}
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1

%build
%cmake \
  -DWANT_QT5=ON \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_SKIP_RPATH=OFF \
  -Wno-dev
%make_jobs

%install
%cmake_install
mkdir -p '%{buildroot}%{_defaultdocdir}/lmms/'
# remove unneeded static helper library from install
rm %{buildroot}%{_libdir}/libqx11embedcontainer.a
# workaround: copy bash completion manually into install dir because it fails during cmake install
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions
cp %{_builddir}/lmms*/doc/bash-completion/lmms %{buildroot}/%{_datadir}/bash-completion/completions/lmms

%fdupes -s %{buildroot}/%{_datadir}

%files
%doc doc/AUTHORS README.md INSTALL.txt
%license LICENSE.txt
%{_bindir}/lmms
%{_mandir}/man1/lmms.1%{?ext_man}
%{_libdir}/lmms/
%{_datadir}/lmms/
%{_datadir}/applications/lmms.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/lmms.xml
%{_datadir}/bash-completion/completions/lmms

%files devel
%defattr(0644,root,root,0755)
%{_includedir}/lmms/

%changelog
