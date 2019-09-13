#
# spec file for package python-sphinx_rtd_theme
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-sphinx_rtd_theme%{psuffix}
Version:        0.4.3
Release:        0
Summary:        ReadTheDocs.org theme for Sphinx
License:        MIT AND Apache-2.0 AND OFL-1.1
Group:          Development/Languages/Python
URL:            https://github.com/snide/sphinx_rtd_theme/
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_rtd_theme/sphinx_rtd_theme-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module readthedocs-sphinx-ext}
%endif
%python_subpackages

%description
This is a prototype mobile-friendly sphinx theme I made for readthedocs.org. It's
currently in development and includes some rtd variable checks that can be ignored
if you're just trying to use it on your project outside of that site.

%prep
%setup -q -n sphinx_rtd_theme-%{version}
dos2unix OFL-License.txt

%build
%python_build

%install
%if !%{with test}
%python_install
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
%{python_sitelib}/sphinx_rtd_theme*
%endif

%changelog
