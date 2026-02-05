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
%define _minor_version 15
%define _patch_version 0
%define _major_minor_ver %{_major_version}.%{_minor_version}
Name:           zls
Version:        %{_major_minor_ver}.%{_patch_version}
Release:        0
Summary:        Language server implementation for Zig in Zig
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/zigtools/zls
Source0:        https://github.com/zigtools/zls/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
# ZLS only follows versions for zig except patch vers
BuildRequires:  zig >= %{_major_minor_ver}.1
BuildRequires:  zig-rpm-macros >= %{_major_minor_ver}.1
BuildRequires:  zstd

%description
Zig Language Server, or zls, is an unofficial language server for Zig.

%prep
%autosetup -a1

%build
%zig_build -Dpie --cache-dir $PWD/zig-cache --global-cache-dir $PWD/vendor/

%install
%zig_install -Dpie --cache-dir $PWD/zig-cache --global-cache-dir $PWD/vendor/

%check
%zig_test --verbose -Dpie --cache-dir $PWD/zig-cache --global-cache-dir $PWD/vendor/

%files
%{_bindir}/zls
%license LICENSE
%doc README.md

%changelog
