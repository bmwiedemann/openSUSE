#
# spec file for package asclock
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           asclock
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
Provides:       astools:/usr/X11R6/bin/asclock
Version:        2.0.12
Release:        0
Summary:        AfterStep digital clock
License:        GPL-2.0+
Group:          Amusements/Toys/Clocks
Url:            http://www.tigr.net/afterstep/
Source:         asclock-%{version}.tar.bz2
Patch:          gcc4.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A swallowable applet shows clock and calendar. Supports themes for
different looks.

%prep
%setup -q
%patch

%build
rm -f languages/english/*~
./configure <<EOF
shaped
1
EOF
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/usr/share/asclock
cp -ar themes $RPM_BUILD_ROOT/usr/share/asclock/
cp -ar languages $RPM_BUILD_ROOT/usr/share/asclock/

%files
%defattr(-,root,root)
/usr/bin/asclock
/usr/share/asclock

%changelog
