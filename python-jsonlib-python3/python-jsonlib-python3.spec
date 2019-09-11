#
# spec file for package python-jsonlib-python3
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
%define skip_python2 1
Name:           python-jsonlib-python3
Version:        1.6.1
Release:        0
Summary:        JSON serializer/deserializer for Python
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://launchpad.net/jsonlib
Source:         https://files.pythonhosted.org/packages/source/j/jsonlib-python3/jsonlib-python3-%{version}.tar.gz
Patch0:         test-fixes.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
JSON serializer/deserializer for Python.

%prep
%setup -q -n jsonlib-python3-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{python3_version_nodots} > 34
# Tests rely on 3.6-3.7 dict ordering
%check
%python_exec ./test_jsonlib.py
%endif

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%{python_sitearch}/*

%changelog
