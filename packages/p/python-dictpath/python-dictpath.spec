#
# spec file for package python-dictpath
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-dictpath
Version:        0.1.3
Release:        0
Summary:        Object-oriented dictionary paths
License:        Apache-2.0
URL:            https://github.com/p1c2u/dictpath
# Use the github tarball because it contains the tests
Source:         https://github.com/p1c2u/dictpath/archive/refs/tags/%{version}.tar.gz#/dictpath-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-six
# SECTION test requirements
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python2-mock
%endif
# /SECTION
%python_subpackages

%description
Object-oriented dictionary paths:
  * Traverse resources like paths
  * Access resources on demand with separate accessor layer

%prep
%setup -q -n dictpath-%{version}
# remove coverage flags for pytest
sed -i '/addopts/ d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
