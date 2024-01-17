#
# spec file for package python-pydash
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-pydash
Version:        6.0.2
Release:        0
Summary:        The kitchen sink of Python functional utility libraries
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dgilland/pydash
Source:         https://files.pythonhosted.org/packages/source/p/pydash/pydash-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The kitchen sink of Python utility libraries for doing "stuff" in a functional way.
Based on the Lo-Dash Javascript library.

%prep
%setup -q -n pydash-%{version}
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i '/--.*cov/d' setup.cfg
%pytest tests/

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
