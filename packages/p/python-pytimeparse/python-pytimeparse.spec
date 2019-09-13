#
# spec file for package python-pytimeparse
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without  test
Name:           python-pytimeparse
Version:        1.1.8
Release:        0
Summary:        Time expression parser
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/wroberts/pytimeparse
Source:         https://files.pythonhosted.org/packages/source/p/pytimeparse/pytimeparse-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module nose}
%endif
BuildRequires:  fdupes
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
