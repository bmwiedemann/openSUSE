#
# spec file for package python-notify2
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


%{?sle15_python_module_pythons}
Name:           python-notify2
Version:        0.3.1
Release:        0
Summary:        Python interface to DBus notifications
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/notify2/
Source:         https://files.pythonhosted.org/packages/source/n/notify2/notify2-%{version}.tar.gz
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-dbus-python
%python_subpackages

%description
This is a pure-python replacement for notify-python, using python-dbus
to communicate with the notifications server directly. It's compatible
with Python 2 and 3, and its callbacks can work with Gtk 3 or Qt 4
applications.

%prep
%setup -q -n notify2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/notify2.py*
%pycache_only %{python_sitelib}/__pycache__/notify2*
%{python_sitelib}/notify2-%{version}-*info

%changelog
