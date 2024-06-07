#
# spec file for package python-regex
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-regex
Version:        2024.5.15
Release:        0
Summary:        Alternative regular expression module for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mrabarnett/mrab-regex
Source:         https://files.pythonhosted.org/packages/source/r/regex/regex-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-testsuite
%python_subpackages

%description
An alternate regex implementation. It differs from "re" in that

* Zero-width matches are handled like in Perl and PCRE:
  * ``.split`` will split a string at a zero-width match.
  * ``.sub`` will handle zero-width matches correctly.
* Inline flags apply to the end of the group or pattern, and they can
  be turned off.
* Nested sets and set operations are supported.
* Case-insensitive matches in Unicode use full case-folding by
  default.

%prep
%setup -q -n regex-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1
# test_main invokes unittest.main, which raises SystemExit, which fails on pytest.
%pytest_arch %{buildroot}%{$python_sitearch}/regex -k 'not test_main'

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%doc docs/*
%{python_sitearch}/*

%changelog
