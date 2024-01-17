#
# spec file for package kafka
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define src_install_dir /usr/src/%{name}

Name:           kafka
Version:        2.1.0
Release:        0
Summary:        Apache Kafka Server
License:        Apache-2.0
Group:          Productivity/Networking/Other
Url:            http://kafka.apache.org
Source0:        %{name}-%{version}.tar.xz
Source1:        BUILD
Source2:        WORKSPACE
BuildRequires:  fdupes

%description
The %{name} package contains the Kafka distributed streaming platform.

%package source
Summary:        Source code of Apache Kafka
Group:          Productivity/Networking/Other

%description source
Source code of the Kafka distributed streaming platform.

%prep
%setup -q
cp %{SOURCE1} .
cp %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}

%files source
%defattr(-,root,root)
%license LICENSE
%doc NOTICE
%{src_install_dir}

%changelog
