#
# spec file for package python-Flask-Cors
#
# Copyright (c) 2021 SUSE LLC
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
Version:        3.0.10
Release:        0
Summary:        A Flask extension adding a decorator for CORS support
License:        MIT
URL:            https://github.com/corydolphin/flask-cors
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Cors/Flask-Cors-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.9}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.9
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%prep
%setup -q -n Flask-Cors-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/flask_cors
%{python_sitelib}/Flask_Cors-%{version}*-info

%changelog
