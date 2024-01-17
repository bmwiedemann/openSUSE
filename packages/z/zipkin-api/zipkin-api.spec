#
# spec file for package zipkin-api
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define src_install_dir /usr/src/%{name}

Name:           zipkin-api
Version:        0.2.2
Release:        0
Summary:        Zipkin's language independent model and HTTP Api Definitions
License:        Apache-2.0
Group:          Development/Libraries/Other       
Url:            https://github.com/openzipkin/zipkin-api
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        WORKSPACE
Source3:        BUILD
BuildRequires:  fdupes

%description
Zipkin API includes service and model definitions used for Zipkin-compatible services

%package source
Summary:        Source code of zipkin-api
Group:          Development/Sources
BuildArch:      noarch

%description source
This package contains source code of zipkin-api

%prep
%setup -q
cp %{SOURCE2} .
cp %{SOURCE3} .

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}

# Fix env-script-interpreter error.
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec sed -i 's|#!/usr/bin/env bash|#!/bin/bash|' "{}" +
chmod 755 %{buildroot}%{src_install_dir}/travis/deploy.sh

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
