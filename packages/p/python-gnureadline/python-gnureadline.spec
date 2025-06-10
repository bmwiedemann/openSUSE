#
# spec file for package python-gnureadline
#
# Copyright (c) 2025 SUSE LLC
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


%define         _modname gnureadline
Name:           python-gnureadline
Version:        8.2.13
Release:        0
Summary:        The standard Python readline extension statically linked against the GNU readline library
License:        GPL-3.0-or-later
URL:            http://github.com/ludwigschwardt/python-gnureadline
# tests on pypi are broken
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  %{python_module pytest}
%python_subpackages

%description
The standard Python readline extension statically linked against the GNU readline library.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch tests/test.py tests/conftest.py

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%pycache_only %{python_sitearch}/__pycache__
%{python_sitearch}/%{_modname}-%{version}.dist-info
%{python_sitearch}/%{_modname}.cpython*.so
%{python_sitearch}/override_readline.py
%{python_sitearch}/readline.py

%changelog
