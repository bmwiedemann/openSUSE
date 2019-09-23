#
# spec file for package dvbsnoop
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


Name:           dvbsnoop
Version:        1.4.50
Release:        0
Summary:        DVB / MPEG stream analyzer program
License:        GPL-2.0+
Group:          Hardware/TV
Url:            https://dvbsnoop.sourceforge.net/
Source:         https://sourceforge.net/projects/dvbsnoop/files/dvbsnoop/dvbsnoop-%{version}/dvbsnoop-%{version}.tar.gz

%description
Its purpose is to debug, dump or view digital stream information (e.g.
digital television broadcasts) send via satellite, cable or terrestrial.
Streams can be SI, PES or TS. Basically you can describe dvbsnoop as a
"swiss army knife" analyzing program for DVB, MHP, DSM-CC or MPEG - similar
to TCP network sniffer programs like the old and famous snoop on Sun
Solaris or tcpdump on Linux (which is in fact a kind of a clone of SunOS
'snoop'). You may also analyze offline mpeg streams, e.g. stored on DVD or
mpeg2 movie files.

%prep
%setup -q
chmod 644 AUTHORS COPYING NEWS README

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/dvbsnoop
%{_mandir}/man1/dvbsnoop.1%{ext_man}

%changelog
