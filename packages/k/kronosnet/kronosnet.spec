#
# spec file for package kronosnet
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
%bcond_without zstd
%bcond_with kronosnetd
%bcond_without libnozzle
%bcond_without runautogen
%bcond_with rpmdebuginfo
%bcond_with overriderpmdebuginfo
%bcond_without buildman
%bcond_with installtests

%if %{with overriderpmdebuginfo}
%undefine _enable_debug_packages
%endif

%if %{with sctp}
BuildRequires:  lksctp-tools-devel
%endif
%if %{with nss}
%if 0%{suse_version}
BuildRequires:  mozilla-nss-devel
%else
BuildRequires:  nss-devel
%endif
%endif
%if %{with openssl}
%if 0%{?suse_version}
BuildRequires:  libopenssl-devel
%else
BuildRequires:  openssl-devel
%endif
%endif
%if %{with zlib}
BuildRequires:  zlib-devel
%endif
%if %{with lz4}
%if 0%{?suse_version}
BuildRequires:  liblz4-devel
%else
BuildRequires:  lz4-devel
%endif
%endif
%if %{with lzo2}
BuildRequires:  lzo-devel
%endif
%if %{with lzma}
BuildRequires:  xz-devel
%endif
%if %{with bzip2}
%if 0%{?suse_version}
BuildRequires:  libbz2-devel
%else
BuildRequires:  bzip2-devel
%endif
%endif
%if %{with zstd}
BuildRequires:  libzstd-devel
%endif
%if %{with libnozzle}
BuildRequires:  libnl3-devel
%endif
%if %{with kronosnetd}
BuildRequires:  pam-devel
%endif
%if %{with runautogen}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
%if %{with buildman}
BuildRequires:  doxygen
BuildRequires:  libqb-devel
BuildRequires:  libxml2-devel
%endif
# main (empty) package
# http://www.rpm.org/max-rpm/s1-rpm-subpack-spec-file-changes.html
Name:           kronosnet
Version:        1.28
Release:        0
Summary:        Multipoint-to-Multipoint VPN daemon
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Clustering/HA
URL:            https://kronosnet.org
Source0:        https://kronosnet.org/releases/kronosnet-%{version}.tar.xz

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
%if %{defined buildcompresszstd}
BuildRequires:  libzstd-devel
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
%if %{defined buildlibnozzle}
BuildRequires:  libnl3-devel
%endif

%prep
%setup -q -n %{name}-%{version}%{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}

%build
%if %{with runautogen}
./autogen.sh
%endif

%configure \
%if %{with installtests}
    --enable-install-tests \
%else
    --disable-install-tests \
%endif
%if %{with buildman}
    --enable-man \
%else
    --disable-man \
%endif
%if %{with sctp}
    --enable-libknet-sctp \
%else
    --disable-libknet-sctp \
%endif
%if %{with nss}
    --enable-crypto-nss \
%else
    --disable-crypto-nss \
%endif
%if %{with openssl}
    --enable-crypto-openssl \
%else
    --disable-crypto-openssl \
%endif
%if %{with zlib}
    --enable-compress-zlib \
%else
    --disable-compress-zlib \
%endif
%if %{with lz4}
    --enable-compress-lz4 \
%else
    --disable-compress-lz4 \
%endif
%if %{with lzo2}
    --enable-compress-lzo2 \
%else
    --disable-compress-lzo2 \
%endif
%if %{with lzma}
    --enable-compress-lzma \
%else
    --disable-compress-lzma \
%endif
%if %{with bzip2}
    --enable-compress-bzip2 \
%else
    --disable-compress-bzip2 \
%endif
%if %{with zstd}
    --enable-compress-zstd \
%else
    --disable-compress-zstd \
%endif
%if %{with kronosnetd}
    --enable-kronosnetd \
%else
    --disable-kronosnetd \
%endif
%if %{with libnozzle}
    --enable-libnozzle \
%else
    --disable-libnozzle \
%endif
    --with-initdefaultdir=%{_sysconfdir}/sysconfig/ \
    --with-systemddir=%{_unitdir}

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# tree cleanup
# remove static libraries
find %{buildroot} -name "*.a" -exec rm {} \;
# remove libtools leftovers
find %{buildroot} -type f -name "*.la" -exec rm {} \;

# remove init scripts
rm -rf %{buildroot}/etc/init.d

# remove docs
rm -rf %{buildroot}/usr/share/doc/kronosnet

# main empty package
%description
 The kronosnet source

