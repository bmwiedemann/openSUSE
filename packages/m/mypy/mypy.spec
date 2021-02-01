#
# spec file for package mypy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           mypy
Version:        0.800
Release:        0
Summary:        Optional static typing for Python
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.mypy-lang.org/
Source0:        https://files.pythonhosted.org/packages/source/m/mypy/mypy-%{version}.tar.gz
Source99:       mypy-rpmlintrc
BuildRequires:  %{python_module mypy_extensions >= 0.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typed-ast >= 1.4.0}
BuildRequires:  %{python_module typing_extensions >= 3.7.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mypy_extensions >= 0.4.0
Requires:       python-typed-ast >= 1.4.0
Requires:       python-typing_extensions >= 3.7.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       mypy = %{version}
Obsoletes:      mypy < %{version}
%endif
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module pytest}
# /SECTION
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
%autosetup -n mypy-%{version} -p1

for scr in mypy/typeshed/tests/*.py ; do
    sed -i -e '1 s|env ||' $scr
done

sed -i '/env python3/d' ./mypy/stubgenc.py
sed -i '/env python3/d' ./mypy/stubgen.py
sed -i '1s/env //' mypy/typeshed/scripts/update-stubtest-whitelist.py

%build
%python_build
pushd docs
%make_build html
rm build/html/.buildinfo
popd

%install
%python_install
%python_clone -a  %{buildroot}%{_bindir}/dmypy
%python_clone -a  %{buildroot}%{_bindir}/mypy
%python_clone -a  %{buildroot}%{_bindir}/mypyc
%python_clone -a  %{buildroot}%{_bindir}/stubgen
%python_clone -a  %{buildroot}%{_bindir}/stubtest
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i '/plugin/d' ./mypy_self_check.ini
sed -i '/warn_unused_ignores/d' ./mypy_self_check.ini
sed -i '/python_version.*$/d' ./mypy_self_check.ini
%python_exec -m mypy --config-file mypy_self_check.ini -p mypy
# py.test3 -v … we need to analyze subset of tests which would be
# available and without large dependencies.

%post
%python_install_alternative mypy dmypy mypyc stubgen stubtest

%postun
%python_uninstall_alternative mypy

%files %{python_files}
%doc docs/README.md docs/build/html/
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/dmypy
%python_alternative %{_bindir}/mypy
%python_alternative %{_bindir}/mypyc
%python_alternative %{_bindir}/stubgen
%python_alternative %{_bindir}/stubtest

%changelog
