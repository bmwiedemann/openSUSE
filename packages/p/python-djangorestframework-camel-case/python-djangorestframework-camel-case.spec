#
# spec file for package python-djangorestframework-camel-case
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-djangorestframework-camel-case
Version:        1.4.2
Release:        0
Summary:        Camel case JSON support for Django REST framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vbabiy/djangorestframework-camel-case
Source:         https://files.pythonhosted.org/packages/source/d/djangorestframework-camel-case/djangorestframework-camel-case-%{version}.tar.gz
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-djangorestframework
BuildArch:      noarch
%python_subpackages

%description
Camel case JSON support for Django REST framework.

%prep
%setup -q -n djangorestframework-camel-case-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
