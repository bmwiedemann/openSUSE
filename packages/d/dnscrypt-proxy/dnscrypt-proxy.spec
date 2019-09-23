#
# spec file for package dnscrypt-proxy
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


Name:           dnscrypt-proxy
Version:        1.9.5
Release:        0
Summary:        A tool for securing communications between a client and a DNS resolver
License:        BSD-3-Clause
Group:          Productivity/Networking/DNS/Utilities
Url:            https://dnscrypt.org/
Source:         https://download.dnscrypt.org/dnscrypt-proxy/%{name}-%{version}.tar.bz2
Source1:        %{name}@.service
Source5:        %{name}.tmpfile
Patch0:         dnscrypt-proxy-default-config.patch
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  shadow
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
Requires(pre):  coreutils
Requires(pre):  diffutils
Requires(pre):  fillup
Requires(pre):  grep
%{?systemd_requires}
Provides:       dnscrypt = %{version}-%{release}
Obsoletes:      dnscrypt < %{version}-%{release}

%description
dnscrypt-proxy provides local service which can be used directly as your local resolver or as a DNS forwarder,
encrypting and authenticating requests using the DNSCrypt protocol and passing them to an upstream server,
by default Cisco who run this on their resolvers. (It used to be OpenDNS.)

The DNSCrypt protocol uses elliptic-curve cryptography and is similar to DNSCurve, but focuses on
securing communications between a client and its first-level resolver.

While not providing end-to-end security, it protects the local network, which is often the weakest point
of the chain, against man-in-the-middle attacks. It also provides some confidentiality to DNS queries.

%package devel
Summary:        Header files for development of DNSCrypt plugins
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
Header files for development of DNSCrypt plugins.

%prep
%setup -q
%patch0 -p1
# Strip __DATE__
sed -i "s/__DATE__/\"%(date -u -r ChangeLog +%%F)\"/" src/proxy/options.c
# Don't install COPYING with make, we use our %%license marcro if possible
sed -i "/\tCOPYING / d" Makefile.am
sed -i "s/COPYING //" Makefile.in

%build
%configure \
%if 0%{?suse_version} >= 1210
	--with-systemd \
%endif
	--enable-plugins \
	--docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install

install -d -m 755 %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_libexecdir}/tmpfiles.d/
install -m 644 %{SOURCE5} %{buildroot}%{_libexecdir}/tmpfiles.d/%{name}.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.conf.d
mv %{buildroot}%{_sysconfdir}/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf.d/default.conf

%pre
if ! %{_bindir}/getent group dnscrypt >/dev/null; then
    %{_sbindir}/groupadd -r dnscrypt
fi
if ! %{_bindir}/getent passwd dnscrypt >/dev/null; then
    %{_sbindir}/useradd -c "DNSCrypt daemon" -d %{_localstatedir}/lib/empty -g dnscrypt \
  -r -s /bin/false dnscrypt
fi
%if 0%{?suse_version} >= 1210
%service_add_pre %{name}@.service
%endif

%post
%service_add_post %{name}@.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
if [ $1 == 2 ] && [ -r %{_sysconfdir}/sysconfig/%{name} ] ; then
	rm -f %{_sysconfdir}/sysconfig/%{name}
fi
if [ $1 == 2 ] && [ -r %{_sysconfdir}/sysconfig/dnscrypt ] ; then
	rm -f %{_sysconfdir}/sysconfig/dnscrypt
fi

%preun
%if 0%{?suse_version} >= 1210
%service_del_preun %{name}@.service
%endif

%postun
%if 0%{?suse_version} >= 1210
%service_del_postun %{name}@.service
%endif

%files
%doc AUTHORS ChangeLog README.markdown NEWS DNSCRYPT-V2-PROTOCOL.txt 
%doc THANKS README-PLUGINS.markdown dnscrypt-proxy.conf
%if 0%{?leap_version} >= 420200 || 0%{?suse_version} > 1320
%license COPYING
%else
%doc COPYING
%endif
%dir %{_sysconfdir}/%{name}.conf.d
%config %{_sysconfdir}/%{name}.conf.d/default.conf
%{_bindir}/hostip
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}@.service
%{_mandir}/man8/hostip.8%{ext_man}
%{_mandir}/man8/%{name}.8%{ext_man}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dnscrypt-resolvers.csv
%{_datadir}/%{name}/minisign.pub
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libdcplugin_example.so
%{_libdir}/%{name}/libdcplugin_example_logging.so
%{_libdir}/%{name}/libdcplugin_example_cache.so
%{_libexecdir}/tmpfiles.d/%{name}.conf
%ghost %dir %{_localstatedir}/log/%{name}
%ghost %dir /run/%{name}

%files devel
%dir %{_includedir}/dnscrypt/
%{_includedir}/dnscrypt/*

%changelog
