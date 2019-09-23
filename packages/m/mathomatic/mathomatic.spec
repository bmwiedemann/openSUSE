#
# spec file for package mathomatic
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           mathomatic
Version:        16.0.4
Release:        0
Summary:        Computer algebra system
License:        LGPL-2.1
Group:          Productivity/Scientific/Math

Url:            http://www.mathomatic.org/
Source:         http://www.mathomatic.org/archive/mathomatic-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  readline-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
Requires:       m4
# BuildArch:      noarch

Source1:        mathomatic.desktop
ExcludeArch:    ppc64

%description
Mathomatic is a free, portable, general-purpose Computer Algebra System (CAS)
that can automatically solve, differentiate, simplify, combine, and compare
algebraic equations, perform standard, complex number, modular, and polynomial
arithmetic, etc. It does some calculus and is very easy to learn and use.
Plotting expressions with gnuplot is also supported. This package
is complete, including Mathomatic, the Prime Number Tools, m4 Mathomatic,
and all documentation.

Author:
-------
    George Gesslein II <gesslein@mathomatic.org>

%package devel
Summary:        Development Package for Mathomatic
Group:          Development/Libraries/C and C++

%description devel
This package contains the Mathomatic symbolic math library, for using the
Mathomatic code inside of any C compatible program.  This is a static
library only, with no dependencies or requirements.  It has a small, easy
to use API that is written in C.  The Mathomatic code is not re-entrant.

Author:
-------
    George Gesslein II <gesslein@mathomatic.org>

%prep
%setup -q

%build
make OPTFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} READLINE=1
make -C primes OPTFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}
make -C lib OPTFLAGS="$RPM_OPT_FLAGS -g" %{?_smp_mflags} lib

%check
make check
make -C primes check bigcheck

%install
make bininstall matho-rmath-install DESTDIR=%{buildroot} prefix=%{_prefix} docdir=%{_docdir} datadir=%{_datadir}
install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/mathomatic.desktop
%if 0%{?suse_version}
%suse_update_desktop_file -n mathomatic
%endif
make -C primes install DESTDIR=%{buildroot} prefix=%{_prefix}
make -C lib install DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} includedir=%{_includedir}
make -C lib distclean

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc examples tests
%doc README.txt AUTHORS COPYING NEWS doc
%{_mandir}/man1/mathomatic.1*
%{_mandir}/man1/matho.1*
%{_mandir}/man1/rmath.1*
%{_mandir}/man1/matho-primes.1*
%{_mandir}/man1/matho-pascal.1*
%{_mandir}/man1/matho-sumsq.1*
%{_mandir}/man1/primorial.1*
%{_mandir}/man1/matho-mult.1*
%{_mandir}/man1/matho-sum.1*
%{_datadir}/%{name}
%{_bindir}/mathomatic
%{_bindir}/matho
%{_bindir}/rmath
%{_bindir}/matho-primes
%{_bindir}/matho-pascal
%{_bindir}/matho-sumsq
%{_bindir}/primorial
%{_bindir}/matho-mult
%{_bindir}/matho-sum
%{_datadir}/pixmaps/mathomatic.*
%{_datadir}/applications/mathomatic.desktop

%files devel
%defattr(-,root,root,-)
%doc lib
%{_mandir}/man3/matho_init.3*
%{_mandir}/man3/matho_clear.3*
%{_mandir}/man3/matho_parse.3*
%{_mandir}/man3/matho_process.3*
%{_libdir}/libmathomatic.a
%{_includedir}/mathomatic.h

%changelog
