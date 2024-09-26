#
# spec file for package python-ollama
#
# Copyright (c) 2024 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?sle15_python_module_pythons}
Name:           python-ollama
Version:        0.3.1
Release:        0
License:        MIT
Summary:        Ollama python bindings
Group:          Development/Languages/Python
Url:            https://www.ollama.ai
Source:         https://files.pythonhosted.org/packages/source/o/ollama/ollama-%{version}.tar.gz
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pip}
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

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
