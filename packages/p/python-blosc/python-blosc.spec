#
# spec file for package python-blosc
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


%{?sle15_python_module_pythons}
Name:           python-blosc
Version:        1.11.2
Release:        0
Summary:        Blosc data compressor for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Blosc/python-blosc
Source:         https://files.pythonhosted.org/packages/source/b/blosc/blosc-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-build >= 0.11.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  blosc-devel >= 1.21
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.14.0
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.16 with %python-numpy < 2}
BuildRequires:  %{python_module psutil}
# /SECTION
Recommends:     python-numpy
%python_subpackages

%description
Blosc is a high performance compressor optimized for binary data in
Python.

%prep
%autosetup -p1 -n blosc-%{version}
rm -r blosc/c-blosc

%build
export CFLAGS="%{optflags}"
export USE_SYSTEM_BLOSC=1
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand #
export PYTHONPATH=%{buildroot}%{$python_sitearch}
export PYTHONDONTWRITEBYTECODE=1
$python -m blosc.test
}

%files %{python_files}
%license LICENSE.txt
%doc ANNOUNCE.rst README.rst RELEASE_NOTES.rst
%{python_sitearch}/blosc-%{version}.dist-info
%{python_sitearch}/blosc/

%changelog
