#
# spec file for package openssl-3
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


%define ssletcdir %{_sysconfdir}/ssl
%define sover 3
%define _rname openssl
%define man_suffix 3ssl
Name:           openssl-3
# Don't forget to update the version in the "openssl" meta-package!
Version:        3.0.7
Release:        0
Summary:        Secure Sockets and Transport Layer Security
License:        Apache-2.0
URL:            https://www.openssl.org/
Source:         https://www.%{_rname}.org/source/%{_rname}-%{version}.tar.gz
# to get mtime of file:
Source1:        %{name}.changes
Source2:        baselibs.conf
Source3:        https://www.%{_rname}.org/source/%{_rname}-%{version}.tar.gz.asc
# https://www.openssl.org/about/
# http://pgp.mit.edu:11371/pks/lookup?op=get&search=0xA2D29B7BF295C759#/openssl.keyring
Source4:        %{_rname}.keyring
Source5:        showciphers.c
# PATCH-FIX-OPENSUSE: Do not install html docs as it takes ages
Patch1:         openssl-no-html-docs.patch
Patch2:         openssl-truststore.patch
Patch3:         openssl-pkgconfig.patch
Patch4:         openssl-DEFAULT_SUSE_cipher.patch
Patch5:         openssl-ppc64-config.patch
Patch6:         openssl-no-date.patch
# Add crypto-policies support
Patch7:         openssl-Add-support-for-PROFILE-SYSTEM-system-default-cipher.patch
Patch8:         openssl-Override-default-paths-for-the-CA-directory-tree.patch
# PATCH-FIX-UPSTREAM bsc#1206374 CVE-2022-3996 X.509 Policy Constraints Double Locking
Patch9:         openssl-3-Fix-double-locking-problem.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
Requires:       libopenssl3 = %{version}-%{release}
Requires:       openssl
Conflicts:      ssl
Provides:       ssl
Provides:       openssl(cli)
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       crypto-policies
%endif
# Needed for clean upgrade path, boo#1070003
Obsoletes:      openssl-1_0_0
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      openssl-1_1_0

%description
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl3
Summary:        Secure Sockets and Transport Layer Security
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       crypto-policies
%endif
Recommends:     ca-certificates-mozilla
# install libopenssl and libopenssl-hmac close together (bsc#1090765)
Suggests:       libopenssl3-hmac = %{version}-%{release}
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0
Conflicts:      %{name} < %{version}-%{release}

%description -n libopenssl3
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl-3-devel
Summary:        Development files for OpenSSL
Requires:       libopenssl3 = %{version}
Requires:       pkgconfig(zlib)
Recommends:     %{name} = %{version}
Conflicts:      libressl-devel
# Conflicting names with libopenssl-1_1-devel
Conflicts:      libopenssl-1_1-devel
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl-1_1_0-devel
# Needed for clean upgrade from SLE-12 openssl-1_0_0, bsc#1158499
Obsoletes:      libopenssl-1_0_0-devel

%description -n libopenssl-3-devel
This subpackage contains header files for developing applications
that want to make use of the OpenSSL C API.

%package doc
Summary:        Additional Package Documentation
Conflicts:      openssl-doc
Provides:       openssl-doc = %{version}
Obsoletes:      openssl-doc < %{version}
BuildArch:      noarch

%description doc
This package contains optional documentation provided in addition to
this package's base documentation.

%package -n libopenssl3-hmac
Summary:        HMAC files for FIPS 140-3 integrity checking of the openssl shared libraries
License:        BSD-3-Clause
Requires:       libopenssl3 = %{version}-%{release}
BuildRequires:  fipscheck
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0-hmac
# Needed for clean upgrade from SLE-12 openssl-1_0_0, bsc#1158499
Obsoletes:      libopenssl-1_0_0-hmac

%description -n libopenssl3-hmac
The FIPS compliant operation of the openssl shared libraries is NOT
possible without the HMAC hashes contained in this package!

%prep
%autosetup -p1 -n %{_rname}-%{version}

%build
%ifarch armv5el armv5tel
export MACHINE=armv5el
%endif
%ifarch armv6l armv6hl
export MACHINE=armv6l
%endif

./config \
    no-mdc2 no-ec2m no-sm2 no-sm4 \
    enable-rfc3779 enable-camellia enable-seed \
%ifarch x86_64 aarch64 ppc64le
    enable-ec_nistp_64_gcc_128 \
%endif
    enable-fips \
    zlib \
    --prefix=%{_prefix} \
    --libdir=%{_lib} \
    --openssldir=%{ssletcdir} \
    %{optflags} \
    -Wa,--noexecstack \
    -Wl,-z,relro,-z,now \
    -fno-common \
    -DTERMIO \
    -DPURIFY \
    -D_GNU_SOURCE \
    -DOPENSSL_NO_BUF_FREELISTS \
    $(getconf LFS_CFLAGS) \
    -Wall \
    --with-rand-seed=getrandom \
    --system-ciphers-file=%{_sysconfdir}/crypto-policies/back-ends/openssl.config

# Show build configuration
perl configdata.pm --dump

# Do not run this in a production package the FIPS symbols must be patched-in
# util/mkdef.pl crypto update

%make_build depend
%make_build all

