#
# spec file for package python-multi_key_dict
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
Name:           python-multi_key_dict
Version:        2.0.3
Release:        0
Summary:        Multi key dictionary implementation
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/formiaczek/multi_key_dict
Source:         https://pypi.python.org/packages/source/m/multi_key_dict/multi_key_dict-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Multi-key dict provides also extended interface for iterating over items and
keys (e.g. by the key type), which might be useful when creating, e.g.
dictionaries with index-name key pair allowing to iterate over items using
either: names or indexes.
It can be useful for many many other similar use-cases, and there is no limit
to the number of keys used to map to the value.

%prep
%setup -q -n multi_key_dict-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
