#
# spec file for package python-click-extra
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


%define module_name click-extra
%{?sle15_python_module_pythons}
Name:           python-click-extra
Version:        6.1.0
Release:        0
Summary:        Drop-in replacement for Click to make user-friendly and colorful CLI
License:        GPL-2.0-or-later
URL:            https://github.com/kdeldycke/click-extra
Source:         https://github.com/kdeldycke/click-extra/archive/v%{version}.tar.gz#/%{module_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION Build dependencies
# https://github.com/kdeldycke/click-extra/blob/v6.0.3/pyproject.toml#L73
BuildRequires:  %{python_module PyYAML >= 6.0.3}
BuildRequires:  %{python_module boltons >= 25.0.0}
BuildRequires:  %{python_module click >= 8.3.0}
BuildRequires:  %{python_module cloup >= 3.0.7}
BuildRequires:  %{python_module deepmerge >= 2.0}
BuildRequires:  %{python_module extra-platforms >= 3.1.0}
BuildRequires:  %{python_module requests >= 2.32.4}
BuildRequires:  %{python_module tabulate >= 0.9}
BuildRequires:  %{python_module tomli >= 2.0.1 if %python-base < 3.11}
BuildRequires:  %{python_module wcmatch >= 10.0}
BuildRequires:  %{python_module xmltodict >= 0.15.1}
BuildRequires:  git-core
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module pygments >= 2.14}
BuildRequires:  %{python_module Sphinx >= 8.2}
BuildRequires:  %{python_module myst-parser}
BuildRequires:  %{python_module pygments-ansi-color >= 0.3.0}
BuildRequires:  %{python_module pytest >= 8.2.1}
BuildRequires:  %{python_module pytest-httpserver >= 1.0.6}
BuildRequires:  %{python_module pytest-randomly >= 3.16.0}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0.0
Requires:       python-boltons >= 25.0.0
Requires:       python-click >= 8.2.2
Requires:       python-cloup >= 3.0.7
Requires:       python-deepmerge >= 2.0
Requires:       python-extra-platforms >= 3.1.0
Requires:       python-requests >= 2.32.3
Requires:       python-tabulate >= 0.9
Requires:       python-wcmatch >= 10.0
Requires:       python-xmltodict >= 0.14.2
Requires:       (python-tomli >= 2.0.1 if python-base < 3.11)
Suggests:       python-pygments >= 2.14
Suggests:       python-pygments-ansi-color >= 0.3.0
BuildArch:      noarch
%python_subpackages

%description
🌈 Drop-in replacement for Click to make user-friendly and colorful CLI

%prep
%autosetup -p1 -n %{module_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# remove coverage configuration
sed -i '/--cov.*",/d' pyproject.toml
# ignore test that requires network connectivity
IGNORED_CHECKS="test_ansi_lexers_candidates"
# assumes that the testsuite is running in a git checkout
IGNORED_CHECKS+=" or test_debug_output or (test_integrated_verbosity_options and DEBUG)"
IGNORED_CHECKS+=" or test_integrated_color_option or test_conf_file_overrides_defaults"
IGNORED_CHECKS+=" or test_context_meta or test_required_command"
IGNORED_CHECKS+=" or test_no_option_leaks_between_subcommands or test_unset_conf_debug_message"
# table rendering with emojis involves extra spaces
IGNORED_CHECKS+=" or test_all_table_rendering"
IGNORED_CHECKS+=" or test_conf_default_path"
IGNORED_CHECKS+=" or test_integrated_show_params_option"

%pytest -k "not (${IGNORED_CHECKS})"

%files %{python_files}
%license license
%doc readme.md
%{python_sitelib}/click_extra
%{python_sitelib}/click_extra-%{version}.dist-info

%changelog
