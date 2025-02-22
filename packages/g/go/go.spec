#
# spec file for package go
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

# NOTE: This logic must come from the latest go1.x package specfile.
# We only build go-race on supported systems.
%if 0%{suse_version} >= 1500 || 0%{?sle_version} >= 150000
%define tsan_arch x86_64 aarch64 s390x ppc64le
%else
# Cannot use {nil} here (ifarch doesn't like it) so just make up a fake
# architecture that no build will ever match.
%define tsan_arch openSUSE_FAKE_ARCH
%endif

Name:           go
Version:        1.24
# Version must always be a valid golang(API) version
%define api_version %{version}
Release:        0
Summary:        A compiled, garbage-collected, concurrent programming language
License:        BSD-3-Clause
Group:          Development/Languages/Go
Url:            http://golang.org
Source:         README
Recommends:     go-doc = %{version}
ExclusiveArch:  %ix86 x86_64 %arm aarch64 ppc64 ppc64le s390x riscv64
# We provide golang(API) so that projects can Prefer: go. Any project using Go
# code with golang(API) BuildRequires should add Prefer: go.
Provides:       golang(API) = %{api_version}
# We provide this for RH/Fedora compatibility
Provides:       golang = %{version}
# Make this both Requires and BuildRequires go1.x so that we get build errors
# if it is missing.
BuildRequires:  go%{api_version}
Requires:       go%{api_version}

%description
Go is an expressive, concurrent, garbage collected systems programming language
that is type safe and memory safe. It has pointers but no pointer arithmetic.
Go has fast builds, clean syntax, garbage collection, methods for any type, and
run-time reflection. It feels like a dynamic language but has the speed and
safety of a static language.

%package doc
Summary:        Go documentation
License:        BSD-3-Clause
Group:          Documentation/Other
# We provide this for RH/Fedora compatibility
Provides:       golang-docs = %{version}
Requires:       go = %{version}
Supplements:    go = %{version}
Requires:       go%{api_version}-doc

%description doc
Go examples and documentation.

%ifarch %{tsan_arch}
# boo#1052528
%package race
Summary:        Go runtime race detector
License:        NCSA or MIT
Group:          Development/Languages/Go
Url:            https://compiler-rt.llvm.org/
Requires:       go = %{version}
Supplements:    go = %{version}
ExclusiveArch:  %{tsan_arch}
# We provide this for RH/Fedora compatibility
Provides:       golang-race = %{version}
# Make this both Requires and BuildRequires go1.x-race so that we get build
# errors if it is missing.
BuildRequires:  go%{api_version}-race
Requires:       go%{api_version}-race

%description race
Go runtime race detector libraries. Install this package if you wish to use the
-race option, in order to detect race conditions present in your Go programs.
%endif

%prep

%build

%install
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/go/README
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/go-doc/README
%ifarch %{tsan_arch}
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/go-race/README
%endif

%files
%defattr(-,root,root,-)
%doc /usr/share/doc/packages/go/

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/packages/go-doc/

%ifarch %{tsan_arch}
%files race
%doc /usr/share/doc/packages/go-race/
%defattr(-,root,root,-)
%endif

%changelog
