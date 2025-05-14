#
# spec file for package python-Flask-RESTful
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
Name:           python-Flask-RESTful
Version:        0.3.10
Release:        0
Summary:        Framework for creating REST APIs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://www.github.com/flask-restful/flask-restful/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-RESTful/Flask-RESTful-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.8
Requires:       python-aniso8601 >= 0.82
Requires:       python-pytz
Requires:       python-six >= 1.3.0
BuildArch:      noarch
%python_subpackages

%description
Flask-RESTful provides the building blocks for creating a REST API.

%prep
%setup -q -n Flask-RESTful-%{version}
sed -i '1{/^#!/d}' flask_restful/__version__.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand \
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/flask_restful/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/flask_restful/
}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/flask_restful
%{python_sitelib}/[Ff]lask[_-][Rr][Ee][Ss][Tt]ful-%{version}.dist-info

%changelog
