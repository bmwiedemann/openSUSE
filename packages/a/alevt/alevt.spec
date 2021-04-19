#
# spec file for package alevt
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


Name:           alevt
Version:        1.8.0
Release:        0
Summary:        Teletext and Videotext Decoder for the BTTV Driver
License:        GPL-2.0-or-later
Group:          Hardware/TV
URL:            https://gitlab.com/alevt/alevt
Source0:        %{URL}/-/archive/v%{version}/alevt-v%{version}.tar.bz2
Source1:        alevt.desktop
# PATCH-FEATURE-UPSTREAM use-pkgconfig.patch -- https://gitlab.com/alevt/alevt/-/issues/1
Patch0:         use-pkgconfig.patch
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2)

%description
AleVT is a teletext and videotext decoder and browser for the BTTV
driver (/dev/vbi) and the X Window System.  It features multiple
windows, a page cache, regexp searching, a built-in manual, and more.
There is also a program to get the time from teletext.

%prep
%autosetup -p1 -n alevt-v%{version}
# Enable ZVBI
sed -i "s|#DEFS+=-DUSE_LIBZVBI|DEFS+=-DUSE_LIBZVBI|" Makefile

%build
%make_build OPT="%{optflags}"

%install
%make_install PREFIX="%{_prefix}"
%suse_update_desktop_file -i alevt

%files
%license COPYRIGHT
%doc CHANGELOG README.md
%{_bindir}/alevt
%{_bindir}/alevt-cap
%{_bindir}/alevt-date
%{_datadir}/pixmaps/mini-alevt.xpm
%{_datadir}/applications/*.desktop
%{_mandir}/man1/alevt*.1{,x}*

%changelog
