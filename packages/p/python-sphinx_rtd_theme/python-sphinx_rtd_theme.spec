#
# spec file for package python-sphinx_rtd_theme
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-sphinx_rtd_theme%{psuffix}
Version:        3.1.0
Release:        0
Summary:        ReadTheDocs.org theme for Sphinx
License:        Apache-2.0 AND MIT AND OFL-1.1
URL:            https://github.com/snide/sphinx_rtd_theme/
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_rtd_theme/sphinx_rtd_theme-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 6
Requires:       python-docutils
Requires:       python-sphinxcontrib-jquery >= 4.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinx_rtd_theme = %{version}}
%endif
%python_subpackages

%description
This is a prototype mobile-friendly sphinx theme I made for readthedocs.org. It's
currently in development and includes some rtd variable checks that can be ignored
if you're just trying to use it on your project outside of that site.

%prep
%setup -q -n sphinx_rtd_theme-%{version}
dos2unix OFL-License.txt

# We cannot build the Javascript from source at this time, due to many missing
# dependencies.  Convince the build script to skip building the Javascript and
# go on to the python.
mkdir -p build/lib/%{srcname}/static/js
cp -p sphinx_rtd_theme/static/js/badge_only.js build/lib/%{srcname}/static/js
cp -p sphinx_rtd_theme/static/js/theme.js build/lib/%{srcname}/static/js
sed -i "/'build_py'/d" setup.py

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE OFL-License.txt Apache-License-2.0.txt
%doc README.rst
%{python_sitelib}/sphinx_rtd_theme
%{python_sitelib}/sphinx_rtd_theme-%{version}.dist-info
%endif

%changelog
