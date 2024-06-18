#
# spec file for package dante
#
# Copyright (c) 2024 SUSE LLC
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


%define lname	libsocks0
Name:           dante
Version:        1.4.3
Release:        0
Summary:        A SOCKSv4 and v5 client implementation
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
URL:            http://www.inet.no/dante/
Source0:        https://www.inet.no/dante/files/dante-%{version}.tar.gz
Source1:        sockd.service
Source2:        baselibs.conf
Source3:        %{name}-rpmlintrc
Patch2:         dante-1.4.0-sockd_conf_man_format.patch
Patch3:         dante-1.4.0-socksify_man_format.patch
Patch4:         dante-1.4.0-glibc-2.17.patch
Patch5:         dante-1.4.0-sendbuf_macro.patch
Patch6:         dante-1.4.1-gcc5-fixes.patch
BuildRequires:  autoconf >= 2.61
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcpd-devel
%if 0%{?suse_version} != 1315
BuildRequires:  libminiupnpc-devel
%endif

%description
Dante is an implementation of the following proxy protocols: SOCKS
version 4, SOCKS version 5 (RFC 1928), and msproxy. It can be used as a
firewall between networks.

%package -n %{lname}
Summary:        A SOCKSv4 and v5 client implementation
Group:          System/Libraries

%description -n %{lname}
Dante is an implementation of the following proxy protocols: SOCKS
version 4, SOCKS version 5 (RFC 1928), and msproxy. It can be used as a
firewall between networks.

This package contains the dynamic libraries required to make existing
applications become socks clients.

%package server
Summary:        A SOCKS v4/v5 server implementation
Group:          Productivity/Networking/Other
Requires:       dante
Provides:       dantesrv = %{version}
Obsoletes:      dantesrv < %{version}
%{?systemd_requires}

%description server
This package contains the socks proxy daemon and its documentation. The
sockd is the server part of the Dante socks proxy package and allows
socks clients to connect through it to the network.

%package devel
Summary:        Development files for the Dante SOCKSv4/v5 library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Provides:       dantedev = %{version}
Obsoletes:      dantedev < %{version}

%description devel
Dante is an implementation of the following proxy protocols: SOCKS
version 4, SOCKS version 5 (RFC 1928), and msproxy.

This package contains the header files for Dante.

%prep
%setup -q
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 5 -p1
%patch -P 6 -p1

%build
DANTELIBC=`find /%{_lib}/ -maxdepth 1 -iname "libc.so.*"`
echo >> acinclude.m4
sed -i -e 's:AM_CONFIG_HEADER:AC_CONFIG_HEADERS:' configure.ac
autoreconf --force --install --verbose

# optflags contains -grecord-gcc-switches which is breaking configure
#CFLAGS="%%{optflags} -fno-strict-aliasing" \
CFLAGS=$(echo "%{optflags}" | sed "s|-grecord-gcc-switches||")
%configure \
  --disable-static \
  --enable-preload \
  --enable-clientdl \
  --enable-serverdl \
  --enable-drt-fallback \
  --enable-shared \
  --with-libc=$DANTELIBC
%make_build V=1

%install
%make_install
#set library as executable - prevent ldd from complaining
chmod +x %{buildroot}%{_libdir}/*.so.*.*
install -d 	%{buildroot}%{_unitdir} \
	   	%{buildroot}%{_bindir} \
	   	%{buildroot}%{_sbindir} \
        %{buildroot}%{_sysconfdir}
install -m 644 example/socks.conf %{buildroot}/%{_sysconfdir}
install -m 644 example/sockd.conf %{buildroot}/%{_sysconfdir}
install -m 644 %{SOURCE1}	  %{buildroot}/%{_unitdir}/sockd.service
#
# fix bug #23141
#
mv %{buildroot}%{_bindir}/socksify %{buildroot}%{_bindir}/socksify.old
sed -e 's|libdl.so|/%{_lib}/libdl.so.2|' < %{buildroot}%{_bindir}/socksify.old > %{buildroot}%{_bindir}/socksify
#
rm %{buildroot}%{_bindir}/socksify.old
find %{buildroot} -type f -name "*.la" -delete -print

rm Makefile* SPECS/Makefile*
rm INSTALL

%pre server
%service_add_pre sockd.service

%preun server
%service_del_preun sockd.service

%ldconfig_scriptlets -n %{lname}

%post server
%service_add_post sockd.service

%postun server
%service_del_postun sockd.service

%files
#files beginning with two capital letters are docs: BUGS, README.foo etc.
%doc [A-Z][A-Z]*
%{_libdir}/libdsocks.so
%attr(755,root,root) %{_bindir}/socksify
%{_mandir}/man1/socksify.1%{?ext_man}
%{_mandir}/man5/socks.conf.5%{?ext_man}
%config(noreplace) %{_sysconfdir}/socks.conf

%files -n %{lname}
%{_libdir}/libsocks.so.0.1.1
%{_libdir}/libsocks.so.0

%files server
%{_mandir}/man8/sockd.8%{?ext_man}
%{_mandir}/man5/sockd.conf.5%{?ext_man}
%attr(755,root,root) %{_sbindir}/sockd
%config(noreplace) %{_sysconfdir}/sockd.conf
%{_unitdir}/sockd.service

%files devel
%{_libdir}/libsocks.so
%{_includedir}/*.h

%changelog
