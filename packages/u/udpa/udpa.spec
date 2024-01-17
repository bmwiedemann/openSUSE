#
# spec file for package udpa
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


%define src_install_dir /usr/src/%{name}

Name:           udpa
Version:        0.0.1
Release:        0
Summary:        Universal Data Plane API
License:        Apache-2.0
Group:          Development/Tools/Building 
URL:            https://github.com/cncf/udpa
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
Universal Data Plane API is a common control and configuration API for data plane proxies and load balancers

%package source
Summary:        Source code of Universal Data Plane API
Group:          Development/Sources
BuildArch:      noarch

%description source
This package contains source code of Universal Data Plane API

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}

# Fix env-script-interpreter error.
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!/usr/bin/env python.*$|#!/usr/bin/python3|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec sed -i 's|#!/usr/bin/env bash|#!/bin/bash|' "{}" +

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
