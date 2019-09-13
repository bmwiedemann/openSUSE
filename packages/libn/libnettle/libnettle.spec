#
# spec file for package libnettle
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


%define soname 7
%define hogweed_soname 5
Name:           libnettle
Version:        3.5.1
Release:        0
Summary:        Cryptographic Library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.lysator.liu.se/~nisse/nettle/
Source0:        https://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz
Source1:        https://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
# PATCH-FIX-UPSTREAM respect cflags while building
Patch0:         nettle-respect-cflags.patch
BuildRequires:  gmp-devel
BuildRequires:  m4
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
Requires(post): %{install_info_prereq}

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
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Productivity/Security

%description -n nettle
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

This package contains a few command-line tools to perform cryptographic
operations using the nettle library.

%prep
%setup -q -n nettle-%{version}
%patch0 -p1

%build
%configure \
    --disable-static \
    --enable-shared \
    --enable-fat
make %{?_smp_mflags}

%install
%make_install

%post   -n libnettle%{soname} -p /sbin/ldconfig
%postun -n libnettle%{soname} -p /sbin/ldconfig
%post   -n libhogweed%{hogweed_soname} -p /sbin/ldconfig
%postun -n libhogweed%{hogweed_soname} -p /sbin/ldconfig
%post -n libnettle-devel
%install_info --info-dir="%{_infodir}" "%{_infodir}"/nettle.info%{ext_info}

%preun -n libnettle-devel
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}"/nettle.info%{ext_info}

%check
make check %{?_smp_mflags}

%files -n libnettle%{soname}
%license COPYING*
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libnettle.so.%{soname}
%{_libdir}/libnettle.so.%{soname}.*

%files -n libhogweed%{hogweed_soname}
%{_libdir}/libhogweed.so.%{hogweed_soname}
%{_libdir}/libhogweed.so.%{hogweed_soname}.*

%files -n libnettle-devel
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
