#
# spec file for package python-lexicon
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lexicon
Version:        1.0.0
Release:        0
Summary:        Python dict subclass(es) with aliasing and attribute access
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/bitprophet/lexicon
Source:         https://files.pythonhosted.org/packages/source/l/lexicon/lexicon-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: add_test_init.patch # fix execution of tests
Patch0:         https://github.com/bitprophet/lexicon/pull/10.patch#/add_test_init.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
# Completely different pkg but same namespece in sitelib folder
Conflicts:      python-dns-lexicon
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module spec}
# /SECTION tests
%python_subpackages

%description
Lexicon is a collection of dict subclasses:

* AliasDict, a dictionary supporting both simple and complex key aliasing
* AttributeDict, supporting attribute read and write access
* Lexicon, a subclass of both of the above which exhibits both sets of behavior

%prep
%setup -q -n lexicon-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand spec-%{$python_bin_suffix}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
