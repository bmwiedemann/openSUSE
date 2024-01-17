#
# spec file for package python-formats
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016-2020, Martin Hauke <mardnh@gmx.de>
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
Name:           python-formats
Version:        0.1.1
Release:        0
Summary:        Support multiple formats with ease
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/redodo/formats
Source:         https://files.pythonhosted.org/packages/source/f/formats/formats-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/redodo/formats/master/LICENSE
Source2:        https://raw.githubusercontent.com/redodo/formats/master/test_formats.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Formats will provide you with a consistent API to parse and compose data.

%prep
%setup -q -n formats-%{version}
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand %python_exec -m unittest discover -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/formats*

%changelog
