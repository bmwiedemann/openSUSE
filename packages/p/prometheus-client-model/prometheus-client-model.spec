#
# spec file for package prometheus-client-model
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           prometheus-client-model
Version:        20190109
Release:        0
Summary:        Data model artifacts for Prometheus
License:        Apache-2.0
Group:          Development/Libraries/Cross
Url:            https://github.com/prometheus/client_model
Source0:        %{name}-%{version}.tar.xz
Source1:        BUILD
Source2:        WORKSPACE
BuildRequires:  fdupes

%description
prometheus-client-model provides data model artifacts for Prometheus in form of
protobufs and libraries.

%package source
Summary:        Source code of prometheus-client-model
Group:          Development/Sources
BuildArch:      noarch

%description source
prometheus-client-model provides data model artifacts for Prometheus in form of
protobufs and libraries.

This package contains source code for prometheus-client-model.

%prep
%setup -q
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
# TODO: If anyone will be interested in prometheus-client-model libraries for
# Python, they need to be built and installed.

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
