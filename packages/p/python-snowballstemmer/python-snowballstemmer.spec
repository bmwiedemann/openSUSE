#
# spec file for package python-snowballstemmer
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-snowballstemmer
Version:        3.1.1
Release:        0
Summary:        16 stemmer algorithms
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/shibukawa/snowball_py
Source:         https://files.pythonhosted.org/packages/source/s/snowballstemmer/snowballstemmer-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package provides 32 stemmer algorithms generated from Snowball
algorithms. It includes following language algorithms: Arabic,
Armenian, Basque, Catalan, Danish, Dutch, Dutch (Porter),
English (Standard, Porter), Esperanto, Estonian, Finnish, French,
German, Greek, Hindi, Hungarian, Indonesian, Irish, Italian,
Lithuanian, Nepali, Norwegian, Portuguese, Romanian, Russian,
Serbian, Spanish, Swedish, Tamil, Turkish, Yiddish.

%prep
%setup -q -n snowballstemmer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc README.rst NEWS
%{python_sitelib}/snowballstemmer
%{python_sitelib}/snowballstemmer-%{version}*-info

%changelog
