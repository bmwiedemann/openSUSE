#
# spec file for package python-datamodel-code-generator
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


%define upname datamodel-code-generator
Name:           python-datamodel-code-generator
Version:        0.102.0
Release:        0
Summary:        Datamodel Code Generator
License:        MIT
URL:            https://github.com/koxudaxi/datamodel-code-generator/
Source0:        https://github.com/koxudaxi/datamodel-code-generator/archive/refs/tags/%{version}.tar.gz#/datamodel-code-generator-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0.1
Requires:       python-argcomplete >= 2.10.1
Requires:       python-black >= 19.10b0
Requires:       python-genson >= 1.2.1
Requires:       python-inflect >= 4.1.0
Requires:       python-isort >= 4.3.21
Requires:       python-jinja2 >= 2.10.1
Requires:       python-pydantic >= 2.12
Requires:       python-typing_extensions >= 4.16
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-PySnooper >= 0.4.1
Recommends:     python-graphql-core
Recommends:     python-grpcio-tools >= 1.62
Recommends:     python-httpx >= 0.24.1
Recommends:     python-openapi-spec-validator >= 0.2.8
Recommends:     python-prance >= 0.18.2
Recommends:     python-ruamel.yaml >= 0.5.1
Recommends:     python-ruff >= 0.9.10
Recommends:     python-watchfiles >= 1.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PySnooper >= 0.4.1}
BuildRequires:  %{python_module argcomplete >= 1.11.1}
BuildRequires:  %{python_module black >= 19.10b0}
BuildRequires:  %{python_module cryptography >= 50}
BuildRequires:  %{python_module email-validator >= 2.2}
BuildRequires:  %{python_module genson >= 1.2.1}
BuildRequires:  %{python_module graphql-core}
BuildRequires:  %{python_module grpcio-tools}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module hypothesis >= 6.136.6}
BuildRequires:  %{python_module hypothesis-jsonschema >= 0.23.1}
BuildRequires:  %{python_module inflect >= 4.1.0}
BuildRequires:  %{python_module inline-snapshot >= 0.37}
BuildRequires:  %{python_module isort >= 4.3.21}
BuildRequires:  %{python_module jinja2 >= 2.11.2}
BuildRequires:  %{python_module jsonschema >= 4.24}
BuildRequires:  %{python_module lxml >= 5.3}
BuildRequires:  %{python_module msgspec >= 0.22}
BuildRequires:  %{python_module openapi-spec-validator >= 0.2.8}
BuildRequires:  %{python_module prance >= 0.18.2}
BuildRequires:  %{python_module pydantic >= 2.12}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist >= 3.3.1}
BuildRequires:  %{python_module ruff}
BuildRequires:  %{python_module trustme}
#BuildRequires:  %%{python_module ruamel.yaml}
BuildRequires:  %{python_module time-machine >= 3.1}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module covdefaults}
BuildRequires:  %{python_module watchfiles}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
Generate Python data models from schema definitions quickly.

%prep
%autosetup -p1 -n %{upname}-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/datamodel-codegen
%python_clone -a %{buildroot}%{_bindir}/datamodel-code-generator
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
workers=$(( ($(nproc) + 1) / 2 ))
# Requires node installed
skiptests="test_release_benchmark_chart_range_e2e_uses_fixture_data"
ignore=" --ignore tests/test_build_migration_docs_script.py"
# Pydantic 2.14 oddness
skiptests+=" or test_multi_module_output"
skiptests+=" or test_multi_module_relative_parent_import"
skiptests+=" or test_generated_root_model_aliases"
# Missing upstream snapshots in 0.102.0
skiptests+=" or test_payload_validation_cases_cover_discovered_schema_files"
skiptests+=" or reuse_reference_identifier_starts"
skiptests+=" or identifier_type_alias_target"
# Heavy multi-subprocess determinism test crashes xdist worker in OBS
skiptests+=" or test_generation_is_deterministic"
# PYTHONPATH wierdness
skiptests+=" or test_model_resolver_pickles_are_compatible_across_the_resolver_state_rename"
skiptests+=" or test_regular_generation_does_not_load_watch_dependency_collector"
ignore+=" --ignore tests/test_behaviour_diff_script.py"
ignore+=" --ignore tests/test_compare_release_script.py"
ignore+=" --ignore tests/test_verify_script.py"
ignore+=" --ignore tests/test_conftest_helpers.py"
ignore+=" --ignore tests/main/test_shape_compositions.py"
# Upstream CI-only script tests
ignore+=" --ignore tests/test_ci_coverage_script.py"
ignore+=" --ignore tests/test_recommender_calibrate_script.py"
# Run testsuite in two chunks due to memory pressure
%pytest tests/main $ignore -n $workers -m "not perf" -k "not ($skiptests)"
ignore+=" --ignore tests/main"
# Requires collecting tests/main in the same pytest run
skiptests+=" or test_all_options_have_cli_doc_markers"
%pytest $ignore -n $workers -m "not perf" -k "not ($skiptests)"

%post
%python_install_alternative datamodel-codegen datamodel-code-generator

%postun
%python_uninstall_alternative datamodel-codegen datamodel-code-generator

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/datamodel-codegen
%python_alternative %{_bindir}/datamodel-code-generator
%{python_sitelib}/datamodel[_-]code[_-]generator
%{python_sitelib}/datamodel[_-]code[_-]generator-%{version}.dist-info

%changelog
