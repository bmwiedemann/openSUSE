#
# spec file for package python-python-dbusmock
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


Name:           python-python-dbusmock
Version:        0.24.1
Release:        0
Summary:        Python library for creating mock D-Bus objects
License:        LGPL-3.0-or-later
URL:            https://github.com/martinpitt/python-dbusmock
Source:         https://files.pythonhosted.org/packages/source/p/python-dbusmock/python-dbusmock-%{version}.tar.gz
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gobject-introspection-1.0)
Requires:       dbus-1-x11
Requires:       python-dbus-python
Requires:       python-gobject
Provides:       python-dbusmock = %{version}
BuildArch:      noarch
%if %python_version_nodots < 37
Requires:       python-dataclasses
%endif
%python_subpackages

%description
With this program/Python library, one can create mock objects on D-Bus.
This is useful for writing tests for software which talks to D-Bus services
such as upower, systemd, logind, gnome-session or others, and it is hard
(or impossible without root privileges) to set the state of the real services
to what one may expect in tests.

%prep
%autosetup -p1 -n python-dbusmock-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc NEWS README.rst
%{python_sitelib}/dbusmock
%{python_sitelib}/python_dbusmock-%{version}*-info

%changelog
