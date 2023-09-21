#
# spec file for package hoard
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


Name:           hoard
Version:        v.1.4.2~0
Release:        0
Summary:        CLI command organizer
License:        Apache-2.0 AND BSD-3-Clause AND GPL-2.0-only AND ISC AND MIT AND OpenSSL AND BSD-4-Clause AND CC-BY-3.0 AND CC-BY-SA-4.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND MPL-2.0 AND Zlib AND CC0-1.0
Group:          Productivity/File utilities
URL:            https://hyde46.github.io/hoard/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  libopenssl-devel

%description
Command organizer tool to hoard all your precious commands.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%{_bindir}/%{name}

%changelog
