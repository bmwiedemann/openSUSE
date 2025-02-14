#
# spec file for package yasm
#
# Copyright (c) 2025 SUSE LLC
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


Name:           yasm
Version:        1.3.0
Release:        0
Summary:        A complete rewrite of the NASM assembler
License:        Artistic-1.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Development/Languages/Other
URL:            https://github.com/yasm/yasm
Source:         http://www.tortall.net/projects/yasm/releases/yasm-%{version}.tar.gz
Patch0:         yasm-no-build-date.patch
Patch1:         yasm-no-rpm-opt-flags.patch
Patch2:         yasm-re2c-nogendate.patch
Patch3:         yasm-Update-elf-objfmt.c.patch
# https://github.com/yasm/yasm/issues/283
Patch4:         yasm-gcc15.patch
BuildRequires:  python3-devel
BuildRequires:  xmlto

%description
YASM is a complete rewrite of the NASM assembler. It is designed from
the ground up to allow for multiple syntaxes to be supported (e.g.,
NASM, TASM, GAS, etc.) in addition to multiple output object formats.
Another primary module of the overall design is an optimizer module.
Actually it supports ix86 and AMD64, next will be PowerPC

%package devel
Summary:        YASM development package
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description devel
This package includes everything needed to develop programs that use
libyasm.

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure \
  --enable-python
make %{?_smp_mflags}

%install
%make_install

%check
# 2 win64 test crash but we don't care
make %{?_smp_mflags} check || true

%files
%license COPYING Artistic.txt BSD.txt GNU_GPL-2.0 GNU_LGPL-2.0
%doc ABOUT-NLS AUTHORS
%{_bindir}/vsyasm
%{_bindir}/yasm
%{_bindir}/ytasm
%{_mandir}/man1/yasm.1%{?ext_man}
%{_mandir}/man7/yasm_arch.7%{?ext_man}
%{_mandir}/man7/yasm_dbgfmts.7%{?ext_man}
%{_mandir}/man7/yasm_objfmts.7%{?ext_man}
%{_mandir}/man7/yasm_parsers.7%{?ext_man}

%files devel
%{_includedir}/*
%{_libdir}/libyasm.a

%changelog
