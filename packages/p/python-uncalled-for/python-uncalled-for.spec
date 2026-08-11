#
# spec file for package python-uncalled-for
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


Name:           python-uncalled-for
Version:        0.4.0
Release:        0
Summary:        Async-friendly dependency injection for Python
License:        MIT
URL:            https://github.com/chrisguidry/uncalled-for
Source:         https://files.pythonhosted.org/packages/source/u/uncalled_for/uncalled_for-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 9.0.2}
BuildRequires:  %{python_module pytest-asyncio >= 0.24.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A small, async-friendly dependency-injection helper for Python: declare
function parameters as dependencies and have them resolved automatically.

%prep
%autosetup -p1 -n uncalled_for-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/uncalled_for
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Upstream's addopts are CI-only gates: --cov*/--cov-fail-under=100 need
# pytest-cov and enforce a coverage target, and --timeout=30 needs
# pytest-timeout and is flaky on loaded OBS workers. Drop both and keep
# upstream's import mode so the full suite still runs against the installed
# package (asyncio_mode=auto stays in effect from pyproject.toml).
%pytest -o addopts="--import-mode=importlib"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/uncalled_for
%{python_sitelib}/uncalled_for-%{version}.dist-info

%changelog
