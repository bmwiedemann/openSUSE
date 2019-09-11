#
# spec file for package openslp
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


%define libname libslp1
Name:           openslp
Version:        2.0.0
Release:        0
Summary:        An Implementation of Service Location Protocol V2
License:        BSD-3-Clause
Group:          System/Daemons
URL:            http://www.openslp.org/
Source0:        http://sourceforge.net/projects/openslp/files/2.0.0/%{version}/%{name}-%{version}.tar.gz
Source2:        README.SUSE
Source3:        openslp.desktop
Source4:        openslp-devel.desktop
Source5:        openslp.logrotate
Source8:        baselibs.conf
Source9:        slpd.service
Source10:       openslp.logrotate.systemd
Patch1:         openslp.audit.diff
Patch2:         extensions.diff
Patch3:         openslp.truncate.diff
Patch4:         openslp.netlink.diff
Patch5:         openslp.initda.diff
Patch6:         openslp.visibility.diff
Patch7:         openslp.daemon.diff
Patch8:         openslp.cloexec.diff
Patch9:         openslp.hardmtu.diff
Patch10:        openslp.tcplocal.diff
Patch11:        openslp.localtime.diff
Patch12:        openslp.sd_notify.diff
Patch13:        openslp.predicatestorage.diff
Patch14:        openslp.doubleequal.diff
Patch15:        openslp.noconvenience.diff
Patch16:        openslp.xrealloc.diff
Patch17:        openslp.foldws.diff
Patch18:        openslp.openssl-1.1.diff
Patch19:        openslp.localaddr.diff
Patch20:        openslp.tcpunicast.diff
Patch21:        openslp-2.0.0-ifdef-slpv2.diff
Patch22:        openslp.tcpknownda.diff
Patch23:        openslp.nullattr.diff
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)

%description
Service Location Protocol is an IETF standards track protocol that
provides a framework that allows networking applications to discover
the existence, location, and configuration of networked services in
networks.

OpenSLP is an open source implementation of the SLPv2 protocol as
defined by RFC 2608 and RFC 2614.  This package includes the slptool
and runtime libraries.

%package server
Summary:        The OpenSLP Implementation of the Service Location Protocol V2
Group:          System/Daemons
Requires(pre):  group(daemon)
Requires(pre):  shadow
Recommends:     logrotate
%{?systemd_requires}

%description server
Service Location Protocol is an IETF standards track protocol that
provides a framework that allows networking applications to discover
the existence, location, and configuration of networked services in
networks.

This package contains the SLP server. Every system, which provides any
services that should be used via an SLP client must run this server and
register the service.

%package -n %{libname}
Summary:        An Implementation of the Service Location Protocol V2
Group:          System/Libraries

%description -n %{libname}
Service Location Protocol is an IETF standards track protocol that
provides a framework that allows networking applications to discover
the existence, location, and configuration of networked services in
networks.

%package devel
Summary:        Header files for OpenSLP
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       openssl-devel

%description devel
Service Location Protocol is an IETF standards track protocol that
provides a framework that allows networking applications to discover
the existence, location, and configuration of networked services in
networks.

This package contains header and library files to compile applications
with SLP support. It also contains developer documentation to develop
such applications.

%prep
%setup -q
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
%patch11
%patch12
%patch13
%patch14
%patch15
%patch16
%patch17
%patch18 -p2
%patch19
%patch20
%patch21 -p1
%patch22
%patch23

%build
autoreconf -fiv
%configure \
  --disable-static \
  --with-pic \
  --enable-slpv1 \
  --enable-async-api \
  --enable-slpv2-security
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sysconfdir}/slp.reg.d
mkdir -p %{buildroot}%{_sysconfdir}/slp.reg.d/slpd
cp etc/slp.conf %{buildroot}%{_sysconfdir}
cp etc/slp.reg %{buildroot}%{_sysconfdir}
cp etc/slp.spi %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/%{_libdir}
./libtool --mode=install install libslp/libslp.la %{buildroot}/%{_libdir}
rm %{buildroot}%{_libdir}/libslp.la
mkdir -p  %{buildroot}%{_sbindir}
./libtool --mode=install install slpd/slpd %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_bindir}
./libtool --mode=install install slptool/slptool %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}
cp libslp/slp.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
find . -name CVS -o -name .cvsignore -o -name .xvpics | xargs rm -rf
cp -a AUTHORS README FAQ doc/doc/rfc doc/doc/html %{SOURCE2} \
   %{buildroot}%{_defaultdocdir}/%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcslpd
cat > %{buildroot}%{_sbindir}/rcopenslp <<'EOF'
#!/bin/sh
exec %{_sbindir}/rcslpd "$@"
EOF
chmod 755 %{buildroot}%{_sbindir}/rcopenslp
install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/logrotate.d/openslp-server
# install susehelp file
mkdir -p %{buildroot}%{_datadir}/susehelp/meta/Administration/
install -m 0644 %{SOURCE3} \
	%{buildroot}%{_datadir}/susehelp/meta/Administration/
mkdir -p %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/
install -m 0644 %{SOURCE4} \
	%{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/

install -D -m 644 %{SOURCE9} %{buildroot}%{_unitdir}/slpd.service

#XXX test suite requires root
#check
#make check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%pre server
getent passwd openslp >/dev/null || useradd -r -g daemon -d %{_localstatedir}/lib/empty -s /sbin/nologin -c "openslp daemon" openslp
%service_add_pre slpd.service

%post server
%service_add_post slpd.service

%postun server
%service_del_postun slpd.service

%preun server
%service_del_preun slpd.service

%files -n %{libname}
%{_libdir}/libslp.so.*

%files
%license COPYING
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/html
%doc %{_defaultdocdir}/%{name}/AUTHORS
%doc %{_defaultdocdir}/%{name}/README
%doc %{_defaultdocdir}/%{name}/README.SUSE
%{_bindir}/slptool
%config(noreplace) %{_sysconfdir}/slp.conf
%config(noreplace) %{_sysconfdir}/slp.spi

%files server
%dir %{_datadir}/susehelp
%dir %{_datadir}/susehelp/meta
%dir %{_datadir}/susehelp/meta/Administration
%doc %{_defaultdocdir}/%{name}/FAQ
%doc %{_defaultdocdir}/%{name}/html/IntroductionToSLP
%doc %{_defaultdocdir}/%{name}/html/UsersGuide
%doc %{_defaultdocdir}/%{name}/html/faq.html
%doc %{_defaultdocdir}/%{name}/rfc
%doc %{_datadir}/susehelp/meta/Administration/openslp.desktop
%dir %{_sysconfdir}/slp.reg.d/
%dir %{_sysconfdir}/slp.reg.d/slpd
%{_sbindir}/rcopenslp
%{_sbindir}/rcslpd
%{_sbindir}/slpd
%config(noreplace) %{_sysconfdir}/slp.reg
%config(noreplace) %{_sysconfdir}/logrotate.d/openslp-server
%{_unitdir}/slpd.service

%files devel
%dir %{_datadir}/susehelp
%dir %{_datadir}/susehelp/meta
%dir %{_datadir}/susehelp/meta/Development
%dir %{_datadir}/susehelp/meta/Development/Libraries
%doc %{_defaultdocdir}/%{name}/html/ProgrammersGuide
%doc %{_datadir}/susehelp/meta/Development/Libraries/openslp-devel.desktop
%{_includedir}/slp.h
%{_libdir}/libslp.so

%changelog
