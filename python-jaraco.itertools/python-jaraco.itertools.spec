#
# spec file for package python-jaraco.itertools
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
Name:           python-jaraco.itertools
Version:        4.4.2
Release:        0
Summary:        Tools to work with iterables
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/jaraco.itertools
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.itertools/jaraco.itertools-%{version}.tar.gz
BuildRequires:  %{python_module inflect}
BuildRequires:  %{python_module jaraco.base >= 6.1}
BuildRequires:  %{python_module more-itertools >= 4.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-inflect
Requires:       python-jaraco.base >= 6.1
Requires:       python-more-itertools >= 4.0.0
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
jaraco.itertools Tools for working with iterables.
Complements itertools and more_itertools.

%prep
%setup -q -n jaraco.itertools-%{version}
sed -i 's/--flake8//' pytest.ini

%build
%python_build

%install
%python_install

%{python_expand rm -f %{buildroot}%{$python_sitelib}/jaraco/__init__.py* \
  %{buildroot}%{$python_sitelib}/jaraco/__pycache__/__init__.*
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/jaraco/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/jaraco/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/jaraco.itertools-%{version}-py*.egg-info
%{python_sitelib}/jaraco/itertools.py*
%pycache_only %{python_sitelib}/jaraco/__pycache__/itertools*.py*

%changelog
