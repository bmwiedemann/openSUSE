#
# spec file for package rgbds
#
# Copyright (c) 2021 SUSE LLC
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


Name:           rgbds
Version:        1.0.1
Release:        0
Summary:        An assembly toolchain for the Nintendo Game Boy & Game Boy Color
License:        MIT
Group:          System/Emulators/Other
URL:            https://rgbds.gbdev.io/
Source:         %{version}/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)

%description
RGBDS (Rednex Game Boy Development System) is a free assembler/linker package
for the Game Boy and Game Boy Color.

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%{_bindir}/rgbasm
%{_bindir}/rgbfix
%{_bindir}/rgbgfx
%{_bindir}/rgblink
%{_mandir}/man1/rgbasm.1%{?ext_man}
%{_mandir}/man1/rgbfix.1%{?ext_man}
%{_mandir}/man1/rgbgfx.1%{?ext_man}
%{_mandir}/man1/rgblink.1%{?ext_man}
%{_mandir}/man5/rgbasm.5%{?ext_man}
%{_mandir}/man5/rgbds.5%{?ext_man}
%{_mandir}/man5/rgbasm-old.5%{?ext_man}
%{_mandir}/man5/rgblink.5%{?ext_man}
%{_mandir}/man7/gbz80.7%{?ext_man}
%{_mandir}/man7/rgbds.7%{?ext_man}

%changelog
