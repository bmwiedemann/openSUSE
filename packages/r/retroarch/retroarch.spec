#
# spec file for package retroarch
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           retroarch
Version:        1.22.2
Release:        0
Summary:        Emulator frontend
License:        GPL-3.0-only
URL:            https://www.retroarch.com
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}_migrate_old_config.py
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  p7zip
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm) >= 9.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack) >= 0.120.1
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.13
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sdl2) >= 2.0.0
BuildRequires:  pkgconfig(wayland-egl) >= 10.1.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.2
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
# Xbox One/Series controller wireless driver
Recommends:     xpadneo
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(Qt6Concurrent) >= 6.2
BuildRequires:  pkgconfig(Qt6Core) >= 6.2
BuildRequires:  pkgconfig(Qt6Gui) >= 6.2
BuildRequires:  pkgconfig(Qt6Network) >= 6.2
BuildRequires:  pkgconfig(Qt6Widgets) >= 6.2
%else
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
%endif
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(libavcodec) >= 57
BuildRequires:  pkgconfig(libavdevice) >= 57
BuildRequires:  pkgconfig(libavformat) >= 57
BuildRequires:  pkgconfig(libavutil) >= 55
BuildRequires:  pkgconfig(libswscale) >= 4
BuildRequires:  pkgconfig(vulkan)
%endif

%description
RetroArch is a modular multi-system emulator system that is designed to be
fast, lightweight, and portable. It has features few other emulators frontends
have, such as real-time rewinding and game-aware shading.

%prep
%autosetup

# Change /usr/bin/env python to /usr/bin/python
sed -i s~%{_bindir}/env\ python~%{_bindir}/python~g tools/cg2glsl.py

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
# Quickbuild script, not autotools
./configure --prefix=%{_prefix} \
    --enable-materialui \
    --enable-xmb \
    --enable-sdl2 \
    --enable-udev \
    --enable-threads \
    --enable-thread_storage \
    --enable-ffmpeg \
    --enable-ssa \
    --enable-dylib \
    --enable-networking \
    --enable-networkgamepad \
    --enable-opengl \
    --enable-x11 \
    --enable-xinerama\
    --enable-kms \
    --enable-wayland \
    --enable-egl \
    --enable-zlib \
    --enable-alsa \
    --enable-al \
    --enable-jack \
    --enable-pulse \
    --enable-freetype \
    --enable-xvideo \
    --enable-v4l2 \
    --enable-qt \
    --enable-dbus \
%ifarch x86
    --enable-sse \
%endif
%if 0%{is_opensuse}
    --enable-vulkan \
%endif
    --enable-7zip \
    --enable-mmap
%make_build

%install
%make_install
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}_migrate_old_config

%fdupes %{buildroot}

%post
%{_bindir}/%{name}_migrate_old_config

%files
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_bindir}/%{name}
%{_bindir}/%{name}_migrate_old_config
%{_bindir}/%{name}-cg2glsl
%{_datadir}/applications/com.libretro.RetroArch.desktop
%{_datadir}/metainfo/com.libretro.*.xml
%{_datadir}/pixmaps/com.libretro.RetroArch.svg
%{_mandir}/man?/%{name}.?*
%{_mandir}/man?/%{name}-cg2glsl.?*
%{_datadir}/doc/%{name}

%changelog
