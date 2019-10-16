#
# spec file for package python-twodict
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
Name:           python-twodict
Version:        1.2
Release:        0
Summary:        Simple two-way ordered dictionary for Python
# The Unlicense
License:        SUSE-Permissive
URL:            https://github.com/MrS0m30n3/twodict
Source0:        https://files.pythonhosted.org/packages/source/t/twodict/twodict-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
TwoWayOrderedDict is a custom dictionary in which one can get the
key:value relationship but can also get the value:key relationship.
It also remembers the order in which the items were inserted and
supports almost all the features of the built-in dict.

%prep
%setup -q -n twodict-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_twodict.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
