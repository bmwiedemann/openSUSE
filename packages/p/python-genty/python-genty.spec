#
# spec file for package python-genty
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
Name:           python-genty
Version:        1.3.2
Release:        0
Summary:        Python module to run a test with multiple data sets
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/box/genty
Source:         https://files.pythonhosted.org/packages/source/g/genty/genty-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Suggests:       python-ordereddict
BuildArch:      noarch
%python_subpackages

%description
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of
input. Genty makes this a breeze.

%prep
%setup -q -n genty-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
