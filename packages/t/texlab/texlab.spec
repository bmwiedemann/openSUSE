#
# spec file for package texlab
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


Name:           texlab
Version:        4.3.2
Release:        0
Summary:        Implementation of the Language Server Protocol for LaTeX
License:        ( 0BSD OR MIT OR Apache-2.0 ) AND ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR MIT ) AND ( Apache-2.0 OR Apache-2.0 OR MIT ) AND ( CC0-1.0 OR Artistic-2.0 ) AND ( MIT OR Apache-2.0 OR Zlib ) AND ( MIT OR Zlib OR Apache-2.0 ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND Apache-2.0 AND BSD-3-Clause AND GPL-3.0 AND GPL-3.0+ AND ISC AND MIT AND MPL-2.0 AND MPL-2.0+ AND GPL-3.0
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://github.com/latex-lsp/texlab
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo >= 1.59
ExclusiveArch:  %{rust_arches}

%description
Cross-platform implementation of the Language Server Protocol providing rich cross-editing support for the LaTeX typesetting system.
The server may be used with any editor that implements the Language Server Protocol.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

# They deleted it.
# install -Dm644 texlab.1 -t %%{buildroot}%%{_mandir}/man1/

#%%check
#%%{cargo_test}

%files
%{_bindir}/texlab
%license LICENSE
%doc README.md CHANGELOG.md
# %{_mandir}/man1/texlab.1%{?ext_man}

%changelog
