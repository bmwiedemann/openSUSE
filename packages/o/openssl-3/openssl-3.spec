#
# spec file for package openssl-3
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


%define ssletcdir %{_sysconfdir}/ssl
%define sover 3
%define _rname  openssl
Name:           openssl-3
# Don't forget to update the version in the "openssl" package!
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
# PATCH-FIX-OPENSUSE: do not install html mans as it takes ages
Patch1:         openssl-1.1.0-no-html.patch
Patch2:         openssl-truststore.patch
Patch3:         openssl-pkgconfig.patch
Patch4:         openssl-DEFAULT_SUSE_cipher.patch
Patch5:         openssl-ppc64-config.patch
Patch6:         openssl-no-date.patch
# Patches for crypto-policies
Patch7:         openssl-Add-support-for-PROFILE-SYSTEM-system-default-cipher.patch
Patch8:         openssl-Override-default-paths-for-the-CA-directory-tree.patch
# use openssl3.cnf
Patch9:         openssl-use-versioned-config.patch
Patch10:        fix-config-in-tests.patch
# PATCH-FIX-UPSTREAM bsc#1206374 CVE-2022-3996 X.509 Policy Constraints Double Locking
Patch11:        openssl-3-Fix-double-locking-problem.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
# Add requires for ct_log_list.cnf{,.dist}
Requires:       openssl
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       crypto-policies
%endif

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
# We need to have around only the exact version we are able to operate with
Conflicts:      libopenssl-devel < %{version}
Conflicts:      libopenssl-devel > %{version}
Conflicts:      libressl-devel
Conflicts:      ssl-devel

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
    no-idea \
    no-ec2m \
    enable-rfc3779 \
%ifarch x86_64 aarch64 ppc64le
    enable-ec_nistp_64_gcc_128 \
%endif
    enable-camellia \
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

# util/mkdef.pl crypto update
%make_build depend
%make_build all

%check

# We must revert patch8 before running tests, otherwise they will fail.
patch -p1 -R < %{P:8}

export MALLOC_CHECK_=3
export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
# export HARNESS_VERBOSE=yes
LD_LIBRARY_PATH="$PWD" make TESTS='-test_evp_fetch_prov -test_tsa -test_ssl_new -test_sslapi' test -j1
# show ciphers
gcc -o showciphers %{optflags} -I%{buildroot}%{_includedir} %{SOURCE5} -L%{buildroot}%{_libdir} -lssl -lcrypto
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./showciphers

%install
%make_install %{?_smp_mflags}

# Kill static libs
rm -f %{buildroot}%{_libdir}/lib*.a
# Remove the cnf.dist
rm -f %{buildroot}%{_sysconfdir}/ssl/openssl3.cnf.dist
mkdir %{buildroot}/%{_datadir}/ssl-3
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl-3/
ln -sf ./%{_rname} %{buildroot}/%{_includedir}/ssl
mkdir %{buildroot}/%{_datadir}/ssl
# Rename binary
mv %{buildroot}%{_bindir}/%{_rname} %{buildroot}%{_bindir}/%{name}
# Avoid file conflicts with man pages from other packages
pushd %{buildroot}/%{_mandir}
find . -type f -exec chmod 644 {} +
# Some man pages now contain spaces. This makes several
# scripts go havoc, among them /usr/sbin/Check.
# Replace spaces by underscores
# for i in man?/*\ *; do mv -v "$i" "${i// /_}"; done

touch $OLDPWD/filelist.doc $OLDPWD/filelist
which readlink &>/dev/null || function readlink { ( set +x; target=$(file $1 2>/dev/null); target=${target//* }; test -f $target && echo $target; ) }
for i in man?/*; do
  if test -L $i ; then
    LDEST=`readlink $i`
    rm -f $i ${i}ssl
    ln -sf ${LDEST}ssl-3 ${i}ssl-3
  else
    mv $i ${i}ssl-3
  fi
  case "$i" in
    *.1)
      # These are the pages mentioned in openssl(1). They go into the main package.
      echo %doc %{_mandir}/${i}ssl-3%{?ext_man} >> $OLDPWD/filelist;;
    *)
      # The rest goes into the openssl-doc package.
      echo %doc %{_mandir}/${i}ssl-3%{?ext_man} >> $OLDPWD/filelist.doc;;
  esac
done
popd

mv %{buildroot}%{_bindir}/c_rehash %{buildroot}%{_bindir}/c_rehash-3

# They are provided by openssl package
rm %{buildroot}%{ssletcdir}/ct_log_list.cnf*

# Do not install demo scripts executable under /usr/share/doc
find demos -type f -perm /111 -exec chmod 644 {} +

# Place showciphers.c for %%doc macro
cp %{SOURCE5} .

%post -n libopenssl3 -p /sbin/ldconfig
%postun -n libopenssl3 -p /sbin/ldconfig

%files -n libopenssl3
%license LICENSE.txt
%{_libdir}/libssl.so.%{sover}
%{_libdir}/libcrypto.so.%{sover}
%{_libdir}/engines-%{sover}
%dir %{_libdir}/ossl-modules
#%%{_libdir}/ossl-modules/fips.so
%{_libdir}/ossl-modules/legacy.so

%files -n libopenssl-3-devel
%{_includedir}/%{_rname}/
%{_includedir}/ssl
%{_libdir}/libssl.so
%{_libdir}/libcrypto.so
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/openssl.pc

%files doc -f filelist.doc
%doc doc/* demos
%doc showciphers.c

%files -f filelist
%doc CHANGE*
%dir %{ssletcdir}
%config (noreplace) %{ssletcdir}/openssl3.cnf
%attr(700,root,root) %{ssletcdir}/private

%dir %{_datadir}/ssl-3
%{_datadir}/ssl-3/misc
%{_bindir}/c_rehash-3
%{_bindir}/%{name}

%changelog
