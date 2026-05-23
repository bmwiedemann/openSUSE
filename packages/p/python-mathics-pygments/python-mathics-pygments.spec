#
# spec file for package python-mathics-pygments
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


%define modname mathics_pygments
Name:           python-mathics-pygments
Version:        10.0.0
Release:        0
Summary:        Mathematica/Wolfram Language Lexer for Pygments
License:        MIT
URL:            http://github.com/Mathics3/mathics-pygments/
Source:         https://github.com/Mathics3/mathics-pygments/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Mathics-Scanner >= 10.0.0}
BuildRequires:  %{python_module Pygments >= 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Mathics-Scanner >= 10.0.0
Requires:       python-Pygments >= 2
Provides:       python-Mathics3-pygments
BuildArch:      noarch
%python_subpackages

%description
A lexer and highlighter for Mathematica/Wolfram Language source code using the
pygments engine.

%prep
%autosetup -n Mathics3-pygments-%{version}
sed -Ei "1{\@/usr/bin/env@d}" mathics_pygments/generate/build_pygments_tables.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.md
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/mathics3_pygments-%{version}*.*-info/

%changelog
