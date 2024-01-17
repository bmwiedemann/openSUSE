#
# spec file for package dynamic-wallpapers-11x
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           dynamic-wallpapers-11x
Url:            http://gitorious.org/opensuse/art/trees/master/wallpaper
Summary:        Dynamic wallpapers for GNOME, from previous versions of openSUSE
License:        GPL-3.0 and CC-BY-SA-2.5
Group:          System/GUI/GNOME
Version:        11.4
Release:        0
Source0:        gnome-wallpaper-11.0.2.tar.bz2
Source1:        gnome-wallpaper-11.1.tar.bz2
Source2:        gnome-wallpaper-11.2.tar.bz2
Source3:        gnome-wallpaper-11.3.tar.bz2
Source4:        gnome-wallpaper-11.4.tar.bz2
Source10:       COPYING
Source11:       COPYING.CCBYSA
Source12:       COPYING.GPLv3
Enhances:       dynamic-wallpaper-branding-openSUSE
# The files were installed by openSUSE-dynamic-wallpapers-old (from gconf2-branding-openSUSE) up until openSUSE 11.4 (included)
Provides:       openSUSE-dynamic-wallpapers-old = %{version}
Obsoletes:      openSUSE-dynamic-wallpapers-old <= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains dynamic wallpapers from previous versions of
openSUSE.

A dynamic wallpaper changes depending on the time of the day: it is
generally bright during the day, and dark during the night.

%prep
%setup -q -T -a0 -a1 -a2 -a3 -a4 -c %{name}-%{version}
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} .

%build

%install
install -d %{buildroot}%{_datadir}/backgrounds %{buildroot}%{_datadir}/gnome-background-properties

cp -a grass %{buildroot}%{_datadir}/backgrounds/
install -m0644 desktop-backgrounds-grass.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.0.xml
cp -a glass %{buildroot}%{_datadir}/backgrounds/
install -m0644 desktop-backgrounds-glass.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.1.xml
cp -a daft %{buildroot}%{_datadir}/backgrounds/
install -m0644 desktop-backgrounds-daft.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.2.xml
cp -a gnome-wallpaper-11.3/IK %{buildroot}%{_datadir}/backgrounds/
install -m0644 gnome-wallpaper-11.3/desktop-backgrounds-IK.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.3.xml
cp -a stripes %{buildroot}%{_datadir}/backgrounds/
install -m0644 desktop-backgrounds-stripes.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.4.xml

%files
%defattr(-,root,root)
%doc COPYING COPYING.CCBYSA COPYING.GPLv3
%{_datadir}/backgrounds/grass/
%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.0.xml
%{_datadir}/backgrounds/glass/
%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.1.xml
%{_datadir}/backgrounds/daft/
%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.2.xml
%{_datadir}/backgrounds/IK/
%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.3.xml
%{_datadir}/backgrounds/stripes/
%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.4.xml
# FIXME: Should be owned by a different package:
%dir %{_datadir}/backgrounds
%dir %{_datadir}/gnome-background-properties

%changelog
