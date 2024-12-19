#
# spec file for package lychee
#
# Copyright (c) 2024 SUSE LLC
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


Name:           lychee
Version:        0.18.0~0
Release:        0
Summary:        Fast, async, stream-based link checker written in Rust
License:        Apache-2.0 OR MIT
URL:            https://lychee.cli.rs
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  libopenssl-devel
ExclusiveArch:  %{rust_tier1_arches}

%description
Fast, async, stream-based link checker written in Rust. Finds broken URLs and mail addresses inside Markdown, HTML, reStructuredText, websites and more!

%prep
%autosetup -p1 -a1

%build
%{cargo_build} --all

%install
%{cargo_install -p lychee-bin}

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%{_bindir}/%{name}

%changelog
