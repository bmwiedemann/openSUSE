#
# spec file for package lapack-man
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


Name:           lapack-man
%define _name   lapack
Version:        3.5.0
Release:        0
Summary:        Manpages for LAPACK
License:        BSD-3-Clause
Group:          Documentation/HTML
Url:            http://www.netlib.org/lapack/
Source0:        http://www.netlib.org/lapack/%{_name}-%{version}.tgz
BuildRequires:  doxygen >= 1.7
Provides:       lapack-manpages = %{version}
Obsoletes:      lapack-manpages < %{version}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Manpages for LAPACK

%package     -n blas-man
Summary:        Documentation for BLAS (Basic Linear Algebra Subprograms)
Group:          Development/Libraries/Parallel
Provides:       blasman = %{version}
Obsoletes:      blasman < %{version}

%description -n blas-man
The blas-man package contains documentation for BLAS (Basic Linear
Algebra subprograms) routines, in the form of man pages.

%prep
%setup -q -n %{_name}-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
cp make.inc.example make.inc
# Create man pages - and do some cleanup
make man %{?_smp_mflags}
rm -f DOCS/man/man3/*tst*
rm -f DOCS/man/man3/TST*
rm -f DOCS/man/man3/MYSUB.3
rm -f DOCS/man/man3/INSTALL_lsame.f.3
rm -f DOCS/man/man3/xerbla.f.3
rm -f DOCS/man/man3/xerbla_array.f.3
rm -f DOCS/man/man3/*_.3
rm -f DOCS/man/man3/dsecnd_*.3
rm -f DOCS/man/man3/DSECND.3
rm -f DOCS/man/man3/second_*3
rm -f DOCS/man/man3/SECOND.3
rm -f DOCS/man/man3/LAPACK_version.f.3
rm -f DOCS/man/man3/SRC_ilaver.f.3
rm -f DOCS/man/man3/SRC_xerbla.f.3
rm -f DOCS/man/man3/SRC_xerbla_array.f.3
rm -f DOCS/man/man3/SLAMC2.3.gz
rm -f DOCS/man/man3/SLAMC3.3.gz
rm -f DOCS/man/man3/SLAMC4.3.gz
rm -f DOCS/man/man3/SLAMC5.3.gz
rm -f DOCS/man/man3/DLAMC2.3.gz
rm -f DOCS/man/man3/DLAMC3.3.gz
rm -f DOCS/man/man3/DLAMC4.3.gz
rm -f DOCS/man/man3/DLAMC5.3.gz
rm -f DOCS/man/man3/SLADIV1.3.gz
rm -f DOCS/man/man3/SLADIV2.3.gz
rm -f DOCS/man/man3/DLADIV1.3.gz
rm -f DOCS/man/man3/DLADIV2.3.gz
mv DOCS/man/man3/BLAS_SRC_lsame.f.3 DOCS/man/man3/lsame.f.3
mv DOCS/man/man3/BLAS_SRC_xerbla.f.3 DOCS/man/man3/xerbla.f.3
mv DOCS/man/man3/BLAS_SRC_xerbla_array.f.3 DOCS/man/man3/xerbla_array.f.3
mv DOCS/man/man3/INSTALL_ilaver.f.3 DOCS/man/man3/ilaver.f.3
rm -f DOCS/psfig.tex # see bnc#757332

%install
install -d %{buildroot}%{_mandir}/man3
install -m 0644 DOCS/man/man3/*.3 %{buildroot}%{_mandir}/man3/
find BLAS/SRC/ -name \*.f -type f -printf "%{_mandir}/man3/%f.3.gz\n" \
     > blasmans
find BLAS/SRC/ -name \*.f -type f -printf "%f\n" \
     | tr 'a-z' 'A-Z' |sed -e 's#\(.*\).F#'%{_mandir}/man3/'\1.3.gz#' \
     >> blasmans
find SRC/ -name \*.f -type f -printf "%{_mandir}/man3/%f.3.gz\n" \
     | grep -v -E 'lsame.f|sceil.f|xerbla.f|xerbla_array.f' \
     | sort -u > lapackmans
find SRC/ -name \*.f -type f -printf "%f\n" \
     | grep -v -E 'sceil.f|xerbla.f|xerbla_array.f' \
     | tr 'a-z' 'A-Z' |sed -e 's#\(.*\).F#'%{_mandir}/man3/'\1.3.gz#' \
     | sort -u >> lapackmans
echo %{_mandir}/man3/SLAMC1.3.gz >> lapackmans
echo %{_mandir}/man3/SLAMC2.3.gz >> lapackmans
echo %{_mandir}/man3/SLAMC3.3.gz >> lapackmans
echo %{_mandir}/man3/SLAMC4.3.gz >> lapackmans
echo %{_mandir}/man3/SLAMC5.3.gz >> lapackmans
echo %{_mandir}/man3/SLAMCH.3.gz >> lapackmans
echo %{_mandir}/man3/DLAMC1.3.gz >> lapackmans
echo %{_mandir}/man3/DLAMC2.3.gz >> lapackmans
echo %{_mandir}/man3/DLAMC3.3.gz >> lapackmans
echo %{_mandir}/man3/DLAMC4.3.gz >> lapackmans
echo %{_mandir}/man3/DLAMC5.3.gz >> lapackmans
echo %{_mandir}/man3/DLAMCH.3.gz >> lapackmans
echo %{_mandir}/man3/SLADIV1.3.gz >> lapackmans
echo %{_mandir}/man3/SLADIV2.3.gz >> lapackmans
echo %{_mandir}/man3/DLADIV1.3.gz >> lapackmans
echo %{_mandir}/man3/DLADIV2.3.gz >> lapackmans
echo %{_mandir}/man3/slamch.f.3.gz >> lapackmans
echo %{_mandir}/man3/slamchf77.f.3.gz >> lapackmans
echo %{_mandir}/man3/dlamch.f.3.gz >> lapackmans
echo %{_mandir}/man3/dlamchf77.f.3.gz >> lapackmans
ln -s SLAMC1.3.gz %{buildroot}/%{_mandir}/man3/SLAMC2.3.gz
ln -s SLAMC1.3.gz %{buildroot}/%{_mandir}/man3/SLAMC4.3.gz
ln -s SLAMC1.3.gz %{buildroot}/%{_mandir}/man3/SLAMC5.3.gz
ln -s SLAMCH.3.gz %{buildroot}/%{_mandir}/man3/SLAMC3.3.gz
ln -s DLAMC1.3.gz %{buildroot}/%{_mandir}/man3/DLAMC2.3.gz
ln -s DLAMC1.3.gz %{buildroot}/%{_mandir}/man3/DLAMC4.3.gz
ln -s DLAMC1.3.gz %{buildroot}/%{_mandir}/man3/DLAMC5.3.gz
ln -s DLAMCH.3.gz %{buildroot}/%{_mandir}/man3/DLAMC3.3.gz
ln -s SLADIV.3.gz %{buildroot}/%{_mandir}/man3/SLADIV1.3.gz
ln -s SLADIV.3.gz %{buildroot}/%{_mandir}/man3/SLADIV2.3.gz
ln -s DLADIV.3.gz %{buildroot}/%{_mandir}/man3/DLADIV1.3.gz
ln -s DLADIV.3.gz %{buildroot}/%{_mandir}/man3/DLADIV2.3.gz

%files -f lapackmans
%defattr(-,root,root)

%files -n blas-man -f blasmans
%defattr(-,root,root)

%changelog
