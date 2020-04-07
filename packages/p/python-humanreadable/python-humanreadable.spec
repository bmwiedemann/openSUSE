#
# spec file for package python-humanreadable
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
%define skip_python2 1
Name:           python-humanreadable
Version:        0.1.0
Release:        0
Summary:        A Python library to convert from human-readable values to Python values
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/humanreadable
Source:         https://files.pythonhosted.org/packages/source/h/humanreadable/humanreadable-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typepy >= 0.6.4}
# /SECTION
BuildRequires:  fdupes
Requires:       python-setuptools >= 38.3.0
Requires:       python-typepy >= 0.6.4
BuildArch:      noarch
%python_subpackages

%description
humanreadable is a Python library to convert from human-readable
values to Python values.

%prep
%setup -q -n humanreadable-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/humanreadable*

%changelog
