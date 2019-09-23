#
# spec file for package python-autodoc
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
%define upname autodoc

Name:           python-%{upname}
Version:        0.5.0
Release:        0
Summary:        Autodoc Python implementation
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/heavenshell/py-%{upname}
Source:         https://files.pythonhosted.org/packages/source/a/%{upname}/%{upname}-%{version}.tar.gz
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Autodoc generates documentation from your unit test.
This library is a Python implementation of Autodoc.

%prep
%setup -q -n %{upname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/heavenshell/py-autodoc/pull/15
# %%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/%{upname}*

%changelog
