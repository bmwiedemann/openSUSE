#
# spec file for package python-datadiff
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
Name:           python-datadiff
Version:        2.2.0
Release:        0
Summary:        DataDiff is a library to provide human-readable diffs of python data structures
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://sourceforge.net/projects/datadiff/
#Source:         https://files.pythonhosted.org/packages/source/d/datadiff/datadiff-%%{version}.tar.gz
#Git-Clone:     https://git.code.sf.net/p/datadiff/code
Source:         datadiff-%{version}.tar.xz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
DataDiff is a library to provide human-readable diffs of python data structures.
It can handle sequence types (lists, tuples, etc), sets, and dictionaries.
Dictionaries and sequences will be diffed recursively, when applicable.
It has special-case handling for multi-line strings, showing them as a typical unified diff.
Drop-in replacements for some nose assertions are available.  If the assertion fails,
a nice data diff is shown, letting you easily pinpoint the root difference.

%prep
%setup -q -n datadiff-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE-2.0.txt
%{python_sitelib}/*

%changelog
