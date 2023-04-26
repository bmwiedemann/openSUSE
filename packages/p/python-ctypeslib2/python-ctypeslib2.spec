#
# spec file for package python-ctypeslib2
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


# Until python3-clang is converted to multiflavor, we have the primary flavor only
# Please keep the multiflavor macro usage in the specfile consistent.
%define pythons python3
# help in the rename from multiflavor to python3 only
%define primary_python3 python%{python3_version_nodots}
%ifarch %{ix86} x86_64
%bcond_without test
%else
%bcond_with test
%endif
%if 0%{suse_version} >= 1599
# Tumbleweed default 16 is not compatible
%define clangmajor 15
%endif
Name:           python-ctypeslib2
Version:        2.3.4
Release:        0
Summary:        Python FFI toolkit using clang
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/trolldbois/ctypeslib
Source:         https://github.com/trolldbois/ctypeslib/archive/refs/tags/%{version}.tar.gz#/ctypeslib2-%{version}-gh.tar.gz
# PATCH-FIX-OPENSUSE ctypeslib2-suse-remove-info-check.patch code@bnavigator.de, python3-clang does not provide dist- or egg-info, we do not use the unofficial pypi package there
Patch1:         ctypeslib2-suse-remove-info-check.patch
BuildRequires:  %{python_module clang%{?clangmajor} >= 11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  clang%{?clangmajor} >= 11
BuildRequires:  fdupes
%{?clangmajor:BuildRequires:  llvm%{?clangmajor}-libclang13}
BuildRequires:  python-rpm-macros >= 20220610
Requires:       python-clang%{?clangmajor} >= 11
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       %{primary_python3}-ctypeslib2 = %{version}-%{release}
Obsoletes:      %{primary_python3}-ctypeslib2 < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Python FFI toolkit using clang.

%prep
%autosetup -p1 -n ctypeslib-%{version}
sed -i '1{/^#!/d}' ctypeslib/clang2py.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/clang2py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
CFLAGS="-Wall -Wextra -Werror -Wno-strict-prototypes -std=c99 -pedantic -fpic"
LDFLAGS="-shared"
clang $CFLAGS $LDFLAGS -o test/data/test-callbacks.so test/data/test-callbacks.c

%python_flavored_alternatives
export LANG=en_US.UTF-8
export CPATH=$(clang  -print-resource-dir)/include
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # not for 32-bit (looks for gnu/stubs-64.h)
  sed -i 's/test_includes/_&/' test/test_fast_clang.py
  # c_long != c_int -- https://github.com/trolldbois/ctypeslib/issues/61
  sed -i 's/test_extern_function_pointer_multiarg/_&/' test/test_types_values.py
fi

%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} clang2py --version
%pyunittest -v test.alltests
%endif

%post
%python_install_alternative clang2py

%postun
%python_uninstall_alternative clang2py

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/clang2py
%{python_sitelib}/ctypeslib
%{python_sitelib}/ctypeslib2-%{version}*-info

%changelog
