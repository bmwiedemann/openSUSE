#
# spec file for package python-invoke
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-invoke%{psuffix}
Version:        2.2.1
Release:        0
Summary:        Pythonic Task Execution
License:        BSD-2-Clause
URL:            https://www.pyinvoke.org
Source:         https://files.pythonhosted.org/packages/source/i/invoke/invoke-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove-icecream.patch mcepl@suse.com
# We don’t need icecream as yet another complication.
Patch0:         remove-icecream.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools > 56}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-fluidity-sm
Requires:       python-lexicon
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module fluidity-sm}
BuildRequires:  %{python_module invocations >= 3.0.1}
BuildRequires:  %{python_module invoke >= %version}
BuildRequires:  %{python_module lexicon}
BuildRequires:  %{python_module pytest-relaxed}
BuildRequires:  %{python_module pytest}
BuildRequires:  zsh
%endif
%python_subpackages

%description
Invoke is a Python (2.7 and 3.4+) task execution tool & library, drawing
inspiration from various sources to arrive at a powerful & clean feature set.

%prep
%autosetup -p1 -n invoke-%{version}
# Remove bundled libs, import will fallback to system provided libs
rm -fr invoke/vendor/*

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/inv
%python_clone -a %{buildroot}%{_bindir}/invoke
%python_group_libalternatives inv invoke
%endif

%if %{with test}
%check
# gh#pyinvoke/invoke#705
skiptests="setcbreak_called_on_tty_stdins or setcbreak_not_called_if_process_not_foregrounded"
skiptests+=" or tty_stdins_have_settings_restored_by_default or tty_stdins_have_settings_restored_on_KeyboardInterrupt"
skiptests+=" or when_pty_True_we_use_pty_fork_and_os_exec or pty_uses_WEXITSTATUS_if_WIFEXITED"
skiptests+=" or pty_uses_WTERMSIG_if_WIFSIGNALED or WTERMSIG_result_turned_negative_to_match_subprocess"
skiptests+=" or pty_is_set_to_controlling_terminal_size or spurious_OSErrors_handled_gracefully"
skiptests+=" or other_spurious_OSErrors_handled_gracefully or non_spurious_OSErrors_bubble_up"
skiptests+=" or can_be_overridden_by_kwarg or can_be_overridden_by_config"
skiptests+=" or overridden_fallback_affects_result_pty_value or defaults_to_bash_or_cmdexe_when_pty_True"
skiptests+=" or may_be_overridden_when_pty_True or uses_execve_for_pty_True or stop_mutes_errors_on_pty_close"
%pytest -s -k "not ($skiptests)" tests
%endif

%post
%python_install_alternative inv invoke

%postun
%python_uninstall_alternative inv

%pre
%python_libalternatives_reset_alternative inv

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/inv
%python_alternative %{_bindir}/invoke
%{python_sitelib}/invoke
%{python_sitelib}/invoke-%{version}*-info
%endif

%changelog
