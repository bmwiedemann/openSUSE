#
# spec file for package fmtools
#
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


Name:           fmtools
Version:        2.0.8
Release:        0
Summary:        FM radio tuner for V4L2 supported devices
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://benpfaff.org/fmtools/
#Git-Clone:     https://repo.or.cz/fmtools.git
Source0:        https://benpfaff.org/fmtools/%{name}-%{version}.tar.gz
Source1:        https://benpfaff.org/fmtools/%{name}-%{version}.tar.gz.asc
Patch0:         fmtools-report-correct-version.patch
BuildRequires:  autoconf
BuildRequires:  automake

%description
Command-line utilities for adjusting the frequency and volume and
muting of supported FM radio cards.

fm - control frequency, volume, mute/unmute of FM radio card
fmscan - scan FM band for radio stations

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README
%{_bindir}/fm
%{_bindir}/fmscan
%{_mandir}/man1/fm.1%{?ext_man}
%{_mandir}/man1/fmscan.1%{?ext_man}

%changelog
