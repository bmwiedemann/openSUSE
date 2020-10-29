#
# spec file for package python-tqdm
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define test 1
%define pkg_suffix -test
%bcond_without test
%else
%define pkg_suffix %{nil}
%bcond_with test
%endif
Name:           python-tqdm%{pkg_suffix}
Version:        4.50.2
Release:        0
Summary:        An extensible progress meter
License:        MPL-2.0 AND MIT
URL:            https://github.com/tqdm/tqdm
Source:         https://files.pythonhosted.org/packages/source/t/tqdm/tqdm-%{version}.tar.gz
# https://github.com/tqdm/tqdm/pull/1052
Patch0:         python-tqdm-remove-nose.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tqdm}
BuildRequires:  python3-ipython
BuildRequires:  python3-ipywidgets
# /SECTION
%endif
%python_subpackages

%description
tqdm lets you output a progress meter from within loops by wrapping
any iterable with "tqdm(iterable)".
tqdm's overhead is one order of magnitude less than python-progressbar
and does not require ncurses.

%prep
%setup -q -n tqdm-%{version}
%patch0 -p1

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/tqdm
install -m 644 -D tqdm/completion.sh %{buildroot}%{_datadir}/bash-completion/completions/tqdm
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if !%{with test}
%post
%{python_install_alternative tqdm tqdm.1}

%postun
%python_uninstall_alternative tqdm
%endif

%if %{with test}
%check
# test_perf: flaky
# test_synchronisation: hangs
# test_main: todo upstream, TypeError: a bytes-like object is required, not 'str'
#            also disabled in https://github.com/tqdm/tqdm/pull/1052
#            and left upstream to solve
%pytest -k "not (tests_perf or tests_synchronisation or test_main)" tqdm/
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst logo.png
%doc examples/
%license LICENCE
%{python_sitelib}/tqdm/
%{python_sitelib}/tqdm-%{version}-py*.egg-info
%python_alternative %{_bindir}/tqdm
%{_datadir}/bash-completion/completions/tqdm
%endif

%changelog
