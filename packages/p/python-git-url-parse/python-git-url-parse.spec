#
# spec file for package python-git-url-parse
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-git-url-parse
Version:        1.2.2
Release:        0
Summary:        A GIT URL parser for Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/retr0h/git-url-parse
Source:         https://files.pythonhosted.org/packages/source/g/git-url-parse/git-url-parse-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
Requires:       python-pbr

%python_subpackages

%description
git-url-parse is a GIT URL parser.

%prep
%setup -q -n git-url-parse-%{version}
sed -i '/addopts/d' pytest.ini

%build
# Dont let pbr install yapf, which isnt a real test dependency
echo > test-requirements.txt
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest -v

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
