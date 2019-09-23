#
# spec file for package python-blosc
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-blosc
Version:        1.8.1
Release:        0
Summary:        Blosc data compressor for Python
License:        MIT
Group:          Development/Languages/Python
Url:            http://www.blosc.org/
Source:         https://files.pythonhosted.org/packages/source/b/blosc/blosc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  blosc-devel >= 1.9.0
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module psutil}
# /SECTION
Requires:       blosc-devel
Recommends:     python-numpy
ExclusiveArch:  %ix86 x86_64
%python_subpackages

%description
Blosc is a high performance compressor optimized for binary data in
Python.

%prep
%setup -q -n blosc-%{version}

%build
export CFLAGS="%{optflags}"
%python_exec setup.py build_ext --inplace --blosc=%{_prefix}
%python_exec setup.py build --blosc=%{_prefix}

%install
%python_exec setup.py install -O1 --skip-build --force --root=%{buildroot} --prefix=%{_prefix} --blosc=%{_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mkdir empty
pushd empty
%{python_expand export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c "import blosc; blosc.print_versions()"
nosetests-%{$python_bin_suffix} blosc
}
popd

%files %{python_files}
%defattr(-,root,root,-)
%doc ANNOUNCE.rst README.rst RELEASE_NOTES.rst
%license LICENSES/*.txt
%{python_sitearch}/blosc-%{version}-py*.egg-info
%{python_sitearch}/blosc/

%changelog
