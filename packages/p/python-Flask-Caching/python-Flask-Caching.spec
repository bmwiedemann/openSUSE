#
# spec file for package python-Flask-Caching
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
Name:           python-Flask-Caching
Version:        1.9.0
Release:        0
Summary:        Adds caching support to your Flask application
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sh4nks/flask-caching
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Caching/Flask-Caching-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
BuildArch:      noarch
%python_subpackages

%description
Adds caching support to your Flask application. Continuation of the Flask-Cache
Extension.

%prep
%setup -q -n Flask-Caching-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES README.md
%license LICENSE
%{python_sitelib}/flask_caching
%{python_sitelib}/Flask_Caching-%{version}-py*.egg-info

%changelog
