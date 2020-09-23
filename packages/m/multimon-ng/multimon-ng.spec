#
# spec file for package multimon-ng
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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


Name:           multimon-ng
Version:        1.1.9
Release:        0
Summary:        A fork of multimon that decodes multiple digital transmission modes
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/EliasOenal/multimon-ng
Source:         https://github.com/EliasOenal/multimon-ng/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(x11)
Recommends:     sox

%description
MultimonNG a fork of multimon. It decodes the following digital transmission modes:
* POCSAG512 POCSAG1200 POCSAG2400
* EAS
* UFSK1200 CLIPFSK AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3
* HAPN4800
* FSK9600
* DTMF
* ZVEI1 ZVEI2 ZVEI3 DZVEI PZVEI
* EEA EIA CCIR
* MORSE CW
* FLEX

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/multimon-ng.1%{?ext_man}

%changelog
