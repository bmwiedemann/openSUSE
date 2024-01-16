#
# spec file for package python-httpagentparser
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
Name:           python-httpagentparser
Version:        1.9.5
Release:        0
Summary:        Extracts OS Browser etc information from http user agent string
License:        MIT
URL:            https://github.com/shon/httpagentparser
Source:         https://files.pythonhosted.org/packages/source/h/httpagentparser/httpagentparser-%{version}.tar.gz
# Not shipped in sdist, no releases/tags on github
Source1:        https://raw.githubusercontent.com/shon/httpagentparser/master/tests.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Extracts OS Browser etc information from http user agent string

%prep
%autosetup -p1 -n httpagentparser-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests.py

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/httpagentparser
%{python_sitelib}/httpagentparser-%{version}.dist-info

%changelog
