#
# spec file for package bazel0.19
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


Name:           bazel0.19
Version:        0.19.2
Release:        0
Summary:        Tool for the automation of building and testing of software
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            http://bazel.io/
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-dist.zip
Source1:        https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-dist.zip.sig
BuildRequires:  gcc-c++
BuildRequires:  java-1_8_0-openjdk-devel
BuildRequires:  python
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bash-completion)

Requires:       java-1_8_0-openjdk-devel

Provides:       bazel = %{version}
Conflicts:      bazel > %{version}

ExcludeArch:    armv7l i586

%define bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)

%description
Tool for the automation of building and testing of software. It supports Java,
C++ and Go as programing languages. It also has a support for Android and iOS
as mobile operating systems.

%prep
%setup -q -c
# Remove executable permissions
chmod 0644 AUTHORS CHANGELOG.md CONTRIBUTORS LICENSE
# Fix collision between grpc's gettid and glibc's gettid
find third_party/grpc -type f -name "*.c" -exec sed -i -e 's|gettid(|my_gettid(|g' {} +

%build
%ifarch %arm aarch64
export BAZEL_JAVAC_OPTS="-J-Xmx2g -J-Xms200m"
%endif
CC=gcc
CXX=g++
./compile.sh
./output/bazel shutdown

%install
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define __debug_install_post %nil
: >debugfiles.list
: >debugsources.list
: >debugsourcefiles.list

install -Dm0755 output/bazel %{buildroot}%{_bindir}/bazel-%{version}
ln -s %{_bindir}/bazel-%{version} %{buildroot}%{_bindir}/bazel

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG.md CONTRIBUTORS
%license LICENSE
%{_bindir}/bazel-%{version}
%{_bindir}/bazel

%changelog
