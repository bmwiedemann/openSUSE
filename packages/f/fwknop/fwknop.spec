#
# spec file for package fwknop
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


%define soname 3

%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           fwknop
Version:        2.6.10
Release:        0
Summary:        The fwknop Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.cipherdyne.org/fwknop/
Source:         https://www.cipherdyne.org/fwknop/download/%{name}-%{version}.tar.bz2
Source1:        https://www.cipherdyne.org/fwknop/download/%{name}-%{version}.tar.bz2.asc#/%{name}-%{version}.tar.bz2.sig
# https://www.cipherdyne.org/signing_key
Source2:        %{name}.keyring
Source3:        %{name}d.service
BuildRequires:  gdbm-devel
BuildRequires:  gpg2
BuildRequires:  iptables
BuildRequires:  libgpgme-devel
BuildRequires:  libpcap-devel
BuildRequires:  systemd-rpm-macros

%description
fwknop stands for the "FireWall KNock OPerator", and implements an authorization
scheme called Single Packet Authorization (SPA).

%package -n libfko%{soname}
Summary:        The Firewall Knock Operator Library
Group:          System/Libraries

%description -n libfko%{soname}
The Firewall Knock Operator library, libfko, provides the Single Packet
Authorization implementation and API for the other fwknop components.

%package -n libfko-devel
Summary:        The Development Files for the Firewall Knock Operator Library
Group:          Development/Libraries/C and C++
Requires:       libfko%{soname} = %{version}
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description -n libfko-devel
The Firewall Knock Operator library, libfko, provides the Single Packet
Authorization implementation and API for the other fwknop components.

This subpackage contains libraries and header files for developing
applications that want to make use of libfko.

%package -n fwknopd
Summary:        The fwknop Server
Group:          Productivity/Networking/Security
%{?systemd_requires}

%description -n fwknopd
fwknop stands for the "FireWall KNock OPerator", and implements an authorization
scheme called Single Packet Authorization (SPA).

%prep
%setup -q

%build
export CFLAGS="%optflags -fcommon"
%configure --disable-static
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
install -D -m 644 %{SOURCE3} %{buildroot}/%{_unitdir}/%{name}d.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}d
find %{buildroot} -type f -name "*.la" -delete -print

%pre -n fwknopd
%service_add_pre %{name}d.service

%post -n fwknopd
%service_add_post %{name}d.service

%preun -n fwknopd
%service_del_preun %{name}d.service

%postun -n fwknopd
%service_del_postun %{name}d.service

%post -n libfko%{soname} -p /sbin/ldconfig
%post -n libfko-devel
%install_info --info-dir=%{_infodir} %{_infodir}/libfko.info.gz

%postun -n libfko%{soname} -p /sbin/ldconfig
%postun -n libfko-devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libfko.info.gz

%files
%license COPYING
%doc AUTHORS CREDITS NEWS README
%{_bindir}/fwknop
%{_mandir}/man8/fwknop.8%{?ext_man}

%files -n fwknopd
%{_unitdir}/%{name}d.service
%{_sbindir}/rc%{name}d
%{_sysconfdir}/fwknop
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/fwknop/access.conf
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/fwknop/fwknopd.conf
%{_sbindir}/fwknopd
%{_mandir}/man8/fwknopd.8%{?ext_man}

%files -n libfko%{soname}
%{_libdir}/libfko.so.%{soname}*

%files -n libfko-devel
%{_includedir}/fko.h
%{_libdir}/libfko.so
%{_infodir}/libfko.info%{?ext_info}

%changelog
