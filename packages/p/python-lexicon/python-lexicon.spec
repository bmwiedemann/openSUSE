#
# spec file for package python-lexicon
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-lexicon
Version:        2.0.1
Release:        0
Summary:        Python dict subclass(es) with aliasing and attribute access
License:        BSD-2-Clause
URL:            https://github.com/bitprophet/lexicon
Source:         https://files.pythonhosted.org/packages/source/l/lexicon/lexicon-%{version}.tar.gz
# PATCH-FIX-UPSTREAM (sort of) Not in the sdist, but on GitHub
Patch0:         add-pytest-ini.patch
# PATCH-FIX-OPENSUSE Support pytest >= 8
Patch1:         support-pytest-8.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Completely different pkg but same namespece in sitelib folder
Conflicts:      python-dns-lexicon
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module pytest-relaxed}
# /SECTION tests
%python_subpackages

%description
Lexicon is a collection of dict subclasses:

* AliasDict, a dictionary supporting both simple and complex key aliasing
* AttributeDict, supporting attribute read and write access
* Lexicon, a subclass of both of the above which exhibits both sets of behavior

%prep
%autosetup -p1 -n lexicon-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/lexicon
%{python_sitelib}/lexicon-%{version}.dist-info

%changelog
