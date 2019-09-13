#
# spec file for package bitmap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           bitmap
Version:        1.0.9
Release:        0
Summary:        X bitmap editor and converter utilities
License:        X11
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xbitmaps)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The bitmap program is a rudimentary tool for creating or editing
rectangular images made up of 1's and 0's. Bitmaps are used in X for
defining clipping regions, cursor shapes, icon shapes, and tile and
stipple patterns.

The bmtoa and atobm filters convert bitmap files to and from ASCII
strings. They are most commonly used to quickly print out bitmaps and
to generate versions for including in text.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/atobm
%{_bindir}/bitmap
%{_bindir}/bmtoa
%{_includedir}/X11/bitmaps/
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Bitmap
%{_datadir}/X11/app-defaults/Bitmap-color
%{_datadir}/X11/app-defaults/Bitmap-nocase
%{_mandir}/man1/atobm.1%{?ext_man}
%{_mandir}/man1/bitmap.1%{?ext_man}
%{_mandir}/man1/bmtoa.1%{?ext_man}

%changelog
