#
# spec file for package numlockx
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


Name:           numlockx
Url:            http://freecode.com/projects/numlockx
BuildRequires:  automake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
Version:        1.2
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       x11-tools:/usr/X11R6/bin/numlock
Summary:        Switch on/off or toggle numlock
License:        MIT
Group:          System/YaST
Source:         http://home.kde.org/~seli/numlockx/numlockx-%{version}.tar.gz

%description
This little thingy allows you to start X with NumLock turned on ( which
is a feature that a lot of people seem to miss and nobody really knew
how to achieve this ). This code relies on X extensions called XTest
and XKB, so you need to have at least one of these X extensions
installed ( you most probably do ).



Authors:
--------
    Lubos Lunak <l.lunak@kde.org>
    XKB stuff by Oswald Buddenhagen <ossi@kde.org>

%prep
%setup

%build
autoreconf -fi
%configure --x-libraries=/usr/%_lib
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README
/usr/bin/numlockx

%changelog
