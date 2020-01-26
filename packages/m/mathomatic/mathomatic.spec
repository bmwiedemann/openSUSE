#
# spec file for package mathomatic
#
# Copyright (c) 2019 SUSE LLC
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


Name:           mathomatic
Version:        16.0.5
Release:        0
Summary:        Computer algebra system
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.mathomatic.org/
Source:         http://mathomatic.orgserve.de/mathomatic-%{version}.tar.bz2
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
Requires:       m4

%description
Mathomatic is a free, portable, general-purpose Computer Algebra System (CAS)
that can automatically solve, differentiate, simplify, combine, and compare
algebraic equations, perform standard, complex number, modular, and polynomial
arithmetic, etc. It does some calculus and is very easy to learn and use.
Plotting expressions with gnuplot is also supported. This package
is complete, including Mathomatic, the Prime Number Tools, m4 Mathomatic,
and all documentation.

%package devel
Summary:        Development Package for Mathomatic
Group:          Development/Libraries/C and C++

%description devel
This package contains the Mathomatic symbolic math library, for using the
Mathomatic code inside of any C compatible program.  This is a static
library only, with no dependencies or requirements.  It has a small, easy
to use API that is written in C.  The Mathomatic code is not re-entrant.

%prep
%setup -q

%build
make OPTFLAGS="%{optflags}" %{?_smp_mflags} READLINE=1
make -C primes OPTFLAGS="%{optflags}" %{?_smp_mflags}
make -C lib %{?_smp_mflags} lib \
%if 0%{?suse_version} > 1500
OPTFLAGS="%{optflags} -g -ffat-lto-objects"
%else
OPTFLAGS="%{optflags} -g"
%endif

%install
make bininstall matho-rmath-install DESTDIR=%{buildroot} prefix=%{_prefix} docdir=%{_docdir} datadir=%{_datadir}
rm %{buildroot}%{_datadir}/pixmaps/mathomatic.{png,xpm}
install -m0644 icons/mathomatic.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
%suse_update_desktop_file -n %{name}
make -C primes install DESTDIR=%{buildroot} prefix=%{_prefix}
make -C lib install DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} includedir=%{_includedir}
make -C lib distclean

%check
make check
make -C primes check bigcheck

%files
%license COPYING
%doc examples tests
%doc README.txt AUTHORS NEWS doc
%{_mandir}/man1/mathomatic.1%{?ext_man}
%{_mandir}/man1/matho.1%{?ext_man}
%{_mandir}/man1/rmath.1%{?ext_man}
%{_mandir}/man1/matho-primes.1%{?ext_man}
%{_mandir}/man1/matho-pascal.1%{?ext_man}
%{_mandir}/man1/matho-sumsq.1%{?ext_man}
%{_mandir}/man1/primorial.1%{?ext_man}
%{_mandir}/man1/matho-mult.1%{?ext_man}
%{_mandir}/man1/matho-sum.1%{?ext_man}
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
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%files devel
%doc lib
%{_mandir}/man3/matho_init.3%{?ext_man}
%{_mandir}/man3/matho_clear.3%{?ext_man}
%{_mandir}/man3/matho_parse.3%{?ext_man}
%{_mandir}/man3/matho_process.3%{?ext_man}
%{_libdir}/libmathomatic.a
%{_includedir}/mathomatic.h

%changelog
