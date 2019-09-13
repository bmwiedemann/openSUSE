#
# spec file for package googleapis
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

Name:           googleapis
Version:        20180523
Release:        0
Summary:        Public interface and protobuf definitions of Google APIs
License:        Apache-2.0
Group:          Development/Libraries/Cross
Url:            https://github.com/googleapis/googleapis
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
Googleapis are the interface definitions of public Google APIs that support
both REST and gRPC protocols.

%package source
Summary:        Source code of googleapis
Group:          Development/Sources
BuildArch:      noarch

%description source
Googleapis are the interface definitions of public Google APIs that support
both REST and gRPC protocols.

This package contains source code for googleapis.

%prep
%setup -q

%build
# TODO: If anyone will be interested in compiled googleapis protobufs for C++
# they need to be built and installed.

%install
mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}

%fdupes %{buildroot}%{src_install_dir}
# Fix hidden-dile-or-dir warning.
find %{buildroot}%{src_install_dir} -name ".*" -exec rm -rf "{}" +
# Prevent requiring ridiculously old Python version
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!/usr/bin/python2.4|#!/usr/bin/python2.7|' "{}" +
# Some headers have executable bits...
find %{buildroot}%{src_install_dir} -type f -name "*.h" -exec chmod -x "{}" +

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
