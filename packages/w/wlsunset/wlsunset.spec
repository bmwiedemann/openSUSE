#
# spec file for package wlsunset
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


Name:           wlsunset
Version:        0.2.0
Release:        0
Summary:        Day/night gamma adjustments for Wayland compositors
License:        MIT
URL:            https://git.sr.ht/~kennylevinsen/wlsunset
Source:         https://git.sr.ht/~kennylevinsen/wlsunset/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(scdoc) >= 1.9.7
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

%description
Day/night gamma adjustments for Wayland compositors supporting wlr-gamma-control-unstable-v1

%prep
%setup -q

%build
%meson

%meson_build

%install
%meson_install

%files
%{_bindir}/wlsunset
%{_mandir}/man1/wlsunset.1%{?ext_man}

%changelog
