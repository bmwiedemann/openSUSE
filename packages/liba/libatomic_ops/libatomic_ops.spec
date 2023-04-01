#
# spec file for package libatomic_ops
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


Name:           libatomic_ops
Version:        7.8.0
Release:        0
Summary:        A portable library for atomic memory operations
License:        GPL-2.0-or-later AND MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/ivmai/libatomic_ops
Source:         https://github.com/ivmai/libatomic_ops/releases/download/v%version/%name-%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
Provides implementations for atomic memory update operations on a
number of architectures. This allows direct use of these in reasonably
portable code. Unlike earlier similar packages, this one explicitly
considers memory barrier semantics, and allows the construction of code
that involves minimum overhead across a variety of architectures.

%package devel
Summary:        A portable library for atomic memory operations
Group:          Development/Languages/C and C++
Obsoletes:      libatomic-ops-devel < %version-%release
Provides:       libatomic-ops-devel = %version-%release

%description devel
Provides implementations for atomic memory update operations on a
number of architectures. This allows direct use of these in reasonably
portable code. Unlike earlier similar packages, this one explicitly
considers memory barrier semantics, and allows the construction of code
that involves minimum overhead across a variety of architectures.

%prep
%autosetup

%build
%global _lto_cflags %_lto_cflags -ffat-lto-objects
autoreconf -fiv
%configure --docdir="%_docdir/%name"
%make_build

%install
%make_install
rm -fv "%buildroot/%_libdir"/*.la
cp -av ChangeLog "%buildroot/%_docdir/%name/"

%check
%if !0%{?qemu_user_space_build:1}
%make_build check
%endif

%files devel
%_libdir/libatomic_ops*.a
%_includedir/atomic_ops/
%_includedir/atomic_ops*.h
%_libdir/pkgconfig/atomic_ops.pc
%_docdir/%name/

%changelog
