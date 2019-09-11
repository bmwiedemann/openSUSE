#
# spec file for package xcb
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xcb
%define _appdefdif %_prefix/share/X11/app-defaults
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
Url:            http://www.goof.com/pcg/marc/xcb.html
Version:        2.5
Release:        0
Summary:        X11 cut&paste utility
License:        MIT
Group:          System/X11/Utilities
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xcb provides access to the cut buffers built into every X server. It
allows the buffers to be manipulated either via the command line or
with the mouse in a point and click manner.  The buffers can be used as
holding pens to store and retrieve arbitrary data fragments, so any
number of different pieces of data can be saved and recalled later. The
program is designed primarily for use with textual data.

%prep
%setup -q

%build
xmkmf -a
make CCOPTIONS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make "DESTDIR=$RPM_BUILD_ROOT" install
make "DESTDIR=$RPM_BUILD_ROOT" install.man

%files
%defattr(-,root,root)
%_bindir/xcb
%_appdefdif
%doc %_mandir/man1/xcb.1x*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
