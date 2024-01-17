#
# spec file for package python-freetype-py
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
Name:           python-freetype-py
Version:        2.4.0
Release:        0
Summary:        Freetype python bindings
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rougier/freetype-py
Source:         https://files.pythonhosted.org/packages/source/f/freetype-py/freetype-py-%{version}.zip
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  freetype2
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       freetype2
BuildArch:      noarch
%python_subpackages

%description
Freetype python provides bindings for the FreeType library.
Only the high-level API is bound.

%prep
%autosetup -p1 -n freetype-py-%{version}
sed -i -e '/^#!\//, 1d' freetype/ft_structs.py freetype/ft_types.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/freetype
%{python_sitelib}/freetype_py-%{version}*-info

%changelog
