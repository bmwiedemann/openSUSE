#
# spec file for package python-distorm3
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
%define modname distorm3
Name:           python-%{modname}
Version:        3.4.1
Release:        0
Summary:        Disassembler Library For x86/AMD64
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/gdabah/distorm
Source:         https://files.pythonhosted.org/packages/source/d/distorm3/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%python_subpackages

%description
diStorm3 is a decomposer, which means it takes an instruction and
returns a binary structure which describes it rather than static
text.

%prep
%setup -q -n %{modname}-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# tests are not packaged in the upstream tarball

%files %{python_files}
%license COPYING
%{python_sitearch}/*

%changelog
