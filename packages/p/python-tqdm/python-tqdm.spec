#
# spec file for package python-tqdm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define suffix -test
%bcond_without test
%else
%define suffix %{nil}
%bcond_with test
%endif
Name:           python-tqdm%{suffix}
Version:        4.35.0
Release:        0
Summary:        An extensible progress meter
License:        MPL-2.0 AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/tqdm/tqdm
Source:         https://files.pythonhosted.org/packages/source/t/tqdm/tqdm-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module tqdm}
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

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/tqdm
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
%{python_expand PYTHONPATH=%{$python_sitelib}
nosetests-%%{$python_bin_suffix} --ignore-files="tests_perf\.py" --ignore-files="tests_synchronisation\.py" tqdm/
}
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst logo.png
%doc examples/
%license LICENCE
%dir %{python_sitelib}/tqdm
%dir %{python_sitelib}/tqdm-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/tqdm/*
%{python_sitelib}/tqdm-%{version}-py%{py_ver}.egg-info/*
%python_alternative %{_bindir}/tqdm
%endif

%changelog
