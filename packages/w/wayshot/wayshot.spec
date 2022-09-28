#
# spec file for package wayshot
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

Name:           wayshot
Version:        1.2.2
Release:        0
Summary:        Screenshot tool for wlroots based compositors
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND BSD-3-Clause AND ISC AND MIT AND Zlib AND BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            https://github.com/waycrate/wayshot
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
%if 0%{?suse_version} >= 1500
BuildRequires:  cargo-packaging
%else
BuildRequires:  cargo
%endif

%description
A screenshot tool for wlroots based compositors implementing zwlr_screencopy_v1

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%if 0%{?suse_version} >= 1500
RUSTFLAGS=%{rustflags} %{cargo_build}
%else
sed -i 's/2021/2018/g' Cargo.toml
RUSTFLAGS=%{rustflags} cargo build --offline --release
%endif

%install
%if 0%{?suse_version} >= 1500
RUSTFLAGS=%{rustflags} %{cargo_install}
%else
RUSTFLAGS=%{rustflags} cargo install --root=%{buildroot}%{_prefix} --path .
%endif

%files
%{_bindir}/wayshot
%license LICENSE
%doc README.md

%changelog
