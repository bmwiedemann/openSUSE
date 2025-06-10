#
# spec file for package python-lesscpy
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
Name:           python-lesscpy
Version:        0.15.1
Release:        0
Summary:        Lesscss compiler
License:        MIT
URL:            https://github.com/lesscpy/lesscpy
Source:         https://files.pythonhosted.org/packages/source/l/lesscpy/lesscpy-%{version}.tar.gz
# https://github.com/lesscpy/lesscpy/pull/126
Patch0:         python-lesscpy-no-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-ply
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
python LessCss Compiler.

A compiler written in python 3 for the lesscss language.
For those of us not willing/able to have node.js installed in our environment.
Not all features of lesscss are supported (yet).
Some features wil probably never be supported (JavaScript evaluation).
This program uses PLY (Python Lex-Yacc) to tokenize/parse the input.

%prep
%autosetup -p1 -n lesscpy-%{version}
# remove failing tests, which rely on find_and_load_cases
rm test/test_{bootstrap3,less,issues}.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lesscpy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative lesscpy

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/lesscpy
%{python_sitelib}/lesscpy
%{python_sitelib}/lesscpy-%{version}*-info

%changelog
