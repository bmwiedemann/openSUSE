#
# spec file for package cryptsetup
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


%define so_ver 12
%if 0%{?is_backports}
Name:           cryptsetup2
%else
Name:           cryptsetup
%endif
Version:        2.3.4
Release:        0
Summary:        Setup program for dm-crypt Based Encrypted Block Devices
License:        SUSE-GPL-2.0-with-openssl-exception AND LGPL-2.0-or-later
Group:          System/Base
URL:            https://gitlab.com/cryptsetup/cryptsetup/
Source0:        https://www.kernel.org/pub/linux/utils/cryptsetup/v2.3/cryptsetup-%{version}.tar.xz
# GPG signature of the uncompressed tarball.
Source1:        https://www.kernel.org/pub/linux/utils/cryptsetup/v2.3/cryptsetup-%{version}.tar.sign
Source2:        baselibs.conf
Source3:        cryptsetup.keyring
BuildRequires:  device-mapper-devel
BuildRequires:  fipscheck
BuildRequires:  fipscheck-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libpwquality-devel
BuildRequires:  libselinux-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig(openssl)
# 2.6.38 has the required if_alg.h
BuildRequires:  linux-glibc-devel >= 2.6.38
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  suse-module-tools
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libargon2)
%if 0%{?is_backports}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
Requires(post): coreutils
Requires(postun): coreutils

%lang_package(cryptsetup)

%description
cryptsetup is used to conveniently set up dm-crypt based device-mapper
targets. It allows to set up targets to read cryptoloop compatible
volumes as well as LUKS formatted ones. The package additionally
includes support for automatically setting up encrypted volumes at boot
time via the config file %{_sysconfdir}/crypttab.

%package -n libcryptsetup%{so_ver}
Summary:        Library for setting up dm-crypt Based Encrypted Block Devices
Group:          System/Libraries
Suggests:       libcryptsetup%{so_ver}-hmac = %{version}-%{release}

%description -n libcryptsetup%{so_ver}
cryptsetup is used to conveniently set up dm-crypt based device-mapper
targets. It allows to set up targets to read cryptoloop compatible
volumes as well as LUKS formatted ones. The package additionally
includes support for automatically setting up encrypted volumes at boot
time via the config file %{_sysconfdir}/crypttab.

%package -n libcryptsetup%{so_ver}-hmac
Summary:        Checksums for libcryptsetup%{so_ver}
Group:          System/Base
Requires:       libcryptsetup%{so_ver} = %{version}-%{release}

%description -n libcryptsetup%{so_ver}-hmac
This package contains HMAC checksums for integrity checking of libcryptsetup4,
used for FIPS.

%package -n lib%{name}-devel
Summary:        Header files for libcryptsetup
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcryptsetup%{so_ver} = %{version}
# cryptsetup-devel last used 11.1
Provides:       cryptsetup-devel = %{version}
Obsoletes:      cryptsetup-devel < %{version}
%if 0%{?is_backports}
# have to conflict with main package that is in SLE
Conflicts:      cryptsetup-devel < %{version}
%endif

%description -n lib%{name}-devel
cryptsetup is used to conveniently set up dm-crypt based device-mapper
targets. It allows to set up targets to read cryptoloop compatible
volumes as well as LUKS formatted ones. The package additionally
includes support for automatically setting up encrypted volumes at boot
time via the config file %{_sysconfdir}/crypttab.

%prep
%setup -n cryptsetup-%{version} -q
%if 0%{?is_backports}
sed -i -e '/AC_INIT/s/cryptsetup/cryptsetup2/' configure.ac
autoreconf -f -i
%endif

%build
%configure \
  --enable-cryptsetup-reencrypt \
  --enable-selinux \
  --enable-fips \
  --enable-pwquality \
  --enable-gcrypt-pbkdf2 \
  --enable-libargon2 \
  --with-default-luks-format=LUKS1 \
  --with-luks2-lock-path=/run/cryptsetup \
  --with-tmpfilesdir='%{_tmpfilesdir}'
make %{?_smp_mflags} V=1

%install
# Generate HMAC checksums (FIPS)
%define __spec_install_post \
  %{?__debug_package:%{__debug_install_post}} \
  %{__arch_install_post} \
  %__os_install_post \
  fipshmac %{buildroot}/%{_libdir}/libcryptsetup.so.* \
%{nil}

%make_install
%if 0%{?is_backports}
# need to rename a files to avoid file conflict
for i in cryptsetup integritysetup veritysetup cryptsetup-reencrypt; do
	mv %{buildroot}%{_sbindir}/$i %{buildroot}%{_sbindir}/${i}2
	mv %{buildroot}%{_mandir}/man8/$i.8 %{buildroot}%{_mandir}/man8/${i}2.8
done
rm -f %{buildroot}%{_tmpfilesdir}/cryptsetup.conf
%endif
install -dm 0755 %{buildroot}/sbin
ln -s ..%{_sbindir}/cryptsetup%{?is_backports:2} %{buildroot}/sbin
# don't want this file in /lib (FHS compat check), and can't move it to /usr/lib
find %{buildroot} -type f -name "*.la" -delete -print
#
%find_lang %{name} --all-name

%if !0%{?is_backports}
#
%post
%{?regenerate_initrd_post}
%tmpfiles_create %{_tmpfilesdir}/cryptsetup.conf

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}
#
%endif

%post -n libcryptsetup%{so_ver} -p /sbin/ldconfig
%postun -n libcryptsetup%{so_ver} -p /sbin/ldconfig

%files
%doc AUTHORS COPYING* FAQ README TODO docs/ChangeLog.old docs/*ReleaseNotes
/sbin/cryptsetup%{?is_backports:2}
%{_sbindir}/cryptsetup%{?is_backports:2}
%{_sbindir}/veritysetup%{?is_backports:2}
%{_sbindir}/integritysetup%{?is_backports:2}
%{_sbindir}/cryptsetup-reencrypt%{?is_backports:2}
%{_mandir}/man8/cryptsetup%{?is_backports:2}.8%{ext_man}
%{_mandir}/man8/cryptsetup-reencrypt%{?is_backports:2}.8%{ext_man}
%{_mandir}/man8/veritysetup%{?is_backports:2}.8%{ext_man}
%{_mandir}/man8/integritysetup%{?is_backports:2}.8%{ext_man}
%if !0%{?is_backports}
%{_tmpfilesdir}/cryptsetup.conf
%ghost %dir /run/cryptsetup
%endif

%files lang -f %{name}.lang

%files -n libcryptsetup%{so_ver}
%{_libdir}/libcryptsetup.so.%{so_ver}*

%files -n libcryptsetup%{so_ver}-hmac
%{_libdir}/.libcryptsetup.so.%{so_ver}*hmac

%files -n lib%{name}-devel
%doc docs/examples/
%{_includedir}/libcryptsetup.h
%{_libdir}/libcryptsetup.so
%{_libdir}/pkgconfig/*

%changelog
