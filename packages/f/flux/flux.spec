#
# spec file for package flux
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

%define libflux_suffix %(echo %{version} | tr . _)

Name:           flux
Version:        0.196.1
Release:        0
Summary:        Influx data language
License:        Apache-2.0 AND MIT AND (Apache-2.0 OR MIT) AND Apache-2.0 WITH LLVM-exception AND CC-BY-3.0 AND CC-BY-SA-4.0 AND (Apache-2.0 OR BSL-1.0) AND BSD-3-Clause AND MPL-2.0 AND Zlib AND X11 AND Unicode-DFS-2016 AND Unicode-TOU
URL:            https://github.com/influxdata/flux
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Patch1:         disable-static-library.patch
Patch2:         fix-unsigned-char.patch
Patch3:         allow-missing-docs-for-tests-modules.patch
BuildRequires:  cargo
BuildRequires:  rust
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Flux is a lightweight scripting language for querying databases (like InfluxDB)
and working with data. It is part of InfluxDB 1.7 and 2.0, but can be run
independently of those. This repository contains the language definition and an
implementation of the language core.

%package -n libflux%{libflux_suffix}
Summary:        Influx data language
Provides:       libflux = %{version}-%{release}

%description -n libflux%{libflux_suffix}
Flux is a lightweight scripting language for querying databases (like InfluxDB)
and working with data. It is part of InfluxDB 1.7 and 2.0, but can be run
independently of those. This repository contains the language definition and an
implementation of the language core.

%package -n libflux-devel
Summary:        Development libraries and header files for Influx data language
Requires:       libflux%{libflux_suffix} = %{version}-%{release}

%description -n libflux-devel
This package contains the header files and libraries for building
programs using Influx data language.

%prep
%setup -q
pushd libflux
tar -Jxf %{SOURCE1}

patch -p2 < %{PATCH1}
patch -p2 < %{PATCH2}
patch -p2 < %{PATCH3}
patch -p2 <<EOF
--- a/libflux/flux/build.rs
+++ b/libflux/flux/build.rs
@@ -79,5 +79,7 @@ fn main() -> Result<()> {
     let path = dir.join("stdlib.data");
     serialize(Environment::from(imports), fb::build_env, &path)?;

+    println!("cargo:rustc-cdylib-link-arg=-Wl,-soname,libflux.so.%{version}");
+
     Ok(())
 }
EOF
popd

%build
pushd libflux
RUSTFLAGS=%{rustflags} cargo build --release
RUSTFLAGS=%{rustflags} cargo build --features=doc --release --bin fluxdoc
popd

%install
install -D -m 644 libflux/include/influxdata/flux.h %{buildroot}%{_includedir}/influxdata/flux.h
install -D -m 755 libflux/target/release/libflux.so %{buildroot}%{_libdir}/libflux.so.%{version}
ln -sf ./libflux.so.%{version} %{buildroot}%{_libdir}/libflux.so

cat > flux.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name:           Flux
Version:        %{version}
Description: Library for the InfluxData Flux engine
Libs: -L%{_libdir} -lflux
Libs.private: -ldl -lpthread
Cflags: -I%{_includedir}
EOF

install -D -m 644 flux.pc %{buildroot}%{_libdir}/pkgconfig/flux.pc

install -D -m 755 libflux/target/release/fluxdoc %{buildroot}%{_bindir}/fluxdoc

%check
pushd libflux
RUSTFLAGS=%{rustflags} cargo test --release
popd

%post -n libflux%{libflux_suffix} -p /sbin/ldconfig
%postun -n libflux%{libflux_suffix} -p /sbin/ldconfig

%files -n libflux%{libflux_suffix}
%{_libdir}/libflux.so.%{version}

%files -n libflux-devel
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/fluxdoc
%{_libdir}/libflux.so
%{_libdir}/pkgconfig/flux.pc
%dir %{_includedir}/influxdata
%{_includedir}/influxdata/flux.h

%changelog
