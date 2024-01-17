#
# spec file for package tkfont
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


Name:           tkfont
Version:        1.1
Release:        0
Summary:        Tool to select fonts
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
Requires:       tk
Requires:       xlsfonts
Source:         %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.dif
Patch1:         tkfont-sort.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
It is a program similar to xfontsel.



Authors:
--------
    Neil Grant <grantj@sfu.ca>

%prep
%setup
%patch0
%patch1

%build

%install
install -d -m755 %buildroot%_bindir %buildroot/usr/lib/tkfont
install -m 755 tkfont %buildroot%_bindir
install -m 755 FindFont GetFontDirs %buildroot/usr/lib/tkfont

%files
%defattr(-,root,root)
%license COPYING
%doc README
%doc *.txt
/usr/lib/tkfont
%_bindir/*

%changelog
