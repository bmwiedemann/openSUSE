#
# spec file for package nfdump
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


%define nfcapddatadir   %{_localstatedir}/lib/nfcapd
%define sfcapddatadir   %{_localstatedir}/lib/sfcapd
%define nfhomedir       %{_var}/lib/%{name}
%define sover           1_7_1
Name:           nfdump
Version:        1.7.1
Release:        0
Summary:        CLI tools to collect and process netflow data
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/phaag/nfdump
Source:         https://github.com/phaag/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  rrdtool
BuildRequires:  rrdtool-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libcurl)
Requires:       rrdtool

%description
The nfdump tools collect and process netflow data on the command line.
They are part of the NFSEN project which is explained more detailed at
http://www.terena.nl/tech/task-forces/tf-csirt/meeting12/nfsen-Haag.pdf

%package -n libnfdump%{sover}
Summary:        Shared Library part of libnfdump
Group:          System/Libraries

%description -n libnfdump%{sover}
Shared Library part of libnfdump.

%package devel
Summary:        Development files for libnfdump
Group:          Development/Libraries/C and C++
Requires:       libnfdump%{sover} = %{version}

%description devel
This package contains libraries and header files for developing
applications that use libnfdump.

%prep
%setup -q
chmod a-x AUTHORS COPYING LICENSE README.md ChangeLog

%build
autoreconf -fiv
%configure \
        --enable-nfprofile \
        --enable-nftrack \
        --enable-nsel \
        --enable-sflow \
        --enable-influxdb
%make_build

%install
%make_install
install -D -d -m 0750 \
        %{buildroot}%{nfhomedir} \
        %{buildroot}%{nfcapddatadir} \
        %{buildroot}%{sfcapddatadir}
rm -v "%{buildroot}/%{_libdir}"/libnfdump.{a,la}

%check
#%%make_build check

%pre
%{_sbindir}/groupadd -r %{name} &>/dev/null || :
%{_sbindir}/useradd -g %{name} -s /bin/false -r -c "User for Netflow Dumper" -d %{nfhomedir} %{name} &>/dev/null || :

%post   -n libnfdump%{sover} -p /sbin/ldconfig
%postun -n libnfdump%{sover} -p /sbin/ldconfig

%files
%license COPYING LICENSE
%doc AUTHORS README.md ChangeLog
# nfdump.conf.dist: As the name implies it's not really a config file but a template.
# Used the %%config macro only to avoid "W: non-conffile-in-etc /etc/nfdump.conf.dist" warning.
%config %{_sysconfdir}/nfdump.conf.dist
%{_bindir}/nfanon
%{_bindir}/nfcapd
%{_bindir}/nfdump
%{_bindir}/nfexpire
%{_bindir}/nfprofile
%{_bindir}/nfreplay
%{_bindir}/nftrack
%{_bindir}/sfcapd
%{_mandir}/man1/nfanon.1%{?ext_man}
%{_mandir}/man1/nfcapd.1%{?ext_man}
%{_mandir}/man1/nfdump.1%{?ext_man}
%{_mandir}/man1/nfexpire.1%{?ext_man}
%{_mandir}/man1/nfprofile.1%{?ext_man}
%{_mandir}/man1/nfreplay.1%{?ext_man}
%{_mandir}/man1/sfcapd.1%{?ext_man}
%dir %attr(-,%{name},%{name}) %{nfcapddatadir}
%dir %attr(-,%{name},%{name}) %{sfcapddatadir}
%dir %attr(-,%{name},%{name}) %{nfhomedir}

%files -n libnfdump%{sover}
%{_libdir}/libnfdump-*.so

%files devel
%{_libdir}/libnfdump.so

%changelog
