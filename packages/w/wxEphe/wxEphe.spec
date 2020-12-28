#
# spec file for package wxEphe
#
# Copyright (c) 2020 SUSE LLC
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


Name:           wxEphe
Version:        1.7
Release:        0
Summary:        Astronomical ephemeris for the Sun, Moon and solar system planets
License:        GPL-3.0-only
Group:          Productivity/Scientific/Astronomy
URL:            http://www.jpmr.org/
#Freshcode-URL:	https://freshcode.club/projects/wxephe
Source:         https://downloads.sf.net/wxephe/wxEphe-%version.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  wxWidgets-devel >= 3

%description
wxEphe displays astronomical ephemeris for the Sun, the Moon and
solar system planets, given the date and observer's location.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
%find_lang %name

%files -f %name.lang
%license COPYING
%_bindir/wxEphe
%_datadir/applications/*
%_datadir/pixmaps/*

%changelog
