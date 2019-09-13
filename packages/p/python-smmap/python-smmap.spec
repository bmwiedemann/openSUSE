#
# spec file for package python-smmap
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-smmap
Version:        0.9.0
Release:        0
Summary:        A pure git implementation of a sliding window memory map manager
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/gitpython-developers/smmap
Source:         https://files.pythonhosted.org/packages/source/s/smmap/smmap-%{version}.tar.gz
# PATCH-FIX-OPENSUSE delete_platform_specific_test.patch -- fix tests on powerpc
Patch0:         delete_platform_specific_test.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nosexcover}
BuildRequires:  %{python_module nose}
%endif
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
When reading from many possibly large files in a fashion similar to random
access, it is usually the fastest and most efficient to use memory maps.
Although memory maps have many advantages, they represent a very limited
system resource as every map uses one file descriptor, whose amount is
limited per process. On 32 bit systems, the amount of memory you can have
mapped at a time is naturally limited to theoretical 4GB of memory, which
may not be enough for some applications.

The documentation can be found here: http://packages.python.org/smmap

%prep
%setup -q -n smmap-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
