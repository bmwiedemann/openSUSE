#
# spec file for package hare
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


%bcond_without  test
%define relver 0.25.2
Name:           hare
Release:        0
Version:        0.26.0
Summary:        Hare system programming language
Group:          Development/Tools/Building
License:        MPL-2.0
URL:            https://harelang.org
Source0:        %{name}-%{version}.tar.zst
Source1:        %{name}-rpmlintrc
Source2:        README-suse-maint.md
Source3:        roast_scm.info
BuildRequires:  binutils
BuildRequires:  gcc
# Hare and the HareC compiler should have the same version
BuildRequires:  harec >= %{relver}
BuildRequires:  make
BuildRequires:  qbe
BuildRequires:  scdoc
BuildRequires:  timezone
BuildRequires:  zstd
Requires:       harec >= %{relver}
# Hare requires QBE 1.2 like HareC does
Requires:       qbe = 1.2
Requires:       timezone

%description
Hare is a systems programming language designed
to be simple, stable, and robust. Hare uses a
static type system, manual memory management,
and a minimal runtime. It is well-suited to
writing operating systems, system tools, compilers,
networking software, and other low-level, high
performance tasks

%prep
%autosetup -p1

cat > config.mk <<-SH
## Install configuration
PREFIX = %{_prefix}
BINDIR = %{_bindir}
MANDIR = %{_mandir}
SRCDIR = %{_prefix}/src
STDLIB = %{_prefix}/src/%{name}/stdlib

## Build configuration

# variables used during the build
PLATFORM = linux
ARCH = %{_arch}
HAREFLAGS =
HARECFLAGS =
QBEFLAGS =
ASFLAGS =
LDLINKFLAGS = --gc-sections -z noexecstack

# commands used by the build script
HAREC = harec
HAREFLAGS =
QBE = qbe
AS = as
LD = ld
AR = ar
SCDOC = scdoc

# build locations
HARECACHE = .cache
BINOUT = .bin

# variables that will be embedded in the binary with the -D definitions
HAREPATH = %{_prefix}/src/%{name}/stdlib:%{_prefix}/src/%{name}/third-party
VERSION  = %{version}

# Cross-compiler toolchains
AARCH64_AS=as
AARCH64_AR=ar
AARCH64_CC=cc
AARCH64_LD=ld

RISCV64_AS=as
RISCV64_AR=ar
RISCV64_CC=cc
RISCV64_LD=ld

X86_64_AS=as
X86_64_AR=ar
X86_64_CC=cc
X86_64_LD=ld
SH

cp config.mk configs/linux.mk

%build
export CFLAGS="%optflags -fPIE -Wl,-z,noexecstack"
export PLATFORM="linux"
export ARCH="%{_arch}"
make %{?_smp_mflags}

%install
export CFLAGS="%optflags -fPIE -Wl,-z,noexecstack"
export PLATFORM="linux"
export ARCH="%{_arch}"
make %{?_smp_mflags} DESTDIR="%{buildroot}" install

%if %{with test}
%check
# Enable only for tumbleweed/factory since
# Timezone package seems to fail this :D
%if 0%{?suse_version} > 1600
export CFLAGS="%optflags"
export PLATFORM="linux"
export ARCH="%{_arch}"
make %{?_smp_mflags} check
%endif
%endif

%files
%defattr(-,root,root)
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}doc
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{_prefix}/src/hare
%{_prefix}/src/hare/*

%changelog
