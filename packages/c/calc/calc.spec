#
# spec file for package calc
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


%define soname 2_14_1_2
%define libname libcalc%{soname}
Name:           calc
Version:        2.14.1.2
Release:        0
Summary:        C-style arbitrary precision calculator
License:        LGPL-2.1-only
Group:          Productivity/Scientific/Math
URL:            http://www.isthe.com/chongo/tech/comp/calc/index.html
Source0:        http://www.isthe.com/chongo/src/calc/%{name}-%{version}.tar.bz2
Source1:        README.openSUSE
BuildRequires:  fdupes
BuildRequires:  ncurses-devel >= 5.5
BuildRequires:  readline-devel >= 5.1
Requires:       %{libname} = %{version}-%{release}
Requires:       less >= 358
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Calc is arbitrary precision C-like arithmetic system that is a
calculator, an algorithm prototype and mathematical research tool.
Calc comes with a rich set of builtin mathematical and programmatic
functions.

%package -n %{libname}
Summary:        Arbitrary precision math library
Group:          System/Libraries

%description -n %{libname}
Part of the calc release consists of an arbitrary precision math link
library.  This link library is used by the calc program to perform its
own calculations.  If you wish, you can ignore the calc program entirely
and call the arbitrary precision math routines from your own C programs.

%package devel
Summary:        Development files for libcalc
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}

%description devel
Part of the calc release consists of an arbitrary precision math link
library.  This link library is used by the calc program to perform its
own calculations.  If you wish, you can ignore the calc program entirely
and call the arbitrary precision math routines from your own C programs.

This package contains the files needed for building programs that use
this library.

%prep
%setup -q

cp "%{SOURCE1}" .

sed -i '/${CC} ${LIBCUSTCALC_SHLIB} ${CUSTCALC_OBJ}/a\
\tln -s $@ libcustcalc.so
' custom/Makefile

%define _NC_FLAGS %(ncursesw6-config --cflags)
%define _NC_LIBS %(ncursesw6-config --libs)

%define makevars \\\
    BINDIR=%{_bindir} \\\
    LIBDIR=%{_libdir} \\\
    SCRIPTDIR=%{_datadir}/%{name}/cscript \\\
    CALC_SHAREDIR=%{_datadir}/%{name} \\\
    CALC_INCDIR=%{_includedir}/calc \\\
    MANDIR=%{_mandir}/man1 \\\
    HAVE_FPOS="-DHAVE_NO_FPOS" \\\
    USE_READLINE="-DUSE_READLINE" \\\
    READLINE_LIB="-lreadline -lhistory %{_NC_LIBS} -L./custom -lcustcalc" \\\
    LD_SHARE="%{_NC_LIBS}" \\\
    ARCH_CFLAGS= \\\
    EXTRA_CFLAGS="%{optflags} -g -fno-strict-aliasing %{_NC_FLAGS}"

%build
make -e %{makevars}

%check
make -e %{makevars} chk

%install
make T=%{buildroot} %{makevars} install
rmdir %{buildroot}%{_includedir}/calc/custom

# dummy-install some docs etc. to create the symlinks
install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -m 644 \
    BUGS CHANGES COPYING COPYING-LGPL HOWTO.INSTALL LIBRARY \
    README.FIRST README.md README.openSUSE \
    custom/CUSTOM_CAL custom/HOW_TO_ADD \
    %{buildroot}%{_docdir}/%{name}/

# create symlinks to the help-dir for the help command, e.g. "help bugs"
ln -sf %{_docdir}/%{name}/COPYING \
    %{buildroot}%{_datadir}/%{name}/help/COPYING
ln -sf %{_docdir}/%{name}/COPYING-LGPL \
    %{buildroot}%{_datadir}/%{name}/help/COPYING-LGPL
ln -sf %{_docdir}/%{name}/BUGS \
    %{buildroot}%{_datadir}/%{name}/help/bug
ln -sf %{_docdir}/%{name}/BUGS \
    %{buildroot}%{_datadir}/%{name}/help/bugs
ln -sf %{_docdir}/%{name}/CHANGES \
    %{buildroot}%{_datadir}/%{name}/help/changes
ln -sf %{_docdir}/%{name}/CHANGES \
    %{buildroot}%{_datadir}/%{name}/help/change
ln -sf %{_docdir}/%{name}/CUSTOM_CAL \
    %{buildroot}%{_datadir}/%{name}/help/custom_cal
ln -sf %{_docdir}/%{name}/HOW_TO_ADD \
    %{buildroot}%{_datadir}/%{name}/help/new_custom

# add symlink to intro to docdir
ln -sf %{_datadir}/%{name}/help/intro \
    %{buildroot}%{_docdir}/%{name}/what-is-calc.txt

%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc BUGS CHANGES COPYING COPYING-LGPL HOWTO.INSTALL LIBRARY
%doc README.FIRST README.md README.openSUSE
%doc custom/CUSTOM_CAL custom/HOW_TO_ADD
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc %{_mandir}/man1/%{name}.1.gz
%doc %{_docdir}/%{name}/what-is-calc.txt

%files -n %{libname}
%defattr(-,root,root)
%attr(755, root, root) %{_libdir}/libcalc.so.*
%attr(755, root, root) %{_libdir}/libcustcalc.so.*

%files devel
%defattr(-, root, root)
%doc %attr(644, root, root) BUGS COPYING COPYING-LGPL LIBRARY
%doc sample_many.c sample_rand.c sample.README README.md README.openSUSE
%{_includedir}/%{name}
%{_libdir}/libcalc.so
%{_libdir}/libcustcalc.so

%changelog
