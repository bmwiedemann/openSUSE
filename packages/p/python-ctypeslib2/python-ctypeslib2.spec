#
# spec file for package python-ctypeslib2
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


# No python2-clang
%define skip_python2 1
%define skip_python36 1
%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%ifarch %{ix86} x86_64
%bcond_without test
%else
%bcond_with test
%endif
Name:           python-ctypeslib2
Version:        2.2.3
Release:        0
Summary:        Python FFI toolkit using clang
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/trolldbois/ctypeslib
Source:         https://files.pythonhosted.org/packages/source/c/ctypeslib2/ctypeslib2-%{version}.tar.gz
Patch0:         https://github.com/trolldbois/ctypeslib/commit/98060fe704f7195356d754a78c67c6fd4756daa7.patch#/clang-version.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
BuildRequires:  python3-clang
Requires:       python3-clang
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
# https://github.com/trolldbois/ctypeslib/issues/26
Conflicts:      %{oldpython}-ctypeslib
%endif
%python_subpackages

%description
Python FFI toolkit using clang.

%prep
%setup -q -n ctypeslib2-%{version}
%patch0 -p1
sed -i '1{/^#!/d}' ctypeslib/clang2py.py

# https://github.com/trolldbois/ctypeslib/issues/60
sed -Ei 's/(test_class|test_macro|test_variable)/_\1/' test/test_clang2py.py

# Skipped on master
# https://github.com/trolldbois/ctypeslib/commit/ef141bb04ef1f9f50774a52195d75a71d55b2749#diff-056c7a7f3e89754296c5f3478ac0ad54630c347a1dc5bf22311ca059cde0ccde
sed -i 's/test_unicode_cpp11/_test_unicode_cpp11/' test/test_types_values.py
sed -i 's/test_unicode/_test_unicode/' test/test_types_values.py

# https://github.com/trolldbois/ctypeslib/issues/61
sed -i 's/test_extern_function_pointer_multiarg/_test_extern_function_pointer_multiarg/' test/test_types_values.py
sed -i 's/test_callbacks/_test_callbacks/' test/test_callbacks.py

# https://github.com/trolldbois/ctypeslib/issues/62
sed -i 's/test_includes/_test_includes/' test/test_fast_clang.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/clang2py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
CFLAGS="-Wall -Wextra -Werror -std=c99 -pedantic -fpic"
LDFLAGS="-shared"
gcc $CFLAGS $LDFLAGS -o test/data/test-callbacks.so test/data/test-callbacks.c

export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
%{python_expand \
  bin_dir=bin-%{$python_version}
  mkdir $bin_dir
  ln -s %{buildroot}%{_bindir}/clang2py-%{$python_version} $bin_dir/clang2py
  export PATH=$PATH:`pwd`/$bin_dir
  export PYTHONPATH=:test/:%{buildroot}%{$python_sitelib}
  $python -m unittest discover -s test/ -v
}
%endif

%post
%python_install_alternative clang2py

%postun
%python_uninstall_alternative clang2py

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/clang2py
%{python_sitelib}/*

%changelog
