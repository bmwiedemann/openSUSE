#
# spec file for package wallpapers-openSUSE-extra
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wallpapers-openSUSE-extra
Version:        15
Release:        0
Provides:       extra-wallpapers
Conflicts:      otherproviders(branding)
Url:            http://github.com/openSUSE/wallpapers
Source0:        wallpapers.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        openSUSE Extra Wallpapers
License:        CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-4.0
Group:          System/GUI/Other
BuildArch:      noarch

%description
Extra wallpapers for openSUSE Leap %{version}

%prep
%setup -q -c

%build

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
%doc leap%{version}/license/*
/usr/share/gnome-background-properties/wallpapers-leap%{version}.xml
/usr/share/wallpapers
/usr/share/wallpapers/leap%{version}
%dir /usr/share/gnome-background-properties

%changelog
