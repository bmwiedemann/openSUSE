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

Name:           python-hatch%{psuffix}
Version:        1.6.3
Release:        0
Summary:        Modern, extensible Python project management
License:        MIT
URL:            https://hatch.pypa.io/latest/
# SourceRepository: https://github.com/pypa/hatch
Source:         https://github.com/pypa/hatch/archive/refs/tags/hatch-v%{version}.tar.gz
# PATCH-FIX-UPSTREAM hatch-pr659-utf8.patch gh#pypa/hatch#659 required due to newer hatchling
Patch1:         hatch-pr659-utf8.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 1.11.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires:       git-core
%{?python_enable_dependency_generator}
%if %{with test}
BuildRequires:  %{python_module filelock >= 3.7.1}
BuildRequires:  %{python_module hatch = %{version}}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-randomly}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trustme}
%endif

%python_subpackages

%description
Hatch is a modern, extensible Python project manager.

Features
  * Standardized build system with reproducible builds by default
  * Robust environment management with support for custom scripts
  * Easy publishing to PyPI or other indexes
  * Version management
  * Configurable project generation with sane defaults
  * Responsive CLI, ~2-3x faster than equivalent tools

%prep
%autosetup -p1 -n hatch-hatch-v%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/hatch
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
# tests expect this to be unset and use their own reproducible value. Nothing installed from here.
# https://hatch.pypa.io/latest/config/build/#reproducible-builds
unset SOURCE_DATE_EPOCH
%pytest
%endif

%post
%python_install_alternative hatch

%postun
%python_uninstall_alternative hatch

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/hatch
%{python_sitelib}/hatch
%{python_sitelib}/hatch-%{version}.dist-info
%endif

%changelog
