#
# spec file for package nbd
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


%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           nbd
Version:        3.20
Release:        0
Summary:        Network Block Device Server and Client Utilities
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://nbd.sourceforge.net/
Source0:        https://sourceforge.net/projects/nbd/files/nbd/%{version}/nbd-%{version}.tar.xz
Source1:        %{name}-server.service
Source3:        config.example
Source4:        nbd-server.sysconfig
Source5:        nbd-client.service
Patch1:         0001_fix_setgroup.patch
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libnl-3.0)
Requires(pre):  %fillup_prereq
Requires(pre):  coreutils
%systemd_requires

%description
This package contains nbd-server. It is the server backend for the nbd
network block device driver that's in the Linux kernel.

nbd can be used to have a filesystem stored on another machine. It does
provide a block device, not a file system; so unless you put a
clustering filesystem on top of it, you can't access it simultaneously
from more than one client. Use NFS or a real cluster FS (such as
ocfs2) if you want to do this. nbd-server can export a file (which may
contain a filesystem image) or a partition. Swapping over nbd is
possible as well, though it's said not to be safe against OOM and
should not be used for that case. nbd-server also has a copy-on-write
mode where changes are saved to a separate file and thrown away when
the connection closes.

The package also contains the nbd-client tools, which you need to
configure the nbd devices on the client side.

%prep
%setup -q
%patch1 -p1

%build
%configure
%make_build

%install
%make_install

# install systemd unit
install -D -p -m 0644  %{SOURCE5} \
  %{buildroot}/%{_unitdir}/%{name}@.service
install -D -p -m 0644  %{SOURCE1} \
  %{buildroot}/%{_unitdir}/%{name}-server.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-server

# autoload nbd module
install -d -m 755 %{buildroot}%{_prefix}/lib/modules-load.d/
echo "nbd" > %{buildroot}%{_prefix}/lib/modules-load.d/%{name}.conf

#echo "#Port	file	options" > $RPM_BUILD_ROOT/etc/nbd-server.conf
mkdir -p %{buildroot}%{_sysconfdir}/nbd-server
touch %{buildroot}%{_sysconfdir}/nbd-server/config
touch %{buildroot}%{_sysconfdir}/nbd-server/allow
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/nbd-server/config.example
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}-server

%post
export DISABLE_RESTART_ON_UPDATE=yes
%service_add_post %{name}-server.service
%fillup_only -n nbd-server
if test -e %{_sysconfdir}/nbd-server.conf; then
  # Do we have to create a generic section?
  unset generic
  if test -e %{_sysconfdir}/nbd-server/config; then generic=1; fi
  grep -vE '^(#|[[:blank:]]*$)' %{_sysconfdir}/nbd-server.conf |
  while read port file opts; do
    if test -z "$generic"; then
      cat >%{_sysconfdir}/nbd-server/config <<-EOF

	[generic]
	   # No generic options yet

	EOF
      generic=1
    fi
    FN=${file%/*}
    nm="cvt.$port.${FN##*/}.${file##*/}"
    echo " ... convert $port $file $opts -> $nm"
    %{_bindir}/nbd-server $port $file $opts -o "$nm" >> %{_sysconfdir}/nbd-server/config
  done
  mv %{_sysconfdir}/nbd-server.conf %{_sysconfdir}/nbd-server.conf.converted
fi

%postun
%service_del_postun %{name}-server.service

%pre
%service_add_pre %{name}-server.service

%preun
%service_del_preun %{name}-server.service

%files
%{_sbindir}/nbd-client
%{_bindir}/nbd-server
%{_bindir}/nbd-trdump
%{_sbindir}/min-nbd-client
%{_sbindir}/rcnbd-server
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}-server.service
%{_mandir}/man1/nbd-server.1%{?ext_man}
%{_mandir}/man1/nbd-trdump.1%{?ext_man}
%{_mandir}/man5/nbd-server.5%{?ext_man}
%{_mandir}/man8/nbd-client.8%{?ext_man}
%{_mandir}/man5/nbdtab.5%{?ext_man}
%doc README.md
%dir %{_sysconfdir}/nbd-server
%ghost %config(noreplace) %{_sysconfdir}/nbd-server/config
%ghost %config(noreplace) %{_sysconfdir}/nbd-server/allow
%config %{_sysconfdir}/nbd-server/config.example
%dir %{_prefix}/lib/modules-load.d/
%{_prefix}/lib/modules-load.d/nbd.conf
%{_fillupdir}/sysconfig.%{name}-server

%changelog
