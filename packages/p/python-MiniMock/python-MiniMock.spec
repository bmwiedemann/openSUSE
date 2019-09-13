#
# spec file for package python-MiniMock
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-MiniMock
Version:        1.2.8
Release:        0
Summary:        A mock library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            http://pypi.python.org/pypi/MiniMock
Source:         https://files.pythonhosted.org/packages/source/M/MiniMock/MiniMock-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-minimock = %{version}
Obsoletes:      %{oldpython}-minimock < %{version}
%endif
%python_subpackages

%description
Minimock is a library for doing Mock objects with doctest.
When using doctest, mock objects can be very simple.

%prep
%setup -q -n MiniMock-%{version}

%build
%python_build

%install
%python_install
%if %{have_python3} && ! 0%{?skip_python3}
2to3 -wn %{buildroot}%{python3_sitelib}/minimock.py
python3 -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/
python3 -O -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/
%endif

%check
%python_expand $python -B %{buildroot}%{$python_sitelib}/minimock.py

%files %{python_files}
%defattr(-,root,root,-)
%doc docs/license.txt
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/minimock.py*
%{python_sitelib}/MiniMock-%{version}-py%{python_version}.egg-info

%changelog
