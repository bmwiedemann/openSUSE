#
# spec file for package python-texttable
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-texttable
Version:        1.6.7
Release:        0
Summary:        Module for creating simple ASCII tables
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/foutaise/texttable/
Source:         https://files.pythonhosted.org/packages/source/t/texttable/texttable-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base
Recommends:     python-wcwidth
BuildArch:      noarch
%python_subpackages

%description
texttable is a module to generate a formatted text table, using ASCII
characters.

%prep
%setup -q -n texttable-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests.py

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/*

%changelog
