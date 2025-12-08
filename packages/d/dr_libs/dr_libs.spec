#
# spec file for package dr_libs
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         flacversion 0.13.2
%define         mp3version 0.7.2
%define         wavversion 0.14.2
Name:           dr_libs
Version:        20251202
Release:        0
Summary:        Audio decoding libraries for C/C++, each in a single source file
License:        MIT-0 OR Unlicense
URL:            https://github.com/mackron/dr_libs
Source0:        %{name}-%{version}.tar.gz
Patch0:         fix-headers.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  miniaudio-devel
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(sndfile)

%description
Public domain, single file audio decoding libraries for C and C++.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Provides:       dr_flac = %{flacversion}
Provides:       dr_mp3 = %{mp3version}
Provides:       dr_wav = %{wavversion}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake -DDR_LIBS_BUILD_TESTS=ON
%cmake_build

%install
install -t '%{buildroot}%{_includedir}/dr' -p -m 0644 -D dr_*.h

%check
%ctest --exclude-regex "^($.wav_encoding|wav_encoding|wav_playback|wav_playback_cpp|mp3_(basic|extract|playback))$"

%files devel
%license LICENSE
%doc README.md
%{_includedir}/dr

%changelog
