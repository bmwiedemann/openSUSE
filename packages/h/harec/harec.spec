#
# spec file for package harec
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


Name:           harec
Release:        0
Version:        0.24.2
Summary:        Bootstrap compiler for hare
Group:          Development/Tools/Building
URL:            https://git.sr.ht/~sircmpwn/harec
Source0:        https://git.sr.ht/~sircmpwn/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        README-suse-maint.md
BuildRequires:  make
BuildRequires:  qbe = 1.2
BuildRequires:  zstd
License:        GPL-3.0-only

%description

HareC is a bootstrap compiler for the Hare programming language. Written in C11 for
POSIX-compatible systems.

%prep
%setup -q

%build
cat > config.mk <<-SH
PREFIX = %{_prefix}
BINDIR = %{_bindir}

PLATFORM = linux
ARCH = %{_arch}
HARECFLAGS =
QBEFLAGS =
ASFLAGS =
LDLINKFLAGS = --gc-sections -z noexecstack
CFLAGS = %{optflags} -Iinclude
LDFLAGS =
LIBS = -lm

CC = cc
AS = as
LD = ld
QBE = qbe

HARECACHE = .cache
BINOUT = .bin

DEFAULT_TARGET = %{_arch}
VERSION = %{version}
SH

%make_build

%install
%make_build DESTDIR=%{buildroot} install

# Test suite only available for those architectures
%ifarch aarch64 riscv64 x86_64
%check
%make_build check
%endif

%files
%{_bindir}/%{name}
%license COPYING
%doc     README.md

%changelog
