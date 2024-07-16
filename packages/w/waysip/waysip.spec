#
# spec file for package waysip
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           waysip
Version:        0.2.3
Release:        0
Summary:        Screen region selector for wayland compositors
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://github.com/waycrate/waysip
Source0:        https://github.com/waycrate/waysip/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
%if 0%{?suse_version} >= 1500
BuildRequires:  cargo-packaging
%else
BuildRequires:  cargo
%endif
BuildRequires:  zstd
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(pangocairo)

%description
A screen region selection tool like slurp but with added dynamic labels of region dimensions and size.

%prep
%autosetup -a1

%build
pushd waysip
%if 0%{?suse_version} >= 1500
RUSTFLAGS=%{rustflags} %{cargo_build}
%else
RUSTFLAGS=%{rustflags} cargo build --offline --release
%endif
popd

%install
pushd waysip
%if 0%{?suse_version} >= 1500
RUSTFLAGS=%{rustflags} %{cargo_install}
%else
RUSTFLAGS=%{rustflags} cargo install --root=%{buildroot}%{_prefix} --path .
%endif
popd

%files
%{_bindir}/waysip
%license LICENSE
%doc README.md

%changelog
