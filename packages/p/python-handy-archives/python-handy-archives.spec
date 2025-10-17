#
# spec file for package python-handy-archives
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-handy-archives%{psuffix}
Version:        0.2.0
Release:        0
Summary:        Some handy archive helpers for Python
License:        MIT
URL:            https://github.com/domdfcoding/handy-archives
Source:         https://github.com/domdfcoding/handy-archives/archive/refs/tags/v%{version}.tar.gz#/handy_archives-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#domdfcoding/handy-archives#3bc48dda6a06545ba53a829c6efb0f1a1b95349e
Patch0:         ignore-tarfile-deprecation-warning.patch
# PATCH-FIX-UPSTREAM: 0001-Use-reason-instead-of-msg-for-pytest.skip.patch gh#domdfcoding/handy-archives#35
Patch1:         0001-Use-reason-instead-of-msg-for-pytest.skip.patch
Patch2:         https://github.com/domdfcoding/handy-archives/commit/18b4319972210d7b4512bb3431c2746708ff8be5.patch#/py313-tests-update.patch
Patch3:         https://github.com/domdfcoding/handy-archives/commit/85526bff5b6b46aa77dd361ba031291fcb21b195.patch#/py313-mode-repr.patch
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
%if %{with test}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module handy-archives = %{version}}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-coincidence >= 0.2.0
Suggests:       python-pytest >= 6.0.0
BuildArch:      noarch
%python_subpackages

%description
Some handy archive helpers for Python.

%prep
%autosetup -p1 -n handy-archives-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# zip64 test are not working in newer python interpreter because there
# are more consistency checks in zipfile
# https://github.com/python/cpython/issues/139700
donttest="test_bad_zip64_extra or test_generated_valid_zip64_extra"
%pytest -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/handy_archives
%{python_sitelib}/handy_archives-%{version}.dist-info
%endif

%changelog
