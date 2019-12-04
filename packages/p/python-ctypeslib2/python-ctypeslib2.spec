#
# spec file for package python-ctypeslib2
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

%ifarch %{ix86} x86_64
%bcond_without test
%else
%bcond_with test
%endif
# No python2-clang
%define skip_python2 1
%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ctypeslib2
Version:        2.2.2
Release:        0
License:        MIT
Summary:        Python FFI toolkit using clang
Url:            https://github.com/trolldbois/ctypeslib
Group:          Development/Languages/Python
Source:         https://github.com/trolldbois/ctypeslib/archive/%{version}.tar.gz#/ctypeslib2-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module clang}
%ifpython2
# https://github.com/trolldbois/ctypeslib/issues/26
Conflicts:      %oldpython-ctypeslib
%endif
BuildRequires:  fdupes
Requires:       python-clang
BuildArch:      noarch

%python_subpackages

%description
Python FFI toolkit using clang.

%prep
%setup -q -n ctypeslib-%{version}
# https://github.com/trolldbois/ctypeslib/issues/60
sed -i 's/test_variable/_test_variable/' test/test_clang2py.py
sed -i 's/test_unicode_cpp11/_test_unicode_cpp11/' test/test_types_values.py
sed -i 's/test_unicode/_test_unicode/' test/test_types_values.py
# https://github.com/trolldbois/ctypeslib/issues/61
sed -i 's/test_extern_function_pointer_multiarg/_test_extern_function_pointer_multiarg/' test/test_types_values.py
# https://github.com/trolldbois/ctypeslib/issues/62
sed -i 's/test_includes/_test_includes/' test/test_fast_clang.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export PATH=$PATH:%{buildroot}%{_bindir}
export LANG=en_US.UTF-8
%python_exec setup.py test
%endif

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python3_only %{_bindir}/clang2py
%{python_sitelib}/*

%changelog
