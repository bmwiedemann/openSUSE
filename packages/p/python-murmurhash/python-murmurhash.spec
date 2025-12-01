#
# spec file for package python-murmurhash
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-murmurhash
Version:        1.0.15
Release:        0
Summary:        Cython bindings for MurmurHash
License:        MIT
URL:            https://github.com/explosion/murmurhash
Source:         https://files.pythonhosted.org/packages/source/m/murmurhash/murmurhash-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Cython bindings for MurmurHash

%package devel
Summary:        Development files for murmurhash
Group:          Development/Libraries/C and C++
Conflicts:      python-murmurhash < %{version}
BuildArch:      noarch

%description devel
This subpackage contains header files for developing
applications that want to make use of murmurhash.

%prep
%autosetup -p1 -n murmurhash-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}
rm -rv %{buildroot}%{$python_sitearch}/murmurhash/include/murmurhash/*
}
mkdir -p %{buildroot}%{_includedir}
cp -r -p murmurhash/include/murmurhash %{buildroot}%{_includedir}/

%check

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/murmurhash
%{python_sitearch}/murmurhash-%{version}.dist-info

%files -n python-murmurhash-devel
%{_includedir}/murmurhash

%changelog
