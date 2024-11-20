#
# spec file for package python-gfloat
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


Name:           python-gfloat
Version:        0.4
Release:        0
Summary:        Generic floating point handling in Python
License:        MIT
URL:            None
Source:         https://files.pythonhosted.org/packages/source/g/gfloat/gfloat-%{version}.tar.gz
Patch1:         no-nbval.patch
BuildRequires:  %{python_module ml-dtypes}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module numpy}
# /SECTION
BuildRequires:  fdupes
Requires:       python-more-itertools
Requires:       python-numpy
BuildArch:      noarch
%python_subpackages

%description
Generic floating point handling in Python

%prep
%autosetup -p1 -n gfloat-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# reduce dependencies
rm -v test/test_jax.py test/test_microxcaling.py
%pytest

%files %{python_files}
%doc ChangeLog README.md
%license LICENSE
%{python_sitelib}/gfloat
%{python_sitelib}/gfloat-%{version}.dist-info

%changelog
