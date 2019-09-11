#
# spec file for package python-BitVector
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-BitVector
Version:        3.4.9
Release:        0
Summary:        A memory-efficient packed representation for bit arrays in pure Python
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://engineering.purdue.edu/kak/dist/
Source:         https://files.pythonhosted.org/packages/source/B/BitVector/BitVector-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
With regard to the basic purpose of the module, it defines
the BitVector class as a memory-efficient packed
representation for bit arrays. The class comes with a large
number of methods for using the representation in diverse
applications such as computer security, computer vision,
etc.

%prep
%setup -q -n BitVector-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python TestBitVector/Test.py

%files %{python_files}
%doc README
%{python_sitelib}/*

%changelog
