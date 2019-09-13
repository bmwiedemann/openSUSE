#
# spec file for package tuxcursors
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


Name:           tuxcursors
Summary:        Tux Cursors!
License:        GPL-2.0
Group:          System/X11/Icons
Version:        0.5
Release:        0
Source:         tuxcursors-0.5.tar.bz2
Source1:        tuxcursors.sh
BuildRequires:  xcursorgen
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A cursor set that has nice animated penguins.

%prep
%setup -n tuxcursors

%build
./build.sh

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/icons
cp -a tuxcursors $RPM_BUILD_ROOT/usr/share/icons
install -m 755 -D %{S:1} $RPM_BUILD_ROOT/usr/bin/%{name}

%files
%defattr(-,root,root)
/usr/share/icons/tuxcursors
/usr/bin/tuxcursors
%doc LICENSE COPYING

%changelog
