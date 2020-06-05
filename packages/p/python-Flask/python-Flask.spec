#
# spec file for package python-Flask
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask
Version:        1.1.2
Release:        0
Summary:        A microframework based on Werkzeug, Jinja2 and good intentions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mitsuhiko/flask/
Source:         https://files.pythonhosted.org/packages/source/F/Flask/Flask-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2 >= 2.4}
BuildRequires:  %{python_module Werkzeug >= 0.15}
BuildRequires:  %{python_module click >= 5.1}
BuildRequires:  %{python_module itsdangerous >= 0.24}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10
Requires:       python-Werkzeug >= 0.15
Requires:       python-click >= 5.1
Requires:       python-itsdangerous >= 0.24
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{?suse_version} < 1500
BuildRequires:  python
%endif
%ifpython2
Provides:       %{oldpython}-flask = %{version}
Obsoletes:      %{oldpython}-flask < %{version}
%endif
%python_subpackages

%description
Flask is a microframework for Python based on Werkzeug, Jinja 2 and good
intentions. And before you ask: It's BSD licensed!

%package doc
Summary:        Documentation for python-Flask
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
This package contains HTML documentation, including tutorials and API
reference for python-Flask.

%prep
%setup -q -n Flask-%{version}

%build
%python_build
# cd docs && make html

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/flask

%fdupes %{buildroot}%{python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative flask

%postun
%python_uninstall_alternative flask

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/flask
%{_bindir}/flask-%{python_bin_suffix}
%dir %{python_sitelib}/flask
%{python_sitelib}/flask/*
%dir %{python_sitelib}/Flask-%{version}-py*.egg-info
%{python_sitelib}/Flask-%{version}-py*.egg-info

%files %{python_files doc}
%doc docs/
%doc examples/

%changelog
