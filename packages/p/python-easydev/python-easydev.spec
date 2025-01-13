#
# spec file for package python-easydev
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


Name:           python-easydev
Version:        0.13.3
Release:        0
Summary:        Common utilities to ease the development of Python packages
License:        BSD-3-Clause
URL:            https://github.com/cokelaer/easydev
Source:         https://github.com/cokelaer/easydev/archive/refs/tags/v%{version}.tar.gz#/easydev-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorama
Requires:       python-colorlog
Requires:       python-line_profiler
Requires:       python-pexpect
Requires:       python-platformdirs
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-line_profiler
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module colorlog}
BuildRequires:  %{python_module line_profiler}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The easydev package  provides miscellaneous functions that are
repeatedly used during the development of Python packages. The goal
is to help developers on speeding up their own dev. It has been used
also as an incubator for other packages and is stable.

%prep
%autosetup -p1 -n easydev-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires network access
%pytest -k 'not test_isurl'

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/easydev
%{python_sitelib}/easydev-%{version}.dist-info

%changelog
