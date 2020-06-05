#
# spec file for package python-check-manifest
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-check-manifest%{psuffix}
Version:        0.40
Release:        0
Summary:        Tool to check Python source package MANIFEST.in for completeness
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mgedmin/check-manifest
Source:         https://files.pythonhosted.org/packages/source/c/check-manifest/check-manifest-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-toml
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       git-core
Suggests:       mercurial
Suggests:       subversion
BuildArch:      noarch
%if %{with test}
BuildRequires:  git-core
BuildRequires:  mercurial
BuildRequires:  subversion
%endif
%python_subpackages

%description
check-manifest is a tool for python developers to check for broken packages
and missing files in MANIFEST.

%prep
%setup -q -n check-manifest-%{version}
sed -i '1{\,^#!%{_bindir}/env python,d}' check_manifest.py
chmod -x check_manifest.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/check-manifest
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
%pytest
%endif

%if !%{with test}
%post
%python_install_alternative check-manifest

%postun
%python_uninstall_alternative check-manifest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%python_alternative %{_bindir}/check-manifest
%{python_sitelib}/*
%endif

%changelog
