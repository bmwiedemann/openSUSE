#
# spec file for package gos-wallpapers (Version 2010)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild
# icecream 0


Name:           gos-wallpapers
Version:        2010
Release:        1
Summary:        Good Old SUSE Wallpapers
License:        GPL-2.0+
Group:          System/GUI/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %name.tar.bz2
Source1:        update_rpm
BuildArch:      noarch

%description
This package contains wallpapers from older SUSE releases.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/wallpapers
tar xfj %{SOURCE0} -C $RPM_BUILD_ROOT/usr/share/wallpapers --no-same-owner 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/share/wallpapers

%changelog
