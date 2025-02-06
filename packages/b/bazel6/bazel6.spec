#
# spec file for package bazel6
#
# Copyright (c) 2025 SUSE LLC
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
# Bazel 4.0 and higher follow semantic versioning.
%define shortver 6

Name:           bazel%{shortver}
Version:        6.5.0
Release:        0
Summary:        Tool for the automation of building and testing of software
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://bazel.build/
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/%{shortname}-%{version}-dist.zip
Source1:        https://github.com/bazelbuild/bazel/releases/download/%{version}/%{shortname}-%{version}-dist.zip.sig
Source2:        abseil-missing-stdint.patch
Source3:        grpc-fix-compile-failuare-in-ppc64le.patch
# PATCH-FIX-OPENSUSE apply-abseil-missing-stdint.patch
Patch0:         apply-abseil-missing-stdint.patch
# PATCH-FIX-OPENSUSE apply-grpc-build-failure-ppc64le.patch
Patch1:         apply-grpc-build-failure-ppc64le.patch
BuildRequires:  gcc-c++
BuildRequires:  java-11-openjdk-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(zlib)
Requires(post): update-alternatives
Requires(postun): update-alternatives
# Bazel6.0 does not support Java 8 and 17
Requires:       java-11-openjdk-devel
Provides:       bazel = %{version}
ExcludeArch:    %ix86 %arm

%description
Tool for the automation of building and testing of software. It supports Java,
C++ and Go as programing languages. It also has a support for Android and iOS
as mobile operating systems.

%prep
%autosetup -p0 -c
# Remove executable permissions
chmod 0644 AUTHORS CHANGELOG.md CONTRIBUTORS LICENSE

cp %{SOURCE2} .
cp %{SOURCE3} .

%build
%ifarch aarch64 %arm
export BAZEL_JAVAC_OPTS="-J-Xmx2g -J-Xms200m"
%endif
%ifarch s390x
export BAZEL_JAVAC_OPTS="-J-Xmx4g -J-Xms1g"
%endif
export CC=gcc
export CXX=g++
export EXTRA_BAZEL_ARGS="--tool_java_runtime_version=local_jdk"
./compile.sh
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
