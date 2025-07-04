#
# spec file for package tiny
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


Name:           tiny
Version:        0.13.0+git5.g2ee969a
Release:        0
Summary:        Terminal IRC client written in Rust
License:        (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR BSD-2-Clause) AND (MIT OR Unlicense) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND MIT
URL:            https://github.com/osa1/tiny
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  zstd
BuildRequires:  pkgconfig(dbus-1)

%description
A terminal IRC client written in Rust.

%prep
%autosetup -a1

%build
%{cargo_build} --features desktop-notifications

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/tiny %{buildroot}%{_bindir}/tiny

%check
%{cargo_test} --workspace --exclude '*termbox*'

%files
%license LICENSE
%doc     README.md CHANGELOG.md
%{_bindir}/tiny

%changelog
