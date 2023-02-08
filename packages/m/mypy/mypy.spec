#
# spec file for package mypy
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


%bcond_without test
%define skip_python2 1
%define typed_ast_version 1.5.8.3
%define types_psutil_version 5.9.5.6
%define types_setuptools_version 65.6.0.3
Name:           mypy
Version:        1.0.0
Release:        0
Summary:        Optional static typing for Python
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.mypy-lang.org/
Source0:        https://files.pythonhosted.org/packages/source/m/mypy/mypy-%{version}.tar.gz
# License Source1: Apache-2.0. Only for the test suite, not packaged here.
Source1:        https://files.pythonhosted.org/packages/source/t/types-typed-ast/types-typed-ast-%{typed_ast_version}.tar.gz
# License Source2: Apache-2.0. Only for the test suite, not packaged here.
Source2:        https://files.pythonhosted.org/packages/source/t/types-psutil/types-psutil-%{types_psutil_version}.tar.gz
# License Source3: Apache-2.0. Only for the test suite, not packaged here.
Source3:        https://files.pythonhosted.org/packages/source/t/types-setuptools/types-setuptools-%{types_setuptools_version}.tar.gz
Source99:       mypy-rpmlintrc
BuildRequires:  %{python_module mypy_extensions >= 0.4.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli >= 1.1.0 if %python-base < 3.11}
BuildRequires:  %{python_module typed-ast >= 1.4.0 if %python-base < 3.8}
BuildRequires:  %{python_module typing_extensions >= 3.10}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mypy_extensions >= 0.4.3
Requires:       python-typing_extensions >= 3.10
%if 0%{?python_version_nodots} < 38
Requires:       python-typed-ast >= 1.4.0
%endif
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1.1.0
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       mypy = %{version}
Obsoletes:      mypy < %{version}
%endif
Suggests:       python-psutil >= 4.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module attrs >= 18}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module filelock >= 3.3}
BuildRequires:  %{python_module importlib-metadata >= 4.6.1}
BuildRequires:  %{python_module lxml >= 4}
BuildRequires:  %{python_module psutil >= 4}
BuildRequires:  %{python_module pytest >= 6.2}
BuildRequires:  %{python_module pytest-forked >= 1.3}
BuildRequires:  %{python_module pytest-xdist >= 1.34}
BuildRequires:  %{python_module typed-ast >= 1.4.0}
BuildRequires:  %{python_module virtualenv >= 20.6}
BuildRequires:  gcc-c++
%endif
# SECTION docs
BuildRequires:  python3-Sphinx >= 1.4.4
BuildRequires:  python3-sphinx_rtd_theme >= 0.1.9
# /SECTION
%python_subpackages

%description
Mypy is an optional static type checker for Python that aims to
combine the benefits of both dynamic (or "duck") typing as well as
static typing.

Mypy type checks standard Python programs. It can catch many
programming errors by analyzing programs without having to run them.
There is basically no runtime overhead when run using any Python VM.
Mypy's type system features type inference, gradual typing, generics
and union types.

%prep
%setup -n mypy-%{version} -a1 -a2 -a3
%autopatch -p1

sed -i '/env python3/d' ./mypy/stubgenc.py
sed -i '/env python3/d' ./mypy/stubgen.py

mkdir mystubs
mv types-typed-ast-%{typed_ast_version}/typed_ast-stubs* mystubs/
mv types-setuptools-%{types_setuptools_version}/setuptools-stubs* mystubs/
mv types-psutil-%{types_psutil_version}/psutil-stubs* mystubs/

%build
%python_build
# building docs fails due to missing theme 'furo'
#pushd docs
#%%make_build html
#rm build/html/.buildinfo
#popd

%install
%python_install
%python_clone -a  %{buildroot}%{_bindir}/dmypy
%python_clone -a  %{buildroot}%{_bindir}/mypy
%python_clone -a  %{buildroot}%{_bindir}/mypyc
%python_clone -a  %{buildroot}%{_bindir}/stubgen
%python_clone -a  %{buildroot}%{_bindir}/stubtest
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check

%{python_expand # self-check with manually provided stubs for typed_ast
export PYTHONPATH=%{buildroot}%{$python_sitelib}:./mystubs
$python -m mypy --config-file mypy_self_check.ini -p mypy
}
unset PYTHONPATH
# cannot compile unoptimized with suse headers
export MYPYC_OPT_LEVEL=2
if [ $(getconf LONG_BIT) -ne 64 ]; then
  # gh#python/mypy#11148
  donttest+=" or testSubclassSpecialize or testMultiModuleSpecialize"
  # gh#python/mypy#14633
  donttest+=" or testI64Cast"
  # fails only in python36 (EOL)
  python36_donttest+=" or testIntOps"
fi
# the fake test_module is not in the modulepath without pytest-xdist
# or with pytest-xdist >= 2.3 -- https://github.com/python/mypy/issues/11019
donttest+=" or teststubtest"
%pytest -n auto -k "not (testallexcept ${donttest} ${$python_donttest})"
%endif

%post
%python_install_alternative mypy dmypy mypyc stubgen stubtest

%postun
%python_uninstall_alternative mypy

%files %{python_files}
%doc docs/
%license LICENSE
%{python_sitelib}/mypy
%{python_sitelib}/mypyc
%{python_sitelib}/mypy-%{version}*-info
%python_alternative %{_bindir}/dmypy
%python_alternative %{_bindir}/mypy
%python_alternative %{_bindir}/mypyc
%python_alternative %{_bindir}/stubgen
%python_alternative %{_bindir}/stubtest

%changelog
