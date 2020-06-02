#
# spec file for package python-featureflow
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
%define         skip_python2 1
Name:           python-featureflow
Version:        3.0.3
Release:        0
Summary:        A python library for building feature extraction pipelines
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/JohnVinyard/featureflow
Source0:        https://files.pythonhosted.org/packages/source/f/featureflow/featureflow-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix_certifi_dependency.patch -- loosen certifi version dependency
Patch0:         fix_certifi_dependency.patch
# https://github.com/JohnVinyard/featureflow/pull/11
Patch1:         python-featureflow-no-unittest2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module certifi >= 2017.7.27.1}
BuildRequires:  %{python_module dill}
BuildRequires:  %{python_module lmdb}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module requests}
# /SECTION
Requires:       python-certifi >= 2017.7.27.1
Requires:       python-dill
Requires:       python-lmdb
Requires:       python-redis
Requires:       python-requests
Recommends:     python-numpy
BuildArch:      noarch

%python_subpackages

%description
Featureflow is a python library that allows users to build feature
extraction pipelines in a declarative way, and control how and where
those features are persisted.

%prep
%setup -q -n featureflow-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
