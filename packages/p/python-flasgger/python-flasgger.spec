#
# spec file for package python-flasgger
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
Name:           python-flasgger
Version:        0.9.3
Release:        0
Summary:        Tool to extract swagger specs from Flask projects
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rochacbruno/flasgger/
Source:         https://files.pythonhosted.org/packages/source/f/flasgger/flasgger-%{version}.tar.gz
#BuildRequires:  %{python_module Flask >= 0.10}
#BuildRequires:  %{python_module PyYAML >= 3.0}
#BuildRequires:  %{python_module flex}
#BuildRequires:  %{python_module jsonschema >= 2.5.1}
#BuildRequires:  %{python_module jsonschema < 4}
#BuildRequires:  %{python_module marshmallow}
#BuildRequires:  %{python_module mistune}
#BuildRequires:  %{python_module pytest >= 3.0.7}
#BuildRequires:  %{python_module six >= 1.10}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.10
Requires:       python-PyYAML >= 3.0
Requires:       python-jsonschema >= 2.5.1
Requires:       python-jsonschema < 4
Requires:       python-mistune
Requires:       python-six >= 1.10
BuildArch:      noarch
%python_subpackages

%description
Flasgger is a Flask extension to extract OpenAPI=Specification from all Flask views registered in an API.

%prep
%setup -q -n flasgger-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# tests currently broken, even in git
#%check
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
