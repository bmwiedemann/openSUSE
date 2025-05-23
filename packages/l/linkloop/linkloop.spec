#
# spec file for package linkloop
#
# Copyright (c) 2023 SUSE LLC
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


Name:           linkloop
Summary:        Test network connectivity at link layer (layer-2)
Version:        1.0.0
Release:        0
License:        GPL-2.0-or-later
BuildRequires:  automake
Group:          Productivity/Networking/Other
Source:         linkloop-%{version}-hp.tar.bz2
Patch0:         linkloop-clear-size-fix.diff
URL:            http://freshmeat.net/projects/linkloop/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Linkloop is similar to ping, but tests the network connectivity at the
link layer (layer 2) instead of the network layer (layer 3).



Authors:
--------
    Oron Peled <oron@actcom.co.il>
    Dominique Domet de Mont <Dominique.Domet-de-Mont@hp.com>

%prep
%autosetup -p0 -n %{name}-%{version}-hp

%build
autoreconf -fi
%configure
%make_build

%install
make DESTDIR="$RPM_BUILD_ROOT" install
# remove unneeded binaries (it's already supported in recent kernel)
rm -rf $RPM_BUILD_ROOT/etc/
rm -rf $RPM_BUILD_ROOT%{_bindir}/linkloop_reply

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_mandir}/man*/*

%changelog
