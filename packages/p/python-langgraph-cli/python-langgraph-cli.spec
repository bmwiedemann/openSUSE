#
# spec file for package python-langgraph-cli
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


%{?sle15_python_module_pythons}
Name:           python-langgraph-cli
Version:        0.4.30
Release:        0
Summary:        CLI for interacting with the LangGraph API
License:        MIT
URL:            https://github.com/langchain-ai/langgraph/tree/main/libs/cli
Source:         https://files.pythonhosted.org/packages/source/l/langgraph_cli/langgraph_cli-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 8.1.7
Requires:       python-httpx >= 0.24.0
Requires:       python-langgraph-sdk >= 0.1.0
Requires:       python-pathspec >= 0.11.0
Requires:       python-python-dotenv >= 0.8.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.1.7}
BuildRequires:  %{python_module httpx >= 0.24.0}
BuildRequires:  %{python_module langgraph-sdk >= 0.1.0}
BuildRequires:  %{python_module pathspec >= 0.11.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv >= 0.8.0}
# /SECTION
%python_subpackages

%description
The LangGraph command line interface lets you build, run and manage LangGraph
deployments. It provides commands to scaffold new projects from templates,
build Docker images, and run a local development server for graphs defined in a
langgraph.json configuration.

%prep
%autosetup -p1 -n langgraph_cli-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/langgraph
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langgraph_cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Offline unit tests only; the integration suite needs a live LangGraph stack.
# Deselect the tests that shell out to a running Docker daemon (unavailable in
# the build environment) and test_prepare_args_and_stdin, which hardcodes the
# upstream monorepo directory name in the generated compose build context.
%pytest tests/unit_tests -k "not (test_dockerfile_command_with_docker_compose or test_build_command_shows_wolfi_warning or test_build_generate_proper_build_context or test_build_command_with_api_version or test_build_command_with_api_version_and_base_image or test_prepare_args_and_stdin)"

%post
%python_install_alternative langgraph

%postun
%python_uninstall_alternative langgraph

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/langgraph
%{python_sitelib}/langgraph_cli
%{python_sitelib}/langgraph_cli-%{version}.dist-info

%changelog
