#
# spec file for package python-python-pseudorandom
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-python-pseudorandom
Version:        0.3.2
Release:        0
Summary:        A Python library for generating pseudorandom condition
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/smathot/python-pseudorandom
Source:         https://github.com/smathot/python-pseudorandom/archive/release/%{version}.tar.gz#/python-pseudorandom-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-datamatrix
Recommends:     python-fastnumbers
Recommends:     python-numpy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module fastnumbers}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module python-datamatrix}
# /SECTION
%python_subpackages

%description
A package for pseudorandomization of DataMatrix objects. That is, it allows
you to apply certain constraints to the randomization.

%prep
%setup -q -n pseudorandom-release-%{version}
# touch _unittest/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest testcases/

%files %{python_files}
%license copyright COPYING
%doc readme.md examples/
%{python_sitelib}/pseudorandom
%{python_sitelib}/python_pseudorandom-%{version}.dist-info

%changelog
