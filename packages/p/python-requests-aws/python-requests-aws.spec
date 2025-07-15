#
# spec file for package python-requests-aws
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-requests-aws
Version:        0.1.8
Release:        0
Summary:        AWS authentication for Amazon S3 for the python requests module
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/tax/python-requests-aws
Source:         https://files.pythonhosted.org/packages/source/r/requests-aws/requests-aws-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.4.1
BuildArch:      noarch
%python_subpackages

%description
AWS authentication for Amazon S3 for the Python "requests" library.
It is made to work with Python 2.7 and 3.
At the moment, only S3 is supported.

%prep
%setup -q -n requests-aws-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%license LICENSE.txt
%doc README.md
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/awsauth.py
%{python_sitelib}/requests_aws-%{version}.dist-info

%changelog
