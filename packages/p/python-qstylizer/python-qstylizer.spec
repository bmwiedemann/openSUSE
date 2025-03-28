#
# spec file for package python-qstylizer
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


Name:           python-qstylizer
Version:        0.2.2
Release:        0
Summary:        Stylesheet Generator for PyQt{4-5}/PySide{1-2}
License:        MIT
URL:            https://github.com/blambright/qstylizer
# no sdist on PyPI
Source:         https://github.com/blambright/qstylizer/archive/refs/tags/%{version}.tar.gz#/qstylizer-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM qstylizer-pr17-fix-py12-mock.patch gh#blambright/qstylizer#17
Patch0:         https://github.com/blambright/qstylizer/pull/17.patch#/qstylizer-pr17-fix-py12-mock.patch
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module inflection > 0.3.0}
BuildRequires:  %{python_module pytest >= 4}
BuildRequires:  %{python_module pytest-mock >= 1.6}
BuildRequires:  %{python_module tinycss2}
#BuildRequires:  %%{python_module pytest-catchlog >= 1}
BuildRequires:  %{python_module pytest-xdist >= 1.1}
# /SECTION
BuildRequires:  unzip
BuildRequires:  fdupes
Requires:       python-inflection > 0.3.0
Requires:       python-tinycss2
BuildArch:      noarch
%python_subpackages

%description
A python package designed to help with the construction of PyQt/PySide stylesheets.

%prep
%autosetup -p1 -n qstylizer-%{version}

%build
export PBR_VERSION=%{version}
%pyproject_wheel

%install
export PBR_VERSION=%{version}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/qstylizer
%{python_sitelib}/qstylizer-%{version}.dist-info

%changelog
