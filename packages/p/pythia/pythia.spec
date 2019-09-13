#
# spec file for package pythia
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


%define ver 8243
%define soname lib%{name}8
Name:           pythia
Version:        8.243
Release:        0
Summary:        A simulation program for particle collisions at very high energies
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://home.thep.lu.se/~torbjorn/Pythia.html
Source:         http://home.thep.lu.se/~torbjorn/pythia8/%{name}%{ver}.tgz
# PATCH-FIX-UPSTREAM pythia-makefile-destdir-support.patch badshah400@gmail.com -- Add DESTDIR support to makefile to prevent touching of buildroot in the %%build section
Patch0:         pythia-makefile-destdir-support.patch
# PATCH-FIX-UPSTREAM pythia-honour-env-cxxflags.patch badshah400@gmail.com -- Append CXXFLAGS from env to default compilations flags; this allows us to pass RPM_OPT_FLAGS during compilation
Patch1:         pythia-honour-env-cxxflags.patch
# PATCH-FIX-UPSTREAM pythia-remove-rpaths.patch badshah400@gmail.com -- Delete rpath references when building libraries; patch sent upstream
Patch2:         pythia-remove-rpaths.patch
BuildRequires:  HepMC2-devel
BuildRequires:  LHAPDF-devel
BuildRequires:  fastjet-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  rsync
BuildRequires:  zlib-devel

%description
Pythia can be used to generate high-energy-physics events, i.e. sets
of outgoing particles produced in the interactions between two
incoming particles.

%package -n %{soname}
Summary:        A simulation program for particle collisions at very high energies
Group:          System/Libraries

%description -n %{soname}
Pythia can be used to generate high-energy-physics events, i.e. sets
of outgoing particles produced in the interactions between two
incoming particles. The objective is to provide as accurate as
possible a representation of event properties in a wide range of
reactions, within and beyond the Standard Model, with emphasis on
those where strong interactions play a role, directly or indirectly,
and therefore multihadronic final states are produced. The physics is
then not understood well enough to give an exact description; instead
the program has to be based on a combination of analytical results and
various QCD-based models. Extensive information is provided on all
program elements: subroutines and functions, switches and parameters,
and particle and process data. This should allow the user to tailor
the generation task to the topics of interest.

This package provides the shared libraries for %{name}.

%package -n %{soname}lhapdf6
Summary:        A simulation program for particle collisions at very high energies
Group:          System/Libraries

%description -n %{soname}lhapdf6
Pythia can be used to generate high-energy-physics events, i.e. sets
of outgoing particles produced in the interactions between two
incoming particles.

This package provides the shared libraries for the lhapdf6 bindings of
%{name}.

%package devel
Summary:        A simulation program for particle collisions at very high energies
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}
Requires:       %{soname}lhapdf6 = %{version}
Recommends:     %{name}-doc

%description devel
Pythia can be used to generate high-energy-physics events, i.e. sets
of outgoing particles produced in the interactions between two
incoming particles.

This package provides the header and source files for development with
%{name}.

%package doc
Summary:        A simulation program for particle collisions at very high energies
Group:          Documentation/HTML

%description doc
Pythia can be used to generate high-energy-physics events, i.e. sets
of outgoing particles produced in the interactions between two
incoming particles.

This package provides documentation for development with %{name}.

