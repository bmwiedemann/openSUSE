#
# spec file for package arping2
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


Name:           arping2
Version:        2.20
Release:        0
Summary:        Layer-2 Ethernet pinger
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
Url:            http://www.habets.pp.se/synscan/programs.php?prog=arping

#Git-Clone:	git://github.com/ThomasHabets/arping
Source0:        http://www.habets.pp.se/synscan/files/arping-%version.tar.gz
Source1:        http://www.habets.pp.se/synscan/files/arping-%version.tar.gz.asc
Source2:        %name.keyring
Patch1:         arping-setgroups.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel

%description
Arping is a util to find out it a specific IP address on the LAN is
"taken" and what MAC address owns it. It is designed to work on
unrouted networks and with ICMP-blocking hosts.

%prep
%setup -n arping-%version
%patch -P 1 -p1

%build
%configure
make %{?_smp_mflags}

%install
b="%buildroot";
%make_install
# Avoid collision with iputils's inferior arping.
mv "$b/%_sbindir"/{arping,%name};
mv "$b/%_mandir/man8"/{arping.8,%name.8};

%files
%defattr(-,root,root)
%_sbindir/arping2
%_mandir/man8/arping2.8*
%doc README

%changelog
