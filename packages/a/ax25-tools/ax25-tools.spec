#
# spec file for package ax25-tools
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ax25-tools
Version:        0.0.10rc4_87
Release:        0
Summary:        AX.25 tools
License:        GPL-2.0-only
URL:            http://www.linux-ax25.org
Source:         ax25-tools-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libax25-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel

%description
These are the support utilities required to make use of the internal
AX.25, NET/ROM and Rose support in the linux kernel. The ax25tools are
mostly configuration utilities, applications can be found in the
package ax25apps.

%prep
%setup -q

%build
export CFLAGS="%optflags -fcommon"
autoreconf -fiv
%configure \
  --localstatedir=%{_localstatedir}/lib
make %{?_smp_mflags}

%install
%make_install installconf
rm -rf %{buildroot}%{_datadir}/doc/ax25-tools
rm -rf %{buildroot}%{_localstatedir}/lib/ax25/mheard/mheard.dat

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README yamdrv/README.yamdrv
%doc dmascc/README.dmascc user_call/README.user_call tcpip/ttylinkd.INSTALL
%doc tcpip/ttylinkd.README
%dir %{_sysconfdir}/ax25
%dir %{_localstatedir}/lib/ax25
%dir %{_localstatedir}/lib/ax25/mheard
%config(noreplace) %{_sysconfdir}/ax25/ax25.profile
%config(noreplace) %{_sysconfdir}/ax25/ax25d.conf
%config(noreplace) %{_sysconfdir}/ax25/axspawn.conf
%config(noreplace) %{_sysconfdir}/ax25/nrbroadcast
%config(noreplace) %{_sysconfdir}/ax25/rip98d.conf
%config(noreplace) %{_sysconfdir}/ax25/rxecho.conf
%config(noreplace) %{_sysconfdir}/ax25/ttylinkd.conf
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man4/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_mandir}/man9/*

%changelog
