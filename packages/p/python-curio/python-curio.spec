#
# spec file for package python-curio
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
%define skip_python2 1
Name:           python-curio
Version:        1.4
Release:        0
Summary:        Concurrent I/O library for Python 3
License:        BSD-Source-Code
URL:            https://github.com/dabeaz/curio
Source:         https://github.com/dabeaz/curio/archive/%{version}.tar.gz#/curio-%{version}.tar.gz
Patch0:         make-tests-reproducible.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Curio is a library for performing concurrent I/O with coroutines in Python 3.

%prep
%setup -q -n curio-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# disabled network tests
%pytest -k 'not (test_ssl_outgoing or test_socket_funcs)'

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/*

%changelog
