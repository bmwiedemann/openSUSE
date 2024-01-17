#
# spec file for package python-JsonWeb
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-JsonWeb
Version:        0.8.2
Release:        0
Summary:        Add JSON (de)serialization to your python objects
License:        BSD-3-Clause
URL:            http://www.jsonweb.info/
Source:         https://files.pythonhosted.org/packages/source/J/JsonWeb/JsonWeb-%{version}.tar.gz
# PATCH-FIX-OPENSUSE python-311.patch
Patch0:         python-311.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Quickly add json serialization and deserialization
to your python classes.

%prep
%autosetup -p1 -n JsonWeb-%{version}

%build
%python_build

%install
%python_install

%check
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/jsonweb
%{python_sitelib}/JsonWeb-%{version}*-info

%changelog
