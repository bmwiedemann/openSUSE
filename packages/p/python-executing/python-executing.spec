#
# spec file for package python-executing
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-executing
Version:        0.5.3
Release:        0
License:        MIT
Summary:        Get the currently executing AST node of a frame, and other information
Url:            https://github.com/alexmojaki/executing
Group:          Development/Languages/Python
#Source:         https://github.com/alexmojaki/executing/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source:         https://files.pythonhosted.org/packages/source/e/executing/executing-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools_scm >= 4.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module asttokens}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Get the currently executing AST node of a frame, and other information

%prep
%setup -q -n executing-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#%%pytest
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
