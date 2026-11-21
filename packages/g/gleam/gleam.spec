#
# spec file for package gleam
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


Name:           gleam
Version:        1.19.2
Release:        0
Summary:        A friendly language for building type-safe, scalable systems!
License:        Apache-2.0
URL:            https://gleam.run/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# PATCH-FIX-OPENSUSE fix-for-CVE-2026-115905.patch bsc#1287931 GHSA-wjr6-mhvj-cjvm GHSA-gmfj-vffv-32pw jan.fooken@suse.com -- Update zip crate due to several security issues
Patch1:         fix-for-CVE-2026-115905.patch
BuildRequires:  cargo-packaging
# Gleam depends on the duration_constructors feature
# https://github.com/rust-lang/rust/issues/120301
BuildRequires:  cargo >= 1.91.0
# For tests
BuildRequires:  erlang >= 27
BuildRequires:  git-core
Requires:       erlang >= 27
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
# tests::echo* requires JavaScript engines that aren't packaged on openSUSE
# tests::escript_success_with_dependency requires network access
# tests::all_files_have_copyright_notice has a bug where id doesn't handle gleam.lock files
%{cargo_test} -- \
	--skip tests::echo \
	--skip tests::output::echo_bitarray \
	--skip tests::output::echo_bool \
	--skip tests::output::echo_charlist \
	--skip tests::output::echo_circular_reference \
	--skip tests::output::echo_custom_type \
	--skip tests::output::echo_dict \
	--skip tests::output::echo_float \
	--skip tests::output::echo_function \
	--skip tests::output::echo_importing_module_named_inspect \
	--skip tests::output::echo_int \
	--skip tests::output::echo_list \
	--skip tests::output::echo_nan_infinity \
	--skip tests::output::echo_nil \
	--skip tests::output::echo_singleton \
	--skip tests::output::echo_string \
	--skip tests::output::echo_tuple \
	--skip tests::output::echo_with_message \
	--skip tests::escript_success_with_dependency \
	--skip tests::all_files_have_copyright_notice

%files
%license LICENCE
%{_bindir}/%{name}

%changelog
