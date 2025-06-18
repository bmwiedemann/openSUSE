#
# spec file for package python-ansi2html
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-ansi2html
Version:        1.9.2
Release:        0
Summary:        Python module to convert text with ANSI color codes to HTML or LaTeX
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/pycontribs/ansi2html/
Source:         https://github.com/pycontribs/ansi2html/archive/v%{version}.tar.gz
# PATCH-FIX-OPENSUSE opensuse-test.patch bsc#[0-9]+ mcepl@suse.com
# Make tests work with versioned executables before alts kick in
# If any other test fails, because the executable is not
# "ansi2html", replace it with self.cmd_exe
Patch0:         opensuse-test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
Convert text with ANSI color codes to HTML or to LaTeX.

Inspired by and developed off of the work of pixelbeat and blackjack.

Read the [docs](https://ansi2html.readthedocs.io/) for more informations.

%prep
%autosetup -p1 -n ansi2html-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/ansi2html

%check
# https://github.com/pycontribs/ansi2html/issues/169
sed -i 's:from mock:from unittest.mock:' tests/test_ansi2html.py
export PATH=$PATH:%{buildroot}%{_bindir}
# ansi2html not available (update alternatives); solvable
# but it runs just ansi2html --version
%pytest

%pre
%python_libalternatives_reset_alternative ansi2html

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/ansi2html
%{python_sitelib}/ansi2html/
%{python_sitelib}/ansi2html-*.dist-info/

%changelog
