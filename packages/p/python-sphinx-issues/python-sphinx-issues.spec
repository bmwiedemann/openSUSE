#
# spec file for package python-sphinx-issues
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
Name:           python-sphinx-issues
Version:        4.1.0
Release:        0
Summary:        A Sphinx extension for linking to a project's issue tracker
License:        MIT
URL:            https://github.com/sloria/sphinx-issues
Source:         https://github.com/sloria/sphinx-issues/archive/%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-mock
%endif
%python_subpackages

%description
A Sphinx extension for linking to a project's issue tracker. It
includes roles for linking to issues as well as user profiles, with
built-in support for GitHub (though this works with other services).

%prep
%setup -q -n sphinx-issues-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/sphinx_issues
%{python_sitelib}/sphinx_issues-%{version}.dist-info

%changelog
