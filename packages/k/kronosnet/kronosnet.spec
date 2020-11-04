#
# spec file for package kronosnet
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# set defaults from ./configure invokation
%bcond_without sctp
%bcond_without nss
%bcond_without openssl
%bcond_without zlib
%if 0%{?suse_version} >= 1500
%bcond_without lz4
%else
%bcond_with lz4
%endif
%bcond_without lzo2
%bcond_without lzma
%bcond_without bzip2
%bcond_with kronosnetd
%bcond_with libtap
%bcond_without runautogen
%bcond_with rpmdebuginfo
%bcond_with overriderpmdebuginfo
%bcond_without buildman

%if %{with overriderpmdebuginfo}
%undefine _enable_debug_packages
%endif

%if %{with sctp}
%global buildsctp 1
%endif
%if %{with nss}
%global buildcryptonss 1
%endif
%if %{with openssl}
%global buildcryptoopenssl 1
%endif
%if %{with zlib}
%global buildcompresszlib 1
%endif
%if %{with lz4}
%global buildcompresslz4 1
%endif
%if %{with lzo2}
%global buildcompresslzo2 1
%endif
%if %{with lzma}
%global buildcompresslzma 1
%endif
%if %{with bzip2}
%global buildcompressbzip2 1
%endif
%if %{with libtap}
%global buildlibtap 1
%endif
%if %{with kronosnetd}
%global buildlibtap 1
%global buildkronosnetd 1
%endif
%if %{with runautogen}
%global buildautogen 1
%endif
%if %{with buildman}
%global buildmanpages 1
%endif
# main (empty) package
# http://www.rpm.org/max-rpm/s1-rpm-subpack-spec-file-changes.html
Name:           kronosnet
Version:        1.3
Release:        0
Summary:        Multipoint-to-Multipoint VPN daemon
License:        GPL-2.0+ AND LGPL-2.1+
Group:          Productivity/Clustering/HA
Url:            https://github.com/kronosnet/kronosnet/
Source0:        %{name}-%{version}%{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}.tar.gz
Patch1:         add-version.patch
## Setup/build bits
# Build dependencies
BuildRequires:  gcc
BuildRequires:  pkgconfig
%if %{with overriderpmdebuginfo}
%undefine _enable_debug_packages
%endif
# required to build man pages
%if %{defined buildmanpages}
BuildRequires:  doxygen
BuildRequires:  libqb-devel
BuildRequires:  libxml2-devel
%endif
%if %{defined buildsctp}
BuildRequires:  lksctp-tools-devel
%endif
%if %{defined buildcryptonss}
BuildRequires:  mozilla-nss-devel
%endif
%if %{defined buildcryptoopenssl}
BuildRequires:  openssl-devel
%endif
%if %{defined buildcompresszlib}
BuildRequires:  zlib-devel
%endif
%if %{defined buildcompresslz4}
BuildRequires:  liblz4-devel
%endif
%if %{defined buildcompresslzo2}
BuildRequires:  lzo-devel
%endif
%if %{defined buildcompresslzma}
BuildRequires:  xz-devel
%endif
%if %{defined buildcompressbzip2}
BuildRequires:  libbz2-devel
%endif
%if %{defined buildkronosnetd}
BuildRequires:  libqb-devel
BuildRequires:  pam-devel
%endif
%if %{defined buildautogen}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

%prep
%setup -q -n %{name}-%{version}%{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}

%patch1 -p1

%build
%if %{with runautogen}
    ./autogen.sh
%endif

%configure \
%if %{defined buildmanpages}
    --enable-man \
%else
    --disable-man \
%endif
%if %{defined buildsctp}
    --enable-libknet-sctp \
%else
    --disable-libknet-sctp \
%endif
%if %{defined buildcryptonss}
    --enable-crypto-nss \
%else
    --disable-crypto-nss \
%endif
%if %{defined buildcryptoopenssl}
    --enable-crypto-openssl \
%else
    --disable-crypto-openssl \
%endif
%if %{defined buildcompresszlib}
    --enable-compress-zlib \
%else
    --disable-compress-zlib \
%endif
%if %{defined buildcompresslz4}
    --enable-compress-lz4 \
%else
    --disable-compress-lz4 \
%endif
%if %{defined buildcompresslzo2}
    --enable-compress-lzo2 \
%else
    --disable-compress-lzo2 \
%endif
%if %{defined buildcompresslzma}
    --enable-compress-lzma \
%else
    --disable-compress-lzma \
%endif
%if %{defined buildcompressbzip2}
    --enable-compress-bzip2 \
%else
    --disable-compress-bzip2 \
%endif
%if %{defined buildkronosnetd}
    --enable-kronosnetd \
%endif
%if %{defined buildlibtap}
    --enable-libtap \
%endif
    --with-initdefaultdir=%{_sysconfdir}/sysconfig/ \
%if %{defined _unitdir}
    --with-systemddir=%{_unitdir}
%else
    --with-initddir=%{_sysconfdir}/rc.d/init.d/
%endif

make %{?_smp_mflags}

%install
%make_install

