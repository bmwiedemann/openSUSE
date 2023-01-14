#
# spec file for package python-Cython
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


%bcond_with test
Name:           python-Cython
Version:        0.29.33
Release:        0
Summary:        The Cython compiler for writing C extensions for the Python language
License:        Apache-2.0
URL:            https://cython.org/
Source:         https://files.pythonhosted.org/packages/source/C/Cython/Cython-%{version}.tar.gz
Source1:        python-Cython-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-devel
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
The Cython language allows for writing C extensions for the Python
language. Cython is a source code translator based on Pyrex, but
supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python language (and most Python
code is also valid Cython code), but Cython additionally supports calling C
functions and declaring C types on variables and class attributes. This
allows the compiler to generate very efficient C code from Cython code.

%prep
%setup -q -n Cython-%{version}
# Fix non-executable scripts
sed -i "s|^#!.*||" Cython/Debugger/{libpython,Cygdb}.py cython.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
for p in cython cythonize cygdb ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%{python_expand chmod a+x %{buildroot}%{$python_sitearch}/Cython/Build/Cythonize.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitearch}/Cython/Build/Cythonize.py
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/Cython/Build/
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/Cython/Build/
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%if %{with test}
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch} PYTHONDONTWRITEBYTECODE=1
$python runtests.py -v
}
%endif

%post
%python_install_alternative cython cythonize cygdb

%postun
%python_uninstall_alternative cython

%files %{python_files}
%license LICENSE.txt COPYING.txt
%doc README.rst ToDo.txt USAGE.txt
%python_alternative %{_bindir}/cygdb
%python_alternative %{_bindir}/cython
%python_alternative %{_bindir}/cythonize
%{python_sitearch}/Cython/
%{python_sitearch}/Cython-%{version}-py*.egg-info
%{python_sitearch}/cython.py*
%pycache_only %{python_sitearch}/__pycache__/cython*.py*
%{python_sitearch}/pyximport/

%changelog
