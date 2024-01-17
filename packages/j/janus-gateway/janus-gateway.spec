#
# spec file for package janus-gateway
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


%if 0%{?suse_version} > 1320
%bcond_without janus_postprocessing
%endif

Name:           janus-gateway
Version:        1.1.4
Release:        0
License:        GPL-3.0-or-later
Summary:        Janus WebRTC Gateway
URL:            https://github.com/meetecho/janus-gateway
Group:          Productivity/Networking/Other
Source:         %{name}-%{version}.tar.xz
Source1:        janus.service
Source2:        %{name}.sysusers
Source100:      %{name}-rpmlintrc
# for run autogen.sh
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# basic dependencies
BuildRequires:  pkg-config
BuildRequires:  curl-devel
BuildRequires:  gengetopt
BuildRequires:  libconfig-devel
BuildRequires:  sofia-sip-devel
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(ini_config)
BuildRequires:  pkgconfig(jansson) >= 2.5
BuildRequires:  pkgconfig(libmicrohttpd) >= 0.9.59
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libsrtp2)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(nice) >= 0.1.18
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl) >= 1.0.1e
BuildRequires:  pkgconfig(opus)
%if %{with janus_postprocessing}
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
%endif
# data channel support
BuildRequires:  usrsctp-devel
# websockets support
BuildRequires:  libwebsockets-devel >= 4.0.0
# MQTT support
BuildRequires:  libpaho-mqtt-devel
Requires(pre):  shadow
BuildRequires:  pkgconfig(systemd)

%{?systemd_ordering}
%{sysusers_requires}

%description
Janus is a general-purpose WebRTC gateway designed and developed
by Meetecho.

%package devel
Requires:       %{name} = %{version}
Summary:        Development files for Janus Gateway plugins
Group:          Development/Libraries/C and C++

%description devel
Janus is a general-purpose WebRTC gateway designed and developed
by Meetecho.

This package holds the file needed to compile plugins for Janus Gateway.

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE2} %{name}
./autogen.sh
%configure \
  --disable-static \
  --enable-libsrtp2 \
  --enable-plugin-lua \
  %if %{with janus_postprocessing}
  --enable-post-processing \
  %endif
  --disable-rabbitmq \
  --disable-docs
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/janus/plugins/*.la
make configs DESTDIR=%{buildroot}
#
install -D -d -m 755 %{buildroot}%{_sbindir}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/janus.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcjanus
#
pushd %{buildroot}%{_sysconfdir}/janus/
rm -rv *.jcfg.sample
chmod -R o= .
popd
rm -rv %{buildroot}%{_datadir}/doc/%{name}
rm -rv %{buildroot}%{_datadir}/janus/streams/test_gstreamer*.sh
#
install -D -d -m 0750 %{buildroot}%{_sharedstatedir}/janus/

%pre -f %{name}.pre
%service_add_pre janus.service

%post
%service_add_post janus.service

%preun
%service_del_preun janus.service

%postun
%service_del_postun janus.service

%files
%doc README.md
%license COPYING
%config(noreplace) %attr(-,root,janus) %{_sysconfdir}/janus/
%{_sbindir}/rcjanus
%{_bindir}/janus
%{_bindir}/janus-cfgconv
%{_mandir}/man1/janus.1*
%{_mandir}/man1/janus-cfgconv.1*
%if %{with janus_postprocessing}
%{_bindir}/janus-pp-rec
%{_bindir}/mjr2pcap
%{_bindir}/pcap2mjr
%{_mandir}/man1/janus-pp-rec.1*
%{_mandir}/man1/mjr2pcap.1*
%{_mandir}/man1/pcap2mjr.1.gz
%endif
%{_libdir}/janus/
%{_datadir}/janus/
%{_unitdir}/janus.service
%dir %attr(750,janus,janus) %{_sharedstatedir}/janus/

%files devel
%{_includedir}/janus/

%changelog
