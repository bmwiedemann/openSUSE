#
# spec file for package tkfont
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


Name:           tkfont
Version:        1.1
Release:        0
Summary:        Tool to select fonts
License:        GPL-2.0+
Group:          System/X11/Utilities
Requires:       /usr/bin/wish
Source:         %{name}-%{version}.tar.gz
Patch:          %{name}-%{version}.dif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
It is a program similar to xfontsel.



Authors:
--------
    Neil Grant <grantj@sfu.ca>

%prep
%setup
%patch

%build

%install
install -d -m755 %buildroot%_bindir %buildroot/usr/lib/tkfont
install -m 755 tkfont %buildroot%_bindir
install -m 755 FindFont GetFontDirs %buildroot/usr/lib/tkfont

%files
%defattr(-,root,root)
%doc README COPYING *.txt
/usr/lib/tkfont
%_bindir/*

%changelog
