#
# spec file for package wayshot
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

Name:           wayshot
Version:        1.3.1+git56.g28331dcc3886f8b9e6bc09f9951fe59744c16acf
Release:        0
Summary:        Screenshot tool for wlroots based compositors
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND BSD-3-Clause AND ISC AND MIT AND Zlib AND BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            https://github.com/waycrate/wayshot
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
%if 0%{?suse_version} >= 1500
BuildRequires:  cargo-packaging
%else
BuildRequires:  cargo
%endif
BuildRequires:  Mesa-libEGL-devel
BuildRequires:  libgbm-devel
BuildRequires:  zstd
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)

%description
A screenshot tool for wlroots based compositors implementing zwlr_screencopy_v1

%prep
%autosetup -a1

%build
export CARGO_HOME=$PWD/.cargo
export CARGO_TARGET_DIR=$PWD/target
ls -la $CARGO_HOME
pushd wayshot
%if 0%{?suse_version} >= 1500
RUSTFLAGS=%{rustflags} %{cargo_build}
%else
RUSTFLAGS=%{rustflags} cargo build --offline --release
%endif
popd

%install
# cargo install does not work with cached cargo home
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 -t %{buildroot}%{_bindir}/ %{_builddir}/%{name}-%{version}/target/release/wayshot

%files
%{_bindir}/wayshot
%license LICENSE
%doc README.md

%changelog
