#
# spec file for package openrdate
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


Name:           openrdate
Version:        1.2
Release:        0
Summary:        Retrieve the time from an RFC 868 server
License:        GPL-2.0+
Group:          Productivity/Networking/Other
URL:            http://sourceforge.net/projects/openrdate/
Source:         http://sourceforge.net/projects/openrdate/files/openrdate/%{name}-%{version}.tar.gz/%{name}-%{version}.tar.gz
Provides:       rdate = %{version}
# A little tricky but should work
Obsoletes:      rdate < 1.5

%description
rdate retrieves and optionally sets the time from an RFC 868 server. It is
a simple, significantly less complex (and less functional) replacement for
NTP.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/rdate
%{_mandir}/man8/rdate.8%{ext_man}

%changelog
