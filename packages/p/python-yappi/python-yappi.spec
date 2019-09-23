#
# spec file for package python-yappi
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
Name:           python-yappi
Version:        1.0
Release:        0
Summary:        Yet Another Python Profiler
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/sumerc/yappi
Source:         https://files.pythonhosted.org/packages/source/y/yappi/yappi-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
Yet Another Python Profiler

%prep
%setup -q -n yappi-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/yappi
%{python_sitearch}/*

%changelog
