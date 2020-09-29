#
# spec file for package bazel3.0
#
# Copyright (c) 2020 SUSE LLC
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


%define bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%define shortname bazel
%define shortver 3.4

#Workaround for s390x (Java 1.8 runs out of memory)
%ifarch s390x
%if 0%{?suse_version} > 1500
%define openjdktouse java-12-openjdk-devel
%else
%define openjdktouse java-11-openjdk-devel
%endif
%else
%define openjdktouse java-1_8_0-openjdk-devel
%endif

Name:           bazel%{shortver}
Version:        3.4.1
Release:        0
Summary:        Tool for the automation of building and testing of software
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            http://bazel.io/
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/%{shortname}-%{version}-dist.zip
Source1:        https://github.com/bazelbuild/bazel/releases/download/%{version}/%{shortname}-%{version}-dist.zip.sig
Patch0:         0001-python-Always-use-python3.patch
BuildRequires:  gcc-c++
BuildRequires:  java-1_8_0-openjdk-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(zlib)
Requires(post):	update-alternatives
Requires(postun): update-alternatives
Requires:       %{openjdktouse}
Provides:       bazel = %{version}
ExcludeArch:    %ix86

%description
Tool for the automation of building and testing of software. It supports Java,
C++ and Go as programing languages. It also has a support for Android and iOS
as mobile operating systems.

%prep
%setup -q -c
%patch0 -p1
# Remove executable permissions
chmod 0644 AUTHORS CHANGELOG.md CONTRIBUTORS LICENSE
# Use Python 3
find . -type f \( -name "*.py" -o -name "*.txt" \) -exec sed -i 's|#!.*python.*|#!/usr/bin/python3|' "{}" +
find . -type f -name "*.java" -exec sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' "{}" +
# Fix collision between grpc's gettid and glibc's gettid
#grep -R "env python" .
find third_party/grpc -type f -name "*.cc" -exec sed -i -e 's|gettid(|my_gettid(|g' {} +

%build
%ifarch aarch64 %arm
export BAZEL_JAVAC_OPTS="-J-Xmx2g -J-Xms200m"
%endif
%ifarch s390x
export BAZEL_JAVAC_OPTS="-J-Xmx4g -J-Xms1g"
%endif
CC=gcc
CXX=g++
EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk" ./compile.sh
./scripts/generate_bash_completion.sh \
    --bazel=output/bazel \
    --output=output/bazel-complete.bash \
    --prepend=scripts/bazel-complete-header.bash \
    --prepend=scripts/bazel-complete-template.bash
./output/bazel shutdown

%install
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define __debug_install_post %{nil}
: >debugfiles.list
: >debugsources.list
: >debugsourcefiles.list

install -Dm0755 output/bazel %{buildroot}%{_bindir}/bazel%{shortver}
install -Dm0644 output/bazel-complete.bash %{buildroot}%{_datadir}/%{name}/bazel-complete.bash

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/bazel %{buildroot}%{_bindir}/bazel
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
ln -sf %{_sysconfdir}/alternatives/bazel-complete.bash %{buildroot}%{_datadir}/bash-completion/completions/bazel

%post
update-alternatives \
    --install %{_bindir}/bazel bazel %{_bindir}/bazel%{shortver} 100 \
    --slave %{_datadir}/bash-completion/completions/bazel \
        bazel-complete.bash \
        %{_datadir}/%{name}/bazel-complete.bash

%postun
if [ $1 -eq 0 ] ; then
    update-alternatives --remove bazel %{_bindir}/bazel%{shortver}
fi

%files
%doc AUTHORS CHANGELOG.md CONTRIBUTORS
%license LICENSE
%{_bindir}/bazel
%{_bindir}/bazel%{shortver}
%{_datadir}/bash-completion/completions/bazel
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bazel-complete.bash
%ghost %{_sysconfdir}/alternatives/bazel
%ghost %{_sysconfdir}/alternatives/bazel-complete.bash

%changelog
