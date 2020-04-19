#
# spec file for package python-typeshed
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


%define modname typeshed
Name:           python-typeshed
Version:        0.0.1+git.20200312.b44cd294
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
#BuildRequires:  python3-pytype
BuildRequires:  python3-typed-ast
Recommends:     mypy
Provides:       python3-typeshed = %{version}
Obsoletes:      python3-typeshed < %{version}
Provides:       python2-typeshed = %{version}
Obsoletes:      python2-typeshed < %{version}
BuildArch:      noarch

%description
Typeshed models function types for the Python standard library
and Python builtins, as well as third party packages.

This data can e.g. be used for static analysis, type checking or
type inference.

This package stores the typedata in %{_datadir}/typeshed

%prep
%autosetup -p1 -n %{modname}-%{version}

rm -r stdlib/2
rm -rv stdlib/*/typing.pyi

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/typeshed
for dir in stdlib third_party ; do
    cp -r $dir %{buildroot}/%{_datadir}/typeshed/$dir
done
%fdupes %{buildroot}%{_datadir}/typeshed

%check
tests/mypy_test.py || /bin/true
tests/pytype_test.py || /bin/true

%files
%doc CONTRIBUTING.md README.md
%license LICENSE
%{_datadir}/typeshed

%changelog
