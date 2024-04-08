#
# spec file for package pastel
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


Name:           pastel
Version:        0.9.0
Release:        0
Summary:        CLI to generate, analyze, convert and manipulate colors
License:        MIT AND Apache-2.0
Group:          Productivity/Graphics/Other
URL:            https://github.com/sharkdp/pastel
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  zstd
Recommends:     pastel-doc

%description
pastel is a command-line tool to generate, analyze, convert and manipulate
colors. It supports many different color formats and color spaces like RGB
(sRGB), HSL, CIELAB, CIELCh as well as ANSI 8-bit and 24-bit
representations.

%package doc
Summary:        Documentation for pastel
BuildArch:      noarch

%description doc
This package provides the documentation for pastel.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%check

%files
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/%{name}

%files doc
%doc README* doc

%changelog

