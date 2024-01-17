#
# spec file for package WindowMaker-themes
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           WindowMaker-themes
BuildArch:      noarch
Summary:        Themes for Window Maker
Version:        0.1
Release:        374
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            http://www.windowmaker.org
Requires:       WindowMaker
Provides:       wmthemes
Obsoletes:      wmthemes
Source0:        Anger.tar.gz
Source1:        Cosmic.tar.gz
Source2:        CosmicDream.tar.gz
Source3:        Dark.tar.gz
Source4:        FearTech.tar.gz
Source5:        FreakE.tar.gz
Source6:        Generic.tar.gz
Source7:        InDreams.tar.gz
Source8:        Intrigue.tar.gz
Source9:        Lichen.tar.gz
Source10:       Linux.tar.gz
Source11:       Midnight.tar.gz
Source12:       Star19.tar.gz
Source13:       Vivaldi.tar.gz
Source14:       WO.tar.gz
Source15:       YesterdayIdied.tar.gz
Source16:       Circuits.tar.gz
Source17:       COPYRIGHT.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains themes for the Window Maker window manager.
Documentation:

/usr/share/doc/packages/wmthemes

%prep
%setup -c -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16
mv `find Themes -name "*.txt" ` .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/WindowMaker
cp -pr Backgrounds Themes $RPM_BUILD_ROOT/usr/share/WindowMaker
find $RPM_BUILD_ROOT/usr/share/WindowMaker -type f -exec chmod 644 {} \;
find $RPM_BUILD_ROOT/usr/share/WindowMaker -type d -exec chmod 755 {} \;

%files
%defattr(-,root,root)
%dir /usr/share/WindowMaker
/usr/share/WindowMaker/Backgrounds
/usr/share/WindowMaker/Themes
%doc *.txt

%changelog
