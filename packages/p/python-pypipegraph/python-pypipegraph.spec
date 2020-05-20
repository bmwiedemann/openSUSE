#
# spec file for package python-pypipegraph
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
%define         skip_python2 1
Name:           python-pypipegraph
Version:        0.189
Release:        0
Summary:        A workflow (job) engine/pipeline
License:        MIT
URL:            https://github.com/TyberiusPrime/pypipegraph
Source:         https://files.pythonhosted.org/packages/source/p/pypipegraph/pypipegraph-%{version}.tar.gz
# PATCH-FIX-UPSTREAM use_current_exe.patch -- https://github.com/TyberiusPrime/pypipegraph/pull/3
Patch0:         use_current_exe.patch
BuildRequires:  %{python_module setuptools >= 38.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A workflow (job) engine/pipeline for bioinformatics and scientific computing.

%prep
%setup -q -n pypipegraph-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ppg_invariant_diff
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# We don't care about these tests
%pytest -k 'not test_flake8 and not test_notebook'

%post
%python_install_alternative ppg_invariant_diff

%postun
%python_uninstall_alternative ppg_invariant_diff

%files %{python_files}
%doc README.md
%license COPYING
%python_alternative %{_bindir}/ppg_invariant_diff
%{python_sitelib}/*

%changelog
