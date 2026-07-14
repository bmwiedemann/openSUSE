#
# spec file for package python-model-hosting-container-standards
#
# Copyright (c) 2026 SUSE LLC
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
Name:           python-model-hosting-container-standards
Version:        0.1.16
Release:        0
Summary:        Python toolkit for standardized model hosting container implementations
License:        Apache-2.0
URL:            https://github.com/aws/model-hosting-container-standards
Source:         https://files.pythonhosted.org/packages/source/m/model_hosting_container_standards/model_hosting_container_standards-%{version}.tar.gz
BuildRequires:  %{python_module fastapi}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module jmespath}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 2.0.0}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module starlette >= 0.49.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-fastapi
Requires:       python-httpx
Requires:       python-jmespath
Requires:       python-pydantic
Requires:       python-setuptools
Requires:       python-starlette >= 0.49.1
# supervisor is packaged in openSUSE as "supervisor" (legacy python3-only
# package); it does not provide a python-supervisor alias.
Requires:       supervisor >= 4.2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A standardized Python framework for seamless integration between ML
frameworks (TensorRT-LLM, vLLM) and Amazon SageMaker hosting. It provides
unified /ping and /invocations handler endpoints, flexible configuration via
environment variables or decorators, automatic dependency installation, and
supervisor process management for model hosting containers.

%prep
%autosetup -p1 -n model_hosting_container_standards-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/generate-supervisor-config
%python_clone -a %{buildroot}%{_bindir}/standard-supervisor
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# The published sdist ships no test suite, so %%check is an import smoke-test
# exercising the runtime dependency chain (fastapi, pydantic, jmespath) and the
# supervisor backend behind the two console scripts.
%check
# PYTHONDONTWRITEBYTECODE keeps the smoke-test from rewriting the buildroot's
# .pyc files (newer mtime than the shipped .py -> bytecode-inconsistent-mtime).
export PYTHONDONTWRITEBYTECODE=1
%python_exec -c "import model_hosting_container_standards.common.fastapi"
%python_exec -c "import model_hosting_container_standards.supervisor"

%post
%python_install_alternative generate-supervisor-config standard-supervisor

%postun
%python_uninstall_alternative generate-supervisor-config

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/generate-supervisor-config
%python_alternative %{_bindir}/standard-supervisor
%{python_sitelib}/model_hosting_container_standards
%{python_sitelib}/model_hosting_container_standards-%{version}.dist-info

%changelog
