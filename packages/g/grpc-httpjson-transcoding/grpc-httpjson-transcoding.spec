#
# spec file for package grpc-httpjson-transcoding
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

Name:           grpc-httpjson-transcoding
Version:        20190920
Release:        0
Summary:        Library for transcoding HTTP/JSON to gRPC
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/grpc-ecosystem/%{name}
Source0:        %{name}-%{version}.tar.xz
Source100:      grpc-httpjson-transcoding-rpmlintrc
Patch0:         0001-bazel-Update-googleapis-and-do-not-define-custom-BUI.patch
BuildRequires:  fdupes
ExcludeArch:    %ix86

%description
grpc-httpjson-transcoding is a library that supports transcoding so that
HTTP/JSON can be converted to gRPC. It allows to provide APIs in both gRPC and
REST style at the same time.

%package source
Summary:        Source code of grpc-httpjson-transcoding
Group:          Development/Sources
BuildArch:      noarch

%description source
Source code of grpc-httpjson-transcoding - a library that supports transcoding
so that HTTP/JSON can be converted to gRPC. It allows to provide APIs in both
gRPC and REST style at the same time.

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
