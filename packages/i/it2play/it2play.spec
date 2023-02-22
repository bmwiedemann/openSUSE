#
# spec file for package it2play
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


Name:           it2play
Version:        0~git20230215
Release:        0
Summary:        Bit-accurate C port of Impulse Tracker 2.15's IT replayer
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/8bitbubsy/it2play
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.7
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)

%description
Bit-accurate C port of Impulse Tracker 2.15's IT replayer.
This is a direct port of the original asm source codes.

%prep
%setup -q
sed -i 's/\r$//' README.md

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
