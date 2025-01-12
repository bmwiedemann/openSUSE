#
# spec file for package python-pyrad
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


%{?sle15_python_module_pythons}
Name:           python-pyrad
Version:        2.4
Release:        0
Summary:        RADIUS tools
License:        BSD-3-Clause
URL:            https://github.com/pyradius/pyrad
Source0:        https://github.com/pyradius/pyrad/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#pyradius/pyrad#162
Patch0:         use-correct-assertion-methods.patch
# PATCH-FIX-UPSTREAM Based on gh#pyradius/pyrad#208
Patch1:         support-poetry-core-2.patch
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
Requires:       python-netaddr
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
pyrad is an implementation of a RADIUS client/server as described in RFC2865.
It takes care of all the details like building RADIUS packets, sending
them and decoding responses.

%prep
%autosetup -p1 -n pyrad-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/pyrad
%{python_sitelib}/pyrad-%{version}.dist-info

%changelog
