#
# spec file for package python-sphinx-tabs
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
# TODO: use github tarball because upstrean dont distribute tests via pypi
%bcond_with      test
Name:           python-sphinx-tabs
Version:        3.1.0
Release:        0
Summary:        Tabbed views for Sphinx
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/djungelorm/sphinx-tabs
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-tabs/sphinx-tabs-%{version}.tar.gz
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils}
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Requires:       python-Sphinx
Requires:       python-docutils
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinx-testing}
%endif
%python_subpackages

%description
Create tabbed content in Sphinx documentation when building HTML.

%prep
%setup -q -n sphinx-tabs-%{version}

%build
%python_build

%install
%python_install

%if %{with test}
%check
%pytest
%endif

%files %{python_files}
%{python_sitelib}/*

%changelog
