#
# spec file for package python-libtmux
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


%{?sle15_python_module_pythons}
Name:           python-libtmux
Version:        0.62.0
Release:        0
Summary:        Python API / wrapper for tmux
License:        MIT
URL:            https://github.com/tmux-python/libtmux/
Source:         https://github.com/tmux-python/libtmux/archive/v%{version}.tar.gz#/libtmux-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
# https://github.com/tmux-python/libtmux/blob/master/pyproject.toml#L68
BuildRequires:  %{python_module gp-libs >= 0.0.4}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions}
# we do not need pytest-watcher for building on OBS
BuildRequires:  tmux >= 3.2
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
libtmux is a typed python scripting library for tmux. You can use it to command
and control tmux servers, sessions, windows, and panes. It is the tool powering
tmuxp, a tmux workspace manager.

%prep
%setup -q -n libtmux-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Move src to a different path to do not use in tests
mv src src.bak
# Tests fail unless src/libtmux/__about__.py exists...
mkdir -p src/libtmux/
cp src.bak/libtmux/__about__.py src/libtmux/

export TMUX_TMPDIR=/tmp
export PYTEST_IGNORE="test_select_window or "
export PYTEST_IGNORE+="test_session.py::test_select_window or"
export PYTEST_IGNORE+=" tests/test_session.py::test_select_window or"
export PYTEST_IGNORE+=" tests/legacy_api/test_session.py::test_select_window or"
export PYTEST_IGNORE+=" test_function_times_out"

# ModuleNotFoundError: No module named 'gp_sphinx'
rm -f docs/conf.py

echo "Starting tests with PYTEST_IGNORE set to $PYTEST_IGNORE"
%pytest -k "not (${PYTEST_IGNORE})"

rm -rf src/
mv src.bak src

%files %{python_files}
%{python_sitelib}/libtmux/
%{python_sitelib}/libtmux-%{version}*-info
%doc README.md
%license LICENSE

%changelog
