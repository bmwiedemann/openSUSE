#
# spec file for package root-tail
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           root-tail
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Provides:       roottail
Obsoletes:      roottail
Version:        1.2
Release:        0
Summary:        Print Text Directly to the X Window System Root Window
License:        GPL-2.0+
Group:          System/X11/Utilities
Source:         %name-%version.tar.bz2
Patch0:         default-fontset.patch
Patch1:         %name-%version-shade.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://goof.com/pcg/marc/root-tail.html

%description
Tails a given file anywhere on your X Window System root window with a
transparent background. It is customizable with regards to font, color,
and more.



Authors:
--------
    Mike Baker <mjbaker@mtu.edu>
    Marc Lehmann <pcg@goof.com>

%prep
%setup
%patch0 -p1 -b .default-fontset
%patch1 -p1 -b .shade

%build
xmkmf -a
make CFLAGS="$CFLAGS $RPM_OPT_FLAGS"

%install
make "DESTDIR=$RPM_BUILD_ROOT" install
make "DESTDIR=$RPM_BUILD_ROOT" install.man

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
