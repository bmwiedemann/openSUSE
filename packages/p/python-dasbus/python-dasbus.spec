#
# spec file for package python-dasbus
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dasbus
Version:        1.7
Release:        0
Summary:        DBus library in Python 3
License:        LGPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/rhinstaller/dasbus
Source:         https://github.com/rhinstaller/dasbus/releases/download/v%{version}/dasbus-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  python-rpm-macros
Requires:       python-gobject
BuildArch:      noarch
%python_subpackages

%description
DBus library in Python 3, based on GLib and inspired by pydbus.

%prep
%setup -q -n dasbus-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
