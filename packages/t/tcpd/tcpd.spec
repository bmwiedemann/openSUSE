#
# spec file for package tcpd
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


%define lname	libwrap0

Name:           tcpd
Version:        7.6
Release:        0
Summary:        A security wrapper for TCP daemons
License:        BSD-3-Clause
Group:          Productivity/Networking/System
URL:            ftp://ftp.porcupine.org/pub/security/index.html
Source:         ftp://ftp.porcupine.org/pub/security/tcp_wrappers_%{version}.tar.gz
Source2:        baselibs.conf
Patch0:         tcp_wrappers_%{version}.diff
Patch1:         tcp_wrappers_%{version}-ipv6-1.6.diff
Patch2:         tcp_wrappers_%{version}-ipv6-fix.diff
Patch3:         tcp_wrappers_%{version}-ipv6.fix.fix.diff
Patch4:         tcp_wrappers_%{version}-ipv6.fix.fix2.diff
Patch5:         tcp_wrappers_%{version}-host_name_mapping-fix.diff
Patch6:         tcp_wrappers_%{version}-fix_options-fix.diff
Patch7:         tcp_wrappers_%{version}-shared-lib.diff
Patch8:         tcp_wrappers_%{version}-builtin.diff
Patch9:         tcp_wrappers_%{version}-multi_local_interfaces-fix.diff
Patch10:        tcp_wrappers_%{version}-optflags.diff
Patch11:        tcp_wrappers_%{version}-nonvoid.diff
Patch12:        tcp_wrappers_%{version}-prototypes.diff
Patch13:        tcp_wrappers_%{version}-hosts_ctl.diff
Patch14:        tcp_wrappers_%{version}-uninitialized.diff
Patch15:        tcp_wrappers_%{version}-fedora-bug11881.diff
Patch16:        tcp_wrappers_%{version}-fedora-bug141110.diff
Patch17:        tcp_wrappers_%{version}-fedora-docu.diff
Patch18:        tcp_wrappers_%{version}-fedora-sig.diff
Patch19:        tcp_wrappers_%{version}-fedora-sigchld.diff
Patch20:        tcp_wrappers_%{version}-fedora-sigjmp.diff
Patch21:        tcp_wrappers_%{version}-fedora-sigalarm.diff
Patch22:        tcp_wrappers_%{version}-fedora-strerror.diff
Patch23:        tcp_wrappers_%{version}-fedora-fixgethostbyname.diff
Patch24:        tcp_wrappers_%{version}-fedora-bug220015.diff
Patch25:        tcp_wrappers_%{version}-shared-lib2.diff
Patch26:        tcp_wrappers_%{version}-fedora-bug17795.diff
Patch27:        tcp_wrappers_%{version}-fedora-bug17847.diff
Patch28:        tcp_wrappers_7.6-implicit-decl.patch
Patch29:        tcpd-ocloexec.patch
Patch30:        tcp_wrappers_%{version}-ipv6-sockaddr-storage.patch
Patch31:        tcp_wrappers_%{version}-ipv6-subnet.diff
Patch32:        tcp_wrappers_%{version}-ipv6-host-match.patch
Patch33:        tcp_wrappers_%{version}-ipv6-mapped-v4.patch
Patch34:        tcp_wrappers_%{version}-ipv6.fix.fix3.diff
BuildRequires:  linux-kernel-headers
Provides:       nkitb:%{_sbindir}/tcpd
# bug437293
%ifarch ppc64
Obsoletes:      tcpd-64bit
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a small daemon program that can monitor and
filter incoming requests for finger, ftp, telnet, rlogin, rsh, exec,
tftp, talk, and other network services.

%package -n %{lname}
Summary:        The TCP wrapper library
Group:          System/Libraries

%description -n %{lname}
This package contains a library which implements classifying incoming
requests (connections) based upon rule exclusion files (%{_sysconfdir}/hosts.*).

%package devel
Summary:        Include Files and Libraries for the TCP wrapper library
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel
# bug437293
%ifarch ppc64
Obsoletes:      tcpd-devel-64bit
%endif
#

%description devel
This package contains the library and header files, which are necessary
to compile and link programs against the TCP wrapper library.

%prep
%setup -q -n tcp_wrappers_%{version}
%patch0
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
%patch18
%patch19
%patch20
%patch21
%patch22
%patch23
%patch24
%patch25
%patch26
%patch27
%patch28
%patch29
%patch30 -p1
%patch31
%patch32 -p1
%patch33 -p1
%patch34

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
make %{?_smp_mflags} linux CC="cc"

%install
install -d -m 755 %{buildroot}%{_includedir}
install -d -m 755 %{buildroot}%{_libdir}
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_mandir}/man{1,3,5,8}
install -d -m 755 %{buildroot}/%{_lib}
install -m 644 ip6utils.h tcpd.h %{buildroot}%{_includedir}
install -m 644 libwrap.a %{buildroot}/%{_libdir}
install -m 755 safe_finger tcpd tcpdchk tcpdmatch try-from %{buildroot}%{_sbindir}
install -m 644 hosts_access.3 %{buildroot}%{_mandir}/man3
install -m 644 hosts_access.5 hosts_options.5 %{buildroot}%{_mandir}/man5
install -m 644 tcpd.8 tcpdchk.8 tcpdmatch.8 %{buildroot}%{_mandir}/man8
install -m 644 shared/libwrap.so.0.%{version} %{buildroot}/%{_lib}
cd %{buildroot}/%{_lib}
ln -sf libwrap.so.0.%{version} libwrap.so.0
cd %{buildroot}%{_libdir}
ln -sf /%{_lib}/libwrap.so.0.%{version} libwrap.so

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BLURB CHANGES DISCLAIMER README README.ipv6 README.NIS
%doc %{_mandir}/man?/*
%attr(755,root,root) %{_sbindir}/*

%files -n %{lname}
%defattr(-,root,root)
%doc DISCLAIMER
%attr(755,root,root) /%{_lib}/libwrap.so.0*

%files devel
%defattr(644,root,root,755)
%{_includedir}/tcpd.h
%{_includedir}/ip6utils.h
%{_libdir}/libwrap.a
%{_libdir}/libwrap.so

%changelog
