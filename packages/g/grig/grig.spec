#
# spec file for package grig
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define srctag GRIG-0_9_0
Name:           grig
Version:        0.9.0
Release:        0
Summary:        Graphical control program for hamlib
License:        GPL-2.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://groundstation.sourceforge.net/grig/
Source:         https://github.com/fillods/grig/releases/download/%{srctag}/%{name}-%{version}.tar.gz
Patch0:         rename-connect.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gthread-2.0) >= 2.14.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.12.0
BuildRequires:  pkgconfig(hamlib) >= 4.2

%description
Grig is a simple Ham Radio control (CAT) program based on Hamlib. It is
intended to be highly generic presenting the user to the same graphical user
interface regardless of which radio is being controlled.

Grig supports the most commonly used CAT commands that are implemented by
Hamlib, and integrates well with other ham radio programs like Xlog and gMFSK.
Thanks to Hamlib, grig works with most CAT-capable amateur radios.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/grig
%find_lang %{name}

%check
%make_build check

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_bindir}/grig
%{_datadir}/pixmaps/grig
%{_mandir}/man1/grig.1%{?ext_man}

%changelog
