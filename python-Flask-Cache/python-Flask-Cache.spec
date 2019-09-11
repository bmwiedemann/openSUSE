#
# spec file for package python-Flask-Cache
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Cache
Version:        0.13.1
Release:        0
Summary:        Cache support for Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/thadeusb/flask-cache
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Cache/Flask-Cache-%{version}.tar.gz
Patch0:         Flask-Cache-fix-namespace.patch
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
BuildArch:      noarch
%python_subpackages

%description
Adds cache support to your Flask application

%package doc
Summary:        Documentation for python-Flask-Cache
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
This package contains HTML documentation, including tutorials and API
reference for python-Flask-Cache.

%prep
%setup -q -n Flask-Cache-%{version}
%patch0 -p1

%build
%python_build
cd docs && make html && rm _build/html/.buildinfo # Generate HTML documentation

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc CHANGES README
%{python_sitelib}/*

%files %{python_files doc}
%doc docs/_build/html

%changelog
