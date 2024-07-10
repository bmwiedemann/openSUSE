#
# spec file for package mosquitto
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


%define home    %{_localstatedir}/lib/%{name}
%define c_lib   libmosquitto1
%define cpp_lib libmosquittopp1
Name:           mosquitto
Version:        2.0.18
Release:        0
Summary:        A MQTT v3.1/v3.1.1 Broker
License:        EPL-1.0
Group:          Productivity/Networking/Other
URL:            https://mosquitto.org/
Source:         https://mosquitto.org/files/source/mosquitto-%{version}.tar.gz
Source1:        mosquitto.service
Source2:        %{name}-user.conf
Source4:        README-conf-d
Source5:        README-ca_certificates
Source6:        README-certs
Source98:       https://mosquitto.org/files/source/mosquitto-%{version}.tar.gz.asc#/%{name}-%{version}.tar.gz.sig
Source99:       %{name}.keyring
Patch0:         mosquitto-1.4.1_apparmor.patch
Patch1:         mosquitto-1.6.8-config.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libxslt-tools
BuildRequires:  openssl-devel >= 1.0.0
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  tcpd-devel
BuildRequires:  uthash-devel
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(libwebsockets)
%sysusers_requires
%{?systemd_ordering}

%description
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.
This makes it suitable for "machine to machine" messaging such as with low
power sensors or mobile devices such as phones, embedded computers or
microcontrollers like the Arduino. A good example of this is all of the work
that Andy Stanford-Clark (one of the originators of MQTT) has done in home
monitoring and automation with his twittering house and twittering ferry.

%package -n %{c_lib}
Summary:        Shared C Library for %{name}
Group:          Development/Libraries/C and C++

%description -n %{c_lib}
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.

This package holds the shared C library.

%package -n %{cpp_lib}
Summary:        Shared C++ Library for %{name}
Group:          Development/Libraries/C and C++

%description -n %{cpp_lib}
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.

This package holds the shared C++ library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}
Requires:       %{cpp_lib} = %{version}
Provides:       libmosquitto-devel = %{version}-%{release}
Provides:       libmosquittopp-devel = %{version}-%{release}

%description devel
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.

This package holds the development files.

%package clients
Summary:        Client for Mosquitto
Group:          Productivity/Networking/Other

%description clients
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.
This makes it suitable for "machine to machine" messaging such as with low
power sensors or mobile devices such as phones, embedded computers or
microcontrollers like the Arduino. A good example of this is all of the work
that Andy Stanford-Clark (one of the originators of MQTT) has done in home
monitoring and automation with his twittering house and twittering ferry.

Client for Mosquitto.

%prep
%autosetup -p1
find misc -type f -exec chmod a-x "{}" "+"

%build
%sysusers_generate_pre %{SOURCE2} %{name} %{name}-user.conf
%cmake \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
  -DWITH_WEBSOCKETS=ON \
  -DUSE_LIBWRAP=ON
%make_build

%install
%cmake_install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -Dd -m 0750 %{buildroot}%{home}
chmod -R o= %{buildroot}%{_sysconfdir}/%{name}/
install -D -m 644 security/mosquitto.apparmor %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.mosquitto
install -D -m 755 -d                          %{buildroot}%{_sysconfdir}/apparmor.d/local/
echo "# Site-specific additions and overrides for 'usr.sbin.mosquitto'" > %{buildroot}%{_sysconfdir}/apparmor.d/local/usr.sbin.mosquitto
install -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/mosquitto/conf.d/README
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/mosquitto/ca_certificates/README
install -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/mosquitto/certs/README
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}-user.conf

%pre -f %{name}.pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig
%post -n %{cpp_lib} -p /sbin/ldconfig
%postun -n %{cpp_lib} -p /sbin/ldconfig

%files
%license edl-v10 epl-v20 LICENSE.txt
%doc CONTRIBUTING.md ChangeLog.txt *.html *.example
%doc examples/ logo/ security/ misc/
%config(noreplace) %attr(-,root,%{name}) %{_sysconfdir}/mosquitto/
%{_bindir}/mosquitto_passwd
%{_bindir}/mosquitto_ctrl
#%%{_bindir}/mosquitto_ctrl_dynsec
%{_sbindir}/mosquitto
%{_mandir}/man1/mosquitto_ctrl.1%{?ext_man}
%{_mandir}/man1/mosquitto_ctrl_dynsec.1%{?ext_man}
%{_mandir}/man1/mosquitto_passwd.1%{?ext_man}
%{_mandir}/man5/mosquitto.conf.5%{?ext_man}
%{_mandir}/man7/mosquitto-tls.7%{?ext_man}
%{_mandir}/man7/mqtt.7%{?ext_man}
%{_mandir}/man8/mosquitto.8%{?ext_man}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_libdir}/mosquitto_dynamic_security.so
%{_sysusersdir}/%{name}-user.conf
%dir %attr(-,%{name},%{name}) %{home}
%dir %{_sysconfdir}/apparmor.d/
%dir %{_sysconfdir}/apparmor.d/local/
%config %{_sysconfdir}/apparmor.d/usr.sbin.mosquitto
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.sbin.mosquitto

%files clients
%license edl-v10 epl-v20 LICENSE.txt
%{_bindir}/mosquitto_pub
%{_bindir}/mosquitto_sub
%{_bindir}/mosquitto_rr
%{_mandir}/man1/mosquitto_pub.1%{?ext_man}
%{_mandir}/man1/mosquitto_sub.1%{?ext_man}
%{_mandir}/man1/mosquitto_rr.1%{?ext_man}

%files -n %{c_lib}
%license edl-v10 epl-v20 LICENSE.txt
%{_libdir}/libmosquitto.so.*

%files -n %{cpp_lib}
%license edl-v10 epl-v20 LICENSE.txt
%{_libdir}/libmosquittopp.so.*

%files devel
%{_libdir}/libmosquitto.so
%{_libdir}/libmosquittopp.so
%{_includedir}/mosquitto.h
%{_includedir}/mosquitto_*.h
%{_includedir}/mosquittopp.h
%{_includedir}/mqtt_protocol.h
%{_mandir}/man3/libmosquitto.3%{?ext_man}
%{_libdir}/pkgconfig/libmosquitto.pc
%{_libdir}/pkgconfig/libmosquittopp.pc

%changelog
