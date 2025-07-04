#
# spec file for package python-fluidity-sm
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-fluidity-sm
Version:        0.2.0
Release:        0
Summary:        State machine implementation for Python objects
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/nsi-iff/fluidity
Source:         https://github.com/nsi-iff/fluidity/archive/%{version}/fluidity-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG README.*
%license LICENSE
%{python_sitelib}/fluidity
%{python_sitelib}/fluidity[-_]sm-%{version}*-info

%changelog
