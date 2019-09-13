#
# spec file for package tennebon-dynamic-wallpaper
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



Name:           tennebon-dynamic-wallpaper
License:        CC-BY-SA-2.5
Group:          System/GUI/GNOME
Summary:        Tennebon Dynamic wallpaper for GNOME
Version:        1
Release:        1
Source0:        tennebon-wallpaper.tar.bz2
# Note: the license was discussed by mail with jimmac
Source1:        COPYING
Enhances:       openSUSE-dynamic-wallpaper
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains a dynamic wallpaper based on the Tennebon wallpaper.

A dynamic wallpaper changes depending on the time of the day: it is
generally bright during the day, and dark during the night.

%prep
%setup -q -c
cp %{S:1} .

%build

%install
install -d %{buildroot}%{_datadir}/backgrounds %{buildroot}%{_datadir}/gnome-background-properties
cp -a tennebon %{buildroot}%{_datadir}/backgrounds/
install -m0644 tennebon-dynamic-wallpaper.xml %{buildroot}%{_datadir}/gnome-background-properties/tennebon-dynamic-wallpaper.xml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_datadir}/backgrounds/tennebon/
%{_datadir}/gnome-background-properties/tennebon-dynamic-wallpaper.xml
# FIXME: Should be owned by a different package:
%dir %{_datadir}/backgrounds
%dir %{_datadir}/gnome-background-properties

%changelog
