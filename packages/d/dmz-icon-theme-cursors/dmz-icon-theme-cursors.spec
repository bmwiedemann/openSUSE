#
# spec file for package dmz-icon-theme-cursors
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


Name:           dmz-icon-theme-cursors
Version:        11.3.0
Release:        0
# As documented on http://packages.debian.org/changelogs/pool/main/d/dmz-cursor-theme/dmz-cursor-theme_0.4.3/dmz-cursor-theme.copyright
Summary:        DMZ Cursor Theme
License:        CC-BY-SA-3.0
Group:          System/GUI/GNOME
Source:         dmz-cursor-theme_0.4.4.tar.gz
Requires:       hicolor-icon-theme
BuildRequires:  xcursorgen
Provides:       icon-theme-dmz-cursors = %{version}
Obsoletes:      icon-theme-dmz-cursors < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the DMZ cursor theme for X.

%prep
%setup -q -n dmz-cursor-theme-0.4.4

%build
for i in Black White; do
	( cd DMZ-$i/pngs; ./make.sh )
done

%install
for i in Black White; do
	mkdir -p %{buildroot}%{_datadir}/icons/DMZ-$i
	cp -a DMZ-$i/*.theme %{buildroot}%{_datadir}/icons/DMZ-$i/
	cp -a DMZ-$i/xcursors %{buildroot}%{_datadir}/icons/DMZ-$i/cursors
done

%files
%defattr (-, root, root)
%{_datadir}/icons/DMZ-Black
%{_datadir}/icons/DMZ-White

%changelog
