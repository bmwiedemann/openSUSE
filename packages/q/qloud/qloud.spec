#
# spec file for package qloud
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


Name:           qloud
Version:        1.4.2
Release:        0
Summary:        Tool to measure
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/molke-productions/qloud
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Qwt6)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sndfile)
Requires:       jack

%description
QLoud - tool to measure loudspeaker frequency and step responses and
distortions.

Target use:
 * loudspeakers DIY-ing (xovers tuning).

%prep
%autosetup -p1

%build
%qmake5 PREFIX=%{_prefix}
%make_build

%install
%qmake5_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/qloud.xpm
%{_datadir}/applications/qloud.desktop

%changelog
