#
# spec file for package akamai-purge
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


Name:           akamai-purge
Version:        1.1.0
Release:        0
Summary:        Akamai CDN FastPurge Client
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        Apache-2.0
URL:            https://github.com/akamai/cli-purge
Source:         https://github.com/akamai/cli-purge/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}-gh.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  go
BuildRequires:  zstd

%description
Akamai CLI for Purge allows you to purge cached content from the Edge using FastPurge (CCUv3).

FastPurge will typically invalidate (recommended), or delete cached content in under five seconds.

%prep
%autosetup -p1 -a1 -n cli-purge-%{version}

%build
go build -trimpath -buildmode=pie -mod=vendor -o akamai-purge

%install
install -D akamai-purge %{buildroot}%{_bindir}/akamai-purge

%files
%license LICENSE
%doc README.md
%{_bindir}/akamai-purge

%changelog
