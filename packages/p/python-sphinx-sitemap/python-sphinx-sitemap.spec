#
# spec file for package python-sphinx-sitemap
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


Name:           python-sphinx-sitemap
Version:        2.9.0
Release:        0
Summary:        Sitemap generator for Sphinx
License:        MIT
URL:            https://github.com/jdillard/sphinx-sitemap
Source:         https://github.com/jdillard/sphinx-sitemap/archive/refs/tags/v%{version}.tar.gz#/sphinx_sitemap-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module sphinx-last-updated-by-git}
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-sphinx-last-updated-by-git
Suggests:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
Sitemap generator for Sphinx

%prep
%autosetup -p1 -n sphinx-sitemap-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/sphinx_sitemap
%{python_sitelib}/sphinx_sitemap-%{version}.dist-info

%changelog
