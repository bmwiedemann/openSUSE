#
# spec file for package openssl-1_1
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define maj_min 1.1
%define _rname  openssl
Name:           openssl-1_1
# Don't forget to update the version in the "openssl" package!
Version:        1.1.1d
Release:        0
Summary:        Secure Sockets and Transport Layer Security
License:        OpenSSL
Group:          Productivity/Networking/Security
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
# PATCH-FIX-OPENSUSE: do not install html mans it takes ages
Patch1:         openssl-1.1.0-no-html.patch
Patch2:         openssl-truststore.patch
Patch3:         openssl-pkgconfig.patch
Patch4:         openssl-DEFAULT_SUSE_cipher.patch
Patch5:         openssl-ppc64-config.patch
Patch6:         openssl-no-date.patch
# PATCH-FIX-UPSTREAM jsc#SLE-6126 and jsc#SLE-6129
Patch8:         0001-s390x-assembly-pack-perlasm-support.patch
Patch9:         0002-crypto-chacha-asm-chacha-s390x.pl-add-vx-code-path.patch
Patch10:        0003-crypto-poly1305-asm-poly1305-s390x.pl-add-vx-code-pa.patch
Patch11:        0004-s390x-assembly-pack-fix-formal-interface-bug-in-chac.patch
Patch12:        0005-s390x-assembly-pack-import-chacha-from-cryptogams-re.patch
Patch13:        0006-s390x-assembly-pack-import-poly-from-cryptogams-repo.patch
Patch14:        openssl-jsc-SLE-8789-backport_KDF.patch
BuildRequires:  pkgconfig
Conflicts:      ssl
Provides:       ssl
Provides:       openssl(cli)
# Needed for clean upgrade path, boo#1070003
Obsoletes:      openssl-1_0_0
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      openssl-1_1_0

%description
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl1_1
Summary:        Secure Sockets and Transport Layer Security
Group:          Productivity/Networking/Security
Recommends:     ca-certificates-mozilla
# install libopenssl and libopenssl-hmac close together (bsc#1090765)
Suggests:       libopenssl1_1-hmac = %{version}-%{release}
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl1_1_0

%description -n libopenssl1_1
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl-1_1-devel
Summary:        Development files for OpenSSL
Group:          Development/Libraries/C and C++
Requires:       libopenssl1_1 = %{version}
Recommends:     %{name} = %{version}
# we need to have around only the exact version we are able to operate with
Conflicts:      libopenssl-devel < %{version}
Conflicts:      libopenssl-devel > %{version}
Conflicts:      ssl-devel
Provides:       ssl-devel
# Needed for clean upgrade from former openssl-1_1_0, boo#1081335
Obsoletes:      libopenssl-1_1_0-devel

%description -n libopenssl-1_1-devel
This subpackage contains header files for developing applications
that want to make use of the OpenSSL C API.

%package doc
Summary:        Additional Package Documentation
Group:          Productivity/Networking/Security
Conflicts:      openssl-doc
Provides:       openssl-doc = %{version}
Obsoletes:      openssl-doc < %{version}
BuildArch:      noarch

%description doc
This package contains optional documentation provided in addition to
this package's base documentation.

%prep
%setup -q -n %{_rname}-%{version}
%autopatch -p1

%build
%ifarch armv5el armv5tel
export MACHINE=armv5el
%endif
%ifarch armv6l armv6hl
export MACHINE=armv6l
%endif

./config \
    no-idea \
    enable-rfc3779 \
%ifarch x86_64 aarch64 ppc64le
    enable-ec_nistp_64_gcc_128 \
%endif
    enable-camellia \
    no-ec2m \
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
    --with-rand-seed=getrandom

# Show build configuration
perl configdata.pm --dump

util/mkdef.pl crypto update
make depend %{?_smp_mflags}
make all %{?_smp_mflags}

%check
export MALLOC_CHECK_=3
export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
LD_LIBRARY_PATH=`pwd` make test -j1
# show cyphers
gcc -o showciphers %{optflags} -I%{buildroot}%{_includedir} %{SOURCE5} -L%{buildroot}%{_libdir} -lssl -lcrypto
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./showciphers

%install
%make_install %{?_smp_mflags}
# kill static libs
rm -f %{buildroot}%{_libdir}/lib*.a
# remove the cnf.dist
rm -f %{buildroot}%{_sysconfdir}/ssl/openssl.cnf.dist
ln -sf ./%{_rname} %{buildroot}/%{_includedir}/ssl
mkdir %{buildroot}/%{_datadir}/ssl
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl/

# avoid file conflicts with man pages from other packages
#
set +x
pushd %{buildroot}/%{_mandir}
# some man pages now contain spaces. This makes several scripts go havoc, among them /usr/sbin/Check.
# replace spaces by underscores
#for i in man?/*\ *; do mv -v "$i" "${i// /_}"; done
which readlink &>/dev/null || function readlink { ( set +x; target=$(file $1 2>/dev/null); target=${target//* }; test -f $target && echo $target; ) }
for i in man?/*; do
	if test -L $i ; then
	    LDEST=`readlink $i`
	    rm -f $i ${i}ssl
	    ln -sf ${LDEST}ssl ${i}ssl
	else
	    mv $i ${i}ssl
        fi
	case "$i" in
	    *.1)
		# these are the pages mentioned in openssl(1). They go into the main package.
		echo %doc %{_mandir}/${i}ssl%{?ext_man} >> $OLDPWD/filelist;;
	    *)
		# the rest goes into the openssl-doc package.
		echo %doc %{_mandir}/${i}ssl%{?ext_man} >> $OLDPWD/filelist.doc;;
	esac
done
popd
set -x

# Do not install demo scripts executable under /usr/share/doc
find demos -type f -perm /111 -exec chmod 644 {} \;

# Place showciphers.c for %doc macro
cp %{SOURCE5} .

%post -n libopenssl1_1 -p /sbin/ldconfig
%postun -n libopenssl1_1 -p /sbin/ldconfig

%files -n libopenssl1_1
%license LICENSE
%{_libdir}/libssl.so.%{maj_min}
%{_libdir}/libcrypto.so.%{maj_min}
%{_libdir}/engines-%{maj_min}

%files -n libopenssl-1_1-devel
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
%doc CHANGE* NEWS README
%dir %{ssletcdir}
%config (noreplace) %{ssletcdir}/openssl.cnf
%attr(700,root,root) %{ssletcdir}/private
%{ssletcdir}/ct_log_list.cnf
%{ssletcdir}/ct_log_list.cnf.dist

%dir %{_datadir}/ssl
%{_datadir}/ssl/misc
%{_bindir}/c_rehash
%{_bindir}/%{_rname}

%changelog
