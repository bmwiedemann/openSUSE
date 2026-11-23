#
# spec file for package python-click-extra
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


%define module_name click-extra
%define executable_name click-extra

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-click-extra
Version:        10.3.1
Release:        0
Summary:        Drop-in replacement for Click to make user-friendly and colorful CLI
License:        GPL-2.0-or-later
URL:            https://github.com/kdeldycke/click-extra
Source:         https://github.com/kdeldycke/click-extra/archive/v%{version}.tar.gz#/%{module_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build}
# SECTION Build dependencies
# https://github.com/kdeldycke/click-extra/blob/v10.2.0/pyproject.toml
BuildRequires:  %{python_module click >= 8.5.1}
BuildRequires:  %{python_module cloup >= 4}
BuildRequires:  %{python_module extra-platforms >= 14}
BuildRequires:  %{python_module tabulate >= 0.10}
BuildRequires:  %{python_module wcmatch >= 10.0}
BuildRequires:  %{python_module wcwidth >= 0.8.3}
# optional dependencies
BuildRequires:  %{python_module PyYAML >= 6.0.3}
BuildRequires:  %{python_module hjson >= 3.1}
BuildRequires:  %{python_module json5 >= 0.12.1}
BuildRequires:  %{python_module mkdocs >= 1.4}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pygments >= 2.18}
BuildRequires:  %{python_module pymdown-extensions >= 10}
BuildRequires:  git-core
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 8.0}
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module jsonschema >= 4.18}
BuildRequires:  %{python_module myst-parser >= 5.2}
BuildRequires:  %{python_module pytest >= 9.0.0}
BuildRequires:  %{python_module pytest-httpserver >= 1.1.0}
BuildRequires:  %{python_module pytest-randomly >= 4.0.0}
BuildRequires:  %{python_module requests >= 2.34}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 8.5.1
Requires:       python-cloup >= 4
Requires:       python-extra-platforms >= 14
Requires:       python-tabulate >= 0.10
Requires:       python-wcmatch >= 10.0
Requires:       python-wcwidth  >= 0.8.3
Suggests:       python-PyYAML >= 6.0.3
Suggests:       python-pygments >= 2.14
BuildArch:      noarch
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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
%python_clone -a %{buildroot}%{_bindir}/%{executable_name}

%check
# ignore test that requires network connectivity
IGNORED_CHECKS="test_ansi_lexers_candidates"
# assumes that the testsuite is running in a git checkout
IGNORED_CHECKS+=" or test_debug_output or (test_integrated_verbosity_options and DEBUG)"
IGNORED_CHECKS+=" or test_integrated_color_option or test_conf_file_overrides_defaults"
IGNORED_CHECKS+=" or test_context_meta or test_required_command"
IGNORED_CHECKS+=" or test_no_option_leaks_between_subcommands or test_unset_conf_debug_message"
# Broken with extra-platforms 13.10+
IGNORED_CHECKS+=" or test_screen_drawn_with_color"
# the screen names the build host, which can widen it past 80 columns
IGNORED_CHECKS+=" or test_screen_fits_an_eighty_column_terminal"
# timing tests, which fail on a loaded build host
IGNORED_CHECKS+=" or test_startup_time_stays_within_a_ratio_of_click or test_sigterm_shows_the_cursor_again"
# writing TOML needs tomlrt, which is not packaged
IGNORED_CHECKS+=" or (test_all_table_rendering and toml)"
IGNORED_CHECKS+=" or test_export_config or test_serialize_toml or test_serialize_roundtrip"
IGNORED_CHECKS+=" or test_serialize_strips_none or test_show_params_native_types"
IGNORED_CHECKS+=" or test_introspection_flags_load_config_first or test_markup_strips_ansi_by_default"
IGNORED_CHECKS+=" or (test_standalone_no_color_rendering and toml)"
IGNORED_CHECKS+=" or (test_standalone_table_rendering and toml)"
IGNORED_CHECKS+=" or (test_max_column_widths and toml)"
# Broken with cloup <= 4.0.0
IGNORED_CHECKS+=" or test_no_heavy_dependency_ballast_on_startup"

%pytest --import-mode=importlib -m "not network" -k "not (${IGNORED_CHECKS})"

%if %{with libalternatives}
%pre
%python_libalternatives_reset_alternative %{executable_name}
%else

%post
%python_install_alternative %{executable_name}

%postun
# only give the group name for uninstalling
# https://en.opensuse.org/openSUSE:Packaging_Python#Grouped_alternatives
%python_uninstall_alternative %{executable_name}
%endif

%files %{python_files}
%license license
%doc readme.md
%python_alternative %{_bindir}/%{executable_name}
%{python_sitelib}/click_extra
%{python_sitelib}/click_extra-%{version}.dist-info

%changelog
