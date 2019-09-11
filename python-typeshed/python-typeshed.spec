#
# spec file for package python-typeshed
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


%define modname typeshed
Name:           python-typeshed
Version:        0.0.1+git.1562136779.4af283e1
Release:        0
Summary:        Static type information for python modules
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python/typeshed
Source0:        %{modname}-%{version}.tar.xz
Source1:        python-typeshed-rpmlintrc
BuildRequires:  fdupes
# For tests
BuildRequires:  mypy
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  python3-flake8
BuildRequires:  python3-flake8-bugbear
BuildRequires:  python3-flake8-pyi
BuildRequires:  python3-typed-ast
Recommends:     mypy
Provides:       python3-typeshed = %{version}
Obsoletes:      python3-typeshed < %{version}
Provides:       python2-typeshed = %{version}
Obsoletes:      python2-typeshed < %{version}
# BuildRequires:  pytype>=2018.9.19
BuildArch:      noarch

%description
Typeshed models function types for the Python standard library
and Python builtins, as well as third party packages.

This data can e.g. be used for static analysis, type checking or
type inference.

This package stores the typedata in %{_datadir}/typeshed

%prep
%setup -q -n %{modname}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/typeshed
for dir in stdlib third_party ; do
    cp -r $dir %{buildroot}/%{_datadir}/typeshed/$dir
done
%fdupes %{buildroot}%{_datadir}/typeshed

%check
python3 tests/mypy_test.py -v
# python3 tests/pytype_test.py

%files
%doc CONTRIBUTING.md README.md
%license LICENSE
%{_datadir}/typeshed

%changelog
