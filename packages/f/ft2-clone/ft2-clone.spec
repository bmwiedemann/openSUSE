#
# spec file for package ft2-clone
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


Name:           ft2-clone
Version:        1.65
Release:        0
Summary:        Fasttracker II clone
License:        BSD-3-Clause AND CC-BY-NC-SA-4.0
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://16-bits.org/ft2.php
#Git-Clone:     https://github.com/8bitbubsy/ft2-clone.git
Source:         https://github.com/8bitbubsy/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  icns-utils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(sdl2)
Provides:       bundled(rtmidi)

%description
Multi-platform clone of the classic music making software
Fasttracker II. It can load XM, MOD, S3M, STM module files.

%prep
%setup -q
icns2png -x "release/macos/ft2-clone-macos.app/Contents/Resources/ft2-clone-macos.icns"
rm -R src/libflac

%build
%cmake -DEXTERNAL_LIBFLAC=ON
%cmake_build

%install
%cmake_install

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 ft2-clone-macos_256x256x32.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%license LICENSE LICENSES.txt src/gfxdata/bmp/LICENSE.txt
%doc README.md release/problems.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
