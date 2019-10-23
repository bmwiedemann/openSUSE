#
# spec file for package python-Flask-Cors
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
Name:           python-Flask-Cors
Version:        3.0.8
Release:        0
Summary:        A Flask extension adding a decorator for CORS support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/corydolphin/flask-cors
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Cors/Flask-Cors-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-Disable-ACL_ORIGIN-check.patch boo#1154808
Patch1:         0001-Disable-ACL_ORIGIN-check.patch
BuildRequires:  %{python_module Flask >= 0.9}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.9
BuildArch:      noarch
%if 0%{?suse_version} < 1500
BuildRequires:  %{python_module six}
Requires:       python-six
%endif
%python_subpackages

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%prep
%setup -q -n Flask-Cors-%{version}
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%dir %{python_sitelib}/flask_cors
%{python_sitelib}/flask_cors/*
%dir %{python_sitelib}/Flask_Cors-%{version}-py*.egg-info
%{python_sitelib}/Flask_Cors-%{version}-py*.egg-info/*

%changelog
