#
# spec file for package python-phabricator
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
Name:           python-phabricator
Version:        0.7.0
Release:        0
License:        Apache-2.0
Summary:        Phabricator API Bindings
Url:            http://github.com/disqus/python-phabricator
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/phabricator/phabricator-%{version}.tar.gz
BuildRequires:  python-rpm-macros
# For tests
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Phabricator API Bindings

%prep
%setup -q -n phabricator-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests currently broken
#%%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
