#
# spec file for package arti
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


Name:           arti
#               This will be set by osc services, that will run after this.
Version:        1.1.9~0
Release:        0
Summary:        An implementation of Tor, in Rust.
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        Apache-2.0 OR MIT
URL:            https://gitlab.torproject.org/tpo/core/arti
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zstd
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
# Disable this line if you wish to support all platforms.
# In most situations, you will likely only target tier1 arches for user facing components.
ExclusiveArch:  %{rust_tier1_arches}

%description
An implementation of Tor, in Rust.

%prep
%autosetup -p1 -a1
install -D -m 644 %{SOURCE2} .cargo/config
# Remove exec bits to prevent an issue in fedora shebang checking. Uncomment only if required.
# find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
%{cargo_build}

%install
%{cargo_install -p crates/arti}

%check
%{cargo_test}

%files
%{_bindir}/%{name}

%changelog
