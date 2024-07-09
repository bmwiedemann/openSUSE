#
# spec file for package gleam
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gleam
Version:        1.3.0
Release:        0
Summary:        A friendly language for building type-safe, scalable systems!
License:        Apache-2.0
URL:            https://gleam.run/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
# Due to dependency on pulldown-cmark
BuildRequires:  cargo >= 1.74.0
# For tests
BuildRequires:  git-core
Requires:       erlang
Requires:       erlang-rebar3
ExclusiveArch:  %{rust_tier1_arches}

%description
The power of a type system, the expressiveness of functional programming,
and the reliability of the highly concurrent, fault tolerant Erlang runtime,
with a familiar and modern syntax.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/gleam %{buildroot}%{_bindir}/gleam

%check
%{cargo_test}

%files
%license LICENCE
%{_bindir}/%{name}

%changelog
