#
# spec file for package python-ddt
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
Name:           python-ddt
Version:        1.2.1
Release:        0
Summary:        Data-Driven/Decorated Tests
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/txels/ddt
Source:         https://files.pythonhosted.org/packages/source/d/ddt/ddt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
# /SECTION
%python_subpackages

%description
A library to multiply test cases.

%prep
%setup -q -n ddt-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CONTRIBUTING.md README.md
%license LICENSE.md
%{python_sitelib}/*

%changelog
