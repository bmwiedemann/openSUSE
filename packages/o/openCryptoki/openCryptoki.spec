#
# spec file for package openCryptoki
#
# Copyright (c) 2018-2022 SUSE LLC
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


%define openCryptoki_32bit_arch %{ix86} s390 ppc %{arm}
# support in the workings for: ppc64
# no support in sight for: ia64
%define openCryptoki_64bit_arch s390x ppc64 ppc64le x86_64 aarch64
# autobuild:/work/cd/lib/misc/group
#   openCryptoki    pkcs11:x:64:
%define pkcs11_group_id 64
%define oc_cvs_tag opencryptoki

Name:           openCryptoki
Version:        3.19.0
Release:        0
Summary:        An Implementation of PKCS#11 (Cryptoki) v2.11 for IBM Cryptographic Hardware
License:        CPL-1.0
Group:          Productivity/Security
URL:            https://github.com/opencryptoki/opencryptoki
Source:         https://github.com/opencryptoki/%{oc_cvs_tag}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        openCryptoki.pkcsslotd
Source2:        openCryptoki-TFAQ.html
Source3:        openCryptoki-rpmlintrc
# Patch 1 is needed because group pkcs11 doesn't exist in the build environment
# and because we don't want(?) various file and directory permissions to be 0700.
Patch1:         ocki-3.19-remove-make-install-chgrp.patch
BuildRequires:  bison
BuildRequires:  dos2unix
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libitm1
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel >= 1.0
BuildRequires:  pkgconfig
BuildRequires:  trousers-devel
BuildRequires:  pkgconfig(systemd)
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/usermod

# IBM maintains openCryptoki on these architectures:
ExclusiveArch:  %{openCryptoki_32bit_arch} %{openCryptoki_64bit_arch}
%{?systemd_requires}
%ifarch s390 s390x
BuildRequires:  libica-devel
BuildRequires:  libica-tools
%endif

