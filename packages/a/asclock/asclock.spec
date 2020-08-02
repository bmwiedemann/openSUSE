#
# spec file for package asclock
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           asclock
Version:        2.0.12
Release:        0
Summary:        AfterStep digital clock
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Clocks
URL:            http://www.tigr.net/afterstep/
Source:         asclock-%{version}.tar.bz2
Patch0:         gcc4.diff
BuildRequires:  fdupes
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
Provides:       astools:%{_prefix}/X11R6/bin/asclock

%description
A swallowable applet shows clock and calendar. Supports themes for
different looks.

%prep
%autosetup -p0

%build
rm -f languages/english/*~
# not a autotools configure
%configure <<EOF
shaped
1
EOF
%make_build CC="cc %{optflags} -fcommon"

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/asclock
cp -ar themes %{buildroot}%{_datadir}/asclock/
cp -ar languages %{buildroot}%{_datadir}/asclock/

%fdupes %{buildroot}

%files
%{_bindir}/asclock
%{_datadir}/asclock

%changelog
