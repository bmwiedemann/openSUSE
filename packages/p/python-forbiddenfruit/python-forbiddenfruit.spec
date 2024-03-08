#
# spec file for package python-forbiddenfruit
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-forbiddenfruit
Version:        0.1.4
Release:        0
Summary:        Python module to patch python built-in objects
License:        GPL-3.0-only OR MIT
URL:            https://github.com/clarete/forbiddenfruit
Source0:        https://github.com/clarete/forbiddenfruit/archive/%{version}.tar.gz
# https://github.com/clarete/forbiddenfruit/pull/47
Patch0:         remove-nose.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This project allows you to patch built-in objects, declared in C through
python.

%prep
%autosetup -p1 -n forbiddenfruit-%{version}

%build
export FFRUIT_EXTENSION=true
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand ln -s %{buildroot}%{$python_sitearch}/ffruit* tests/unit
%pytest

%files %{python_files}
%license COPYING COPYING.mit
%doc README.md
%{python_sitearch}/ffruit.cpython-*-linux-gnu.so
%{python_sitearch}/forbiddenfruit
%{python_sitearch}/forbiddenfruit-%{version}.dist-info

%changelog
