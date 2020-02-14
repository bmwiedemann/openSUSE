#
# spec file for package dolphin-emu
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


# revision needs to be the full output of 'git rev-parse HEAD'
# (netplay version check relies on it)
%define _revision a205ecb446e5920d1fb6f6ffde6dc83b956fd877
%define _revision_description 5.0-11622

Name:           dolphin-emu
Version:        5.0+git.1581377336.a9dc4ac3f0
Release:        0
Summary:        Dolphin, a GameCube and Wii Emulator
License:        GPL-2.0-or-later
Group:          System/Emulators/Other
URL:            https://dolphin-emu.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  alsa-devel
BuildRequires:  bluez-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libQt5Gui-private-headers-devel >= 5.9
BuildRequires:  libSM-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevdev-devel
BuildRequires:  libhidapi-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpng-devel
BuildRequires:  lzo-devel
BuildRequires:  mbedtls-devel
BuildRequires:  ninja
BuildRequires:  openal-soft-devel
BuildRequires:  pkg-config
BuildRequires:  portaudio-devel
BuildRequires:  soundtouch-devel
BuildRequires:  pkgconfig(systemd)
%if 0%{?suse_version} > 1315
BuildRequires:  sfml2-devel
%endif
BuildRequires:  sed
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(xi)
ExclusiveArch:  x86_64 aarch64
Provides:       dolphin-qt = %{version}
Obsoletes:      dolphin-qt < %{version}
Recommends:     %{name}-lang = %{version}

%description
Dolphin is an emulator for two Nintendo video game consoles, GameCube and the Wii.
It allows PC gamers to enjoy games for these two consoles in full HD with several
enhancements such as compatibility with all PC controllers, turbo speed,
networked multiplayer, and more.
Most games run perfectly or with minor bugs.

%lang_package

%prep
%setup -q

%build
export CCFLAGS='%{optflags} -Wno-return-type'
cmake . \
    -DDISTRIBUTOR=openSUSE \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DENABLE_LTO=OFF \
    -DENABLE_QT=ON \
    -DDOLPHIN_WC_DESCRIBE=%{_revision_description} \
    -DDOLPHIN_WC_REVISION=%{_revision} \
    -DDOLPHIN_WC_BRANCH="master" \
    -DDOLPHIN_WC_IS_STABLE=0 \
    -G "Ninja"
ninja -v

%install
export CCFLAGS='%{optflags}'
DESTDIR=%{buildroot} ninja install

mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 Data/51-usb-device.rules %{buildroot}%{_udevrulesdir}/51-dolphin-usb-device.rules

# Remove gtest and dev files
rm -rf %{buildroot}%{_prefix}/lib/libgtest*
rm -rf %{buildroot}%{_includedir}

# Get rid of static libraries
find %{buildroot} -name '*.a' -delete

%fdupes -s %{buildroot}
%find_lang %{name}

%files lang -f %name.lang

%files
%defattr(0644, root, root, 0755)
%license license.txt
%attr(0755, root, root) %{_bindir}/%{name}
%attr(0755, root, root) %{_bindir}/%{name}-nogui
%{_datadir}/%{name}
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/dolphin-emu.6%{ext_man}
%{_mandir}/man6/dolphin-emu-nogui.6%{ext_man}
%{_udevrulesdir}/51-dolphin-usb-device.rules

%changelog
