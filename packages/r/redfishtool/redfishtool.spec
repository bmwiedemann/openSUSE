#
# spec file for package redfishtool
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           redfishtool
Version:        1.1.5
Release:        0
Summary:        A CLI tool for accessing the Redfish API
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            https://github.com/DMTF/Redfishtool
Source:         https://github.com/DMTF/Redfishtool/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-requests
BuildArch:      noarch

%description
redfishtool is a commandline tool that implements the client side
of the Redfish RESTful API for Data Center Hardware Management.

%prep
%setup -q -n Redfishtool-%{version}

%build
%python3_build

%install
%python3_install
%python_expand %fdupes %{buildroot}%{python3_sitelib}/
rm %{buildroot}/%{_bindir}/redfishtool.py

%files
%license LICENSE.md
%doc AUTHORS.md CHANGELOG.md README.md
%{_bindir}/redfishtool
%{python3_sitelib}/redfishtool*

%changelog
