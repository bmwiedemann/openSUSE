#
# spec file for package proteus
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2014-2024 Dr. Axel Braun
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


%if 0%{?suse_version} >= 1550
%define pythons python3
%define mypython python3
%define mysitelib %python3_sitelib
%else
%{?sle15_python_module_pythons}
%define mypython %pythons
%define mysitelib %{expand:%%%{mypython}_sitelib}
%endif

%define majorver 7.0
Name:           proteus
Version:        %{majorver}.3
Release:        0
Summary:        A library to access Tryton's modules like a client
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source0:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz

# List of additional build dependencies
BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-pip
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros

BuildRequires:  %{mypython}-defusedxml
BuildRequires:  %{mypython}-python-dateutil

BuildRequires:  trytond
Requires:       %{mypython}-defusedxml
Requires:       %{mypython}-python-dateutil
Requires:       trytond
BuildArch:      noarch

%description
Proteus allows you to access Tryton's modules like a client. Useful for automation, data load etc.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{mysitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{mysitelib}
%pyunittest discover -v

%files
%defattr(-,root,root)
%{mysitelib}/proteus*
%doc README.rst
%license LICENSE

%changelog
