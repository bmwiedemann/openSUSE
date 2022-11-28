#
# spec file for package dolphin-emu
#
# Copyright (c) 2022 SUSE LLC
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


%define commit 48c9c224cf9f82f0f9f2690b7cc6283d7448480c
Name:           dolphin-emu
Version:        5.0.17269
Release:        0
Summary:        Dolphin, a GameCube and Wii Emulator
License:        GPL-2.0-or-later
URL:            https://dolphin-emu.org
# n=dolphin-emu && v=5.0.17269 && c=48c9c224cf9f82f0f9f2690b7cc6283d7448480c && cd /tmp && git clone https://github.com/$n/dolphin.git $n && cd $n && git checkout $c && rm -rf .??* && cd .. && n=dolphin-emu && d=$n-$v && mv $n $d && f=$d.tar.xz && tar c --remove-files "$d" | xz -9e > "$f"
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-not-discord-presence.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel >= 5.9
BuildRequires:  mbedtls-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fmt) >= 6.0
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(libevdev)
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
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(sfml-network)
BuildRequires:  pkgconfig(sfml-system)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10-c++
%endif
Requires:       nintendo-gamecube-wiimote-udev-rules
ExclusiveArch:  x86_64 aarch64

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
#Allow building with cmake macro. Build failed on aarch64 with optflags.
%ifarch x86_64
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt
%endif
sed -i 's/minizip>=2.0.0/minizip/' CMakeLists.txt

%build
%if 0%{?suse_version} <= 1500
export CXX=g++-10
%endif

# FIXME: you should use the %%cmake macros
cmake . \
    -LA \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%ifarch x86_64
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
%endif
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DDISTRIBUTOR=openSUSE \
    -DDOLPHIN_WC_BRANCH=beta \
    -DDOLPHIN_WC_DESCRIBE=%{version} \
    -DDOLPHIN_WC_REVISION=%{commit} \
    -DENABLE_ANALYTICS=OFF \
%if 0%{?suse_version} >= 1550
    -DENABLE_LTO=ON \
%endif
    -DENCODE_FRAMEDUMPS=OFF \
    -DUSE_DISCORD_PRESENCE=OFF \
    -DUSE_MGBA=OFF \
    -DUSE_SHARED_ENET=ON \
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
%defattr(0644,root,root,0755)
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
