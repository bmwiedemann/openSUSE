#
# spec file for package tftp
#
# Copyright (c) 2022 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           tftp
Version:        5.2
Release:        0
Summary:        Trivial File Transfer Protocol (TFTP)
License:        BSD-3-Clause
Group:          Productivity/Networking/Ftp/Clients
URL:            https://www.kernel.org/pub/software/network/tftp/
Source:         https://www.kernel.org/pub/software/network/tftp/tftp-hpa/tftp-hpa-%{version}.tar.bz2
Source3:        tftp.service
Source4:        tftp.socket
Source5:        tftp.sysconfig
Patch0:         tftp-hpa-0.43_include_sys_params.patch
Patch1:         tftp-hpa-0.46_colon_check.patch
Patch4:         tftp-hpa-0.49-fortify-strcpy-crash.patch
Patch5:         tftp-hpa-0.48-tzfix.patch
Patch6:         tftp-multi-addresses.patch
Patch7:         tftp-hpa-0.48-macros-crash.patch
Patch8:         tftp-hpa-0.48-macros-v6mapped.patch
Patch43:        tftp-config_h.patch
BuildRequires:  autoconf
BuildRequires:  binutils-devel
BuildRequires:  pkgconfig
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcpd-devel
Requires:       netcfg
Requires(pre):  user(tftp)
Recommends:     inet-daemon
Conflicts:      atftp
Provides:       tftp(client)
Provides:       tftp(server)

%description
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations and for getting or saving network
component configuration files.

%prep
%autosetup -p1 -n %{name}-hpa-%{version}

%build
autoreconf -fi
export CFLAGS="%{optflags} -fcommon"
%configure \
  --enable-largefile \
  --with-tcpwrappers \
  --with-remap \
  --with-ipv6
%make_build

%install
%make_install INSTALLROOT=%{buildroot} MANDIR="%{_mandir}"
install -d -m 0755 %{buildroot}/srv/tftpboot

# Install systemd unit / socket (As an alternativ to xinetd activation)
install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_unitdir}
install -D -m 0644 %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.tftp
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service %{name}.socket

%post
%service_add_post %{name}.service %{name}.socket
%{fillup_only -n tftp}

%preun
%service_del_preun %{name}.service %{name}.socket

%postun
%service_del_postun %{name}.service %{name}.socket

%files
%doc README README.security tftpd/sample.rules
%{_bindir}/tftp
%{_sbindir}/in.tftpd
%{_sbindir}/rctftp
%{_mandir}/man1/tftp.1%{?ext_man}
%{_mandir}/man8/in.tftpd.8%{?ext_man}
%{_mandir}/man8/tftpd.8%{?ext_man}
%{_unitdir}/tftp.service
%{_unitdir}/tftp.socket

%dir %attr(0755,tftp,tftp) /srv/tftpboot
%{_fillupdir}/sysconfig.tftp

%changelog
