#
# spec file for package openCryptoki
#
# Copyright (c) 2026 SUSE LLC
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
%define openCryptoki_64bit_arch s390x ppc64 ppc64le x86_64 aarch64 riscv64
# autobuild:/work/cd/lib/misc/group
#   openCryptoki    pkcs11:x:64:
%define pkcs11_group_id 64
%define pkcs_group pkcs11
%define oc_cvs_tag opencryptoki

%ifarch s390 s390x
    %define ocki_conf_flags --enable-icatok --enable-ccatok --enable-ep11tok --enable-pkcsep11_migrate
%else
    %ifnarch i586
        %define ocki_conf_flags --disable-icatok --enable-ccatok --disable-ep11tok --disable-pkcsep11_migrate --enable-pkcscca_migrate
    %else
        %define ocki_conf_flags --disable-icatok --disable-ccatok --disable-ep11tok --disable-pkcsep11_migrate --disable-pkcscca_migrate
    %endif
%endif

Name:           openCryptoki
Version:        3.26.0
Release:        0
Summary:        An Implementation of PKCS#11 (Cryptoki) v2.11 for IBM Cryptographic Hardware
License:        CPL-1.0
Group:          Productivity/Security
URL:            https://github.com/opencryptoki/opencryptoki
Source:         https://github.com/opencryptoki/%{oc_cvs_tag}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        openCryptoki.pkcsslotd
Source2:        openCryptoki-TFAQ.html
Source3:        openCryptoki-rpmlintrc
# Patch 0 is needed because group pkcs11 doesn't exist in the build environment
# and because we don't want(?) various file and directory permissions to be 0700.
Patch000:       ocki-3.26-remove-make-install-chgrp.patch
#
Patch010:       openCryptoki-CVE-2026-22791-commit-e37e912.patch
Patch011:       openCryptoki-CVE-2026-23893-commit-5e6e4b4.patch
#
BuildRequires:  bison
BuildRequires:  dos2unix
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libitm1
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel >= 1.1.1
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  trousers-devel
BuildRequires:  pkgconfig(systemd)
###
%{?sysusers_requires}
###
Provides:       user(pkcs11)
Provides:       group(pkcs11)

# IBM maintains openCryptoki on these architectures:
ExclusiveArch:  %{openCryptoki_32bit_arch} %{openCryptoki_64bit_arch}
%{?systemd_requires}
%ifarch s390 s390x
BuildRequires:  libica-devel >= 3.3
BuildRequires:  libica-tools
%endif

%description
Opencryptoki implements the PKCS#11 specification v2.20 for a set of
cryptographic hardware, such as IBM 4764 and 4765 crypto cards, and the
Trusted Platform Module (TPM) chip. Opencryptoki also brings a software
token implementation that can be used without any cryptographic
hardware.
This package contains the Slot Daemon (pkcsslotd) and general utilities.

%package devel
Summary:        Development files for openCryptoki, a PKCS#11 implementation for IBM hardware
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libopenssl-devel >= 1.1.1
Requires:       openldap2-devel
Requires:       trousers-devel
%ifarch s390 s390x
Requires:       libica-devel >= 3.3
%endif

