#
# spec file for package python-args
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
Name:           python-args
Version:        0.1.0
Release:        0
Summary:        Python command argument interface
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/kennethreitz/args
Source:         https://files.pythonhosted.org/packages/source/a/args/args-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
This module gives developers an interface for command line argumemnts.

%prep
%setup -q -n args-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
