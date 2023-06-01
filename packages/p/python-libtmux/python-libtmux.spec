#
# spec file for package python-libtmux
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


%{?sle15_python_module_pythons}
Name:           python-libtmux
Version:        0.22.1
Release:        0
Summary:        Python API / wrapper for tmux
License:        MIT
URL:            https://github.com/tmux-python/libtmux/
Source:         https://files.pythonhosted.org/packages/source/l/libtmux/libtmux-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  tmux
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
libtmux is a typed python scripting library for tmux. You can use it to command and control tmux servers, sessions, windows, and panes. It is the tool powering tmuxp, a tmux workspace manager.

%prep
%setup -q -n libtmux-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export TMUX_TMPDIR=/tmp
# Failing tests on ppc64le
# https://github.com/tmux-python/libtmux/issues/477
# Failing tests on armv7l
# https://github.com/tmux-python/libtmux/issues/479
# Failing tests on ppc64le
# https://github.com/tmux-python/libtmux/issues/478
# Intermittent test errors on x86_64
# https://github.com/tmux-python/libtmux/issues/480
# Intermittent test errors on i586
# https://github.com/tmux-python/libtmux/issues/481
# test_capture_pane
# https://github.com/tmux-python/libtmux/issues/484
IGNORED_TESTS="test_capture_pane"
IGNORED_TESTS="${IGNORED_TESTS} or test_capture_pane_start"
IGNORED_TESTS="${IGNORED_TESTS} or test_function_times_out"
IGNORED_TESTS="${IGNORED_TESTS} or test_function_times_out_no_rise"
IGNORED_TESTS="${IGNORED_TESTS} or test_function_times_out_no_raise_assert"
IGNORED_TESTS="${IGNORED_TESTS} or test_select_window"
IGNORED_TESTS="${IGNORED_TESTS} or test_new_window_with_environment[environment0]"
IGNORED_TESTS="${IGNORED_TESTS} or test_new_window_with_environment[environment1]"
IGNORED_TESTS="${IGNORED_TESTS} or test_split_window_with_environment[environment0]"
IGNORED_TESTS="${IGNORED_TESTS} or test_split_window_with_environment[environment1]"
%pytest -k "not (${IGNORED_TESTS})"

%files %{python_files}
%{python_sitelib}/libtmux/
%{python_sitelib}/libtmux-%{version}*-info
%doc README.md
%license LICENSE

%changelog
