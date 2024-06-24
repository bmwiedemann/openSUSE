#
# spec file for package libnettle
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


%define soname 8
%define hogweed_soname 6
Name:           libnettle
Version:        3.10
Release:        0
Summary:        Cryptographic Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.lysator.liu.se/~nisse/nettle/
Source0:        https://ftp.gnu.org/gnu/nettle/nettle-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/nettle/nettle-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
Source4:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  fipscheck
BuildRequires:  gmp-devel >= 6.1.0
BuildRequires:  m4
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
%{?suse_build_hwcaps_libs}

%description
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

%package -n libnettle%{soname}
Summary:        Cryptographic Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libnettle%{soname}
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

%package -n libhogweed%{hogweed_soname}
Summary:        Cryptographic Library for Public Key Algorithms
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libhogweed%{hogweed_soname}
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

The libhogweed library contains public key algorithms to use with libnettle.

%package -n libnettle-devel
Summary:        Cryptographic Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       gmp-devel
Requires:       libhogweed%{hogweed_soname} = %{version}
Requires:       libnettle%{soname} = %{version}

%description -n libnettle-devel
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

%package -n nettle
Summary:        Cryptographic Tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Security

%description -n nettle
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

This package contains a few command-line tools to perform cryptographic
operations using the nettle library.

%prep
%autosetup -p1 -n nettle-%{version}

%build
autoreconf -fiv
%configure \
    --disable-static \
    --enable-shared \
    --enable-fat \
%ifarch s390x
    --enable-s390x-vf \
    --enable-s390x-msa \
%endif
    %{nil}

%make_build

%install
%make_install
chmod 0755 %{buildroot}%{_libdir}/libnettle.so.%{soname}
chmod 0755 %{buildroot}%{_libdir}/libhogweed.so.%{hogweed_soname}

for arch in x86_64 s390x powerpc64 arm arm64 ; do
    cp ${arch}/README ${arch}.README
done

# the hmac hashes:
#
# this is a hack that re-defines the __os_install_post macro
# for a simple reason: the macro strips the binaries and thereby
# invalidates a HMAC that may have been created earlier.
# solution: create the hashes _after_ the macro runs.
#
# this shows up earlier because otherwise the %%expand of
# the macro is too late.
# remark: This is the same as running
#   openssl dgst -sha256 -hmac 'orboDeJITITejsirpADONivirpUkvarP'
%{expand:%%global __os_install_post {%__os_install_post
%{_bindir}/fipshmac %{buildroot}%{_libdir}/libnettle.so.%{soname}
%{_bindir}/fipshmac %{buildroot}%{_libdir}/libhogweed.so.%{hogweed_soname}
}}

%post   -n libnettle%{soname} -p /sbin/ldconfig
%postun -n libnettle%{soname} -p /sbin/ldconfig
%post   -n libhogweed%{hogweed_soname} -p /sbin/ldconfig
%postun -n libhogweed%{hogweed_soname} -p /sbin/ldconfig

%check
%make_build check

%files -n libnettle%{soname}
%license COPYING*
%{_libdir}/libnettle.so.%{soname}
%{_libdir}/libnettle.so.%{soname}.*
%{_libdir}/.libnettle.so.%{soname}.hmac

%files -n libhogweed%{hogweed_soname}
%license COPYING*
%{_libdir}/libhogweed.so.%{hogweed_soname}
%{_libdir}/libhogweed.so.%{hogweed_soname}.*
%{_libdir}/.libhogweed.so.%{hogweed_soname}.hmac

%files -n libnettle-devel
%license COPYING*
%doc AUTHORS ChangeLog NEWS README *.README nettle.html nettle.pdf
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_infodir}/nettle.info%{?ext_info}
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc

%files -n nettle
%license COPYING*
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/nettle-lfib-stream
%{_bindir}/nettle-pbkdf2
%{_bindir}/pkcs1-conv
%{_bindir}/sexp-conv
%{_bindir}/nettle-hash

%changelog
