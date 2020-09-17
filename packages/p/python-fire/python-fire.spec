#
# spec file for package python-fire
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-fire
Version:        0.3.1
Release:        0
Summary:        A library for automatically generating command line interfaces
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/google/python-fire
Source:         https://files.pythonhosted.org/packages/source/f/fire/fire-%{version}.tar.gz
Patch0:         subpoint-usage-test.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       python-termcolor
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Levenshtein}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module termcolor}
# /SECTION
%python_subpackages

%description
Python Fire is a library for automatically generating command line
interfaces (CLIs) from a Python object.

%prep
%setup -q -n fire-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
