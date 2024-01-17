#
# spec file for package python-mathics_pygments
#
# Copyright (c) 2022 SUSE LLC
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
# Mathics-Scanner does not support python2
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-mathics-pygments
Version:        1.0.2
Release:        0
Summary:        Mathematica/Wolfram Language Lexer for Pygments
License:        MIT
URL:            http://github.com/Mathics3/mathics-pygments/
Source:         https://github.com/Mathics3/mathics-pygments/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module Mathics-Scanner >= 1.2.0}
BuildRequires:  %{python_module Pygments >= 2}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Mathics-Scanner >= 1.2.0
Requires:       python-Pygments >= 2
BuildArch:      noarch
%python_subpackages

%description
A lexer and highlighter for Mathematica/Wolfram Language source code using the
pygments engine.

%prep
%setup -q -n mathics-pygments-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.md
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
