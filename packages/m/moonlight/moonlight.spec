#
# spec file for package moonlight
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


Name:           moonlight
Version:        6.1.0
Release:        0
Summary:        GameStream client for PCs
License:        GPL-3.0-only
URL:            https://moonlight-stream.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(sdl2) >= 2.0.16
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  qt6-declarative-devel

%description

Moonlight PC is an open source PC client for NVIDIA GameStream and Sunshine.

%prep
%autosetup

%build
%qmake6 PREFIX=%{_prefix}
%qmake6_build

%install
%qmake6_install

%check

%files
%license LICENSE
%doc README.md
%{_bindir}/moonlight
%{_datadir}/applications/com.moonlight_stream.Moonlight.desktop
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/com.moonlight_stream.Moonlight.appdata.xml

%changelog

