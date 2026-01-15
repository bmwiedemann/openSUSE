#
# spec file for package python-textual
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
%{?sle15_python_module_pythons}
Name:           python-textual%{psuffix}
Version:        7.2.0
Release:        0
Summary:        TUI framework for Python
License:        MIT
URL:            https://github.com/Textualize/textual
Source:         https://files.pythonhosted.org/packages/source/t/textual/textual-%{version}.tar.gz
#
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
%if %{with test}
BuildRequires:  %{python_module jinja2}
BuildRequires:  %{python_module linkify-it-py}
BuildRequires:  %{python_module pytest >= 8.3.1}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-textual-snapshot >= 1.1.0}
BuildRequires:  %{python_module pytest-xdist >= 3.6.1}
BuildRequires:  %{python_module syrupy}
BuildRequires:  %{python_module textual = %{version}}
BuildRequires:  %{python_module tree-sitter}
BuildRequires:  tree-sitter
BuildRequires:  tree-sitter-python
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#
Requires:       python-markdown-it-py >= 2.1.0
Requires:       python-rich >= 13.3.3
Requires:       (python-platformdirs >= 3.6.0 with python-platformdirs < 5)
Requires:       (python-pygments >= 2.19.2 with python-pygments < 2.20)
Requires:       (python-typing-extensions >= 4.4.0 with python-typing-extensions < 5)
Suggests:       python-jinja2
Suggests:       python-tree-sitter
Suggests:       python-tree-sitter-languages
BuildArch:      noarch
%python_subpackages

%description
Textual is a Python framework for creating interactive applications
that run in your terminal.

It adds interactivity to Rich with a Python API inspired by modern
web development.

On modern terminal software (installed by default on most systems),
Textual apps can use 16.7 million colors with mouse support and
smooth flicker-free animation. A layout engine and re-usable
components make it possible to build apps that resemble the desktop
and web experience.

%prep
%autosetup -n textual-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# fixture 'snap_compare' not found
rm -f tests/snapshot_tests/test_snapshots.py
IGNORED_CHECKS="test_textual_env_var"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_allow_focus"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_focus_chain"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_focus_next_and_previous"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_focus_next_and_previous_with_str_selector"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_focus_next_and_previous_with_str_selector_without_self"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_focus_next_and_previous_with_type_selector"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_focus_next_and_previous_with_type_selector_without_self"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_focus_next_wrap_around"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_focus_previous_wrap_around"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_language_binary_missing"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_message_sender_from_reactive"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_no_focus_empty_selector"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_register_language"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_register_language_existing_language"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_wrap_around_selector"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_setting_unknown_language"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_update_highlight_query"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_widget_construct"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_setting_builtin_language_via_constructor"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_setting_builtin_language_via_attribute"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_setting_language_to_none"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_default_theme"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_setting_builtin_themes"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_setting_unknown_theme_raises_exception"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_registering_and_setting_theme"
%pytest -k "not (${IGNORED_CHECKS})"
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/textual
%{python_sitelib}/textual-%{version}*-info
%endif

%changelog