%description devel
The PKCS#11 version 2.01 API implemented for the IBM cryptographic
cards. This package includes support for the IBM 4758 cryptographic
co-processor (with the PKCS#11 firmware loaded) and the IBM eServer
Cryptographic Accelerator (FC 4960 on pSeries).
This package contains the development header files for building
opencryptoki and PKCS#11 based applications


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
# setup -q -n %{oc_cvs_tag}-%{version}
%autosetup -p 1 -n %{oc_cvs_tag}-%{version}

cp %{SOURCE2} .

%build
./bootstrap.sh

%configure --with-systemd=%{_unitdir} \
    --with-libudev=yes \
    --enable-tpmtok \
%ifarch aarch64  # Apparently, gcc for aarch64 doesn't support transactional memory
    --enable-locks \
%endif
    %{ocki_conf_flags}

make %{?_smp_mflags}
dos2unix doc/README.ep11_stdll

# Generate sysusers configuration and pre-install scriptlet
cat > opencryptoki-sysusers.conf <<EOF
# Type Name ID GID Home Shell
g %{pkcs_group} %{pkcs11_group_id} - -
u pkcsslotd - "openCryptoki slot daemon" /run/opencryptoki /sbin/nologin
m pkcsslotd %{pkcs_group}
m root %{pkcs_group}
EOF
%sysusers_generate_pre opencryptoki-sysusers.conf opencryptoki opencryptoki.conf

%install
%make_install
install -d %{buildroot}%{_includedir}

# Define the sysusers.d configuration
install -d %{buildroot}%{_sysusersdir}

# Install the sysusers configuration
install -D -m 0644 opencryptoki-sysusers.conf %{buildroot}%{_sysusersdir}/opencryptoki.conf

# Move data templates from /var to /usr/share/opencryptoki for tmpfiles to use
install -d %{buildroot}%{_datadir}/opencryptoki/templates
install -d %{buildroot}%{_initddir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_prefix}/lib/tmpfiles.d
#
# Define the tmpfiles.d configuration
#
cat > %{buildroot}%{_prefix}/lib/tmpfiles.d/opencryptoki.conf <<EOF
# Type Path        Mode UID  GID  Age Argument
d /run/opencryptoki 0710 pkcsslotd pkcs11 - -
d /var/lib/opencryptoki 0755 root pkcs11 - -
d /var/lib/opencryptoki/swtok 0770 root pkcs11 - -
d /var/lib/opencryptoki/swtok/TOK_OBJ 0770 root pkcs11 - -
d /var/lib/opencryptoki/tpm 0770 root pkcs11 - -
d /var/lib/opencryptoki/icsf 0770 root pkcs11 - -
d /var/lib/opencryptoki/HSM_MK_CHANGE 0770 root pkcs11 - -
d /var/lock/opencryptoki 0770 root pkcs11 - -
d /var/lock/opencryptoki/swtok 0770 root pkcs11 - -
d /var/lock/opencryptoki/tpm 0770 root pkcs11 - -
d /var/lock/opencryptoki/icsf 0770 root pkcs11 - -
EOF
#
%ifnarch i586
cat >> %{buildroot}%{_prefix}/lib/tmpfiles.d/opencryptoki.conf <<EOF
d /var/lib/opencryptoki/ccatok 0770 root pkcs11 - -
d /var/lib/opencryptoki/ccatok/TOK_OBJ 0770 root pkcs11 - -
d /var/lock/opencryptoki/ccatok 0770 root pkcs11 - -
EOF
%endif
#
%ifarch s390 s390x
cat >> %{buildroot}%{_prefix}/lib/tmpfiles.d/opencryptoki.conf <<EOF
d /var/lib/opencryptoki/ep11tok 0770 root pkcs11 - -
d /var/lib/opencryptoki/ep11tok/TOK_OBJ 0770 root pkcs11 - -
d /var/lib/opencryptoki/lite 0770 root pkcs11 - -
d /var/lib/opencryptoki/lite/TOK_OBJ 0770 root pkcs11 - -
d /var/lock/opencryptoki/ep11tok 0770 root pkcs11 - -
d /var/lock/opencryptoki/lite 0770 root pkcs11 - -
EOF
%endif
#
cat >> %{buildroot}%{_prefix}/lib/tmpfiles.d/opencryptoki.conf <<EOF
d /var/log/opencryptoki 0770 root pkcs11 - -
L+ /etc/pkcs11 - - - - /var/lib/opencryptoki
EOF

# Remove manual directory creation in %install that belongs in /var
rm -rf %{buildroot}%{_localstatedir}/lib/opencryptoki
rm -rf %{buildroot}%{_localstatedir}/log/opencryptoki
#
mkdir -p %{buildroot}%{_datadir}/opencryptoki
cp %{buildroot}%{_datadir}/doc/opencryptoki/*.conf %{buildroot}%{_datadir}/opencryptoki
#
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcpkcsslotd
rm -rf %{buildroot}/tmp
#
# Remove all development files
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_libdir}/opencryptoki/methods

# Setup 64-bit symlinks (if applicable for the arch)
%ifarch %{openCryptoki_64bit_arch}
mkdir -p %{buildroot}%{_prefix}/lib/pkcs11
ln -sf %{_libdir}/opencryptoki/libopencryptoki.so %{buildroot}%{_prefix}/lib/pkcs11/PKCS11_API.so64
%endif

# Setup 32-bit symlinks (if applicable for the arch)
%ifarch %{openCryptoki_32bit_arch}
# PKCS11_API and methods
ln -snf libopencryptoki.so %{buildroot}%{_libdir}/opencryptoki/PKCS11_API.so
ln -snf %{_sbindir} %{buildroot}%{_libdir}/opencryptoki/methods

# The stdll symlink directory
mkdir -p %{buildroot}%{_prefix}/lib/pkcs11
ln -snf ../../%{_lib}/opencryptoki/stdll %{buildroot}%{_prefix}/lib/pkcs11/stdll

# The token symlinks (created within the stdll directory)
cd %{buildroot}%{_libdir}/opencryptoki/stdll
[ -f libpkcs11_cca.so ] && ln -snf libpkcs11_cca.so PKCS11_CCA.so || true
[ -f libpkcs11_tpm.so ] && ln -snf libpkcs11_tpm.so PKCS11_TPM.so || true
[ -f libpkcs11_ica.so ] && ln -snf libpkcs11_ica.so PKCS11_ICA.so || true
[ -f libpkcs11_sw.so ]  && ln -snf libpkcs11_sw.so PKCS11_SW.so || true
[ -f libpkcs11_icsf.so ] && ln -snf libpkcs11_icsf.so PKCS11_ICSF.so || true
[ -f libpkcs11_ep11.so ] && ln -snf libpkcs11_ep11.so PKCS11_EP11.so || true
cd -
%endif

%pre -f opencryptoki.pre
%{service_add_pre pkcsslotd.service}

%preun
%{service_del_preun pkcsslotd.service}

%post
# Use the systemd-tmpfiles macro to ensure directories are created on next boot/transaction
%tmpfiles_create %{_tmpfilesdir}/opencryptoki.conf
/sbin/ldconfig
%{service_add_post pkcsslotd.service}

%postun
/sbin/ldconfig
%{service_del_postun pkcsslotd.service}

%ifarch %{openCryptoki_32bit_arch}
%post 32bit
/sbin/ldconfig

%postun 32bit
/sbin/ldconfig
%endif

%ifarch %{openCryptoki_64bit_arch}
%post 64bit
/sbin/ldconfig
%endif

%files
%doc openCryptoki-TFAQ.html FAQ
%doc doc/*
%dir %{_datadir}/doc/opencryptoki
%doc %{_datadir}/doc/opencryptoki/policy-example.conf
%doc %{_datadir}/doc/opencryptoki/strength-example.conf
%doc %{_datadir}/doc/opencryptoki/README.token_data
%doc %{_datadir}/doc/opencryptoki/opencryptoki-howto.md
%dir %{_datadir}/opencryptoki
%{_datadir}/opencryptoki/policy-example.conf
%{_datadir}/opencryptoki/strength-example.conf
  # configuration directory
%dir %{_sysconfdir}/opencryptoki
%config %{_sysconfdir}/opencryptoki/opencryptoki.conf
%config %{_sysconfdir}/opencryptoki/p11kmip.conf
%attr(0640,root,%{pkcs_group}) %config %{_sysconfdir}/opencryptoki/strength.conf
%attr(0640,root,%{pkcs_group}) %config %{_sysconfdir}/opencryptoki/p11sak_defined_attrs.conf
%ifarch s390 s390x
%config %{_sysconfdir}/opencryptoki/ep11cpfilter.conf
%config %{_sysconfdir}/opencryptoki/ep11tok.conf
%endif
%{_sbindir}/p11sak
%{_unitdir}/pkcsslotd.service
%{_tmpfilesdir}/opencryptoki.conf
%{_sbindir}/rcpkcsslotd
  # utilities
%ifarch s390 s390x
%{_sbindir}/pkcsep11_migrate
%{_sbindir}/pkcsep11_session
%endif
%ifnarch i586
%config %{_sysconfdir}/opencryptoki/ccatok.conf
%{_sbindir}/pkcscca
%endif
%{_sbindir}/p11kmip
%{_sbindir}/pkcsslotd
%{_sbindir}/pkcsconf
%{_sbindir}/pkcsicsf
%{_sbindir}/pkcsstats
%{_sbindir}/pkcstok_migrate
%{_sbindir}/pkcstok_admin
%dir %{_libdir}/opencryptoki
%dir %{_libdir}/opencryptoki/stdll
  # State and lock directories
%{_mandir}/man*/*
%{_sbindir}/pkcshsm_mk_change
#
%{_sysusersdir}/opencryptoki.conf

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
%{_libdir}/opencryptoki/PKCS11_API.so
%{_libdir}/opencryptoki/methods
%{_libdir}/opencryptoki/*.0

%ifnarch i586
%{_libdir}/opencryptoki/stdll/libpkcs11_cca.so
%{_libdir}/opencryptoki/stdll/PKCS11_CCA.so
%endif

%{_libdir}/opencryptoki/stdll/libpkcs11_tpm.so
%{_libdir}/opencryptoki/stdll/PKCS11_TPM.so
%{_libdir}/opencryptoki/stdll/libpkcs11_sw.so
%{_libdir}/opencryptoki/stdll/PKCS11_SW.so
%{_libdir}/opencryptoki/stdll/libpkcs11_icsf.so
%{_libdir}/opencryptoki/stdll/PKCS11_ICSF.so

%ifarch s390 s390x
%{_libdir}/opencryptoki/stdll/libpkcs11_ica.so
%{_libdir}/opencryptoki/stdll/PKCS11_ICA.so
%{_libdir}/opencryptoki/stdll/libpkcs11_ep11.so
%{_libdir}/opencryptoki/stdll/PKCS11_EP11.so
%endif

%{_libdir}/opencryptoki/stdll/*.0
%dir %{_prefix}/lib/pkcs11
%{_prefix}/lib/pkcs11/stdll
%{_prefix}/lib/pkcs11/methods
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

%dir %{_prefix}/lib/pkcs11
%{_prefix}/lib/pkcs11/PKCS11_API.so64

%{_libdir}/pkcs11
%{_sysconfdir}/ld.so.conf.d/*
%endif

%changelog
