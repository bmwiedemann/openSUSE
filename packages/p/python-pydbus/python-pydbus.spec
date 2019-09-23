#
# spec file for package python-pydbus
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pydbus
Version:        0.6.0
Release:        0
License:        LGPL-2.1+
Summary:        Pythonic DBus library
Url:            https://github.com/LEW21/pydbus
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pydbus/pydbus-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-gobject
Requires:       girepository-1_0
BuildArch:      noarch

%python_subpackages

%description
A dbus library for Python.

%prep
%setup -q -n pydbus-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*
%license LICENSE
%doc README.rst

%changelog
