#
# spec file for package python-lm-format-enforcer
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
Name:           python-lm-format-enforcer
Version:        0.11.3
Release:        0
Summary:        Enforce the output format (JSON Schema, Regex etc) of a language model
License:        MIT
URL:            https://github.com/noamgat/lm-format-enforcer
Source:         https://files.pythonhosted.org/packages/source/l/lm_format_enforcer/lm_format_enforcer-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.1.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-interegular >= 0.3.2
Requires:       python-packaging
Requires:       python-pydantic >= 1.10.8
Requires:       python-PyYAML
BuildArch:      noarch
# SECTION runtime deps, also needed for the %%check import smoke test
BuildRequires:  %{python_module interegular >= 0.3.2}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pydantic >= 1.10.8}
BuildRequires:  %{python_module PyYAML}
# /SECTION
%python_subpackages

%description
LM Format Enforcer is a library that enforces the output format (JSON
Schema, regular expressions) of a language model by filtering the tokens
that the model is allowed to generate at every timestep. It supports
batched generation and beam search, and integrates with several inference
backends such as Transformers, llama.cpp, vLLM and ExLlamaV2.

%prep
%autosetup -p1 -n lm_format_enforcer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Upstream ships no tests in the sdist; the full test suite (in the git
# repo) needs transformers/torch/numpy, which are heavy/GPU deps not in
# Factory. Run an import smoke test to verify the module and its runtime
# dependencies load.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import lmformatenforcer"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/lmformatenforcer
%{python_sitelib}/lm_format_enforcer-%{version}.dist-info

%changelog
