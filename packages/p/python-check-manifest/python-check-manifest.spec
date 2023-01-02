#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%define skip_python2 1
Name:           python-check-manifest%{psuffix}
Version:        0.49
Release:        0
Summary:        Tool to check Python source package MANIFEST.in for completeness
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mgedmin/check-manifest
Source:         https://files.pythonhosted.org/packages/source/c/check-manifest/check-manifest-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-build
Requires:       python-pep517
Requires:       python-setuptools
Requires:       python-toml
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     git-core > 2.11
Recommends:     python-pip
Recommends:     python-wheel
Suggests:       bzr
Suggests:       mercurial
Suggests:       subversion
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module pep517}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  bzr
BuildRequires:  git-core > 2.11
BuildRequires:  mercurial
BuildRequires:  subversion
%endif
%python_subpackages

%description
check-manifest is a tool for python developers to check for broken packages
and missing files in MANIFEST.

%prep
%setup -q -n check-manifest-%{version}
%autopatch -p1

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
# test_build_sdist uses pip which likes to use internet to resolve versions
# test_python_from_path fails on Leap only
skip='test_build_sdist or test_python_from_path'
%if 0%{?python_version_nodots} <= 36
# E       TypeError: tuple indices must be integers or slices, not str
skip="$skip or test_extra_ignore_args or test_ignore_bad_ideas_args"
%endif
# Fix tests https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1023597
git config --global --add protocol.file.allow always
%pytest -rs -k "not ($skip)"
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
