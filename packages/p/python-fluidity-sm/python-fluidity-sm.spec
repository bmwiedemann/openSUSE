#
# spec file for package python-fluidity-sm
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
Name:           python-fluidity-sm
Version:        0.2.0
Release:        0
Summary:        State machine implementation for Python objects
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/nsi-iff/fluidity
Source:         https://github.com/nsi-iff/fluidity/archive/%{version}/fluidity-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
State machine implementation for Python objects.

A Fluidity state machine must have one initial state and at least two states.

A state may have enter and exit callbacks, for running some code on state enter
and exit, respectively. These params can be method names (as strings),
callables, or lists of method names or callables.

%prep
%setup -q -n fluidity-%{version}
rm -rf *.egg-info/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG README.*
%license LICENSE
%{python_sitelib}/*

%changelog
