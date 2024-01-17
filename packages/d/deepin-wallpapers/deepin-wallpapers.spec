#
# spec file for package deepin-wallpapers
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

Name:           deepin-wallpapers
Version:        1.7.10
Release:        0
Summary:        Deepin Wallpapers
License:        CC0-1.0
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/deepin-wallpapers
Source0:        https://github.com/linuxdeepin/deepin-wallpapers/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Wallpapers provides wallpapers of Deepin Desktop.

%package community
Summary:        Deepin Community Wallpapers
License:        CC0-1.0

%description community
Deepin Wallpapers Community provides community wallpapers of Deepin Desktop.

%prep
%setup -q

%build

%install
install -d %{buildroot}/%{_datadir}/wallpapers/
cp -ar deepin %{buildroot}/%{_datadir}/wallpapers/

%files
%defattr(-,root,root,-)
%doc README.md 
%license LICENSE
%dir %{_datadir}/wallpapers
%{_datadir}/wallpapers/deepin/
%exclude %{_datadir}/wallpapers/deepin/*unsplash.jpg

%files community
%defattr(-,root,root,-)
%doc README.md 
%license LICENSE
%{_datadir}/wallpapers/deepin/*unsplash.jpg

%changelog
