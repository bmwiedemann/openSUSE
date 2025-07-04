#
# spec file for package python-pydbus
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pydbus
Version:        0.6.0
Release:        0
Summary:        Pythonic DBus library
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/LEW21/pydbus
Source:         https://files.pythonhosted.org/packages/source/p/pydbus/pydbus-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       girepository-1_0
Requires:       python-gobject
BuildArch:      noarch
%python_subpackages

%description
A dbus library for Python.

%prep
%setup -q -n pydbus-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/pydbus
%{python_sitelib}/pydbus-%{version}*-info
%license LICENSE
%doc README.rst

%changelog
