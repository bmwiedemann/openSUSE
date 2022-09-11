#
# spec file for package htscodecs
#
# Copyright (c) 2022 SUSE LLC
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


%define   sonum 2
Name:           htscodecs
Version:        1.3.0
Release:        0
Summary:        C library for custom compression for CRAM and other formats
License:        MIT
Group:          Productivity/Scientific/Other
URL:            https://github.com/samtools/htscodecs
Source0:        https://github.com/samtools/htscodecs/releases/download/v%{version}/htscodecs-%{version}.tar.gz
Source100:      baselibs.conf
# PATCH-FIX-UPSTREAM
Patch0:         https://github.com/samtools/htscodecs/commit/843d4f63b1c64905881b4648916a4d027baa1a1c.patch#/fix_ix86_build.patch
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)

%description
htscodecs provides an API to access CRAM codecs used for "EXTERNAL" block types.
These consist of two variants of the rANS codec (8-bit and 16-bit renormalisation,
with run-length encoding and bit-packing also supported in the latter),
a dynamic arithmetic coder, and custom codecs for name/ID compression
and quality score compression derived from fqzcomp.

%package -n lib%{name}%{sonum}
Summary:        C library for custom compression for CRAM and other formats
Group:          System/Libraries

%description -n lib%{name}%{sonum}
htscodecs provides an API to access CRAM codecs used for "EXTERNAL" block types.
These consist of two variants of the rANS codec (8-bit and 16-bit renormalisation,
with run-length encoding and bit-packing also supported in the latter),
a dynamic arithmetic coder, and custom codecs for name/ID compression
and quality score compression derived from fqzcomp.

%package devel
Summary:        Header files and libraries for compiling against %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sonum} = %{version}

%description devel
Header files and libraries of the samtools project for compiling against %{name}.

%prep
%autosetup -p1

%build
# Rebuild configure script after Patch0
autoconf
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la

%post   -n lib%{name}%{sonum} -p /sbin/ldconfig
%postun -n lib%{name}%{sonum} -p /sbin/ldconfig

%files -n lib%{name}%{sonum}
%license LICENSE.md
%{_libdir}/lib%{name}.so.*

%files devel
%doc README.md NEWS.md
%{_includedir}/htscodecs
%{_libdir}/lib%{name}.so

%changelog
