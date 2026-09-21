#
# spec file for package zls
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _major_version 0
%define _minor_version 16
%define _patch_version 0
%define _major_minor_ver %{_major_version}.%{_minor_version}
Name:           zls
Version:        %{_major_minor_ver}.%{_patch_version}
Release:        0
Summary:        Language server implementation for Zig in Zig
License:        MIT
URL:            https://github.com/zigtools/zls
Source0:        https://github.com/zigtools/zls/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
# ZLS only follows versions for zig except patch vers, 0.16.0 needs zig 0.16.0
BuildRequires:  zig >= %{_major_minor_ver}.0
BuildRequires:  zig-rpm-macros >= %{_major_minor_ver}.0
BuildRequires:  zstd

%description
Zig Language Server, or zls, is an unofficial language server for Zig.

%prep
%autosetup -a1

%build
%{zig_build} -Dpie --cache-dir $PWD/zig-cache --global-cache-dir $PWD/vendor/ --system $PWD/vendor/p

%install
%{zig_install} -Dpie --cache-dir $PWD/zig-cache --global-cache-dir $PWD/vendor/ --system $PWD/vendor/p

%check
# The cimport test spawns `zig translate-c`, which zig compiles from
# source on first use; that takes minutes on slow arches, longer than
# the test timeout allows. Pre-compile it into the test cache first.
printf 'void zls_check_warmup(int);\n' > .translate-c-warmup.h
%{__zig} translate-c --zig-lib-dir %{_prefix}/lib/zig --cache-dir $PWD/zig-cache/zls --global-cache-dir $PWD/zig-cache/zls -lc .translate-c-warmup.h > /dev/null
rm .translate-c-warmup.h
%{zig_test} --verbose -Dpie --cache-dir $PWD/zig-cache --global-cache-dir $PWD/vendor/ --system $PWD/vendor/p

%files
%{_bindir}/zls
%license LICENSE
%doc README.md

%changelog
