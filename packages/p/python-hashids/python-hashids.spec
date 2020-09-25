#
# spec file for package python-hashids
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-hashids
Version:        1.3.1
Release:        0
Summary:        Python implementation of hashids
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/davidaurelio/hashids-python
Source:         https://files.pythonhosted.org/packages/source/h/hashids/hashids-%{version}.tar.gz
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python implementation of hashids (http://www.hashids.org).

%prep
%setup -q -n hashids-%{version}
sed -i 's/tool.flit.sdist/sdist/' pyproject.toml

%build
%python_expand $python -m flit build --format wheel
mv dist/*.whl .

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
