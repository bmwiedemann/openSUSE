#
# spec file for package python-BitVector
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


Name:           python-BitVector
Version:        3.5.0
Release:        0
Summary:        A memory-efficient packed representation for bit arrays in pure Python
License:        Python-2.0
URL:            https://engineering.purdue.edu/kak/dist/
Source:         https://files.pythonhosted.org/packages/source/B/BitVector/BitVector-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Use load tests protocol to run the testsuite
Patch0:         no-makesuite.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%autosetup -p1 -n BitVector-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v TestBitVector

%files %{python_files}
%doc README
%{python_sitelib}/BitVector
%{python_sitelib}/BitVector-%{version}.dist-info

%changelog