# tree cleanup
# remove static libraries
find %{buildroot} -name "*.a" -delete
# remove libtools leftovers
find %{buildroot} -type f -name "*.la" -delete -print

# handle systemd vs init script
%if %{defined _unitdir}
# remove init scripts
rm -rf %{buildroot}%{_initddir}
%else
# remove systemd specific bits
find %{buildroot} -name "*.service" -delete
%endif

# remove docs
rm -rf %{buildroot}%{_datadir}/doc/kronosnet

# main empty package
%description
kronosnet source

%if %{defined buildkronosnetd}
## Runtime and subpackages section
%package -n kronosnetd
Summary:        Multipoint-to-Multipoint VPN daemon
Group:          Productivity/Clustering/HA
Requires:       %{_sysconfdir}/pam.d/passwd
Requires:       pam
%if %{defined buildkronosnetd}
Requires:       %{_sysconfdir}/pam.d/passwd
Requires:       pam
Requires(post): shadow-utils
Requires(preun): shadow-utils
%if %{defined _unitdir}
# Needed for systemd unit
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(postun): systemd-units
Requires(preun): systemd-units
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
%endif

%description -n kronosnetd
The kronosnet daemon is a bridge between kronosnet switching engine
and kernel network tap devices, to create and administer a
distributed LAN over multipoint-to-multipoint VPNs.
The daemon does a poor attempt to provide a configure UI similar
to other known network devices/tools (Cisco, quagga).
Beside looking horrific, it allows runtime changes and
reconfiguration of the kronosnet(s) without daemon reload
or service disruption.

%post -n kronosnetd
%if %{defined _unitdir}
 %if 0%{?systemd_post:1}
  %systemd_post kronosnetd.service
 %else
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
 %endif
%else
/sbin/chkconfig --add kronosnetd
%endif
getent group kronosnetadm >/dev/null || %{_sbindir}/groupadd -r kronosnetadm

%preun -n kronosnetd
%if %{defined _unitdir}
 %if 0%{?systemd_preun:1}
  %systemd_preun kronosnetd.service
 %else
if [ "$1" -eq 0 ]; then
    /bin/systemctl --no-reload disable kronosnetd.service
    /bin/systemctl stop kronosnetd.service >/dev/null 2>&1
fi
%endif
%else
if [ "$1" = 0 ]; then
    /sbin/service kronosnetd stop >/dev/null 2>&1
    /sbin/chkconfig --del kronosnetd
fi
%endif

