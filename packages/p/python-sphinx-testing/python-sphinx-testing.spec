#
# spec file for package python-sphinx-testing
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-sphinx-testing
Version:        1.0.1
Release:        0
Summary:        Testing utility classes and functions for Sphinx extensions
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sphinx-doc/sphinx-testing
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-testing/sphinx-testing-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
Requires:       python-six
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-mock
%endif
%python_subpackages

%description
sphinx-testing provides testing utility classes and functions for Sphinx extensions.

%prep
%setup -q -n sphinx-testing-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
