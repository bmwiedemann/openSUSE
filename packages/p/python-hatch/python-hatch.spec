#
# spec file for package python-hatch
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-hatch%{psuffix}
Version:        1.16.2
Release:        0
Summary:        Modern, extensible Python project management
License:        MIT
URL:            https://hatch.pypa.io/latest/
# SourceRepository: https://github.com/pypa/hatch
Source0:        https://github.com/pypa/hatch/archive/refs/tags/hatch-v%{version}.tar.gz
# For the tests gh#pypa/hatch#2123
Source11:       https://files.pythonhosted.org/packages/py3/b/binary/binary-1.0.2-py3-none-any.whl
Source12:       https://files.pythonhosted.org/packages/py3/c/certifi/certifi-2025.11.12-py3-none-any.whl
Source13:       https://files.pythonhosted.org/packages/py3/c/charset_normalizer/charset_normalizer-3.4.4-py3-none-any.whl
Source14:       https://files.pythonhosted.org/packages/py3/c/click/click-8.3.1-py3-none-any.whl
Source15:       https://files.pythonhosted.org/packages/py3/f/flit_core/flit_core-3.10.1-py3-none-any.whl
Source16:       https://files.pythonhosted.org/packages/py3/h/hatchling/hatchling-1.28.0-py3-none-any.whl
Source17:       https://files.pythonhosted.org/packages/py3/i/idna/idna-3.11-py3-none-any.whl
Source18:       https://files.pythonhosted.org/packages/py3/p/packaging/packaging-25.0-py3-none-any.whl
Source19:       https://files.pythonhosted.org/packages/py3/p/pathspec/pathspec-0.12.1-py3-none-any.whl
Source20:       https://files.pythonhosted.org/packages/py3/p/pluggy/pluggy-1.6.0-py3-none-any.whl
Source21:       https://files.pythonhosted.org/packages/py3/r/requests/requests-2.32.5-py3-none-any.whl
Source22:       https://files.pythonhosted.org/packages/py3/s/setuptools/setuptools-80.9.0-py3-none-any.whl
Source23:       https://files.pythonhosted.org/packages/py3/t/trove_classifiers/trove_classifiers-2025.12.1.14-py3-none-any.whl
Source24:       https://files.pythonhosted.org/packages/py3/u/urllib3/urllib3-2.6.2-py3-none-any.whl
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatch-vcs >= 0.3}
BuildRequires:  %{python_module hatchling >= 1.27}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-click >= 8.0.6
Requires:       python-hatchling >= 1.27.0
Requires:       python-httpx >= 0.22.0
Requires:       python-hyperlink >= 21.0.0
Requires:       python-keyring >= 23.5.0
Requires:       python-packaging >= 24.2
Requires:       python-platformdirs >= 2.5.0
Requires:       python-pyproject-hooks
Requires:       python-rich >= 11.2.0
Requires:       python-shellingham >= 1.4.0
Requires:       python-tomli-w >= 1.0
Requires:       python-tomlkit >= 0.11.1
Requires:       python-uv >= 0.5.23
Requires:       python-virtualenv >= 20.26.1
Requires:       (python-backports.zstd > 1 if python-base < 3.14)
Requires:       (python-pexpect >= 4.8 with python-pexpect < 5)
Requires:       (python-userpath >= 1.7 with python-userpath < 2)
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module editables}
BuildRequires:  %{python_module filelock >= 3.7.1}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module hatch = %{version}}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trustme}
BuildRequires:  cargo
%if 0%{?suse_version} >= 1699
BuildRequires:  python39-base
%endif
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
%if 0%{?suse_version} >= 1699
sed -e 's/Source: pip$/Source: system/' \
    -e 's/Source: Pyenv$/Source: system/' \
    -i tests/cli/self/test_report.py
%endif

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
# Need to provide some wheels offline: gh#pypa/hatch#2123
export UV_FIND_LINKS=%{_sourcedir}
export UV_OFFLINE=1
# finds bash instead of expected sh as default shell inside obs
donttest="(test_install and test_already_installed_update_prompt)"
donttest="$donttest or (test_install and test_already_installed_update_flag)"
donttest="$donttest or (test_install and test_all)"
# platform distribution selection errors: https://github.com/pypa/hatch/issues/1145
%ifnarch x86_64
donttest="$donttest or (test_resolve and test_resolution_error)"
donttest="$donttest or (test_resolve and test_legacy_option)"
donttest="$donttest or (test_resolve and test_compatib)"
donttest="$donttest or test_custom_source or test_pypy_custom"
%endif
%ifarch s390x
# Console width different
donttest="$donttest or test_context_formatting"
%endif
# This requires a hatchling not released yet (hatchling > 1.28)
donttest+=" or test_sbom_from_build_data"
%if 0%{?suse_version} < 1699
# Wants to create a Python 3.9 environment and would download the interpreter
donttest+=" or test_workspace_overrides_matrix_conditional_members"
donttest+=" or test_workspace_overrides_combined_conditions"
%endif
# Would need to provide too many offline wheels
donttest+=" or test_workspace_member_features"
donttest+=" or test_workspace_library_with_plugins"
donttest+=" or test_workspace_multi_service_application"
donttest+=" or test_workspace_documentation_generation"
donttest+=" or test_workspace_development_workflow"
donttest+=" or test_workspace_overrides_matrix_conditional_members"
%pytest -n auto -v -k "not ($donttest)"
%endif

%post
%python_install_alternative hatch

%postun
%python_uninstall_alternative hatch

%pre
%python_libalternatives_reset_alternative hatch

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/hatch
%{python_sitelib}/hatch
%{python_sitelib}/hatch-%{version}.dist-info
%endif

%changelog
