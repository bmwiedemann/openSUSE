#
# spec file for package python-columnize
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


%define modname columnize
Name:           python-columnize
Version:        0.3.11
Release:        0
Summary:        Format a simple (i.e. not nested) list into aligned columns
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rocky/pycolumnize
Source0:        https://files.pythonhosted.org/packages/source/c/columnize/columnize-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION For tests
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Format a simple (i.e. not nested) list into aligned columns.

%prep
%autosetup -p1 -n columnize-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc NEWS.md README.rst
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info/

%changelog
