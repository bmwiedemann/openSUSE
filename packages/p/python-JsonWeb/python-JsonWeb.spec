#
# spec file for package python-JsonWeb
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
Name:           python-JsonWeb
Version:        0.8.2
Release:        0
Summary:        Add JSON (de)serialization to your python objects
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://www.jsonweb.info/
Source:         https://files.pythonhosted.org/packages/source/J/JsonWeb/JsonWeb-%{version}.tar.gz
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nose}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
Quickly add json serialization and deserialization
to your python classes.

%prep
%setup -q -n JsonWeb-%{version}

%build
%python_build

%install
%python_install

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
