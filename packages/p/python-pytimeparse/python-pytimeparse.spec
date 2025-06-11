#
# spec file for package python-pytimeparse
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pytimeparse
Version:        1.1.8
Release:        0
Summary:        Time expression parser
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wroberts/pytimeparse
Source:         https://files.pythonhosted.org/packages/source/p/pytimeparse/pytimeparse-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A small Python library to parse various kinds of time expressions,
inspired by a StackOverflow question.

The single function pytimeparse.timeparse.timeparse defined in the
library (also available as pytimeparse.parse) parses time expressions
like the following:

  * 32m
  * 2h32m
  * 3d2h32m
  * 1w3d2h32m
  * 1w 3d 2h 32m
  * 1 w 3 d 2 h 32 m
  * ...

It returns the time as a number of seconds (an integer value if
possible, otherwise a floating-point number)

A number of seconds can be converted back into a string using the
datetime module in the standard library.

%prep
%setup -q -n pytimeparse-%{version}
sed -i '/nose/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest pytimeparse/tests/test*.py

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/pytimeparse
%{python_sitelib}/pytimeparse-%{version}.dist-info

%changelog
