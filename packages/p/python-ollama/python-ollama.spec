#
# spec file for package python-ollama
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


%{?sle15_python_module_pythons}
Name:           python-ollama
Version:        0.3.3
Release:        0
Summary:        Ollama python bindings
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.ollama.ai
Source:         https://github.com/ollama/ollama-python/releases/download/v%{version}/ollama-%{version}.tar.gz#/ollama-%{version}-gh.tar.gz
BuildRequires:  %{python_module httpx >= 0.27.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpx >= 0.27.0
BuildArch:      noarch
%python_subpackages

%description
Official ollama python bindings

%prep
%setup -q -n ollama-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/ollama
%{python_sitelib}/ollama-%{version}.dist-info

%changelog
