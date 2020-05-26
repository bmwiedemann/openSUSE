#
# spec file for package python-mutmut
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
# tri.declarative is Python 3 only
%define skip_python2 1
Name:           python-mutmut
Version:        2.0.0
Release:        0
Summary:        Python mutation testing
License:        BSD-3-Clause
URL:            https://github.com/boxed/mutmut
Source:         https://github.com/boxed/mutmut/archive/%{version}.tar.gz
Patch1:         pr_134.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-glob2
Requires:       python-hammett
Requires:       python-junit-xml >= 1.8
Requires:       python-parso
Requires:       python-pony
Requires:       python-setuptools
Requires:       python-tri.declarative >= 3.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-coverage
Recommends:     python-pytest
Suggests:       python-pytest-cov
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module glob2}
BuildRequires:  %{python_module hammett}
BuildRequires:  %{python_module junit-xml >= 1.8}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module parso}
BuildRequires:  %{python_module pony}
BuildRequires:  %{python_module pytest >= 2.8.7}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module tri.declarative >= 3.0.0}
BuildRequires:  %{python_module whatthepatch >= 0.0.5}
BuildRequires:  ed
BuildRequires:  patch
# /SECTION
%python_subpackages

%description
Python mutation testing.

%prep
%setup -q -n mutmut-%{version}
%autopatch -p1
sed -i 's/==/>=/' *requirements.txt
# Remove maximum pins any anything that follows
sed -Ei 's/,?<=?.*$//' test_requirements.txt
sed -i '1{/^#!/d}' mutmut/__main__.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mutmut
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative mutmut

%postun
%python_uninstall_alternative mutmut

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/mutmut
%{python_sitelib}/*

%changelog
