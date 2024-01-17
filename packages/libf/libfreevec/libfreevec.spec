#
# spec file for package libfreevec
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libfreevec
Version:        1.0.4
Release:        0
Summary:        Altivec Versions of Some libc Functions
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       libfreevec-library
Url:            http://www.freevec.org/
ExclusiveArch:  ppc ppc64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://www.codex.gr/system/files/libfreevec-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
libfreevec is a free (LGPL) library with hand-optimized replacement
routines for GLIBC, such as memcpy() and strlen(). These routines have
been written specifically to take advantage of the AltiVec unit
(Velocity Engine or VMX) and will only work on processors that include
this unit. This means they will not work on older processors, such as
603, 604, 750 (G3), or the POWER family of CPUs.

%package -n libfreevec0
Summary:        Altivec Versions of Some libc Functions
Group:          Development/Libraries/C and C++
Provides:       libfreevec-devel
Provides:       libfreevec-library

%description -n libfreevec0
libfreevec is a free (LGPL) library with hand-optimized replacement
routines for GLIBC, such as memcpy() and strlen(). These routines have
been written specifically to take advantage of the AltiVec unit
(Velocity Engine or VMX) and will only work on processors that include
this unit. This means they will not work on older processors, such as
603, 604, 750 (G3), or the POWER family of CPUs.

%prep
%setup -q

%build
autoreconf -fi
CFLAGS="$RPM_OPT_FLAGS -U_FORTIFY_SOURCE -O3 -maltivec -funroll-loops -DHAVE_ALTIVEC_H -flax-vector-conversions" \
%configure \
	--prefix=%_prefix \
	--libdir=%{_libdir}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT pkglibdir=%{_libdir}

%post -n libfreevec0 -p /sbin/ldconfig

%postun -n libfreevec0 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING FAQ README

%files -n libfreevec0
%defattr(-, root, root)
%{_libdir}/lib*

%changelog
