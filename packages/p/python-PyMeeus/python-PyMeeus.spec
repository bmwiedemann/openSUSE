#
# spec file for package python-PyMeeus
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-PyMeeus
Version:        0.5.12
Release:        0
Summary:        Python implementation of Jean Meeus astronomical routines
License:        LGPL-3.0-only
URL:            https://github.com/architest/pymeeus
Source:         https://files.pythonhosted.org/packages/source/P/PyMeeus/PyMeeus-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PyMeeus is a Python implementation of the astronomical algorithms
described in the classical book "Astronomical Algorithms, 2nd Edition,
Willmann-Bell Inc. (1998)" by Jean Meeus.

%prep
%setup -q -n PyMeeus-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
