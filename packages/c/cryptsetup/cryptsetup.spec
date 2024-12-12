#
# spec file for package cryptsetup
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


%define so_ver 12
Name:           cryptsetup
Version:        2.7.5
Release:        0
Summary:        Setup program for dm-crypt Based Encrypted Block Devices
License:        CC-BY-SA-4.0 AND LGPL-2.0-or-later WITH cryptsetup-OpenSSL-exception
Group:          System/Base
URL:            https://gitlab.com/cryptsetup/cryptsetup/
Source0:        https://www.kernel.org/pub/linux/utils/cryptsetup/v2.7/cryptsetup-%{version}.tar.xz
# GPG signature of the uncompressed tarball.
Source1:        https://www.kernel.org/pub/linux/utils/cryptsetup/v2.7/cryptsetup-%{version}.tar.sign
Source2:        baselibs.conf
Source3:        cryptsetup.keyring
# FAQ.md is CC-BY-SA-4.0
Source4:        https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt#/cc-by-sa-4.0.txt
Patch0:         cryptsetup-fips140-3.patch
# 2.6.38 has the required if_alg.h
BuildRequires:  linux-glibc-devel >= 2.6.38
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  suse-module-tools
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  rubygem(asciidoctor)
Requires(post): coreutils
Requires(postun): coreutils
Provides:       integritysetup = %{version}-%{release}
Provides:       veritysetup = %{version}-%{release}
%if %{?suse_version} >= 1550
# LUKS2 used as default format, which GRUB < 2.06 can't read
Conflicts:      grub2 < 2.06
%endif

%lang_package(cryptsetup)

%description
cryptsetup is used to conveniently set up dm-crypt based device-mapper
targets. It allows to set up targets to read cryptoloop compatible
volumes as well as LUKS formatted ones. The package additionally
includes support for automatically setting up encrypted volumes at boot
time via the config file %{_sysconfdir}/crypttab.

%package ssh
Summary:        Cryptsetup LUKS2 SSH token
License:        LGPL-2.0-or-later WITH cryptsetup-OpenSSL-exception
Group:          System/Base

%description ssh
Experimental cryptsetup plugin for unlocking LUKS2 devices with
token connected to an SSH server.

%package doc
Summary:        Cryptsetup Documentation
License:        CC-BY-SA-4.0 AND LGPL-2.0-or-later WITH cryptsetup-OpenSSL-exception
Group:          Documentation/Man
Supplements:    (cryptsetup and man)
Supplements:    (cryptsetup and patterns-base-documentation)
BuildArch:      noarch

%description doc
Documentation and man pages for cryptsetup

%package -n libcryptsetup%{so_ver}
Summary:        Library for setting up dm-crypt Based Encrypted Block Devices
License:        LGPL-2.0-or-later WITH cryptsetup-OpenSSL-exception
Group:          System/Libraries
Provides:       libcryptsetup%{so_ver}-hmac = %{version}
Obsoletes:      libcryptsetup%{so_ver}-hmac < %{version}

%description -n libcryptsetup%{so_ver}
cryptsetup is used to conveniently set up dm-crypt based device-mapper
targets. It allows to set up targets to read cryptoloop compatible
volumes as well as LUKS formatted ones. The package additionally
includes support for automatically setting up encrypted volumes at boot
time via the config file %{_sysconfdir}/crypttab.

%package -n lib%{name}-devel
Summary:        Header files for libcryptsetup
# cryptsetup-devel last used 11.1
License:        LGPL-2.0-or-later WITH cryptsetup-OpenSSL-exception
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcryptsetup%{so_ver} = %{version}
Provides:       cryptsetup-devel = %{version}
Obsoletes:      cryptsetup-devel < %{version}

%description -n lib%{name}-devel
cryptsetup is used to conveniently set up dm-crypt based device-mapper
targets. It allows to set up targets to read cryptoloop compatible
volumes as well as LUKS formatted ones. The package additionally
includes support for automatically setting up encrypted volumes at boot
time via the config file %{_sysconfdir}/crypttab.

%prep
%autosetup -p1
cp -v %{SOURCE4} .

