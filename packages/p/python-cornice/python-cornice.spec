#
# spec file for package python-cornice
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cornice
Version:        6.0.1
Release:        0
Summary:        Define Web Services in Pyramid
License:        MPL-2.0
URL:            https://cornice.readthedocs.io/
# use github URL for docs and tests
Source:         https://github.com/Cornices/cornice/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source:         https://files.pythonhosted.org/packages/source/c/cornice/cornice-%%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# SECTION tests
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module colander >= 1.0~b1}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module marshmallow >= 3.0.0}
BuildRequires:  %{python_module pyramid >= 1.7}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
# /SECTION
Requires:       python-pyramid >= 1.7
Requires:       python-venusian
BuildArch:      noarch
%python_subpackages

%description
Provides helpers to build & document Web Services with Pyramid.

%prep
%setup -q -n cornice-%{version}
chmod -x docs/source/tutorial.rst

%build
%python_build
# building docs requires unavailable mozilla-sphinx-theme

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/*
%doc README.rst CHANGES.txt docs/
%license LICENSE

%changelog
