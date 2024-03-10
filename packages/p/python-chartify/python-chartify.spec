#
# spec file for package python-chartify
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


%{?sle15_python_module_pythons}
%define skip_python39 1
Name:           python-chartify
Version:        4.0.5
Release:        0
Summary:        Python library for plotting charts
License:        Apache-2.0
URL:            https://github.com/spotify/chartify
Source:         https://github.com/spotify/chartify/archive/%{version}.tar.gz#/chartify-%{version}.tar.gz
# PATCH-FIX-UPSTREAM chartify-pr170-pd.melt-kwarg.patch gh#spotify/chartify#170
Patch0:         chartify-pr170-pd.melt-kwarg.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Pillow >= 8.4.0}
BuildRequires:  %{python_module bokeh >= 3.0.0}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.0.0}
# ignoring https://github.com/SeleniumHQ/selenium/issues/5296
BuildRequires:  %{python_module selenium >= 3.7.0}
# /SECTION
%{?python_enable_dependency_generator}
%python_subpackages

%description
Chartify is a Python library for creating charts.

%prep
%autosetup -p1 -n chartify-%{version}
rm tox.ini
# unpin selenium (see comment above)
# unpin Jinja2 (see release notes), but keep a pinning char for the check in setup.py
sed -i \
  -e '/selenium/ s/,<=3.8.0//' \
  -e '/Jinja2/ s/<3.1.0/>1/' \
  requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/chartify
%{python_sitelib}/chartify-%{version}.dist-info

%changelog
