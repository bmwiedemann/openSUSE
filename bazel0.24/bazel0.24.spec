#
# spec file for package bazel0.24
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


%define bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%define shortname bazel
%define shortver 0.24

#Workaround for aarch64 boo#1138529
%ifarch aarch64
%if 0%{?suse_version} > 1500
%define openjdktouse java-12-openjdk-devel
%else
%define openjdktouse java-11-openjdk-devel
%endif
%else
%define openjdktouse java-1_8_0-openjdk-devel
%endif

Name:           bazel%{shortver}
Version:        0.24.1
Release:        0
Summary:        Tool for the automation of building and testing of software
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            http://bazel.io/
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/%{shortname}-%{version}-dist.zip
Source1:        https://github.com/bazelbuild/bazel/releases/download/%{version}/%{shortname}-%{version}-dist.zip.sig
BuildRequires:  %{openjdktouse}
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(zlib)
Requires(post):	update-alternatives
Requires(postun): update-alternatives
Requires:       %{openjdktouse}
Provides:       bazel = %{version}
%ifarch armv7l
ExclusiveArch:  do_not_build
%endif

%description
Tool for the automation of building and testing of software. It supports Java,
C++ and Go as programing languages. It also has a support for Android and iOS
as mobile operating systems.

%prep
%setup -q -c
# Remove executable permissions
chmod 0644 AUTHORS CHANGELOG.md CONTRIBUTORS LICENSE

%build
%ifarch aarch64 %arm
export BAZEL_JAVAC_OPTS="-J-Xmx2g -J-Xms200m"
%endif
CC=gcc
CXX=g++
EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk" ./compile.sh
./output/bazel shutdown

%install
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define __debug_install_post %{nil}
: >debugfiles.list
: >debugsources.list
: >debugsourcefiles.list

install -Dm0755 output/bazel %{buildroot}%{_bindir}/bazel%{shortver}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/bazel %{buildroot}%{_bindir}/bazel

%post
update-alternatives \
    --install %{_bindir}/bazel bazel %{_bindir}/bazel%{shortver} 24

%postun
if [ $1 -eq 0 ] ; then
    update-alternatives --remove bazel %{_bindir}/bazel%{shortver}
fi

%files
%doc AUTHORS CHANGELOG.md CONTRIBUTORS
%license LICENSE
%{_bindir}/bazel
%{_bindir}/bazel%{shortver}
%ghost %{_sysconfdir}/alternatives/bazel

%changelog
