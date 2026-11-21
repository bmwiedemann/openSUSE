#
# spec file for package python-frostwork
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
%{?sle15_python_module_pythons}
Name:           python-frostwork
Version:        0.2.2
Release:        0
Summary:        Treeless, one-pass HTML extraction with CSS/XPath selectors
# Legal-Review-Notice: linked Rust graph is copyleft-free (re-derived
# with "cargo tree --offline --features python -e normal" over vendor.tar.xz)
# - 49 crates, all permissive: MIT/Apache-2.0, BSD-3-Clause (encoding_rs),
#   Unicode-3.0 (ICU), Unlicense (memchr); no GPL/LGPL/AGPL/MPL/EPL/CDDL
License:        Apache-2.0
URL:            https://github.com/scrapy/frostwork
Source0:        https://files.pythonhosted.org/packages/source/f/frostwork/frostwork-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module maturin >= 1.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typing-extensions >= 4.13}
BuildRequires:  alts
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-typing-extensions >= 4.13
# SECTION test
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module parsel}
BuildRequires:  %{python_module pytest}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
Frostwork compiles a set of CSS or XPath selectors and extracts their
values in one scan of an HTML response, without building a DOM. The
Python package ships the compiled Rust core plus a declarative
Page/Item layer, a web-poet page-object integration (in the unbuilt
`webpoet` extra) and the `frostwork-audit` schema-audit CLI.

%prep
%autosetup -p1 -a1 -n frostwork-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/frostwork-audit
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# web-poet, andi, zyte-common-items not in Factory; css_escapes, has_*,
# flag and grammar cases expect errors only cssselect < 1.6 raises;
# releases_gil times threads, mutation_sweep/version_guard need libxml2 2.15
donttest="frostpage or webpoet_groups or web_poet or attrs_define"
donttest+=" or browser_page or re_first or many_yields or many_builds"
donttest+=" or one_yields or field_missing_from or marker_on_a_non"
donttest+=" or frostwork_input or input_hook or field_all_and_join"
donttest+=" or scan_covers or audit_cli_audits or webpoet_gate"
donttest+=" or required_column or raw_source_allowance"
donttest+=" or processor_registry or changes_a_default or surface_gate"
donttest+=" or non_executable_css_escapes or has_widened_inners"
donttest+=" or has_selector_list_matches"
donttest+=" or attribute_case_insensitive_flag or selector_grammar_surface"
donttest+=" or releases_gil or mutation_sweep_enumerates or oracle_version_guard"
%pytest_arch -m "not webpoet_contract" -k "not ($donttest)"

%pre
%python_libalternatives_reset_alternative frostwork-audit

%files %python_files
%python_alternative %{_bindir}/frostwork-audit
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitearch}/frostwork
%{python_sitearch}/frostwork-%{version}.dist-info

%changelog
