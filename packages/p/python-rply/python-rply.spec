#
# spec file for package python-rply
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rply
Version:        0.7.7
Release:        0
Summary:        A pure Python Lex/Yacc that works with RPython
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/alex/rply
# https://github.com/alex/rply/issues/90
Source:         https://github.com/alex/rply/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
RPLY is a pure Python parser generator that also works with RPython.
It is a more-or-less direct port of David Beazley's PLY, with a new
public API, and with RPython support.

%prep
%setup -q -n rply-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