%if %{with kronosnetd}
## Runtime and subpackages section
%package -n kronosnetd
Summary:        Multipoint-to-Multipoint VPN daemon
Group:          Productivity/Clustering/HA
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): shadow-utils
Requires(preun): shadow-utils
Requires:       /etc/pam.d/passwd
Requires:       pam

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
%systemd_post kronosnetd.service
getent group kronosnetadm >/dev/null || %{_sbindir}/groupadd --force --system kronosnetadm

%preun -n kronosnetd
%systemd_preun kronosnetd.service

%files -n kronosnetd
%license COPYING.* COPYRIGHT
%dir %{_sysconfdir}/kronosnet
%dir %{_sysconfdir}/kronosnet/*
%config(noreplace) %{_sysconfdir}/sysconfig/kronosnetd
%config(noreplace) %{_sysconfdir}/pam.d/kronosnetd
%config(noreplace) %{_sysconfdir}/logrotate.d/kronosnetd
%{_unitdir}/kronosnetd.service
%{_sbindir}/*
%{_mandir}/man8/*
%endif

%if %{with libnozzle}
%package -n libnozzle1
Summary:        Simple userland wrapper around kernel tap devices

%description -n libnozzle1
This is an over-engineered commodity library to manage a pool
of tap devices and provides the basic
pre-up.d/up.d/down.d/post-down.d infrastructure.

%files -n libnozzle1
%license COPYING.* COPYRIGHT
%{_libdir}/libnozzle.so.*

%if 0%{?ldconfig_scriptlets}
%ldconfig_scriptlets -n libnozzle1
%else
%post -n libnozzle1 -p /sbin/ldconfig
%postun -n libnozzle1 -p /sbin/ldconfig
%endif

%package -n libnozzle-devel
Summary:        Simple userland wrapper around kernel tap devices (developer files)
Requires:       libnozzle1%{_isa} = %{version}-%{release}
Provides:       libnozzle1-devel = %{version}
Obsoletes:      libnozzle1-devel <= %{version}
Requires:       pkgconfig

%description -n libnozzle-devel
This is an over-engineered commodity library to manage a pool
of tap devices and provides the basic
pre-up.d/up.d/down.d/post-down.d infrastructure.

%files -n libnozzle-devel
%license COPYING.* COPYRIGHT
%{_libdir}/libnozzle.so
%{_includedir}/libnozzle.h
%{_libdir}/pkgconfig/libnozzle.pc
%if %{with buildman}
%{_mandir}/man3/nozzle*.3.gz
%endif
%endif

%package -n libknet1
Summary:        Kronosnet core switching implementation
Group:          System/Libraries

%description -n libknet1
The whole kronosnet core is implemented in this library.
Please refer to the not-yet-existing documentation for further
information.

%files -n libknet1
%license COPYING.* COPYRIGHT
%{_libdir}/libknet.so.*
%dir %{_libdir}/kronosnet

%if 0%{?ldconfig_scriptlets}
%ldconfig_scriptlets -n libknet1
%else
%post -n libknet1 -p /sbin/ldconfig
%postun -n libknet1 -p /sbin/ldconfig
%endif

%package -n libknet-devel
Summary:        Development files fro the Kronosnet core switching implementation
Group:          Development/Libraries/C and C++
Requires:       libknet1%{_isa} = %{version}-%{release}
Requires:       pkgconfig
Provides:       libknet1-devel = %{version}
Obsoletes:      libknet1-devel <= %{version}

%description -n libknet-devel
The whole kronosnet core is implemented in this library.
Please refer to the not-yet-existing documentation for further
information.

%files -n libknet-devel
%license COPYING.* COPYRIGHT
%{_libdir}/libknet.so
%{_includedir}/libknet.h
%{_libdir}/pkgconfig/libknet.pc
%if %{with buildman}
%{_mandir}/man3/knet_*.3.gz
%endif

%if %{with nss}
%package -n libknet1-crypto-nss-plugin
Summary:        Provides libknet1 nss support
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n libknet1-crypto-nss-plugin
Provides NSS crypto support for libknet1.

%files -n libknet1-crypto-nss-plugin
%{_libdir}/kronosnet/crypto_nss.so
%endif

%if %{with openssl}
%package -n libknet1-crypto-openssl-plugin
Summary:        Provides libknet1 openssl support
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n libknet1-crypto-openssl-plugin
Provides OpenSSL crypto support for libknet1.

%files -n libknet1-crypto-openssl-plugin
%{_libdir}/kronosnet/crypto_openssl.so
%endif

%if %{with zlib}
%package -n libknet1-compress-zlib-plugin
Summary:        Provides libknet1 zlib support
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n libknet1-compress-zlib-plugin
Provides zlib compression support for libknet1.

%files -n libknet1-compress-zlib-plugin
%{_libdir}/kronosnet/compress_zlib.so
%endif

%if %{with lz4}
%package -n libknet1-compress-lz4-plugin
Summary:        Provides libknet1 lz4 and lz4hc support
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n libknet1-compress-lz4-plugin
Provides lz4 and lz4hc compression support for libknet1.

%files -n libknet1-compress-lz4-plugin
%{_libdir}/kronosnet/compress_lz4.so
%{_libdir}/kronosnet/compress_lz4hc.so
%endif

%if %{with lzo2}
%package -n libknet1-compress-lzo2-plugin
Summary:        Provides libknet1 lzo2 support
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n libknet1-compress-lzo2-plugin
Provides lzo2 compression support for libknet1.

%files -n libknet1-compress-lzo2-plugin
%{_libdir}/kronosnet/compress_lzo2.so
%endif

%if %{with lzma}
%package -n libknet1-compress-lzma-plugin
Summary:        Provides libknet1 lzma support
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n libknet1-compress-lzma-plugin
Provides lzma compression support for libknet1.

%files -n libknet1-compress-lzma-plugin
%{_libdir}/kronosnet/compress_lzma.so
%endif

%if %{with bzip2}
%package -n libknet1-compress-bzip2-plugin
Summary:        Provides libknet1 bzip2 support
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n libknet1-compress-bzip2-plugin
Provides bzip2 compression support for libknet1.

%files -n libknet1-compress-bzip2-plugin
%{_libdir}/kronosnet/compress_bzip2.so
%endif

%if %{with zstd}
%package -n libknet1-compress-zstd-plugin
Summary:        Provides libknet1 zstd support
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n libknet1-compress-zstd-plugin
Provides zstd compression support for libknet1.

%files -n libknet1-compress-zstd-plugin
%{_libdir}/kronosnet/compress_zstd.so
%endif

%package -n libknet1-crypto-plugins-all
Summary:        Provides libknet1 crypto plugins meta package
Group:          System/Libraries
%if %{with nss}
Requires:       libknet1-crypto-nss-plugin%{_isa} = %{version}-%{release}
%endif
%if %{with openssl}
Requires:       libknet1-crypto-openssl-plugin%{_isa} = %{version}-%{release}
%endif

%description -n libknet1-crypto-plugins-all
Provides meta package to install all of libknet1 crypto plugins

%files -n libknet1-crypto-plugins-all

%package -n libknet1-compress-plugins-all
Summary:        Provides libknet1 compress plugins meta package
Group:          System/Libraries
%if %{with zlib}
Requires:       libknet1-compress-zlib-plugin%{_isa} = %{version}-%{release}
%endif
%if %{with lz4}
Requires:       libknet1-compress-lz4-plugin%{_isa} = %{version}-%{release}
%endif
%if %{with lzo2}
Requires:       libknet1-compress-lzo2-plugin%{_isa} = %{version}-%{release}
%endif
%if %{with lzma}
Requires:       libknet1-compress-lzma-plugin%{_isa} = %{version}-%{release}
%endif
%if %{with bzip2}
Requires:       libknet1-compress-bzip2-plugin%{_isa} = %{version}-%{release}
%endif
%if %{with zstd}
Requires:       libknet1-compress-zstd-plugin%{_isa} = %{version}-%{release}
%endif

%description -n libknet1-compress-plugins-all
 Meta package to install all of libknet1 compress plugins

%files -n libknet1-compress-plugins-all

%package -n libknet1-plugins-all
Summary:        Provides libknet1 plugins meta package
Group:          System/Libraries
Requires:       libknet1-compress-plugins-all%{_isa} = %{version}-%{release}
Requires:       libknet1-crypto-plugins-all%{_isa} = %{version}-%{release}

%description -n libknet1-plugins-all
 Meta package to install all of libknet1 plugins

%files -n libknet1-plugins-all

%if %{with installtests}
%package -n kronosnet-tests
Summary:        Provides kronosnet test suite
Group:          System/Libraries
Requires:       libknet1%{_isa} = %{version}-%{release}

%description -n kronosnet-tests
 This package contains all the libknet and libnozzle test suite.

%files -n kronosnet-tests
%{_libdir}/kronosnet/tests/*
%endif

%if %{with rpmdebuginfo}
%endif

%changelog
