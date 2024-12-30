#
# spec file for package redsea
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           redsea
Version:        1.1.0
Release:        0
Summary:        An RDS decoder
License:        MIT
Group:          Productivity/Hamradio/Other
URL:            https://github.com/windytan/redsea
#Git-Clone:     https://github.com/windytan/redsea.git
Source:         https://github.com/windytan/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libliquid-devel
BuildRequires:  libsndfile-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(nlohmann_json)
Recommends:     jq
Recommends:     rtl-sdr

%description
redsea is a command-line RDS (Radio Data System) decoder.
It can be used with any RTL-SDR USB radio stick with the rtl_fm tool.
It can also decode the raw ASCII bitstream, the hex format used by RDS Spy,
and audio files containing multiplex signals (MPX).

RDS groups are printed to the terminal as line-delimited JSON objects
or, optionally, undecoded hex blocks (-x).

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc CHANGES.md README.md
%{_bindir}/redsea

%changelog
