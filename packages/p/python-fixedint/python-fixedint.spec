#
# spec file for package python-fixedint
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-fixedint
Version:        0.2.0
Release:        0
Summary:        simple fixed-width integers
License:        Python-2.0
URL:            https://github.com/nneonneo/fixedint
Source:         https://files.pythonhosted.org/packages/source/f/fixedint/fixedint-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
This module provides fixed-size integer classes which retain their fixed nature across
arithmetic operations. It is geared towards users who need to emulate machine integers.

It provides flexible classes for defining integers with a fixed number of bits, as well
as predefined classes for common machine integer sizes. These classes can be used as
drop-in replacements for int/long, and can be sliced to extract bitfields.

Mutable versions of these integers are provided, enabling usages such as emulation
of machine registers.

%prep
%setup -q -n fixedint-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc AUTHORS CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
