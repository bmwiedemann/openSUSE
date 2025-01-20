#
# spec file for package dolphin-emu
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


Name:           dolphin-emu
Version:        2412
Release:        0
Summary:        Dolphin, a GameCube and Wii Emulator
License:        (Apache-2.0 OR MIT) AND BSD-2-Clause AND libpng-2.0 AND GPL-2.0-or-later
URL:            https://dolphin-emu.org
# n=dolphin-emu && v=2412 && d=$n-$v && f=$d.tar.xz && cd /tmp && git clone https://github.com/$n/dolphin.git $n && pushd $n && git checkout $v && git submodule && git submodule update --init --recursive Externals/VulkanMemoryAllocator Externals/cubeb/cubeb Externals/enet/enet Externals/gtest Externals/implot/implot Externals/libspng/libspng Externals/minizip-ng/minizip-ng Externals/rcheevos/rcheevos Externals/tinygltf/tinygltf Externals/zlib-ng/zlib-ng && git submodule status && rm -rf .??* && popd && mv $n $d && tar c --remove-files "$d" | xz -9e > "$f"
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  glslang-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  mbedtls-devel < 3
BuildRequires:  ninja
BuildRequires:  picojson-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  spirv-headers
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fmt) = 10.2.1
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(sdl2) >= 2.30.9
BuildRequires:  pkgconfig(sfml-network)
BuildRequires:  pkgconfig(sfml-system)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
Requires:       nintendo-gamecube-wiimote-udev-rules
ExclusiveArch:  x86_64 aarch64
%if 0%{?sle_version} > 150000 && 0%{?sle_version} < 160000
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%endif

%description
Dolphin is an emulator for two Nintendo video game consoles, GameCube and the Wii.
It allows PC gamers to enjoy games for these two consoles in full HD with several
enhancements such as compatibility with all PC controllers, turbo speed,
networked multiplayer, and more.
Most games run perfectly or with minor bugs.

%package -n nintendo-gamecube-wiimote-udev-rules
Summary:        Udev rules for Nintendo GameCube and Wiimote game controllers
Requires:       udev
BuildArch:      noarch

%description -n nintendo-gamecube-wiimote-udev-rules
This package contains udev rules for Nintendo GameCube and Wiimote game controllers.

%lang_package

%prep
%autosetup -p1

#Allow building with cmake macro
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

#Font license, drop the install directory into thie file
echo "%{_datadir}/%{name}/Sys/GC:" > font-licenses.txt
cat Data/Sys/GC/font-licenses.txt >> font-licenses.txt

%build
# FIXME: you should use the %%cmake macros
cmake . -LA \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if 0%{?sle_version} > 150000 && 0%{?sle_version} < 160000
    -DCMAKE_C_COMPILER=gcc-13 \
    -DCMAKE_CXX_COMPILER=g++-13 \
%endif
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DDISTRIBUTOR=openSUSE \
    -DDOLPHIN_WC_BRANCH=master \
    -DDOLPHIN_WC_DESCRIBE=%{version} \
    -DDOLPHIN_WC_REVISION=%{version} \
    -DENABLE_ANALYTICS=OFF \
    -DENABLE_LTO=ON \
    -DENCODE_FRAMEDUMPS=OFF \
    -DUSE_DISCORD_PRESENCE=OFF \
    -DUSE_MGBA=OFF \
    -DUSE_SANITIZERS=OFF \
    -DXXHASH_FOUND=ON \
    -G Ninja
ninja -v

%install
DESTDIR=%{buildroot} ninja install
sed -i 's/^Exec=.*/Exec=%{name}/' %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm0644 Data/51-usb-device.rules %{buildroot}%{_udevrulesdir}/51-nintendo-gamecube-wiimote.rules
%fdupes -s %{buildroot}
%find_lang %{name}

%files lang -f %{name}.lang

%files
%defattr(0644,root,root,-)
%license COPYING
%doc Readme.md
%attr(0755,root,root) %{_bindir}/%{name}*
%attr(0755,root,root) %{_bindir}/dolphin-tool
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.{png,svg}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}*.6%{?ext_man}

%files -n nintendo-gamecube-wiimote-udev-rules
%{_udevrulesdir}/51-nintendo-gamecube-wiimote.rules

%changelog
