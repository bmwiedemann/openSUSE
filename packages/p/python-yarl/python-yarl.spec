#
# spec file for package python-yarl
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


Name:           python-yarl
Version:        1.8.2
Release:        0
Summary:        Yet another URL library
License:        Apache-2.0
URL:            https://github.com/aio-libs/yarl/
Source:         https://files.pythonhosted.org/packages/source/y/yarl/yarl-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Workaround until gh#aio-libs/yarl#803 is fixed
Patch0:         support-python-311.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module idna >= 2.0}
# test requirements
BuildRequires:  %{python_module multidict >= 4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-idna >= 2.0
Requires:       python-multidict >= 4.0
%python_subpackages

%description
The module provides a URL class for url parsing and changing.

%prep
%autosetup -p1 -n yarl-%{version}
sed -i '/addopts/d' setup.cfg

%build
export CFLAGS="%{optflags} -Wno-return-type"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitearch}/yarl
%{python_sitearch}/yarl-%{version}*-info

%changelog
