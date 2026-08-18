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
Version:        0.72.3
Release:        0
Summary:        Datamodel Code Generator
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/koxudaxi/datamodel-code-generator/
Source0:        https://github.com/koxudaxi/datamodel-code-generator/archive/refs/tags/%{version}.tar.gz#/datamodel-code-generator-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
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
Requires:       python-toml >= 0.10.1
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
BuildRequires:  %{python_module black >= 19.10b0}
BuildRequires:  %{python_module PySnooper >= 0.4.1}
BuildRequires:  %{python_module argcomplete >= 1.11.1}
BuildRequires:  %{python_module black >= 19.10b0}
BuildRequires:  %{python_module email-validator >= 2.2}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module genson >= 1.2.1}
BuildRequires:  %{python_module graphql-core}
BuildRequires:  %{python_module grpcio-tools}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module hypothesis >= 6.136.6}
BuildRequires:  %{python_module hypothesis-jsonschema >= 0.23.1}
BuildRequires:  %{python_module inflect >= 4.1.0}
BuildRequires:  %{python_module inflect}
BuildRequires:  %{python_module inline-snapshot >= 0.34.2}
BuildRequires:  %{python_module isort >= 4.3.21}
BuildRequires:  %{python_module jinja2 >= 2.11.2}
BuildRequires:  %{python_module jsonschema >= 4.24}
BuildRequires:  %{python_module msgspec >= 0.18}
BuildRequires:  %{python_module openapi-spec-validator >= 0.2.8}
BuildRequires:  %{python_module prance >= 0.18.2}
BuildRequires:  %{python_module pydantic >= 2.12}
BuildRequires:  %{python_module pydantic-core}
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
BuildRequires:  %{python_module toml >= 0.10.1}
BuildRequires:  %{python_module watchfiles}
# /SECTION
%python_subpackages

%description
Python Datamodel Code Generator.

%prep
%autosetup -p1 -n %{upname}-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/datamodel-codegen
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
skiptests="test_openapi_parser_parse_remote_ref"
skiptests+=" or test_watch_cli_resolves_relative_coverage_file_for_other_working_directory"
skiptests+=" or test_regular_generation_does_not_load_watch_dependency_collector"
# ruff newline changes
skiptests+=" or test_ruff_check_and_format_combined or test_ruff_check_only"
skiptests+=" or est_ruff_batch_formatting_directory or test_type_checking_imports_default_to_runtime_imports_for_modular_pydantic_ruff"
skiptests+=" or test_no_use_type_checking_imports"
%pytest -k "not ($skiptests)"

%post
%python_install_alternative datamodel-codegen

%postun
%python_uninstall_alternative datamodel-codegen

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/datamodel-codegen
%{python_sitelib}/datamodel[_-]code[_-]generator*/

%changelog
