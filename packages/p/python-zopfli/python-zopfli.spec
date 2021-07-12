#
# spec file for package python-zopfli
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
Name:           python-zopfli
Version:        0.1.8
Release:        0
Summary:        Zopfli module for python
License:        Apache-2.0
URL:            https://github.com/obp/py-zopfli
Source:         https://files.pythonhosted.org/packages/source/z/zopfli/zopfli-%{version}.zip
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%python_subpackages

%description
Zopfli module for python

%prep
%setup -q -n zopfli-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitearch}/*

%changelog
