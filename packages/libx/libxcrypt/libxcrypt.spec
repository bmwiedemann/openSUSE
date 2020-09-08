#
# spec file for package libxcrypt
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


Name:           libxcrypt
Version:        4.4.17
Release:        0
Summary:        Extended crypt library for DES, MD5, Blowfish and others
License:        GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            https://github.com/besser82/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libxcrypt is a modern library for one-way hashing of passwords.  It
supports DES, MD5, SHA-2-256, SHA-2-512, and bcrypt-based password
hashes, and provides the traditional Unix 'crypt' and 'crypt_r'
interfaces, as well as a set of extended interfaces pioneered by
Openwall Linux, 'crypt_rn', 'crypt_ra', 'crypt_gensalt',
'crypt_gensalt_rn', and 'crypt_gensalt_ra'.

%package -n libcrypt1
Summary:        Extended crypt library for DES, MD5, Blowfish and others
License:        LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND SUSE-Public-Domain
Group:          System/Libraries
# Compatibility provides to help the transition from libowcrypt.so.1
# to libcrypt.so.1, which provides all symbols of the former
%ifarch x86_64 s390x ppc64le aarch64
Provides:       libowcrypt.so.1()(64bit)
Provides:       libowcrypt.so.1(OW_CRYPT_1.0)(64bit)
%endif
%ifarch i586
Provides:       libowcrypt.so.1
Provides:       libowcrypt.so.1(OW_CRYPT_1.0)
%endif

%description -n libcrypt1
libxcrypt is a modern library for one-way hashing of passwords.  It
supports DES, MD5, SHA-2-256, SHA-2-512, and bcrypt-based password
hashes, and provides the traditional Unix 'crypt' and 'crypt_r'
interfaces, as well as a set of extended interfaces pioneered by
Openwall Linux, 'crypt_rn', 'crypt_ra', 'crypt_gensalt',
'crypt_gensalt_rn', and 'crypt_gensalt_ra'.

%package devel
Summary:        Development files for %{name}
License:        LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND SUSE-Public-Domain
Group:          Development/Languages/C and C++
Requires:       libcrypt1 = %{version}
Requires:       pkgconfig
Provides:       glibc-devel:%{_libdir}/libcrypt.so
Conflicts:      glibc-devel < 2.28

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package devel-static
Summary:        Static library for -static linking with %{name}
License:        GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND SUSE-Public-Domain
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       glibc-devel-static
Provides:       glibc-devel-static:%{_libdir}/libcrypt.a
Conflicts:      glibc-devel-static < 2.28

%description devel-static
This package contains the libxcrypt static libraries for -static
linking.  You don't need this, unless you link statically, which
is highly discouraged.


%prep
%autosetup -p 1

%build
# Disable LTO due to symbol versioning (boo#1138833):
# (https://en.opensuse.org/openSUSE:LTO#Symbol_versioning).
%define _lto_cflags %{nil}

autoreconf -fi
%configure			\
  --disable-silent-rules	\
  --enable-shared		\
  --enable-static		\
  --enable-obsolete-api=suse	\
  --enable-hashes=all		\
  --with-pkgconfigdir=%{_libdir}/pkgconfig
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -print -delete

%check
%make_build check || \
  {
    rc=$?;
    echo "-----BEGIN TESTLOG-----";
    %{__cat} test-suite.log;
    echo "-----END TESTLOG-----";
    exit $rc;
  }

%post -n libcrypt1 -p /sbin/ldconfig
%postun -n libcrypt1 -p /sbin/ldconfig

%files -n libcrypt1
%license COPYING.LIB LICENSING
%doc AUTHORS NEWS README README.md THANKS
%{_libdir}/libcrypt.so.*
%{_libdir}/libowcrypt.so.*

%files devel
%doc TODO TODO.md
%{_libdir}/libcrypt.so
%{_libdir}/libxcrypt.so
%{_libdir}/libowcrypt.so
%{_includedir}/crypt.h
%{_includedir}/xcrypt.h
%{_libdir}/pkgconfig/libcrypt.pc
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/crypt_rn.3.*
%{_mandir}/man3/crypt_gensalt.3.*
%{_mandir}/man3/crypt.3.*
%{_mandir}/man3/crypt_checksalt.3.*
%{_mandir}/man3/crypt_gensalt_ra.3.*
%{_mandir}/man3/crypt_gensalt_rn.3.*
%{_mandir}/man3/crypt_preferred_method.3.*
%{_mandir}/man3/crypt_r.3.*
%{_mandir}/man3/crypt_ra.3.*
%{_mandir}/man5/crypt.5.*

%files devel-static
%{_libdir}/libcrypt.a
%{_libdir}/libxcrypt.a
%{_libdir}/libowcrypt.a

%changelog
