#
# spec file for package python-backports.csv
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


%define skip_python3 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-backports.csv
Version:        1.0.7
Release:        0
Summary:        Backport of Python 3 csv module
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://github.com/ryanhiebert/backports.csv
Source:         https://files.pythonhosted.org/packages/source/b/backports.csv/backports.csv-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Backport of Python 3 csv module.

The API of the csv module in Python 2 is drastically different from the csv module in Python 3.
This is due, for the most part, to the difference between str in Python 2 and Python 3.

The semantics of Python 3's version are more useful because they support unicode natively,
while Python 2's csv does not.

%prep
%setup -q -n backports.csv-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst HISTORY.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
