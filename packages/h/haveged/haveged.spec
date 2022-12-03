#
# spec file for package haveged
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


%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d }
Name:           haveged
Version:        1.9.18
Release:        0
Summary:        Daemon for feeding entropy into the random pool
License:        GPL-3.0-only
Group:          System/Daemons
URL:            https://github.com/jirka-h/haveged
Source0:        https://github.com/jirka-h/haveged/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        %{name}.service
Source3:        90-haveged.rules
Source4:        haveged-dracut.module
Source5:        %{name}-switch-root.service
Patch0:         ppc64le.patch
# PATCH-FIX-UPSTREAM: don't write to syslog at startup to avoid deadlocks psimons@suse.com bnc#959237
Patch2:         haveged-no-syslog.patch
Patch3:         harden_haveged.service.patch
# PATCH-FIX-UPSTREAM: Synchronize haveged instances during switching root bsc#1203079
Patch4:         haveged-switch-root.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires(post): coreutils
Requires(postun):coreutils
Enhances:       apache2
Enhances:       gpg2
Enhances:       openssl
Enhances:       openvpn
Enhances:       php5
Enhances:       smtp_daemon
Enhances:       systemd
%{?systemd_requires}

%description
The haveged daemon feeds the Linux entropy pool with random
numbers generated from hidden processor state.

For more information, see http://www.issihosts.com/haveged/ .

%package devel
Summary:        Haveged development files
Group:          Development/Libraries/C and C++
Requires:       libhavege2 = %{version}

%description devel
Headers and for the haveged library

This package contains the haveged implementation of the HAVEGE
algorithm and supporting features.

%package -n libhavege2
Summary:        Haveged interface library
Group:          System/Libraries

%description -n libhavege2
Shared object for the haveged library.
This package contains the haveged implementation of the HAVEGE
algorithm and supporting features.

%prep
%autosetup -p1

%build
autoreconf -fvi
export CFLAGS="%{optflags} -fpie -D_DEFAULT_SOURCE -D_GNU_SOURCE"
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
# ENT randomly fails so disable the test
%configure \
    --disable-static \
    --disable-enttest \
    --enable-nistest \
    --enable-daemon \
    --enable-clock_gettime
make %{?_smp_mflags}

%check
#XXX: nist test is killed by SIGKILL with static int random_pool1[_32MB] on
#     32bit. Let change it to _08MB to avoid the test beeing killed, even if I
#     am not sure allocate of 128M is prohibited
%ifarch %{ix86}
sed -i 's/\[_32MB\]/[_08MB]/' nist/nist.c
%endif

make %{?_smp_mflags} check

%install
%make_install
install -Dpm 0644 %{SOURCE2} \
  %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 %{SOURCE3} \
  %{buildroot}%{_udevrulesdir}/90-%{name}.rules
install -Dpm 0644 %{SOURCE5} \
  %{buildroot}%{_unitdir}/%{name}-switch-root.service
install -Dpm 0755 %{SOURCE4} \
  %{buildroot}%{_prefix}/lib/dracut/modules.d/98%{name}/module-setup.sh
rm -f %{buildroot}%{_libdir}/libhavege.*a
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%post
%{?udev_rules_update:%udev_rules_update}
%service_add_post %{name}.service
%service_add_post %{name}-switch-root.service
%{?regenerate_initrd_post}

%postun
%service_del_postun %{name}.service
%service_del_postun %{name}-switch-root.service
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%pre
%service_add_pre %{name}.service
%service_add_pre %{name}-switch-root.service

%preun
%service_del_preun %{name}.service
%service_del_preun %{name}-switch-root.service

%post -n libhavege2 -p /sbin/ldconfig
%postun -n libhavege2 -p /sbin/ldconfig

%files
%license COPYING
%{_sbindir}/rc%{name}
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8%{?ext_man}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-switch-root.service
%{_udevrulesdir}/90-%{name}.rules
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%dir %{_prefix}/lib/dracut/modules.d/98%{name}
%{_prefix}/lib/dracut/modules.d/98%{name}/module-setup.sh

%files devel
%license COPYING
%{_mandir}/man3/libhavege.3%{?ext_man}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/havege.h
%doc contrib/build/havege_sample.c
%{_libdir}/*.so

%files -n libhavege2
%license COPYING
%{_libdir}/*.so.*

%changelog
