#
# spec file for package python-Flask-HTTPAuth
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017 Dr. Axel Braun
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
%define         skip_python2 1
Name:           python-Flask-HTTPAuth
Version:        4.4.0
Release:        0
Summary:        Basic and Digest HTTP authentication for Flask routes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/miguelgrinberg/flask-httpauth/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-HTTPAuth/Flask-HTTPAuth-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
BuildArch:      noarch
%python_subpackages

%description
Simple extension that provides Basic and Digest HTTP authentication for Flask routes.

%prep
%setup -q -n Flask-HTTPAuth-%{version}

%build

%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/flask_httpauth.py*
%{python_sitelib}/Flask_HTTPAuth-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
