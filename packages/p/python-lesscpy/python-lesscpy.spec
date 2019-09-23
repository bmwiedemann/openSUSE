#
# spec file for package python-lesscpy
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
Name:           python-lesscpy
Version:        0.13.0
Release:        0
Summary:        Lesscss compiler
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lesscpy/lesscpy
Source:         https://files.pythonhosted.org/packages/source/l/lesscpy/lesscpy-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ply
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%setup -q -n lesscpy-%{version}
# remove failing tests, which rely on find_and_load_cases
rm test/test_{bootstrap3,less,issues}.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/lesscpy
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%post
%python_install_alternative lesscpy

%postun
%python_uninstall_alternative lesscpy

%check
%python_exec -m nose

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/lesscpy
%{python_sitelib}/lesscpy
%{python_sitelib}/lesscpy-%{version}-py*.egg-info

%changelog
