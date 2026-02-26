#
# spec file for package python-slicerator
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-slicerator
Version:        1.1.0
Release:        0
Summary:        A lazy-loading, fancy-sliceable iterable
License:        BSD-3-Clause
URL:            http://github.com/soft-matter/slicerator
Source:         https://files.pythonhosted.org/packages/source/s/slicerator/slicerator-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module numpy}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A lazy-loading, fancy-sliceable iterable.

%prep
%autosetup -p1 -n slicerator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/slicerator
%{python_sitelib}/slicerator-%{version}.dist-info

%changelog
