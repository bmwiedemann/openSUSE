#
# spec file for package xcur2png
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           xcur2png
Version:        0.7.1
Release:        0
Summary:        A program which let you take PNG image from X cursor
License:        GPL-3.0-or-later
URL:            https://github.com/eworm-de/xcur2png
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-wrong-math.patch [gh#eworm-de/xcur2png#5] -- Fix incorrect color conversion causing opaque white pixels to become black
Patch0:         fix-wrong-math.patch

BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xcursor)

%description
xcur2png is a program which let you take PNG image from X cursor, and 
generate config-file which is reusable by xcursorgen. To put it simply, 
it is converter from X cursor to PNG image

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/xcur2png
%{_mandir}/man1/xcur2png.1%{?ext_man}

%changelog
