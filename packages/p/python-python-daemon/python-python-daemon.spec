#
# spec file for package python-python-daemon
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-python-daemon
Version:        3.0.2
Release:        0
Summary:        Library to implement a well-behaved Unix daemon process
License:        Apache-2.0 AND GPL-3.0-only
URL:            https://pagure.io/python-daemon/
Source:         https://releases.pagure.org/python-daemon/python_daemon-%{version}.tar.gz
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module lockfile >= 0.10}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lockfile >= 0.10
Requires:       python-packaging
Requires:       python-setuptools >= 62.4.0
BuildArch:      noarch
%python_subpackages

%description
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".

A well-behaved Unix daemon process is tricky to get right, but the required
steps are much the same for every daemon program. A DaemonContext instance
holds the behaviour and configured process environment for the program; use the
instance as a context manager to enter a daemon state.

%prep
%autosetup -p1 -n python_daemon-%{version}

sed -i '/docutils/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE.ASF-2 LICENSE.GPL-3 COPYING
%doc README ChangeLog
%{python_sitelib}/daemon
%{python_sitelib}/python_daemon-%{version}.dist-info

%changelog
