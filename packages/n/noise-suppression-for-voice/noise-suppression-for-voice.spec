#
# spec file for package noise-suppression-for-voice
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


Name:           noise-suppression-for-voice
Version:        1.03+git1.226f03b
Release:        0
Summary:        Noise suppression plugin based on Xiph's RNNoise
License:        GPL-3.0-only
URL:            https://github.com/werman/noise-suppression-for-voice
Source:         %{name}-%{version}.tar.xz
BuildRequires:  Mesa-libGL-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ladspa
BuildRequires:  ladspa-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXrandr-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)

%description
The plugin is meant to suppress a wide range of noise origins
(from original paper): computer fans, office, crowd, airplane,
car, train, construction.

From my tests mild background noise is always suppressed,
loud sounds, like clicking of mechanical keyboard, are
suppressed while there is no voice however they are only
reduced in volume when voice is present.

The plugin is made to work with 1 channel and/or 2 channels
(ladspa plugin), 16 bit, 48000 Hz audio input.
Other sample rates may work, or not...

%package     -n lv2-rnnoise
Summary:        Noise suppression plugin based on Xiph's RNNoise - lv2 plugin

%description -n lv2-rnnoise
The plugin is meant to suppress a wide range of noise origins
(from original paper): computer fans, office, crowd, airplane,
car, train, construction.

From my tests mild background noise is always suppressed,
loud sounds, like clicking of mechanical keyboard, are
suppressed while there is no voice however they are only
reduced in volume when voice is present.

The plugin is made to work with 1 channel and/or 2 channels
(ladspa plugin), 16 bit, 48000 Hz audio input.
Other sample rates may work, or not...

This package holds the lv2 plugin.

%package     -n vst3-rnnoise
Summary:        Noise suppression plugin based on Xiph's RNNoise - vst3 plugin

%description -n vst3-rnnoise
The plugin is meant to suppress a wide range of noise origins
(from original paper): computer fans, office, crowd, airplane,
car, train, construction.

From my tests mild background noise is always suppressed,
loud sounds, like clicking of mechanical keyboard, are
suppressed while there is no voice however they are only
reduced in volume when voice is present.

The plugin is made to work with 1 channel and/or 2 channels
(ladspa plugin), 16 bit, 48000 Hz audio input.
Other sample rates may work, or not...

This package holds the vst3 plugin.

%package     -n vst-rnnoise
Summary:        Noise suppression plugin based on Xiph's RNNoise - vst plugin

%description -n vst-rnnoise
The plugin is meant to suppress a wide range of noise origins
(from original paper): computer fans, office, crowd, airplane,
car, train, construction.

From my tests mild background noise is always suppressed,
loud sounds, like clicking of mechanical keyboard, are
suppressed while there is no voice however they are only
reduced in volume when voice is present.

The plugin is made to work with 1 channel and/or 2 channels
(ladspa plugin), 16 bit, 48000 Hz audio input.
Other sample rates may work, or not...

This package holds the vst plugin.

%package     -n ladspa-rnnoise
Summary:        Noise suppression plugin based on Xiph's RNNoise - ladspa plugin

%description -n ladspa-rnnoise
The plugin is meant to suppress a wide range of noise origins
(from original paper): computer fans, office, crowd, airplane,
car, train, construction.

From my tests mild background noise is always suppressed,
loud sounds, like clicking of mechanical keyboard, are
suppressed while there is no voice however they are only
reduced in volume when voice is present.

The plugin is made to work with 1 channel and/or 2 channels
(ladspa plugin), 16 bit, 48000 Hz audio input.
Other sample rates may work, or not...

This package holds the ladspa plugin.

%prep
%autosetup -p1

sed -i -e 's/lxvst/vst/' src/juce_plugin/CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n ladspa-rnnoise
%license LICENSE
%doc README.md
%{_libdir}/ladspa/librnnoise_ladspa.so

%files -n lv2-rnnoise
%license LICENSE
%doc README.md
%{_libdir}/lv2/

%files -n vst3-rnnoise
%license LICENSE
%doc README.md
%{_libdir}/vst3/

%files -n vst-rnnoise
%license LICENSE
%doc README.md
%dir %{_libdir}/vst
%{_libdir}/vst/

%changelog
