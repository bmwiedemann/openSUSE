#
# spec file for package xengine
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


Name:           xengine
Version:        1.11
Release:        0
Summary:        Reciprocating engine for X
License:        ISC
Group:          Productivity/Scientific/Physics
Source:         %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-pi.patch
Patch1:         %{name}-%{version}-warnings-fix.patch
Patch2:         %{name}-%{version}-gcc14.patch
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb /usr/share/X11/xkb
%define _xorg7_termcap /usr/lib/X11/etc
%define _xorg7_serverincl /usr/include/xorg
%define _xorg7_fonts /usr/share/fonts
#%define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix /usr

%description
Xengine displays a reciprocating engine in a window and is a benchmark
for X.

%prep
%autosetup -p0

%build
xmkmf -a
make %{?_smp_mflags} CCOPTIONS="%optflags"

%install
make "DESTDIR=$RPM_BUILD_ROOT" install install.man

%files
%defattr(-,root,root)
/usr/%{_xorg7bin}/xengine
%doc %{_xorg7_mandir}/man1/xengine.1x*

%changelog