%description
The PKCS#11 version 2.11 API implemented for the IBM cryptographic
cards. This package includes support for the IBM 4758 cryptographic
coprocessor (with the PKCS#11 firmware loaded) and the IBM eServer
Cryptographic Accelerator (FC 4960 on pSeries).

%package devel
Summary:        Development files for openCryptoki, a PKCS#11 implementation for IBM hardware
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libopenssl-devel
Requires:       openldap2-devel
Requires:       trousers-devel
%ifarch s390 s390x
Requires:       libica-devel
%endif

%description devel
The PKCS#11 version 2.01 API implemented for the IBM cryptographic
cards. This package includes support for the IBM 4758 cryptographic
co-processor (with the PKCS#11 firmware loaded) and the IBM eServer
Cryptographic Accelerator (FC 4960 on pSeries).

%ifarch %{openCryptoki_32bit_arch}
%package 32bit
Summary:        An Implementation of PKCS#11 (Cryptoki) v2.11 for IBM Cryptographic Hardware
# this is needed to make sure the pkcs11 group exists before
# installation:
Group:          Productivity/Security
Requires:       openCryptoki
ExclusiveArch:  %{openCryptoki_32bit_arch}

%description 32bit
This is a re-packaged binary rpm. For the package source, please look
for the source of the package without the "32bit" ending

The PKCS#11 version 2.11 API implemented for the IBM cryptographic
cards. This package includes support for the IBM 4758 cryptographic
coprocessor (with the PKCS#11 firmware loaded) and the IBM eServer
Cryptographic Accelerator (FC 4960 on pSeries).

%endif

%ifarch %{openCryptoki_64bit_arch}
%package 64bit
Summary:        An Implementation of PKCS#11 (Cryptoki) v2.11 for IBM Cryptographic Hardware
# this is needed to make sure the pkcs11 group exists before
# installation:
Group:          Productivity/Security
Requires:       openCryptoki
ExclusiveArch:  %{openCryptoki_64bit_arch}

%description 64bit
This is a re-packaged binary rpm. For the package source, please look
for the source of the package without the "64bit" ending

The PKCS#11 version 2.11 API implemented for the IBM cryptographic
cards. This package includes support for the IBM 4758 cryptographic
coprocessor (with the PKCS#11 firmware loaded) and the IBM eServer
Cryptographic Accelerator (FC 4960 on pSeries).

%endif

%prep
%setup -q -n %{oc_cvs_tag}-%{version}
%patch1 -p1

cp %{SOURCE2} .

%build
./bootstrap.sh

%configure --with-systemd=%{_unitdir} \
    --with-libudev=yes \
    --enable-tpmtok \
%ifarch aarch64  # Apparently, gcc for aarch64 doesn't support transactional memory
    --enable-locks \
%endif
%ifarch s390 s390x
    --enable-pkcsep11_migrate
%else
    --disable-ccatok
%endif

make %{?_smp_mflags}
dos2unix doc/README.ep11_stdll

%install
%make_install
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_localstatedir}/lib/opencryptoki
install -d %{buildroot}%{_initddir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_prefix}/lib/tmpfiles.d
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcpkcsslotd
rm -rf %{buildroot}/tmp

# Remove all development files
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_libdir}/opencryptoki/methods

%pre
%{service_add_pre pkcsslotd.service}
# autobuild:/work/cd/lib/misc/group
# openCryptoki    pkcs11:x:64:
%{_sbindir}/groupadd -g %{pkcs11_group_id} -r pkcs11 2>/dev/null || true
%{_sbindir}/usermod -a -G pkcs11 root

%preun
%{service_del_preun pkcsslotd.service}

%post
# Symlink from /var/lib/opencryptoki to /etc/pkcs11
if [ ! -L %{_sysconfdir}/pkcs11 ] ; then
	if [ -e %{_sysconfdir}/pkcs11/pk_config_data ] ; then
		mv %{_sysconfdir}/pkcs11/* %{_localstatedir}/lib/opencryptoki
		cd %{_sysconfdir} && rm -rf pkcs11 && \
			ln -sf %{_localstatedir}/lib/opencryptoki pkcs11
	fi
fi
/sbin/ldconfig
%{?tmpfiles_create:%tmpfiles_create %{_tmpfilesdir}/opencryptoki.conf}
%{service_add_post pkcsslotd.service}

%postun
if [ -L %{_sysconfdir}/pkcs11 ] ; then
	rm %{_sysconfdir}/pkcs11
fi
%{service_del_postun pkcsslotd.service}

%ifarch %{openCryptoki_32bit_arch}
%postun 32bit
if [ -L %{_sysconfdir}/pkcs11 ] ; then
	rm %{_sysconfdir}/pkcs11
fi
%{service_del_postun pkcsslotd.service}

%post 32bit
# Old library name links
cd %{_libdir}/opencryptoki && ln -sf ./libopencryptoki.so PKCS11_API.so
ln -sf %{_sbindir} %{_libdir}/opencryptoki/methods
rm -rf %{_libdir}/pkcs11/stdll
test -d %{_prefix}/lib/pkcs11 || mkdir -p %{_prefix}/lib/pkcs11
cd %{_prefix}/lib/pkcs11
ln -sf ../opencryptoki/stdll stdll
cd stdll
[ -f libpkcs11_cca.so ] && ln -sf ./libpkcs11_cca.so PKCS11_CCA.so || true
[ -f libpkcs11_tpm.so ] && ln -sf ./libpkcs11_tpm.so PKCS11_TPM.so || true
[ -f libpkcs11_ica.so ] && ln -sf ./libpkcs11_ica.so PKCS11_ICA.so || true
[ -f libpkcs11_sw.so ] && ln -sf ./libpkcs11_sw.so PKCS11_SW.so || true
/sbin/ldconfig
%endif

%ifarch %{openCryptoki_64bit_arch}
%post 64bit
# Old library name for 64bit libs were under /usr/lib/pkcs11. For migration purposes only.
test -d %{_prefix}/lib/pkcs11 || mkdir -p %{_prefix}/lib/pkcs11
ln -sf %{_libdir}/opencryptoki/libopencryptoki.so %{_prefix}/lib/pkcs11/PKCS11_API.so64
/sbin/ldconfig
%endif

%files
%doc openCryptoki-TFAQ.html FAQ
%doc doc/*
%dir %{_datadir}/doc/opencryptoki
%{_datadir}/doc/opencryptoki/policy-example.conf
%{_datadir}/doc/opencryptoki/strength-example.conf
  # configuration directory
%dir %{_sysconfdir}/opencryptoki
%config %{_sysconfdir}/opencryptoki/opencryptoki.conf
%config %attr(640,root,pkcs11) %{_sysconfdir}/opencryptoki/strength.conf
%config %attr(640,root,pkcs11) %{_sysconfdir}/opencryptoki/p11sak_defined_attrs.conf
%ifarch s390 s390x
%config %{_sysconfdir}/opencryptoki/ccatok.conf
%config %{_sysconfdir}/opencryptoki/ep11cpfilter.conf
%config %{_sysconfdir}/opencryptoki/ep11tok.conf
%{_sbindir}/pkcsep11_migrate
%endif
%{_sbindir}/p11sak
%{_unitdir}/pkcsslotd.service
%{_tmpfilesdir}/opencryptoki.conf
%{_sbindir}/rcpkcsslotd
  # utilities
%ifarch s390 s390x
%{_sbindir}/pkcsep11_session
%{_sbindir}/pkcscca
%endif
%{_sbindir}/pkcsslotd
%{_sbindir}/pkcsconf
%{_sbindir}/pkcsicsf
%{_sbindir}/pkcsstats
%{_sbindir}/pkcstok_migrate
%dir %{_libdir}/opencryptoki
%dir %{_libdir}/opencryptoki/stdll
  # State and lock directories
%dir %attr(755,root,pkcs11) %{_localstatedir}/lib/opencryptoki
%ifarch s390 s390x
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/ccatok
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/ccatok/TOK_OBJ
%endif
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/swtok
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/swtok/TOK_OBJ
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/tpm
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/icsf
%ifarch s390 s390x
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/ep11tok
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/ep11tok/TOK_OBJ
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/lite
%dir %attr(770,root,pkcs11) %{_localstatedir}/lib/opencryptoki/lite/TOK_OBJ
%endif
%dir %attr(770,root,pkcs11) %{_localstatedir}/log/opencryptoki/
%{_mandir}/man*/*

%files devel
%dir %{_libdir}/opencryptoki
%dir %{_libdir}/opencryptoki/stdll
%{_includedir}/opencryptoki
%{_libdir}/pkgconfig/opencryptoki.pc

%ifarch %{openCryptoki_32bit_arch}
%files 32bit
  # these don't conflict because they only exist as 64bit binaries if
  # there is no 32bit version of them usable
%{_libdir}/opencryptoki/libopencryptoki.so
%ghost %{_libdir}/opencryptoki/PKCS11_API.so
%{_libdir}/opencryptoki/*.0
%ifarch s390
%{_libdir}/opencryptoki/stdll/libpkcs11_cca.so
%ghost %{_libdir}/opencryptoki/stdll/PKCS11_CCA.so
%endif
%{_libdir}/opencryptoki/stdll/libpkcs11_tpm.so
%ghost %{_libdir}/opencryptoki/stdll/PKCS11_TPM.so
%{_libdir}/opencryptoki/stdll/libpkcs11_sw.so
%ghost %{_libdir}/opencryptoki/stdll/PKCS11_SW.so
%{_libdir}/opencryptoki/stdll/libpkcs11_icsf.so
%ghost %{_libdir}/opencryptoki/stdll/PKCS11_ICSF.so
%ifarch s390 s390x
%{_libdir}/opencryptoki/stdll/libpkcs11_ica.so
%ghost %{_libdir}/opencryptoki/stdll/PKCS11_ICA.so
%{_libdir}/opencryptoki/stdll/libpkcs11_ep11.so
%ghost %{_libdir}/opencryptoki/stdll/PKCS11_EP11.so
%endif
%{_libdir}/opencryptoki/stdll/*.0
%dir %{_libdir}/pkcs11
%ghost %{_libdir}/pkcs11/stdll
%ghost %{_libdir}/pkcs11/methods
%{_libdir}/pkcs11/*.so
%{_sysconfdir}/ld.so.conf.d/*
%endif

%ifarch %{openCryptoki_64bit_arch}
%files 64bit
%dir %{_libdir}/opencryptoki
%{_libdir}/opencryptoki/*.so
%{_libdir}/opencryptoki/*.0
%dir %{_libdir}/opencryptoki/stdll
%{_libdir}/opencryptoki/stdll/*.so
%{_libdir}/opencryptoki/stdll/*.0
%{_libdir}/pkcs11
%{_sysconfdir}/ld.so.conf.d/*
%endif

%changelog
