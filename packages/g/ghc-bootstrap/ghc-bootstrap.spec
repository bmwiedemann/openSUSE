#
# spec file for package ghc-bootstrap
#
# Copyright (c) 2023 SUSE LLC
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


%global llvm_major 15
%ifarch ppc64le
%define longarch powerpc64le
# something weird on ghc arch detection
%define arch ppc64
%endif
%ifarch s390x
%define longarch s390x
%define sysname ibm
%define arch s390x
%endif
%ifarch aarch64
%define longarch aarch64
%define arch aarch64
%endif
%ifarch x86_64
%define longarch x86_64
%define sysname unknown
%define arch x86_64
%endif
%ifarch riscv64
%define longarch riscv64
%define arch riscv64
%endif
%ifarch ppc64le aarch64 riscv64
%define sysname unknown
%endif
Name:           ghc-bootstrap
Version:        9.8.2
Release:        0
Summary:        Binary distributions of The Glorious Glasgow Haskell Compiler
License:        BSD-3-Clause
URL:            https://build.opensuse.org/package/view_file/devel:languages:haskell:bootstrap
Source1:        README.openSUSE
Source2:        LICENSE
Source13:       ghc-%{version}-powerpc64le-unknown-linux.tar.xz
Source14:       ghc-%{version}-x86_64-unknown-linux.tar.xz
Source16:       ghc-%{version}-s390x-ibm-linux.tar.xz
Source17:       ghc-%{version}-aarch64-unknown-linux.tar.xz
Source19:       ghc-%{version}-riscv64-unknown-linux.tar.xz
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  gcc-PIE
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gmp-devel
BuildRequires:  libffi8 >= 3.4.4
BuildRequires:  libncurses5
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libffi)
Requires:       gmp-devel
Requires:       libffi8 >= 3.4.4
Requires:       libncurses5
Conflicts:      ghc-base
# This package is not meant to be used outside OBS
Requires:       this-is-only-for-build-envs
Requires:       pkgconfig(libffi)
Provides:       ghc-bootstrap-devel
ExclusiveArch:  ppc64le x86_64 s390x aarch64 riscv64
AutoReq:        off
%ifnarch s390x
BuildRequires:  libnuma-devel
%endif
%ifarch s390x riscv64
Requires:       clang%{llvm_major}
Requires:       llvm%{llvm_major}
%endif
%ifnarch s390x
Requires:       libffi-devel
Requires:       libnuma-devel
%endif

%description
This package contains a binary distribution of "The Glorious Glasgow
Haskell Compilation System". See README.openSUSE on how the tarballs
were produced.

Do not install this package! Install 'ghc' instead.

%prep
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE13} .
cp %{SOURCE14} .
cp %{SOURCE16} .
cp %{SOURCE17} .
cp %{SOURCE19} .

%build
tar Jxf ghc-%{version}-%{longarch}-%{sysname}-linux.tar.xz
cd ghc-%{version}-%{longarch}-%{sysname}-linux
# FIXME: you should use the %%configure macro

%install
cd ghc-%{version}-%{longarch}-%{sysname}-linux

./configure --prefix=/opt
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "/opt/lib/ghc-%{version}/lib/%{arch}-linux-ghc-%{version}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/ghc.conf
%make_install
%fdupes -s %{buildroot}
for i in $(find %{buildroot} -type f -executable -exec sh -c "file {} | grep -q 'dynamically linked'" \; -print); do
    chrpath -d $i
done

rm %{buildroot}/opt/lib/ghc-%{version}/lib/package.conf.d/.stamp
(cd %{buildroot}/opt/lib/ghc-%{version}/lib/package.conf.d/
for i in *.conf; do
    mv $i.copy $i
done
)

%post
/sbin/ldconfig
/opt/bin/ghc-pkg recache

%postun -p /sbin/ldconfig

%files
%doc README.openSUSE
%license LICENSE
/opt/*
%config %{_sysconfdir}/ld.so.conf.d/ghc.conf

%changelog
