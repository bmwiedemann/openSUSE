#
# spec file for package python-html5-parser
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

Name:           python-html5-parser
Version:        0.4.7
Release:        0
Summary:        C based HTML 5 parsing for Python
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/kovidgoyal/html5-parser
Source:         https://github.com/kovidgoyal/html5-parser/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml >= 3.8.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%python_subpackages

%description
A standards compliant, C based HTML 5 parser for Python. It processes HTML
about thirty times faster than the "html5lib" pure Python based parser.

%prep
%setup -q -n html5-parser-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-) 
%doc LICENSE README.rst
%{python_sitearch}/html5_parser/
%{python_sitearch}/html5_parser-%{version}-py%{python_version}.egg-info

%changelog
