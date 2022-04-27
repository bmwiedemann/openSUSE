#
# spec file for package ffcall
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


# This package uses assembly to do its work.  This is the entire list of
# supported architectures understood by RPM, even those not currently supported
# by Fedora.  RPM hasn't heard about line continuations, hence the mess.
%global ffcall_arches %ix86 x86_64 %alpha %arm aarch64 parisc hppa1.0 hppa1.1 hppa1.2 hppa2.0 ia64 m68k mips mipsel ppc ppc64 ppc64le ppc8260 ppc8560 ppc32dy4 ppciseries ppcpseries riscv64 s390 s390x %sparc sparc64

Name:           ffcall
Version:        2.4
Release:        0
Summary:        Libraries for foreign function call interfaces
# As this package only provides a static library together with the header files
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
Provides:       %{name}-devel = %version-%release
URL:            https://www.gnu.org/software/libffcall/
#               https://git.savannah.gnu.org/cgit/libffcall.git/snapshot/libffcall-<version>.tar.gz
Source0:        https://ftp.gnu.org/gnu/libffcall/libffcall-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/libffcall/libffcall-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=libffcall&download=1#/%{name}.keyring
Provides:       ffcall-devel
Requires:       libavcall1 = %{version}-%{release}
Requires:       libcallback1 = %{version}-%{release}
Requires:       libffcall0 = %{version}-%{release}
Requires:       libtrampoline1 = %{version}-%{release}
ExclusiveArch:  %{ffcall_arches}

%if ! %{defined _rpmmacrodir}
%define _rpmmacrodir %{_sysconfdir}/rpm
%endif

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.  The four
packages are:
 - avcall: calling C functions with variable arguments
 - vacall: C functions accepting variable argument prototypes
 - trampoline: closures as first-class C functions
 - callback: closures with variable arguments as first-class C functions
   (a reentrant combination of vacall and trampoline)

%package -n libavcall1
Summary:        FFI library for variadic argument functions
Group:          System/Libraries
Conflicts:      libffcall0 < %{version}-%{release}

%description -n libavcall1
A library for building foreign function call interfaces in embedded
interpreters.
This library allows calling C functions with variable argument
prototypes.

%package -n libcallback1
Summary:        FFI library for closures with variable arguments
Group:          System/Libraries
Conflicts:      libffcall0 < %{version}-%{release}

%description -n libcallback1
A library for building foreign function call interfaces in embedded
interpreters.

This library allows for closures with variable arguments as
first-class C functions (a reentrant combination of vacall and
trampoline).

%package -n libffcall0
Summary:        Libraries for foreign function call interfaces
Group:          System/Libraries

%description -n libffcall0
A library for building foreign function call interfaces in embedded
interpreters.

%package -n libtrampoline1
Summary:        FFI library for closures as first-class C functions
Group:          System/Libraries
Conflicts:      libffcall0 < %{version}-%{release}

%description -n libtrampoline1
A library for building foreign function call interfaces in embedded
interpreters.
This library allows using closures (lambdas) as first-class C
functions.

%prep
%setup -q -n libffcall-%{version}
if ! test -e /usr/include/asm/cachectl.h
then
    # FIX-OPENSUSE -- Remove this if there is no <asm/cachectl.h>
    for c in callback/trampoline_r/trampoline.c trampoline/trampoline.c
    do
	echo 'No <asm/cachectl.h> on this architecture %arch'
	sed -ri '/^#ifdef linux/,/^#else/{ \@#include <asm/cachectl.h>@d }' $c
    done
fi

# Remove prebuilt object files
find . -name \*.o | xargs rm -f

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -g -fPIC -fno-strict-aliasing"
export STRIP=true STRIPPROG=true
%configure --disable-rpath --with-gnu-ld --enable-thread=posix
if test -e /.build.log
then
    grep -E '^#define (CODE|HAVE)' config.h
    sed -rn '/checking whether code in malloc\(\)ed memory is executable/,/result: /p' config.log
fi
make # %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
export STRIP=true STRIPPROG=true
make install DESTDIR=%{buildroot} STRIP=true STRIPPROG=true
rm -fr %{buildroot}%{_datadir}/html
rm -f %{buildroot}%{_libdir}/*.la
if test %debug = yes ; then
    install config.log %{buildroot}%{_defaultdocdir}/%{name}
    echo %{_defaultdocdir}/%{name}/config.log > list
else
    > list
fi
cd %{buildroot}%{_mandir}/man3

# Advertise supported architectures
mkdir -p %{buildroot}%{_rpmmacrodir}
cat > %{buildroot}%{_rpmmacrodir}/macros.%{name} << EOF
# arches that ffcall supports
%%ffcall_arches %{ffcall_arches}
EOF

# Fix man pages with overly generic names (bz 800360)
for page in *; do
  mv $page %{name}-$page
done

%post   -n libavcall1 -p /sbin/ldconfig
%postun -n libavcall1 -p /sbin/ldconfig
%post   -n libcallback1 -p /sbin/ldconfig
%postun -n libcallback1 -p /sbin/ldconfig
%post   -n libffcall0 -p /sbin/ldconfig
%postun -n libffcall0 -p /sbin/ldconfig
%post   -n libtrampoline1 -p /sbin/ldconfig
%postun -n libtrampoline1 -p /sbin/ldconfig

%files -f list
%if 0%{?sle_version} > 120200 || 0%{?suse_version} > 1320
%license COPYING
%else
%doc COPYING
%endif
%doc README NEWS
%doc avcall/avcall.html
%doc callback/callback.html
%doc callback/trampoline_r/trampoline_r.html
%doc trampoline/trampoline.html
%doc vacall/vacall.html
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*
%doc %{_mandir}/man*/*
%{_rpmmacrodir}/macros.%{name}

%files -n libavcall1
%{_libdir}/libavcall.so.*

%files -n libcallback1
%{_libdir}/libcallback.so.*

%files -n libffcall0
%{_libdir}/libffcall.so.*

%files -n libtrampoline1
%{_libdir}/libtrampoline.so.*

%changelog
