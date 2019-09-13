#
# spec file for package python-numexpr
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
Name:           python-numexpr
Version:        2.7.0
Release:        0
Summary:        Numerical expression evaluator for NumPy
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pydata/numexpr/
Source:         https://files.pythonhosted.org/packages/source/n/numexpr/numexpr-%{version}.tar.gz
Patch0:         fix_test.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.6
%python_subpackages

%description
Numexpr is a numerical expression evaluator for NumPy. It is a C++
module. With it, expressions that operate on arrays (like "3*a+4*b")
can be accelerated and use less memory than doing the same
calculation in Python.

%prep
%setup -q -n numexpr-%{version}
%patch0 -p1
# wrong-file-end-of-line-encoding
sed -i 's/\r$//' ANNOUNCE.rst AUTHORS.txt  README.rst RELEASE_NOTES.rst site.cfg.example
# remove unwanted shebang
sed -i '/^#!/ d' numexpr/cpuinfo.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mkdir tester
pushd tester
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B -c "import sys;import numexpr;sys.exit(0 if numexpr.test().wasSuccessful() else 1)"
}
popd

%files %{python_files}
%doc ANNOUNCE.rst AUTHORS.txt README.rst RELEASE_NOTES.rst site.cfg.example
%license LICENSE.txt
%{python_sitearch}/numexpr/
%{python_sitearch}/numexpr-%{version}-py*.egg-info

%changelog