%files -n kronosnetd
%doc COPYING.* COPYRIGHT
%dir %{_sysconfdir}/kronosnet
%dir %{_sysconfdir}/kronosnet/*
%config(noreplace) %{_sysconfdir}/sysconfig/kronosnetd
%config(noreplace) %{_sysconfdir}/pam.d/kronosnetd
%config(noreplace) %{_sysconfdir}/logrotate.d/kronosnetd
%if %{defined _unitdir}
%{_unitdir}/kronosnetd.service
%else
%config(noreplace) %{_sysconfdir}/rc.d/init.d/kronosnetd
%endif
%{_sbindir}/*
%{_mandir}/man8/*
%endif

%if %{defined buildlibtap}
%package -n libtap1
Summary:        Userland wrapper around kernel tap devices
Group:          System/Libraries

%description -n libtap1
This is an over-engineered commodity library to manage a pool
of tap devices and provides the basic
pre-up.d/up.d/down.d/post-down.d infrastructure.

%post -n libtap1 -p /sbin/ldconfig
%postun -n libtap1 -p /sbin/ldconfig

%files -n libtap1
%doc COPYING.* COPYRIGHT
%{_libdir}/libtap.so.*

%post -n libtap1 -p /sbin/ldconfig
%postun -n libtap1 -p /sbin/ldconfig
%endif

%package -n libtap1-devel
Summary:        Development files for libtap, a userland wrapper around kernel tap devices
Group:          Development/Libraries/C and C++
Requires:       libtap1 = %{version}-%{release}

%description -n libtap1-devel
This is an over-engineered commodity library to manage a pool
of tap devices and provides the basic
pre-up.d/up.d/down.d/post-down.d infrastructure.

%files -n libtap1-devel
%doc COPYING.* COPYRIGHT
%{_libdir}/libtap.so
%{_includedir}/libtap.h
%{_libdir}/pkgconfig/libtap.pc
%endif

%package -n libknet1
Summary:        Kronosnet core switching implementation
Group:          System/Libraries

%description -n libknet1
The whole kronosnet core is implemented in this library.
Please refer to the not-yet-existing documentation for further
information.

%files -n libknet1
%doc COPYING.* COPYRIGHT
%{_libdir}/libknet.so.*
%dir %{_libdir}/kronosnet

%post -n libknet1 -p /sbin/ldconfig
%postun -n libknet1 -p /sbin/ldconfig

%package -n libknet1-devel
Summary:        Development files fro the Kronosnet core switching implementation
Group:          Development/Libraries/C and C++
Requires:       libknet1 = %{version}-%{release}

%description -n libknet1-devel
The whole kronosnet core is implemented in this library.
Please refer to the not-yet-existing documentation for further
information.

%files -n libknet1-devel
%doc COPYING.* COPYRIGHT
%{_libdir}/libknet.so
%{_includedir}/libknet.h
%{_libdir}/pkgconfig/libknet.pc
%{_mandir}/man3/*.3%{ext_man}

%if %{defined buildcryptonss}
%package -n libknet1-crypto-nss-plugin
Summary:        NSS crypto support for libknet1
Group:          System/Libraries
Requires:       libknet1 = %{version}-%{release}

%description -n libknet1-crypto-nss-plugin
NSS crypto support for libknet1.

%files -n libknet1-crypto-nss-plugin
%{_libdir}/kronosnet/crypto_nss.so
%endif

%if %{defined buildcryptoopenssl}
%package -n libknet1-crypto-openssl-plugin
Summary:        OpenSSL support for libknet1
Group:          System/Libraries
Requires:       libknet1 = %{version}-%{release}

%description -n libknet1-crypto-openssl-plugin
OpenSSL crypto support for libknet1.

%files -n libknet1-crypto-openssl-plugin
%{_libdir}/kronosnet/crypto_openssl.so
%endif

%if %{defined buildcompresszlib}
%package -n libknet1-compress-zlib-plugin
Summary:        zlib support for libknet1
Group:          System/Libraries
Requires:       libknet1 = %{version}-%{release}

%description -n libknet1-compress-zlib-plugin
zlib compression support for libknet1.

%files -n libknet1-compress-zlib-plugin
%{_libdir}/kronosnet/compress_zlib.so
%endif

%if %{defined buildcompresslz4}
%package -n libknet1-compress-lz4-plugin
Summary:        LZ4 and LZ4HC support for libknet1
Group:          System/Libraries
Requires:       libknet1 = %{version}-%{release}

%description -n libknet1-compress-lz4-plugin
lz4 and lz4hc compression support for libknet1.

%files -n libknet1-compress-lz4-plugin
%{_libdir}/kronosnet/compress_lz4.so
%{_libdir}/kronosnet/compress_lz4hc.so
%endif

%if %{defined buildcompresslzo2}
%package -n libknet1-compress-lzo2-plugin
Summary:        LZO2 support for libknet1
Group:          System/Libraries
Requires:       libknet1 = %{version}-%{release}

%description -n libknet1-compress-lzo2-plugin
lzo2 compression support for libknet1.

%files -n libknet1-compress-lzo2-plugin
%{_libdir}/kronosnet/compress_lzo2.so
%endif

%if %{defined buildcompresslzma}
%package -n libknet1-compress-lzma-plugin
Summary:        LZMA support for libknet1
Group:          System/Libraries
Requires:       libknet1 = %{version}-%{release}

%description -n libknet1-compress-lzma-plugin
lzma compression support for libknet1.

%files -n libknet1-compress-lzma-plugin
%{_libdir}/kronosnet/compress_lzma.so
%endif

%if %{defined buildcompressbzip2}
%package -n libknet1-compress-bzip2-plugin
Summary:        bzip2 support for libknet1
Group:          System/Libraries
Requires:       libknet1 = %{version}-%{release}

%description -n libknet1-compress-bzip2-plugin
bzip2 compression support for libknet1.

%files -n libknet1-compress-bzip2-plugin
%{_libdir}/kronosnet/compress_bzip2.so
%endif

%package -n libknet1-crypto-plugins-all
Summary:        Libknet1 crypto plugins meta package
Group:          System/Libraries
%if %{defined buildcryptonss}
Requires:       libknet1-crypto-nss-plugin
%endif
%if %{defined buildcryptoopenssl}
Requires:       libknet1-crypto-openssl-plugin
%endif

%description -n libknet1-crypto-plugins-all
Meta package to install all of libknet1 crypto plugins.

%files -n libknet1-crypto-plugins-all

%package -n libknet1-compress-plugins-all
Summary:        Libknet1 compress plugins meta package
Group:          System/Libraries
%if %{defined buildcompresszlib}
Requires:       libknet1-compress-zlib-plugin
%endif
%if %{defined buildcompresslz4}
Requires:       libknet1-compress-lz4-plugin
%endif
%if %{defined buildcompresslzo2}
Requires:       libknet1-compress-lzo2-plugin
%endif
%if %{defined buildcompresslzma}
Requires:       libknet1-compress-lzma-plugin
%endif
%if %{defined buildcompressbzip2}
Requires:       libknet1-compress-bzip2-plugin
%endif

%description -n libknet1-compress-plugins-all
Meta package to install all of libknet1 compress plugins

%files -n libknet1-compress-plugins-all

%package -n libknet1-plugins-all
Summary:        Libknet1 plugins meta package
Group:          System/Libraries
Requires:       libknet1-compress-plugins-all
Requires:       libknet1-crypto-plugins-all

%description -n libknet1-plugins-all
Meta package to install all of libknet1 plugins.

%files -n libknet1-plugins-all

%if %{with rpmdebuginfo}
%endif

%changelog
