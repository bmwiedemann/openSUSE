#
# spec file for package ghc-bootstrap
#
# Copyright (c) 2021 SUSE LLC
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


%ifarch ppc
%define longarch powerpc
%endif
%ifarch ppc64
%define longarch powerpc64
%endif
%ifarch ppc64le
%define longarch powerpc64le
%endif
%ifarch s390
%define longarch s390
%endif
%ifarch s390x
%define longarch s390x
%endif
%ifarch aarch64
%define longarch aarch64
%endif
%ifarch %{arm}
%define longarch arm
%endif
%ifarch x86_64
%define longarch x86_64
%endif
%ifarch riscv64
%define longarch riscv64
%endif
%ifarch s390 s390x
%define sysname ibm
%endif
%ifarch x86_64
%define sysname unknown
%endif
%ifarch %{ix86}
%define sysname unknown
%endif
%ifarch ppc64 ppc64le %{arm} aarch64 riscv64
%define sysname unknown
%endif
Name:           ghc-bootstrap
Summary:        Binary distributions of The Glorious Glasgow Haskell Compiler
License:        BSD-3-Clause
URL:            https://build.opensuse.org/package/view_file/devel:languages:haskell:bootstrap
Source1:        README.openSUSE
Source2:        LICENSE
Source12:       ghc-8.10.1-powerpc64-unknown-linux.tar.xz
Source13:       ghc-8.10.1-powerpc64le-unknown-linux.tar.xz
Source14:       ghc-8.10.1-x86_64-unknown-linux.tar.xz
Source16:       ghc-8.10.2-s390x-ibm-linux.tar.xz
Source17:       ghc-8.10.1-aarch64-unknown-linux.tar.xz
Source18:       ghc-8.10.1-arm-unknown-linux.tar.xz
Source19:       ghc-8.10.1-riscv64-unknown-linux.tar.xz
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  libncurses5
BuildRequires:  pkgconfig(libffi)
BuildRequires:  libffi8 >= 3.4.4
Requires:       gmp-devel
Requires:       libncurses5
Requires:       pkgconfig(libffi)
Requires:       libffi8 >= 3.4.4
# This package is not meant to be used outside OBS
Requires:       this-is-only-for-build-envs
Provides:       ghc-bootstrap-devel
ExclusiveArch:  ppc64 ppc64le x86_64 s390x aarch64 %{arm} riscv64
AutoReq:        off
%ifnarch s390 s390x
Version:        8.10.1
Release:        0
%else
Version:        8.10.2
Release:        0
%endif
%ifnarch %{arm} s390x
BuildRequires:  libnuma-devel
%endif
%ifarch aarch64 %{arm}
Requires:       llvm
%endif
%ifnarch %{arm} s390x
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
cp %{SOURCE12} .
cp %{SOURCE13} .
cp %{SOURCE14} .
cp %{SOURCE16} .
cp %{SOURCE17} .
cp %{SOURCE18} .
cp %{SOURCE19} .

%build
tar Jxf ghc-%{version}-%{longarch}-%{sysname}-linux.tar.xz
cd ghc-%{version}
# FIXME: you should use the %%configure macro
./configure --prefix=/opt

%install
cd ghc-%{version}
%make_install
%fdupes -s %{buildroot}

%post
/opt/bin/ghc-pkg recache

%files
%doc README.openSUSE
%license LICENSE
/opt/*

%changelog