%check
# Relax the crypto-policies requirements for the regression tests
# Revert patch8 before running tests
patch -p1 -R < %{P:8}
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=xyz_nonexistent_file

export MALLOC_CHECK_=3
export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
# export HARNESS_VERBOSE=yes
LD_LIBRARY_PATH="$PWD" make test -j16

# show ciphers
gcc -o showciphers %{optflags} -I%{buildroot}%{_includedir} %{SOURCE5} -L%{buildroot}%{_libdir} -lssl -lcrypto
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./showciphers

%install
%make_install %{?_smp_mflags} MANSUFFIX=%{man_suffix}

rename so.%{sover} so.%{version} %{buildroot}%{_libdir}/*.so.%{sover}
for lib in %{buildroot}%{_libdir}/*.so.%{version} ; do
    chmod 755 ${lib}
    ln -sf $(basename ${lib}) %{buildroot}%{_libdir}/$(basename ${lib} .%{version})
    ln -sf $(basename ${lib}) %{buildroot}%{_libdir}/$(basename ${lib} .%{version}).%{sover}
done

# Remove static libraries
rm -f %{buildroot}%{_libdir}/lib*.a

# Remove the cnf.dist
rm -f %{buildroot}%{ssletcdir}/openssl.cnf.dist
rm -f %{buildroot}%{ssletcdir}/ct_log_list.cnf.dist

# Make a copy of the default openssl.cnf file
cp %{buildroot}%{ssletcdir}/openssl.cnf %{buildroot}%{ssletcdir}/openssl-orig.cnf

# Create openssl ca-certificates dir required by nodejs regression tests [bsc#1207484]
mkdir -p %{buildroot}/var/lib/ca-certificates/openssl
install -d -m 555 %{buildroot}/var/lib/ca-certificates/openssl

# Remove the fipsmodule.cnf because FIPS module is loaded automatically
rm -f %{buildroot}%{ssletcdir}/fipsmodule.cnf

ln -sf ./%{_rname} %{buildroot}/%{_includedir}/ssl
mkdir %{buildroot}/%{_datadir}/ssl
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl/

# Avoid file conflicts with man pages from other packages
pushd %{buildroot}/%{_mandir}
find . -type f -exec chmod 644 {} +
mv man5/config.5%{man_suffix} man5/openssl.cnf.5
popd

# Do not install demo scripts executable under /usr/share/doc
find demos -type f -perm /111 -exec chmod 644 {} +

# Place showciphers.c for %%doc macro
cp %{SOURCE5} .

# Compute the FIPS hmac using the brp-50-generate-fips-hmac script
export BRP_FIPSHMAC_FILES="%{buildroot}%{_libdir}/libssl.so.%{sover} %{buildroot}%{_libdir}/libcrypto.so.%{sover}"

%post -p "/bin/bash"
if [ "$1" -gt 1 ] ; then
    # Check if the packaged default config file for openssl-3, called openssl.cnf,
    # is the original or if it has been modified and alert the user in that case
    # that a copy of the original file openssl-orig.cnf can be used if needed.
    cmp --silent %{ssletcdir}/openssl.cnf %{ssletcdir}/openssl-orig.cnf 2>/dev/null
    if [ "$?" -eq 1 ] ; then
        echo -e " The openssl-3 default config file openssl.cnf is different from" ;
        echo -e " the original one shipped by the package. A copy of the original" ;
        echo -e " file is packaged and named as openssl-orig.cnf if needed."
    fi
fi

%post -n libopenssl3 -p /sbin/ldconfig
%postun -n libopenssl3 -p /sbin/ldconfig

%files -n libopenssl3
%license LICENSE.txt
%attr(0755,root,root) %{_libdir}/libssl.so.%{version}
%{_libdir}/libssl.so.%{sover}
%attr(0755,root,root) %{_libdir}/libcrypto.so.%{version}
%{_libdir}/libcrypto.so.%{sover}
%{_libdir}/engines-%{sover}
%dir %{_libdir}/ossl-modules
%{_libdir}/ossl-modules/fips.so
%{_libdir}/ossl-modules/legacy.so

%files -n libopenssl3-hmac
%{_libdir}/.libssl.so.%{sover}.hmac
%{_libdir}/.libcrypto.so.%{sover}.hmac

%files -n libopenssl-3-devel
%doc NOTES*.md CONTRIBUTING.md HACKING.md AUTHORS.md ACKNOWLEDGEMENTS.md
%{_includedir}/%{_rname}/
%{_includedir}/ssl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%files doc
%doc README.md
%doc doc/html/* doc/HOWTO/* demos
%doc showciphers.c

%files
%license LICENSE.txt
%doc CHANGES.md NEWS.md FAQ.md README.md
%dir %{ssletcdir}
%config %{ssletcdir}/openssl-orig.cnf
%config (noreplace) %{ssletcdir}/openssl.cnf
%config (noreplace) %{ssletcdir}/ct_log_list.cnf
%attr(700,root,root) %{ssletcdir}/private
%dir %{_datadir}/ssl
%{_datadir}/ssl/misc
%dir /var/lib/ca-certificates/
%dir /var/lib/ca-certificates/openssl
%{_bindir}/%{_rname}
%{_bindir}/c_rehash
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%changelog
