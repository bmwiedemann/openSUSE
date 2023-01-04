#
# spec file for package rav1e
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020 Andreas Schneider <asn@cryptomilk.org>.
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


Name:           rav1e
Version:        0.6.2+0
Release:        0
Summary:        Fastest and safest AV1 encoder
License:        BSD-2-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/xiph/rav1e
#
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source98:       README.suse-maint
Source99:       baselibs.conf
#
Patch0:         rav1e-cargo-no-git-default.patch
#
BuildRequires:  cargo-c
BuildRequires:  cargo-packaging
BuildRequires:  nasm

%description
rav1e is an AV1 video encoder.

AV1 is a video codec by the Alliance for Open Media, composed of most
of the important Web companies (Google, Facebook, Netflix, Amazon,
Microsoft, Mozilla...).

AV1 has the potential to be up to 20% better than the HEVC codec, but
the patents license is totally free, while HEVC patents licenses are
insanely high and very confusing.

rav1e features:

* Intra and inter frames
* 64x64 superblocks
* 4x4 to 64x64 RDO-selected square and 2:1/1:2 rectangular blocks
* DC, H, V, Paeth, smooth, and a subset of directional prediction modes
* DCT, (FLIP-)ADST and identity transforms (up to 64x64, 16x16 and 32x32 respectively)
* 8-, 10- and 12-bit depth color
* 4:2:0 (full support), 4:2:2 and 4:4:4 (limited) chroma sampling
* Variable speed settings
* Near real-time encoding at high speed levels

%package -n librav1e0
Summary:        AV1 encoder library
Group:          System/Libraries

%description -n librav1e0
rav1e is an AV1 video encoder libary. It is designed to eventually cover all
use cases, though in its current form it is most suitable for cases where
libaom (the reference encoder) is too slow.

%package devel
Summary:        Development files for rav1e
Group:          Development/Libraries/C and C++
Requires:       librav1e0 = %{version}

%description devel
The rav1e-devel package contains libraries and header files for
developing applications that use rav1e.

%prep
%autosetup -a1 -p1

install -d -m 0755 .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
[term]
verbose = true
EOF
rm -f Cargo.lock

# Disable rav1e_js
sed -i 's/"rav1e_js", //' Cargo.toml

%build
%{cargo_build}
CFLAGS="%{optflags}" cargo cbuild

%install
%{cargo_install}
rm -rf %{buildroot}%{_datadir}/cargo

cargo cinstall \
    --destdir=%{buildroot} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --pkgconfigdir=%{_libdir}/pkgconfig
rm -f %{buildroot}%{_libdir}/librav1e.a
rm -f %{buildroot}%{_prefix}/.crates*

%post   -n librav1e0 -p /sbin/ldconfig
%postun -n librav1e0 -p /sbin/ldconfig

%files
%{_bindir}/rav1e

%files -n librav1e0
%license LICENSE
%{_libdir}/librav1e.so.*

%files devel
%license LICENSE
%doc README.md doc/GLOSSARY.md PATENTS
%dir %{_includedir}/rav1e
%{_includedir}/rav1e/rav1e.h
%{_libdir}/librav1e.so
%{_libdir}/pkgconfig/rav1e.pc

%changelog
