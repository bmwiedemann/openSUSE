#
# spec file for package python-ruff
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without libalternatives
Name:           python-ruff
Version:        0.16.2
Release:        0
Summary:        An extremely fast Python linter, written in Rust
# Legal-Review-Notice: ruff itself is MIT, but the binary statically links
# the vendored Rust dependencies. Re-derived on this re-vendor with
# "cargo tree --offline -p ruff -e normal" over the vendored tree (381
# crates): the only copyleft licence in the linked graph is MPL-2.0, from
# three crates -
#  - colored, a direct dependency of ruff and ruff_linter,
#  - option-ext, pulled in through shellexpand -> dirs -> dirs-sys,
#  - version-ranges, pulled in through pyproject-toml -> pep508_rs ->
#    pep440_rs.
# r-efi offers an LGPL-2.1-or-later option but is UEFI-target-only and is
# absent from the Linux graph. Everything else is permissive (MIT,
# Apache-2.0, Unicode-3.0, BSD, ISC, Zlib, Unlicense, 0BSD, CC0-1.0,
# WTFPL, BSL-1.0). MPL-2.0 section 3.2 is satisfied because the complete
# vendor.tar.zst ships in the src.rpm.
License:        MIT AND MPL-2.0
URL:            https://github.com/astral-sh/ruff
Source:         https://files.pythonhosted.org/packages/source/r/ruff/ruff-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Provides:       ruff = %{version}-%{release}
%python_subpackages

%description
Ruff extremely fast Python linter written in rust supperseding many other linting tools

%prep
%autosetup -a1 -p1 -n ruff-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/ruff
%python_group_libalternatives ruff

%pre
%python_libalternatives_reset_alternative ruff

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/ruff
%{python_sitearch}/ruff
%{python_sitearch}/ruff-%{version}.dist-info

%changelog
