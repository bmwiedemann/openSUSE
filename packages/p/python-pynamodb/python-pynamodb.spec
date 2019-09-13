#
# spec file for package python-pynamodb
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pynamodb
Version:        3.3.1
Release:        0
License:        MIT
Summary:        Python Interface to DynamoDB
Url:            http://jlafon.io/pynamodb.html
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/p/pynamodb/pynamodb-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/pynamodb/PynamoDB/%{version}/LICENSE
# PATCH-FIX-UPSTREAM no_vendored_requests.patch -- use system requests since we remove the vendored version -- https://github.com/pynamodb/PynamoDB/pull/566
Patch0:         no_vendored_requests.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# SECTION test requirements
BuildRequires:  %{python_module botocore >= 1.2.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
# /SECTION
Requires:       python-botocore >= 1.2.0
Requires:       python-python-dateutil >= 2.1
Requires:       python-requests
Requires:       python-six
Recommends:     python-blinker >= 1.3
BuildArch:      noarch

%python_subpackages

%description
A Python interface for Amazon's DynamoDB.

%prep
%setup -q -n pynamodb-%{version}
cp %{SOURCE10} .
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
