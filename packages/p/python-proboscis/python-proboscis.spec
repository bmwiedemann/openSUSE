#
# spec file for package python-proboscis
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
Name:           python-proboscis
Version:        1.2.6.0
Release:        0
Summary:        Extends Nose with certain TestNG like features
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/rackspace/python-proboscis
Source:         https://files.pythonhosted.org/packages/source/p/proboscis/proboscis-%{version}.tar.gz
BuildRequires:  python-rpm-macros
# Test requirements:
BuildRequires:  %{python_module nose}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
Proboscis is a Python test framework that extends Python's built-in unittest module and Nose with features from TestNG.

%prep
%setup -q -n proboscis-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec setup.py test

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
