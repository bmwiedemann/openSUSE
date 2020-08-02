#
# spec file for package python-bjoern
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-bjoern
Version:        3.1.0
Release:        0
Summary:        A screamingly fast Python 2 + 3 WSGI server written in C
License:        BSD-2-Clause
URL:            https://github.com/jonashaag/bjoern
Source:         https://files.pythonhosted.org/packages/source/b/bjoern/bjoern-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libev-devel
BuildRequires:  python-rpm-macros

%python_subpackages

%description
A screamingly fast Python 2 + 3 WSGI server written in C.

%prep
%setup -q -n bjoern-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# there are no unit tests, but e. g. benchmark tests
# using ab

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
