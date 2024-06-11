#
# spec file for package python-Routes
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


Name:           python-Routes
Version:        2.5.1
Release:        0
Summary:        Routing Recognition and Generation Tools
License:        BSD-3-Clause
URL:            https://routes.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/R/Routes/Routes-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/bbangert/routes/pull/113 remove python2 support
Patch:          remove-six.patch
# for testing
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module repoze.lru}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-repoze.lru >= 0.3
Provides:       python-routes = %{version}-%{release}
Obsoletes:      python-routes < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
A Routing package for Python that matches URL's to dicts and vice versa.

%prep
%autosetup -p1 -n Routes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --doctest-modules routes

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{python_sitelib}/routes
%{python_sitelib}/Routes-%{version}*-info

%changelog