%prep
%setup -q -n %{name}%{ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# REMOVE UNNEEDED .orig FILES FROM THE examples DIR
rm -f examples/Makefile.orig

# REMOVE NON-FREE HEADER FILE NOT USED BY PYTHIA DIRECTLY
rm include/Pythia8Plugins/MixMax.h

%build
# FIX EOF ENCODINGS
sed -i 's/\r$//' share/Pythia8/xmldoc/mrstlostarstar.00.dat
sed -i 's/\r$//' share/Pythia8/htmldoc/pythia.css
sed -i 's/\r$//' share/Pythia8/phpdoc/pythia.css
sed -i 's/\r$//' examples/main29.cc

# FOR oS > 1320, "-std=c++14" IS NEEDED FOR BUILDING EXAMPLES
# WITH FASTJET3 (WHICH ALREADY USES THIS STD)
%if 0%{?suse_version} > 1320
export CXXFLAGS="$CXXFLAGS -std=c++14"
%endif

%configure \
  --prefix-lib=%{_libdir} \
  --prefix-share=%{_docdir}/%{name} \
  --enable-shared \
  --disable-rpath \
  --with-lhapdf6 \
  --with-hepmc2 \
  --with-gzip \
  --with-fastjet3

# EXPORT PYTHIA8DATA ENV VARIABLE
cat << EOF >> %{name}.sh
export PYTHIA8DATA=%{_docdir}/%{name}/xmldoc
EOF

cat << EOF >> %{name}.csh
setenv PYTHIA8DATA %{_docdir}/%{name}/xmldoc
EOF

make %{?_smp_mflags}

%install
%make_install

install -D -m0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -D -m0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

# REMOVE STATIC LIBRARY
rm %{buildroot}%{_libdir}/libpythia8.a

# REMOVE AUTHORS, COPYING, GUIDELINES AND README FILES AND BUNDLE THEM IN MAIN PACKAGE USING %%doc
for i in AUTHORS COPYING GUIDELINES README
do
  rm %{buildroot}%{_docdir}/%{name}/${i}
done

# REMOVE BUILDROOT FROM INSTALLED FILES
sed -i "s|%{buildroot}||g" %{buildroot}%{_bindir}/pythia8-config
sed -i "s|%{buildroot}||g" %{buildroot}%{_docdir}/%{name}/examples/Makefile.inc

# REMOVE SPURIOUS EXECUTABLE PERMISSIONS
chmod -x %{buildroot}%{_docdir}/%{name}/xmldoc/GKG18_DPDF_Fit*.dat

# FIX env BASED HASHBANG
sed -E -i "s|%{_bindir}/env bash|/bin/bash|" %{buildroot}%{_bindir}/pythia8-config

# REMOVE UNNECESSARY HIDDEN FILES
rm %{buildroot}%{_includedir}/Pythia8/._*.h
rm %{buildroot}%{_includedir}/Pythia8Plugins/._*.h
find %{buildroot}%{_docdir}/%{name}/ -name "._*" -delete -print

%fdupes -s %{buildroot}%{_docdir}/%{name}/

%check
pushd examples
./runmains
# ADDITIONAL CHECKS FOR BINDINGS; RUN MANUALLY BECAUSE NOT ALL BINDINGS ARE ENABLED
# HEPMC2 AND FASTJET3 TESTS
for t in 41 71 72
do
  echo
  echo Now begin main${t}
  make %{?_smp_mflags} main${t}
  time ./main${t} > out${t}
done
# TESTS 42 REQUIRES INPUT FILES; LOOP TO MAKE IT EASY TO ADD FUTURE TESTS
for t in 42
do
  echo
  echo Now begin main${t}
  make %{?_smp_mflags} main${t}
  time ./main${t} main${t}.cmnd hepmcout${t}.dat > out${t}
done

popd

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig
%post -n %{soname}lhapdf6 -p /sbin/ldconfig
%postun -n %{soname}lhapdf6 -p /sbin/ldconfig

%files -n %{soname}
%{_libdir}/%{soname}.so

%files -n %{soname}lhapdf6
%{_libdir}/%{soname}lhapdf6.so

%files devel
%doc AUTHORS GUIDELINES CODINGSTYLE README
%license COPYING
%{_bindir}/pythia8-config
%{_includedir}/Pythia8/
%{_includedir}/Pythia8Plugins/
%config %{_sysconfdir}/profile.d/%{name}.*
%{_docdir}/%{name}/xmldoc/

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/phpdoc/
%{_docdir}/%{name}/pdfdoc/
%{_docdir}/%{name}/htmldoc/
%{_docdir}/%{name}/examples/
%{_docdir}/%{name}/outref/

%changelog
