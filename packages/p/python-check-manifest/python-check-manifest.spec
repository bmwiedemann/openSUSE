#
# spec file for package python-check-manifest
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-check-manifest%{psuffix}
Version:        0.50
Release:        0
Summary:        Tool to check Python source package MANIFEST.in for completeness
License:        MIT
URL:            https://github.com/mgedmin/check-manifest
Source:         https://files.pythonhosted.org/packages/source/c/check_manifest/check_manifest-%{version}.tar.gz
Patch0:         use-current-interpreter.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-build >= 0.1
Requires:       python-setuptools
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     git-core > 2.11
Recommends:     python-pip
Recommends:     python-wheel
Suggests:       breezy
Suggests:       mercurial
Suggests:       subversion
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module check-manifest = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  breezy
BuildRequires:  git-core > 2.11
BuildRequires:  mercurial
BuildRequires:  subversion
%endif
%python_subpackages

%description
check-manifest is a tool for python developers to check for broken packages
and missing files in MANIFEST.

%prep
%setup -q -n check_manifest-%{version}
%if 0%{?suse_version} == 1500
%patch -P 0 -p1
%endif
sed -i '1{\,^#!%{_bindir}/env python,d}' check_manifest.py
chmod -x check_manifest.py

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/check-manifest
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
# uses pip which likes to use internet to resolve versions
skip='test_build_sdist'
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
%{python_sitelib}/check_manifest.py
%pycache_only %{python_sitelib}/__pycache__/check_manifest*.pyc
%{python_sitelib}/check_manifest-%{version}.dist-info
%endif

%changelog
