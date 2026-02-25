#
# spec file for package resvg
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

%define soname  0
%bcond_without check
Name:           resvg
Version:        0.47.0
Release:        0
Summary:        SVG rendering library
License:        Apache-2.0 OR MIT
Group:          Productivity/Graphics/Convertors
URL:            https://github.com/linebender/resvg
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  zstd
ExclusiveArch:  %{rust_arches}

%description
resvg is an SVG rendering library.
It can be used as a Rust library, as a C library, and as a CLI
application to render static SVG files.
The core idea is to make a fast, small, portable SVG library with the goal to
support the whole SVG spec.
Features:
* Designed for edge-cases
* Safety
* Zero bloat
* Portable
* SVG preprocessing
* Performance
* Reproducibility

%package -n usvg
Summary:        SVG simplification tool
Group:          Productivity/Graphics/Convertors

%description -n usvg
usvg is a command-line utility to simplify SVG files based on a static
SVG Full 1.1 subset. It converts an input SVG to an extremely
simple representation, which is still a valid SVG:
* No basic shapes (rect, circle, etc), only paths
* Only simple paths
* All supported attributes are resolved
* Invisible elements are removed
* Comments will be removed
* DTD will be resolved
* CSS will be resolved
and so on.

%package -n lib%{name}%{soname}
Summary:        SVG rendering library (C++/Qt API)
Group:          Development/Libraries/C and C++

%description -n lib%{name}%{soname}
An SVG rendering library (C++/Qt API).
This package contains shared library.

%package devel
Summary:        SVG rendering library (C++/Qt API)
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{soname} = %{version}-%{release}

%description devel
An SVG rendering library (C++/Qt API).
This package contains development files for %{name}.

%package devel-static
Summary:        SVG rendering library (C++/Qt API)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}-%{release}

%description devel-static
An SVG rendering library (C++/Qt API).
This package contains development files for %{name}.

It contains static libraries for -static linking which is highly discouraged.

%prep
%autosetup -p1 -a1

%build
%global build_rustflags  -Clink-arg=-Wl,-z,relro,-z,now,-soname,libresvg.so.%{soname} -C debuginfo=2 -C strip=none
%{cargo_build} --all

%install
#%%{cargo_install}
install -Dm 0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 ./target/release/usvg %{buildroot}%{_bindir}/usvg
install -Dm 0755 ./target/release/lib%{name}.so %{buildroot}%{_libdir}/lib%{name}.so.%{version}
ln -sf lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so.%{soname}
ln -sf lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so
install -Dm 0644 ./target/release/lib%{name}.a %{buildroot}%{_libdir}/lib%{name}.a
install -Dm 0644 ./crates/c-api/*.h -t %{buildroot}%{_includedir}/

%if %{with check}
%check
%{cargo_test}
%endif

%ldconfig_scriptlets -n lib%{name}%{soname}

%files
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/%{name}
%license LICENSE-APACHE LICENSE-MIT

%files -n usvg
%{_bindir}/usvg

%files -n lib%{name}%{soname}
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_includedir}/ResvgQt.h

%files devel-static
%{_libdir}/lib%{name}.a

%changelog
