#
# spec file for package python-Flask
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%define oldpython python
%define skip_python2 1
%define skip_python36 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask
Version:        2.2.2
Release:        0
Summary:        A microframework based on Werkzeug, Jinja2 and good intentions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://flask.palletsprojects.com
Source0:        https://files.pythonhosted.org/packages/source/F/Flask/Flask-%{version}.tar.gz
Source1:        python-Flask-rpmlintrc
BuildRequires:  %{python_module Jinja2 >= 3.0}
BuildRequires:  %{python_module Werkzeug >= 2.2.2}
BuildRequires:  %{python_module click >= 8.0.0}
BuildRequires:  %{python_module contextvars}
BuildRequires:  %{python_module importlib-metadata >= 3.6.0 if %python-base < 3.10}
BuildRequires:  %{python_module itsdangerous >= 2.0}
BuildRequires:  %{python_module pytest >= 6.2.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-Jinja2 >= 3.0
Requires:       python-Werkzeug >= 2.0
Requires:       python-click >= 8.0.0
Requires:       python-itsdangerous >= 2.0
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-metadata >= 3.6.0
%endif

%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
BuildArch:      noarch
%if %{?suse_version} < 1500
BuildRequires:  python
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
%autosetup -p1 -n Flask-%{version}

%build
%python_build
# cd docs && make html

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/flask
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative flask

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
