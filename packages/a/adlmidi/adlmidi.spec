#
# spec file for package adlmidi
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           adlmidi
Version:        1.2.6.2
Release:        0
Summary:        A MIDI player that uses OPL3 emulation
License:        GPL-3.0-only AND GPL-2.0-or-later
URL:            https://bisqwit.iki.fi/source/adlmidi.html
#Git-Clone:     https://github.com/bisqwit/adlmidi.git
Source:         https://bisqwit.iki.fi/src/arch/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM
Patch1:         adlmidi-fix-arm.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)

%description
AdlMIDI is a commandline program that plays MIDI files using software
OPL3 emulation (FM synthesis).

%prep
%setup -q
%patch1 -p1
sed -i 's|-march=native||' Makefile

%build
export CPPFLAGS='%{optflags}'
make %{?_smp_mflags}

%install
install -D -m 0755 adlmidi %{buildroot}%{_bindir}/adlmidi

%files
%doc README.html
%{_bindir}/adlmidi

%changelog
