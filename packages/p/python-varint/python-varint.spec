#
# spec file for package python-varint
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
Name:           python-varint
Version:        1.0.2
Release:        0
Summary:        Library for encoding variable length integer data
License:        MIT
URL:            http://github.com/fmoo/python-varint
Source0:        https://files.pythonhosted.org/packages/source/v/varint/varint-%{version}.tar.gz
Source1:        LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
varints are a common encoding for variable length integer data,
used in libraries such as sqlite, protobuf, v8, and more.

%prep
%setup -q -n varint-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No testsuite

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
