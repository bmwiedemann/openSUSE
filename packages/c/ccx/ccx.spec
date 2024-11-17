#
# spec file for package ccx
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


Name:           ccx
Version:        2.22
Release:        0
Summary:        An open source finite element package
License:        BSD-3-Clause AND GPL-2.0-only AND SUSE-Public-Domain
Group:          Productivity/Scientific/Other
URL:            http://www.dhondt.de/
Source0:        http://www.dhondt.de/ccx_%{version}.src.tar.bz2
Source1:        http://www.dhondt.de/ccx_%{version}.test.tar.bz2
Source2:        ccx-rpmlintrc
# PATCH-FIX-OPENSUSE -- pass global optflags
Patch0:         ccx-2.16-build.patch
Patch1:         0001-Fixup-spooles-include-dir.patch
BuildRequires:  arpack-ng-devel
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  sed
BuildRequires:  spooles-devel

%description
CalculiX is a package designed to solve field problems.
The method used is the finite element method. So far only
structural problems can be solved but it is planned to
extend the capabilities.

%package examples
Summary:        Example problems for CalculiX
Group:          Productivity/Scientific/Other
BuildArch:      noarch
Conflicts:      ccx-doc < 2.16
Provides:       ccx-doc:%{_datadir}/%{name}-examples-2.12/achtel2.inp

%description examples
CalculiX is a package designed to solve field problems.
The method used is the finite element method. %{name}-examples
contains examples problems, together with reference data
to check your installation.

%prep
%setup -c -q
%setup -D -T -a 1 -q
# fixup dirs: very deep directory structure, not suitable for patching
mv CalculiX/ccx_%{version}/{src,test} ./
rmdir -p CalculiX/ccx_%{version}

%autopatch -p1

# Make reproducible
sed -i 's@./date.pl; *@@' src/Makefile

%build
cd src
export CFLAGS="%{optflags}"
export FFLAGS="%{optflags}"
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
cp src/ccx_%{version} %{buildroot}/%{_bindir}
chmod 755 %{buildroot}/%{_bindir}/ccx_%{version}
# symlink needed or apps like FreeCAD won't find it
ln -s ccx_%{version} %{buildroot}/%{_bindir}/ccx

mkdir -p %{buildroot}/%{_datadir}/%{name}-examples-%{version}
cp test/* %{buildroot}/%{_datadir}/%{name}-examples-%{version}
chmod 644 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/*
chmod 755 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/compare
chmod 755 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/datcheck.pl
chmod 755 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/frdcheck.pl
chmod 755 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/compare_valgrind_leaks

chmod 444 src/BUGS src/LOGBOOK src/README.INSTALL src/TODO

%fdupes %{buildroot}/%{_datadir}/%{name}-examples-%{version}

%check
cd test
# beamfsh1 slightly deviates on aarch64 and i586
%ifarch aarch64 %{ix86}
for f in beamfsh1.inp; do mv $f ${f}_disabled ; done
%endif
# Apparent mismatch between script and golden data, disable for now (2.20)
for f in beamread3.inp beamwrite3.inp ; do mv $f ${f}_error; done
# beamread* depends on beamwrite*
# beamprand is random
# beamptied{5,6} have nondeterministic order of eigenvalues
# beamhtfc2 needs output from beamhtfc
for f in beamread*.inp beamprand.inp beamptied{5,6}.inp beamhtfc2.inp; do mv $f ${f}_disabled ; done
set +x
function checkInput() {
    f=`basename $1 .inp`
    echo -n "Procesing $f " | tee -a ccxlog
    %{buildroot}/%{_bindir}/ccx $f >> ccxlog || echo -n "-> $?" ; echo
    [ -f $f.dat -a -f $f.frd ] || echo "$f failed!" | tee -a errorlog
    [ -f $f.dat.ref ] || return 0
    [ "$(wc -l < $f.dat)" -eq "$(wc -l < $f.dat.ref)" ] || echo "Wrong size: $f.dat" | tee -a errorlog
    grep NaN $f.dat && echo "Contains NaN: $f.dat" | tee -a errorlog
    ./datcheck.pl $f | tee -a errorlog
    [ -f $f.frd.ref ] || return 0
    [ "$(wc -l < $f.frd)" -eq "$(wc -l < $f.frd.ref)" ] || echo "Wrong size: $f.frd" | tee -a errorlog
    ./frdcheck.pl $f | tee -a errorlog
}

for f in beam*.inp ; do
    checkInput $f
done

# Second round
cp beamhtfc.rout beamhtfc2.rin
mv beamhtfc2.inp{_disabled,}
checkInput beamhtfc2.inp

for f in beamwrite*.inp ; do
    tc=${f##beamwrite}; tc=${tc%%.inp}
    mv beamread${tc}.inp_disabled beamread${tc}.inp
    cp beamwrite${tc}.rout beamread${tc}.rin
    checkInput beamread${tc}.inp
done

# Check results
set -x
if [ -s errorlog ] ; then
    cat ccxlog
    cat errorlog
    exit 1
fi

%files
%{_bindir}/ccx
%{_bindir}/ccx_%{version}
%doc src/BUGS src/LOGBOOK src/README.INSTALL src/TODO

%files examples
%{_datadir}/%{name}-examples-%{version}

%changelog