%build
# force regeneration of manual pages from AsciiDoc
rm -f man/*.8

%configure \
  --enable-selinux \
  --enable-fips \
  --enable-pwquality \
  --enable-gcrypt-pbkdf2 \
  --enable-libargon2 \
%if %{?suse_version} < 1550
  --with-default-luks-format=LUKS1 \
%endif
  --with-luks2-lock-path=/run/cryptsetup \
  --with-tmpfilesdir='%{_tmpfilesdir}'
%make_build

%install

%make_install
%if 0%{?suse_version} < 1550
install -dm 0755 %{buildroot}/sbin
ln -s ..%{_sbindir}/cryptsetup %{buildroot}/sbin
%endif
# don't want this file in /lib (FHS compat check), and can't move it to /usr/lib
find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %{name} --all-name

%fdupes -s %{buildroot}%{_mandir}/man8

%check
%make_build check

%post
%{?regenerate_initrd_post}
%tmpfiles_create %{_tmpfilesdir}/cryptsetup.conf

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%ldconfig_scriptlets -n libcryptsetup%{so_ver}

%files
%license COPYING*
%if 0%{?suse_version} < 1550
/sbin/cryptsetup
%endif
%{_sbindir}/cryptsetup
%{_sbindir}/veritysetup
%{_sbindir}/integritysetup
%{_tmpfilesdir}/cryptsetup.conf
%ghost %attr(700, -, -) %dir /run/cryptsetup

%files lang -f %{name}.lang
%license COPYING*

%files -n libcryptsetup%{so_ver}
%license COPYING*
%{_libdir}/libcryptsetup.so.%{so_ver}*

%files -n lib%{name}-devel
%license COPYING*
%doc docs/examples/
%{_includedir}/libcryptsetup.h
%{_libdir}/libcryptsetup.so
%{_libdir}/pkgconfig/*

%files ssh
%license COPYING*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libcryptsetup-token-ssh.so
%{_mandir}/man8/cryptsetup-ssh.8%{?ext_man}
%{_sbindir}/cryptsetup-ssh

%files doc
%license COPYING*
%license cc-by-sa-4.0.txt
%doc AUTHORS FAQ.md README.md docs/*ReleaseNotes docs/on-disk-format*.pdf
%{_mandir}/man8/cryptsetup.8%{?ext_man}
%{_mandir}/man8/cryptsetup-benchmark.8%{?ext_man}
%{_mandir}/man8/cryptsetup-bitlkDump.8%{?ext_man}
%{_mandir}/man8/cryptsetup-bitlkOpen.8%{?ext_man}
%{_mandir}/man8/cryptsetup-close.8%{?ext_man}
%{_mandir}/man8/cryptsetup-config.8%{?ext_man}
%{_mandir}/man8/cryptsetup-convert.8%{?ext_man}
%{_mandir}/man8/cryptsetup-create.8%{?ext_man}
%{_mandir}/man8/cryptsetup-erase.8%{?ext_man}
%{_mandir}/man8/cryptsetup-isLuks.8%{?ext_man}
%{_mandir}/man8/cryptsetup-loopaesOpen.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksAddKey.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksChangeKey.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksConvertKey.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksDump.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksErase.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksFormat.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksHeaderBackup.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksHeaderRestore.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksKillSlot.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksOpen.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksRemoveKey.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksResume.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksSuspend.8%{?ext_man}
%{_mandir}/man8/cryptsetup-luksUUID.8%{?ext_man}
%{_mandir}/man8/cryptsetup-open.8%{?ext_man}
%{_mandir}/man8/cryptsetup-plainOpen.8%{?ext_man}
%{_mandir}/man8/cryptsetup-reencrypt.8%{?ext_man}
%{_mandir}/man8/cryptsetup-refresh.8%{?ext_man}
%{_mandir}/man8/cryptsetup-repair.8%{?ext_man}
%{_mandir}/man8/cryptsetup-resize.8%{?ext_man}
%{_mandir}/man8/cryptsetup-status.8%{?ext_man}
%{_mandir}/man8/cryptsetup-tcryptDump.8%{?ext_man}
%{_mandir}/man8/cryptsetup-tcryptOpen.8%{?ext_man}
%{_mandir}/man8/cryptsetup-token.8%{?ext_man}
%{_mandir}/man8/integritysetup.8%{?ext_man}
%{_mandir}/man8/veritysetup.8%{?ext_man}
%{_mandir}/man8/cryptsetup-fvault2Dump.8%{?ext_man}
%{_mandir}/man8/cryptsetup-fvault2Open.8%{?ext_man}

%changelog
