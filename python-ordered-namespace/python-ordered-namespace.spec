#
# spec file for package python-ordered-namespace
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
Name:           python-ordered-namespace
Version:        2019.6.8
Release:        0
Summary:        Python namespace class
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/who8mylunch/OrderedNamespace
Source:         https://files.pythonhosted.org/packages/source/o/ordered_namespace/ordered_namespace-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/Who8MyLunch/OrderedNamespace/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python namespace class derived from OrderedDict,
including tab-completion

%prep
%setup -q -n ordered_namespace-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests have no way of being executed properly
# on github there are no tags

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
