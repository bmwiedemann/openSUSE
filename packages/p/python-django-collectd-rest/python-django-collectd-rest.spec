#
# spec file for package python-django-collectd-rest
#
# Copyright (c) 2024 SUSE LLC
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


%define skip_python2 1
%define skip_python36 1
%{?sle15_python_module_pythons}
Name:           python-django-collectd-rest
Version:        0.2.6
Release:        0
Summary:        A simple Django application to demonstrate RRD plots
License:        BSD-2-Clause
URL:            https://github.com/matwey/django-collectd-rest
Source:         https://files.pythonhosted.org/packages/source/d/django-collectd-rest/django_collectd_rest-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module djangorestframework >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-build-core}
# sqlite3 from standard library is requires for tests
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
BuildRequires:  rrdtool-devel
Requires:       python-djangorestframework >= 3.7
Requires:       rrdtool
%python_subpackages

%description
django-collectd-rest is a simple Django application to demonstrate RRD plots generated by collectd or any other rrd data.
The application is built on top of django-rest-framework and provides REST API to access the plots.

%prep
%setup -q -n django_collectd_rest-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/collectd_rest
%{python_sitearch}/django_collectd_rest-%{version}.dist-info

%changelog
