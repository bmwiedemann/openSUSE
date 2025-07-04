#
# spec file for package python-html5-parser
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


%{?sle15_python_module_pythons}
Name:           python-html5-parser
Version:        0.4.12
Release:        0
Summary:        C based HTML 5 parsing for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/kovidgoyal/html5-parser
Source:         https://github.com/kovidgoyal/html5-parser/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml >= 3.8.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
%python_subpackages

%description
A standards compliant, C based HTML 5 parser for Python. It processes HTML
about thirty times faster than the "html5lib" pure Python based parser.

%prep
%setup -q -n html5-parser-%{version}

%build
find . -name '*.py' -exec sed -i '/#.*usr.bin.env.*python/d' {} \;
%pyproject_wheel

%install
%pyproject_install

%check
%if 0%{?suse_version} > 1500
%pyunittest_arch -v test/*.py
%else
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/html5_parser/
%{python_sitearch}/html5_parser-%{version}*-info

%changelog
