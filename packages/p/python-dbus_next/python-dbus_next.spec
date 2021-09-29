#
# spec file for package python-dbus_next
#
# Copyright (c) 2021 SUSE LLC
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
%define modname python-dbus-next
Name:           python-dbus_next
Version:        0.2.3
Release:        0
Summary:        A zero-dependency DBus library for Python with asyncio support
License:        MIT
URL:            https://github.com/altdesktop/python-dbus-next
Source0:        https://github.com/altdesktop/python-dbus-next/archive/v%{version}/%{modname}-%{version}.tar.gz
Source99:       python-dbus_next-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
python-dbus-next is a Python library for DBus that aims to be a fully featured high level library primarily geared towards integration of applications into Linux desktop and mobile environments.

Desktop application developers can use this library for integrating their applications into desktop environments by implementing common DBus standard interfaces or creating custom plugin interfaces.

Desktop users can use this library to create their own scripts and utilities to interact with those interfaces for customization of their desktop environment.

python-dbus-next plans to improve over other DBus libraries for Python in the following ways:

Zero dependencies and pure Python 3.
Support for multiple IO backends including asyncio and the GLib main loop.
Nonblocking IO suitable for GUI development.
Target the latest language features of Python for beautiful services and clients.
Complete implementation of the DBus type system without ever guessing types.
Integration tests for all features of the library.
Completely documented public API.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Test are only supported inside provided docker container. https://github.com/altdesktop/python-dbus-next/issues/94#issuecomment-881654674

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
