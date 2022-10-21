#
# spec file for package flux
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

%define libflux_suffix %(echo %{version} | tr . _)

Name:           flux
Version:        0.171.0
Release:        0
Summary:        Influx data language
License:        MIT
URL:            https://github.com/influxdata/flux
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Patch1:         disable-static-library.patch
Patch2:         0001-fix-compile-error-with-Rust-1.64-5273.patch
BuildRequires:  cargo
BuildRequires:  rust >= 1.45
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
install -D %{SOURCE2} .cargo/config

patch -p2 < %{PATCH1}
patch -p2 < %{PATCH2}
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
RUSTFLAGS=%{rustflags} cargo build --release --bin fluxc
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

install -D -m 755 libflux/target/release/fluxc %{buildroot}%{_bindir}/fluxc
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
%{_bindir}/fluxc
%{_bindir}/fluxdoc
%{_libdir}/libflux.so
%{_libdir}/pkgconfig/flux.pc
%dir %{_includedir}/influxdata
%{_includedir}/influxdata/flux.h

%changelog
