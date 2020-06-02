#
# spec file for package python-zake
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-zake
Version:        0.2.2
Release:        0
Summary:        Testing utilities for the kazoo library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/yahoo/Zake
Source:         https://files.pythonhosted.org/packages/source/z/zake/zake-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/yahoo/Zake/master/LICENSE
BuildRequires:  %{python_module kazoo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-kazoo
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
A python package that works to provide a nice set of testing utilities for the kazoo library.

%prep
%setup -q -n zake-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip upstream failing test_child_watch_no_create
# Skip test_clients_counter that is absolutely random
%pytest -k 'not (test_child_watch_no_create or test_clients_counter)'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
