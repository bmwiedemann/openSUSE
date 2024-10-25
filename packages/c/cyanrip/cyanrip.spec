#
# spec file for package cyanrip
#
# Copyright (c) 2024 SUSE LLC
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


Name:           cyanrip
Version:        0.9.3.1
Release:        0
Summary:        Bule-ish CD ripper
License:        LGPL-2.1-or-later
URL:            https://github.com/cyanreg/cyanrip
Source:         https://github.com/cyanreg/cyanrip/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  meson >= 0.53.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libavcodec) >= 58.19.100
BuildRequires:  pkgconfig(libavfilter) >= 7.16.100
BuildRequires:  pkgconfig(libavformat) >= 58.13.100
BuildRequires:  pkgconfig(libavutil) >= 56.15.100
BuildRequires:  pkgconfig(libcdio) >= 2.0
BuildRequires:  pkgconfig(libcdio_paranoia) >= 10.2
BuildRequires:  pkgconfig(libcurl) >= 7.66.0
BuildRequires:  pkgconfig(libmusicbrainz5) >= 5.1
BuildRequires:  pkgconfig(libswresample) >= 3.2.100

%description
Fully featured CD ripping program able to take out most of the tedium. Fully accurate, has advanced features most rippers don't, yet has no bloat and is cross-platform.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%license LICENSE.md
%doc README.md

%changelog
