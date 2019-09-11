#
# spec file for package python-RegexOrder
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
# For LICENSE file
%define tag     23f0ac4ac46527404e3ec9097df931378d3d803a
Name:           python-RegexOrder
Version:        0.2
Release:        0
Summary:        Python module to search a regex that fits all query strings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/chuanconggao/RegexOrder
Source:         https://files.pythonhosted.org/packages/source/R/RegexOrder/RegexOrder-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/chuanconggao/RegexOrder/%{tag}/LICENSE
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-regex >= 2018.2.21
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module regex >= 2018.2.21}
# /SECTION
%python_subpackages

%description
A module to search the regex that fits all query strings.

- Dozens of pre-written regexes are indexed and organized as a partial order, available in `regexorder/templates.json`.
- The regex of all the querying strings' least upper bound in the partial order is returned.
- templates.svg plots the partial order.

%prep
%setup -q -n RegexOrder-%{version}
cp %{SOURCE10} .
sed -i -e '/^#!\s*\//, 1d' regexorder/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
