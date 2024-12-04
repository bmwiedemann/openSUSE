#
# spec file for package xcolors
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


%define _xorg7libs %{_lib}
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %{_mandir}
%define _xorg7pixmaps include
%define _xorg7libshare share
Name:           xcolors
Version:        91.10.4
Release:        0
Summary:        Displays colors defined in rgb.txt
License:        SUSE-Public-Domain
Group:          System/X11/Utilities
Source:         xcolors-04oct91.tar.bz2
Patch0:         xcolors-04oct91.patch
Patch1:         xcolors-04oct91-xorg7_rgbtxt.patch
Patch2:         xcolors-gcc14.patch
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)

%description
Xcolorsel displays colors defined in rgb.txt. You can create an RGB
file by redirecting the output of showrgb to a file.

%prep
%autosetup -n xcolors-04oct91 -p0

%build
xmkmf -a
%make_build CCOPTIONS="%{optflags}"

%install
%make_install install.man

%files
%doc Changes
%{_prefix}/%{_xorg7bin}/xcolors
%dir %{_prefix}/%{_xorg7libshare}/X11/app-defaults
%config %{_prefix}/%{_xorg7libshare}/X11/app-defaults/Xcolors
%{_xorg7_mandir}/man1/xcolors.1x*

%changelog
