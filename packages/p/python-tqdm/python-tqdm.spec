#
# spec file for package python-tqdm
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


%define         allpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define test 1
%define pkg_suffix -test
%bcond_without test
%else
%define pkg_suffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-tqdm%{pkg_suffix}
Version:        4.67.1
Release:        0
Summary:        An extensible progress meter
License:        MIT AND MPL-2.0
URL:            https://github.com/tqdm/tqdm
Source:         https://files.pythonhosted.org/packages/source/t/tqdm/tqdm-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Enhances:       python-ipython
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module pytest-asyncio >= 0.24}
# Conditional required for SLE-15-SP4+
BuildRequires:  %{python_module numpy if (python-base without python36-base)}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tqdm = %{version}}
%if ! 0%{?_with_ringdisabled}
# Conditional required for SLE-15-SP4+
BuildRequires:  %{python_module pandas if (python-base without python36-base)}
%endif
# /SECTION
%endif
%python_subpackages

%description
tqdm lets you output a progress meter from within loops by wrapping
any iterable with "tqdm(iterable)".
tqdm's overhead is one order of magnitude less than python-progressbar
and does not require ncurses.

%package -n %{allpython}-tqdm-bash-completion
Summary:        Bash completion for python-tqdm
Requires:       bash-completion
Supplements:    %{python_module tqdm and bash-completion}

%description -n %{allpython}-tqdm-bash-completion
tqdm lets you output a progress meter from within loops by wrapping
any iterable with "tqdm(iterable)".
tqdm's overhead is one order of magnitude less than python-progressbar
and does not require ncurses.

This package provides the completion file for bash

%prep
%autosetup -p1 -n tqdm-%{version}
# ignore new asyncio mode warning from pytest-asyncio 0.17
sed -i 's/-W=error//' pyproject.toml
# remove bash shebang for completion script
sed -i '1 s/^#!.*/# bash completion for tqdm       -*- shell-script -*-/' tqdm/completion.sh
chmod a-x tqdm/completion.sh

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/tqdm
install -m 644 -D tqdm/completion.sh %{buildroot}%{_datadir}/bash-completion/completions/tqdm
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if !%{with test}
%post
%python_install_alternative tqdm

%postun
%python_uninstall_alternative tqdm
%endif

%if %{with test}
%check
# test_perf: flaky
# test_synchronisation: hangs
%pytest -k "not (tests_perf or tests_synchronisation)"
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst logo.png
%doc examples/
%license LICENCE
%{python_sitelib}/tqdm/
%{python_sitelib}/tqdm-%{version}.dist-info
%python_alternative %{_bindir}/tqdm

%files -n %{allpython}-tqdm-bash-completion
%license LICENCE
%{_datadir}/bash-completion/completions/tqdm
%endif

%changelog
