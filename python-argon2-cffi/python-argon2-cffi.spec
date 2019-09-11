#
# spec file for package python-argon2-cffi
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
Name:           python-argon2-cffi
Version:        19.1.0
Release:        0
Summary:        The Argon2 password hashing algorithm for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hynek/argon2_cffi
Source:         https://files.pythonhosted.org/packages/source/a/argon2_cffi/argon2_cffi-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 6.0}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python2-enum34
BuildRequires:  pkgconfig(libargon2)
Requires:       python-cffi >= 1.0.0
Requires:       python-six
Provides:       python-argon2_cffi
Obsoletes:      python-argon2_cffi
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
A Python module that uses CFFI to access the Argon2 password hashing
C library.

%prep
%setup -q -n argon2_cffi-%{version}

%build
export ARGON2_CFFI_USE_SYSTEM=1
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test_argument_ranges - randomly fails
%pytest_arch -k 'not test_argument_ranges'

%files %{python_files}
%doc README.rst CHANGELOG.rst FAQ.rst
%license LICENSE
%{python_sitearch}/*

%changelog
