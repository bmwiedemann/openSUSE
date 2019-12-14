#
# spec file for package qloud
#
# Copyright (c) 2019 SUSE LLC
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
Version:        1.2
Release:        0
Summary:        Tool to measure
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://gaydenko.com/qloud/
Source0:        http://gaydenko.com/qloud/download/%{name}-%{version}.tar.bz2
# PATCh-FIX-UPSTREAM qloud-Qt5.patch aloisio@gmx.com -- adapted from this fork: https://github.com/molke-productions/qloud
Patch0:         qloud-Qt5.patch
BuildRequires:  pkgconfig
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
%qmake5
%make_build

%install
%qmake5_install

%files
%license COPYING
%doc README
%{_bindir}/%{name}

%changelog
