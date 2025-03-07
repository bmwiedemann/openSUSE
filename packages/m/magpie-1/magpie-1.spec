#
# spec file for package magpie-1
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

%define rname magpie
Name:           magpie-1
Version:        0.0.0+209
Release:        0
Summary:        Magpie v1
License:        Apache-2.0
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/magpie
Source0:        %{rname}-%{version}.tar.xz
Obsoletes:      magpie
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(argparse)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.18)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)

%description
Magpie v1 is a wlroots-based Wayland compositor designed for the Budgie Desktop.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/magpie-wm
%{_datadir}/applications/org.buddiesofbudgie.MagpieWm.desktop

%changelog
