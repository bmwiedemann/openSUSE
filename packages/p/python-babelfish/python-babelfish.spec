#
# spec file for package python-babelfish
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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
Name:           python-babelfish
Version:        0.5.5
Release:        0
Summary:        A Python library to work with countries and languages
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://travis-ci.org/Diaoul/babelfish
Source:         https://files.pythonhosted.org/packages/source/b/babelfish/babelfish-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
BabelFish is a Python library to work with countries and languages.

%prep
%setup -q -n babelfish-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/babelfish
%{python_sitelib}/babelfish-%{version}-py%{py_ver}.egg-info

%changelog
