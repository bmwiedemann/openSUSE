#
# spec file for package netdate
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           netdate
Version:        1.2
Release:        0
Summary:        Set Date and Time by ARPA Internet RFC 868
License:        SUSE-Public-Domain
URL:            ftp://ftp.code-monkey.de/pub/netdate/
Source:         netdate-%{version}.tar.bz2
Patch0:         %{name}-%{version}.dif
Provides:       nkitb:%{_sbindir}/netdate

%description
Netdate takes a list of names of Internet hosts as arguments, selects
the one that supplies the best time, and sets the system time
accordingly.

The "best" time is chosen by polling the named hosts once each to find
their times and taking their differences from the local host's time.
These differences are used to find the largest group of hosts whose
times agree with each other within a certain limit. The first host in
the largest group is picked as the best host.

%prep
%setup -q
%patch0

%build
%make_build

%install
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_mandir}/man8
%make_install

%files
%license COPYRIGHT
%{_sbindir}/netdate
%{_mandir}/man8/netdate.8%{?ext_man}

%changelog
