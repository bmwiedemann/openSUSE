#
# spec file for package python-hatch
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
Name:           python-hatch%{psuffix}
Version:        1.9.4
Release:        0
Summary:        Modern, extensible Python project management
License:        MIT
URL:            https://hatch.pypa.io/latest/
# SourceRepository: https://github.com/pypa/hatch
Source:         https://github.com/pypa/hatch/archive/refs/tags/hatch-v%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on parts of the following commits:
# gh#pypa/hatch#9a80ffc2567bb09160e97f1ade1dd4c768004089
# gh#pypa/hatch#f3b2159a8c4221062692881774bc58dfed5aaa76
Patch0:         support-hatchling-1.22.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-vcs >= 0.3}
BuildRequires:  %{python_module hatchling >= 1.19}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       git-core
Requires:       python-click >= 8.0.6
Requires:       python-hatchling >= 1.21.0
Requires:       python-httpx >= 0.22.0
Requires:       python-hyperlink >= 21.0.0
Requires:       python-keyring >= 23.5.0
Requires:       python-packaging >= 21.3
Requires:       python-platformdirs >= 2.5.0
Requires:       python-rich >= 11.2.0
Requires:       python-shellingham >= 1.4.0
Requires:       python-tomli-w >= 1.0
Requires:       python-tomlkit >= 0.11.1
Requires:       python-virtualenv >= 20.16.2
Requires:       python-zstandard < 1
Requires:       (python-pexpect >= 4.8 with python-pexpect < 5)
Requires:       (python-userpath >= 1.7 with python-userpath < 2)
%if %{with test}
BuildRequires:  %{python_module editables}
BuildRequires:  %{python_module filelock >= 3.7.1}
BuildRequires:  %{python_module hatch = %{version}}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trustme}
BuildRequires:  cargo
%else
BuildArch:      noarch
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

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
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
# finds bash instead of expected sh as default shell inside obs
donttest="(test_install and test_already_installed_update_prompt)"
donttest="$donttest or (test_install and test_already_installed_update_flag)"
donttest="$donttest or (test_install and test_all)"
# platform distribution selection errors: https://github.com/pypa/hatch/issues/1145
%ifnarch x86_64
donttest="$donttest or (test_resolve and test_resolution_error)"
%endif
%ifarch s390x
# Console width different
donttest="$donttest or test_context_formatting"
%endif
%pytest -v -k "not ($donttest)"
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
