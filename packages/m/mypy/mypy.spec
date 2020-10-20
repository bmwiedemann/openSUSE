#
# spec file for package mypy
#
# Copyright (c) 2020 SUSE LLC
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


Name:           mypy
Version:        0.790
Release:        0
Summary:        Optional static typing for Python
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.mypy-lang.org/
Source0:        https://files.pythonhosted.org/packages/source/m/mypy/mypy-%{version}.tar.gz
Source99:       mypy-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-mypy_extensions >= 0.4.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-typed-ast >= 1.4.0
BuildRequires:  python3-typing_extensions >= 3.7.4
# SECTION tests
BuildRequires:  python3-pytest
# /SECTION
Requires:       python3
Requires:       python3-mypy_extensions >= 0.4.0
Requires:       python3-typed-ast >= 1.4.0
Requires:       python3-typing_extensions >= 3.7.4
Provides:       python3-mypy = %{version}
Obsoletes:      python3-mypy < %{version}
BuildArch:      noarch
# SECTION docs
BuildRequires:  python3-Sphinx >= 1.4.4
BuildRequires:  python3-sphinx_rtd_theme >= 0.1.9
# /SECTION

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
%python3_build
pushd docs
make %{?_smp_mflags} html
rm build/html/.buildinfo
popd

%install
%python3_install
%fdupes %{buildroot}

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
sed -i '/plugin/d' ./mypy_self_check.ini
sed -i '/warn_unused_ignores/d' ./mypy_self_check.ini
python3 -m mypy --config-file mypy_self_check.ini -p mypy
# py.test3 -v … we need to analyze subset of tests which would be
# available and without large dependencies.

%files
%doc docs/README.md docs/build/html/
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/dmypy
%{_bindir}/mypy
%{_bindir}/mypyc
%{_bindir}/stubgen
%{_bindir}/stubtest

%changelog
