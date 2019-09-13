#
# spec file for package Crystalcursors
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           Crystalcursors
BuildRequires:  libpng
BuildRequires:  xcursorgen
Url:            http://digilander.iol.it/m4rt/crystalcursors.html
Summary:        Mouse Cursors in Crystal Icon Style
License:        LGPL-2.1+
Group:          System/X11/Icons
Version:        0.5
Release:        0
Source:         6240-%{name}.tar.bz2
Patch:          root-installation.diff
Patch1:         Crystalcursors.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Four different mouse cursor icon sets in the KDE CrystalSVG style. In
white, gray, blue, and green versions. They can be selected from KDE
Control Center, in the mouse configuration.

%prep
%setup -q -n %name
%patch1
%patch

%build
# the crowd complained about the speed ..
for i in */watch/*conf; do
 awk '{ print $1" "$2" "$3" "$4" 240" }' $i > ${i}.new
 mv ${i}.new ${i}
done
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-, root, root)
%doc CHANGELOG CREDITS LICENSE README
/usr/share/icons/*

%changelog
