#
# spec file for package python-yamlloader
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-yamlloader
Version:        0.5.5
Release:        0
License:        MIT
Summary:        Ordered YAML loader and dumper for PyYAML
Url:            https://github.com/Phynix/yamlloader
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/y/yamlloader/yamlloader-%{version}.tar.gz
# PATCH-FIX-UPSTREAM happy_utf8.patch gh#Phynix/yamlloader#16 mcepl@suse.com
# Python 3.6 shouldn’t fail on opening utf8 encoded README.rst
Patch0:         happy_utf8.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
This module provides loaders and dumpers for PyYAML. Currently, an
OrderedDict loader/dumper is implemented, allowing to keep items order
when loading resp. dumping a file from/to an OrderedDict (Python 3.7:
Also regular dicts are supported and are the default items to be loaded
to. As of Python 3.7 preservation of insertion order is a language
feature of regular dicts.)

[API Documentation](https://phynix.github.io/yamlloader/index.html).

%prep
%setup -q -n yamlloader-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# there are no tests at all. Sorry.

%files %{python_files}
%{python_sitelib}/*

%changelog
