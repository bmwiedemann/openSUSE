#
# spec file for package python-Levenshtein
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Levenshtein
Version:        0.12.0
Release:        0
Summary:        Python extension computing string distances and similarities
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ztane/python-Levenshtein/
Source0:        https://files.pythonhosted.org/packages/source/p/python-Levenshtein/python-Levenshtein-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The Levenshtein Python C extension module contains functions for fast
computation of

 * Levenshtein (edit) distance, and edit operations
 * string similarity
 * approximate median strings, and generally string averaging
 * string sequence and set similarity

It supports both normal and Unicode strings.

%prep
%setup -q

%build
%python_build

%install
%python_install
rm -v %{buildroot}%{_libdir}/python*/*/Levenshtein/_levenshtein.{c,h}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license COPYING
%doc HISTORY.txt README.rst NEWS
%{python_sitearch}/*

%changelog
