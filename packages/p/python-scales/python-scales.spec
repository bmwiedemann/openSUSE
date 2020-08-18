#
# spec file for package python-scales
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
Name:           python-scales
Version:        1.0.9
Release:        0
Summary:        Stats for Python processes
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://www.github.com/Cue/scales
Source:         https://files.pythonhosted.org/packages/source/s/scales/scales-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/Cue/scales/master/LICENSE
Patch0:         python38.patch
# PATCH-FEATURE-UPSTREAM clean_testsuite.patch gh#Cue/scales#50 mcepl@suse.com
# clean up test suite
Patch1:         clean_testsuite.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Statistic generator for python processes

%prep
%setup -q -n scales-%{version}
%autopatch -p1

cp %{SOURCE99} .
sed -i '/nose/d' setup.py

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
