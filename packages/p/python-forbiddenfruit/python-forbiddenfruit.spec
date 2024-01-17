#
# spec file for package python-forbiddenfruit
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
Name:           python-forbiddenfruit
Version:        0.1.3
Release:        0
Summary:        Python module to patch python built-in objects
License:        GPL-3.0-only OR MIT
Group:          Development/Languages/Python
URL:            https://github.com/clarete/forbiddenfruit
Source0:        https://github.com/clarete/forbiddenfruit/archive/%{version}.tar.gz
# https://github.com/clarete/forbiddenfruit/issues/30
Source1:        COPYING.GPL
# https://github.com/clarete/forbiddenfruit/pull/47
Patch0:         remove-nose.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This project allows you to patch built-in objects, declared in C through
python.

%prep
%setup -q -n forbiddenfruit-%{version}
cp %{SOURCE1} .
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand ln -s %{buildroot}%{$python_sitearch}/ffruit* tests/unit
%pytest

%files %{python_files}
%license COPYING.GPL COPYING.mit
%doc README.md
%{python_sitearch}/*

%changelog
