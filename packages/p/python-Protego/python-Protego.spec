#
# spec file for package python-Protego
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
Name:           python-Protego
Version:        0.6.0
Release:        0
Summary:        Pure-Python robotstxt parser with support for modern conventions
License:        BSD-3-Clause
URL:            https://github.com/scrapy/protego
Source:         https://files.pythonhosted.org/packages/source/P/Protego/protego-%{version}.tar.gz
BuildRequires:  %{python_module hatchling >= 1.27.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Protego is a pure-Python `robots.txt` parser with support for modern conventions.

%prep
%setup -q -n protego-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/protego
%{python_sitelib}/[Pp]rotego-%{version}.dist-info

%changelog
