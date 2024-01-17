#
# spec file for package radvd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif

Name:           radvd
Version:        2.19
Release:        0
Summary:        Router ADVertisement Daemon for IPv6
License:        BSD-3-Clause
Group:          Productivity/Networking/Routing
URL:            http://v6web.litech.org/radvd
Source0:        https://radvd.litech.org/dist/%{name}-%{version}.tar.xz
Source2:        sysconfig.radvd
Source3:        system-user-radvd.conf
Source42:       https://radvd.litech.org/dist/%{name}-%{version}.tar.xz.asc
Source43:       %{name}.keyring
Patch1:         0001-run-as-user-radvd-by-default.diff
Patch2:         radvd-configure.patch
# PATCH-FIX-OPENSUSE radvd-tmpfile-grpname.patch dimstar@opensuse.org -- On openSUSE, we add the radvd user to the group daemon. Thus, we also need to create the folders with the respective group owner (otherwise, the systemd-tmpfiles service fails).
Patch3:         radvd-systemd.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libdaemon-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  xz
BuildRequires:  pkgconfig(check)
Requires(pre):  %fillup_prereq
%sysusers_requires
%if 0%{?suse_version} >= 1330
Requires(pre):  group(daemon)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
RADVD is the Router ADVertisement Daemon. It sends IPv6 RA packets
to advertise available IPv6 networks, and is used for automated
configuration of IPv6 clients.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-silent-rules \
	--with-configfile=%{_sysconfdir}/radvd.conf \
	--with-pidfile=%{_rundir}/radvd/radvd.pid
make %{?_smp_mflags}
#
%sysusers_generate_pre %{SOURCE3} radvd system-user-radvd.conf

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mkdir -p %{buildroot}/run/radvd
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/
install -m 644 /dev/null %{buildroot}%{_sysconfdir}/radvd.conf

install -D -m 644 %{SOURCE3} %{buildroot}%{_sysusersdir}/system-user-radvd.conf

install -D -m 0644 redhat/systemd/radvd.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 redhat/systemd/radvd-tmpfs.conf %{buildroot}%{_tmpfilesdir}/%name.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcradvd

%pre -f radvd.pre
%service_add_pre %{name}.service

%post
# zap old (<= 11.4) default
test -f %{_sysconfdir}/sysconfig/radvd && sed -ie '/^RADVD_OPTIONS/s/-u daemon//' %{_sysconfdir}/sysconfig/radvd
%{fillup_only radvd}
#
random() {
	od -An -d -N2 /dev/urandom
}
if [ ! -e %{_sysconfdir}/radvd.conf ]; then
	# yeah, not quite the rfc4193 algorithm but hopefully
	# random enough
	prefix=`printf "fd%%02x:%%04x:%%04x:0001::/64\n" $(($(random) %% 256)) $(random) $(random)`
	cat > %{_sysconfdir}/radvd.conf <<EOF
interface eth0
{
	AdvSendAdvert on;

	# life time zero means we don't actually advertise a
	# router but only our ULA address. Remove if you want this
	# host to be advertised as router.
	AdvDefaultLifetime 0;

	# ULA address according to RFC 4193.
	# It was randomly created at installation of the package for
	# use in your local network.
	prefix $prefix
	{
	};
};
EOF
	echo "created %{_sysconfdir}/radvd.conf with ULA prefix $prefix"
fi
%tmpfiles_create %{_tmpfilesdir}/%name.conf

%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%preun
%service_del_preun %{name}.service

%files
%ghost %dir %attr(0755,radvd,radvd) /run/radvd/
%ghost %config(noreplace) %{_sysconfdir}/radvd.conf
%{_fillupdir}/sysconfig.radvd
%{_sbindir}/radvd
%{_sbindir}/radvdump
%{_mandir}/man8/radvd.8.gz
%{_mandir}/man8/radvdump.8.gz
%{_mandir}/man5/radvd.conf.5.gz
%doc CHANGES COPYRIGHT TODO INTRO.html
%doc radvd.conf.example
%{_sbindir}/rcradvd
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/system-user-radvd.conf

%changelog
