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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%global debug_package %{nil}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define origname python-ruff
%bcond_without libalternatives
Name:           %{origname}%{psuffix}
Version:        0.16.3
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
BuildRequires:  cargo-packaging
# The test flavour only builds and runs the Rust test suite. It needs no
# Python at all, so it skips the singlespec machinery entirely - running
# cargo test once per Python flavour would double the cost for no gain.
# Everything below is guarded so the test flavour advertises no providers.
# NOTE: spec-cleaner wants to hoist %%python_subpackages out of this %%if -
# do not apply that, it makes the test flavour declare a phantom
# python313-ruff-test subpackage that OBS then parses for scheduling.
%if %{without test}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Provides:       ruff = %{version}-%{release}
%python_subpackages
%endif

%description
Ruff extremely fast Python linter written in rust supperseding many other linting tools

%prep
%autosetup -a1 -p1 -n ruff-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%if %{without test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/ruff
%python_group_libalternatives ruff
%endif

%if %{with test}
%check
# The PyPI sdist does not ship crates/ruff_linter/resources/test/fixtures/,
# so every ruff_linter rule test that reads a fixture file fails on a missing
# path (2209 of its 2807 tests). Exclude that one crate, plus the single ruff
# test that walks the same fixture tree, instead of disabling the whole suite -
# the rest of the workspace (parser, formatter, semantic model, notebooks, CLI,
# server, doctests) runs entirely offline against the vendored dev-dependencies.
# The leading "--" is required: %%cargo_test is a parametrised macro, so
# without it rpm parses "--workspace" as a macro option and aborts the build.
%{cargo_test -- --workspace --exclude ruff_linter -- --skip cache::tests::same_results::ruff_linter_fixtures}
%endif

%if %{without test}
%pre
%python_libalternatives_reset_alternative ruff

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/ruff
%{python_sitearch}/ruff
%{python_sitearch}/ruff-%{version}.dist-info
%endif

%changelog
