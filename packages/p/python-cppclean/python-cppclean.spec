#
# spec file for package python-cppclean
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


%bcond_without libalternatives
Name:           python-cppclean
Version:        0.13
Release:        0
Summary:        Program to find problems in C++ source code
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/myint/cppclean
Source:         https://github.com/myint/cppclean/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  bash
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
CPPclean attempts to find problems in C++ source that slow development
in large code bases, for example various forms of unused code.
Unused code can be unused functions, methods, data members, types, etc
to unnecessary #include directives. Unnecessary #includes can cause
considerable extra compiles increasing the edit-compile-run cycle.

%prep
%setup -q -n cppclean-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cppclean
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHON=%{__$python} bash test.bash

%pre
# Removing old update-alternatives entries.
%python_libalternatives_reset_alternative cppclean

%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/cppclean
%{python_sitelib}/cpp
%{python_sitelib}/cppclean-%{version}*-info

%changelog
