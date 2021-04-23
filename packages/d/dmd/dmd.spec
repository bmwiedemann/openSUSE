#
# spec file for package dmd
#
# Copyright (c) 2020 SUSE LLC
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


%define bootstrap_version 2.078.0
%define sover	0_94
%define auto_bootstrap 1
Name:           dmd
Version:        2.094.2
Release:        0
Summary:        D Programming Language 2.0
License:        BSL-1.0
Group:          Development/Languages/Other
URL:            https://dlang.org/
Source:         https://github.com/D-Programming-Language/dmd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/D-Programming-Language/druntime/archive/v%{version}.tar.gz#/druntime-%{version}.tar.gz
Source2:        https://github.com/D-Programming-Language/phobos/archive/v%{version}.tar.gz#/phobos-%{version}.tar.gz
Source8:        http://downloads.dlang.org/releases/2.x/%{bootstrap_version}/dmd.%{bootstrap_version}.linux.tar.xz
Source9:        dmd.conf
# PATCH-FIX-OPENSUSE dmd_use_tarball_bootstrap.diff So the tarball is not downloaded
Patch0:         dmd_use_tarball_bootstrap.diff
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  xz
Recommends:     phobos-devel
# Bootstrap is only possible with x86*
ExclusiveArch:  %{ix86} x86_64
%ifarch i586
#!BuildIgnore:  gcc-PIE
%endif
%if !%{auto_bootstrap}
BuildRequires:  dmd
BuildRequires:  phobos-devel-static
%endif

%description
The D programming language is an object-oriented, imperative,
multi-paradigm system programming language. It has type inference,
automatic memory management and syntactic sugar for common types,
bounds checking, design by contract features, and a concurrency-aware
type system.

%package 	-n 	libphobos2-%{sover}
Summary:        Standard library for the D language
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n libphobos2-%{sover}
Phobos is the standard library for the D Programming Language.

This package contains the shared library needed to run programs compiled with
dmd.

%package 	-n 	phobos-devel
Summary:        Development files for the D standard library
Group:          Development/Libraries/Other
Requires:       libphobos2-%{sover} = %{version}

%description -n phobos-devel
Phobos is the standard library for the D Programming Language.

This package contains the includes needed to compile programs against Phobos.

%package 	-n 	phobos-devel-static
Summary:        Development files for the D standard library
Group:          Development/Libraries/Other
Requires:       phobos-devel = %{version}

%description -n phobos-devel-static
Phobos is the standard library for the D Programming Language.

This package contains the static library for static linking. You don't need
this, unless you link statically, which is highly discouraged.

%prep
%setup -q
%setup -q -T -D -a 1
%setup -q -T -D -a 2
%patch0 -p1
echo %{version} > phobos-%{version}/VERSION
cd %{_builddir}
ln -s dmd-%{version} dmd
ln -s druntime-%{version} druntime
ln -s phobos-%{version} phobos
mv dmd-%{version}/druntime-%{version} .
mv dmd-%{version}/phobos-%{version} .

%build
# dmd
cd ..
pushd dmd
	make %{?_smp_mflags} -f posix.mak \
	%if %{auto_bootstrap}
		AUTO_BOOTSTRAP=1 \
		HOST_DMD_VER=%{bootstrap_version} \
	%endif
		BUILD=release \
		PIC=1 \
		ENABLE_RELEASE=1
popd

# druntime
pushd druntime
	make %{?_smp_mflags} -f posix.mak \
		BUILD=release \
		DMD="../dmd/generated/linux/release/*/dmd" \
		PIC=1 \
		ENABLE_RELEASE=1
popd

# phobos
pushd phobos
	make %{?_smp_mflags} -f posix.mak \
		BUILD=release \
		DMD="../dmd/generated/linux/release/*/dmd" \
		PIC=1 \
		ENABLE_RELEASE=1
popd

%install
# install files manually since the install script distributed put files all over the place
# dmd
install -dm755 %{buildroot}%{_bindir}
install -Dm755 %{_builddir}/dmd/generated/linux/release/*/dmd %{buildroot}%{_bindir}/dmd

install -dm755 %{buildroot}%{_sysconfdir}
install -Dm644 %{_sourcedir}/dmd.conf %{buildroot}%{_sysconfdir}/dmd.conf

install -dm755 %{buildroot}%{_mandir}
cp -r %{_builddir}/dmd/docs/man/* %{buildroot}%{_mandir}/

install -dm755 %{buildroot}%{_datadir}/licenses/dmd
install -Dm644 %{_builddir}/dmd/LICENSE.txt %{buildroot}%{_datadir}/licenses/dmd/LICENSE.txt

install -dm755 %{buildroot}%{_datadir}/%{name}/samples
cp -r %{_builddir}/dmd/samples/* %{buildroot}%{_datadir}/dmd/samples/

# phobos
install -dm755 %{buildroot}%{_libdir}
cp -a $(find %{_builddir}/phobos/generated/linux/release/ \( -iname "*.a" -a \! -iname "*.so.a" \) -o \( -iname "*.so*" -a \! -iname "*.o" -a \! -iname "*.a" \) ) %{buildroot}%{_libdir}

install -dm755 %{buildroot}%{_includedir}/dlang/dmd
cp -r %{_builddir}/phobos/{*.d,etc,std} %{buildroot}%{_includedir}/dlang/dmd
cp -r %{_builddir}/druntime/import/* %{buildroot}%{_includedir}/dlang/dmd/

%fdupes %{buildroot}

/sbin/ldconfig -N %{buildroot}%{_libdir}

%post   -n libphobos2-%{sover} -p /sbin/ldconfig
%postun -n libphobos2-%{sover} -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE.txt
%config(noreplace) %{_sysconfdir}/dmd.conf
%{_bindir}/dmd
%{_datadir}/dmd
%{_mandir}/man*/*

%files -n libphobos2-%{sover}
%{_libdir}/libphobos2.so.*

%files -n phobos-devel
%dir %{_includedir}/dlang
%dir %{_includedir}/dlang/dmd
%{_includedir}/dlang/dmd/*
%{_libdir}/libphobos2.so

%files -n phobos-devel-static
%{_libdir}/libphobos2.a

%changelog
