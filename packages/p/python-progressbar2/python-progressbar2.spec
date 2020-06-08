#
# spec file for package python-progressbar2
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-progressbar2
Version:        3.51.3
Release:        0
Summary:        Python progressbar library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/WoLpH/python-progressbar
Source:         https://files.pythonhosted.org/packages/source/p/progressbar2/progressbar2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-utils >= 2.3.0
Requires:       python-six
Conflicts:      python-progressbar
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module freezegun >= 0.3.11}
BuildRequires:  %{python_module pytest >= 4.3.1}
BuildRequires:  %{python_module python-utils >= 2.3.0}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A Python Progressbar library to provide visual (yet text based)
progress to long running operations.

%prep
%setup -q -n progressbar2-%{version}
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
