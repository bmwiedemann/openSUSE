#
# spec file for package xcb
#
# Copyright (c) 2025 SUSE LLC
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


%define _appdefdif %{_datadir}/X11/app-defaults
Name:           xcb
Version:        2.5
Release:        0
Summary:        X11 cut&paste utility
License:        MIT
Group:          System/X11/Utilities
URL:            http://www.goof.com/pcg/marc/xcb.html
Source:         %{name}-%{version}.tar.bz2
Patch0:         xcb-prototype.patch
# fix build with gcc 15
Patch1:         xcb-gcc15.patch
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)

%description
Xcb provides access to the cut buffers built into every X server. It
allows the buffers to be manipulated either via the command line or
with the mouse in a point and click manner.  The buffers can be used as
holding pens to store and retrieve arbitrary data fragments, so any
number of different pieces of data can be saved and recalled later. The
program is designed primarily for use with textual data.

%prep
%autosetup -p1

%build
xmkmf -a
%make_build CCOPTIONS="%{optflags}"

%install
%make_install install.man

%files
%doc README Changes
%{_bindir}/xcb
%{_appdefdif}
%{_mandir}/man1/xcb.1x*

%changelog
