#
# spec file for package python-serpent
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-serpent
Version:        1.42
Release:        0
Summary:        Serialization based on astliteral_eval
License:        MIT
URL:            https://github.com/irmen/Serpent
Source:         https://files.pythonhosted.org/packages/source/s/serpent/serpent-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
# /SECTION
%python_subpackages

%description
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network for instance)
and de-serialize it there.

%prep
%setup -q -n serpent-%{version}

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/serpent.py
%pycache_only %{python_sitelib}/__pycache__/serpent*
%{python_sitelib}/serpent-%{version}*-info

%changelog
