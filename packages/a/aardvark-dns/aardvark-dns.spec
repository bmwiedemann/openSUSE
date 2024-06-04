#
# spec file for package aardvark-dns
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


Name:           aardvark-dns
Version:        1.11.0
Release:        0
Summary:        Authoritative dns server for A/AAAA container records
License:        Apache-2.0
URL:            https://github.com/containers/%{name}
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  cargo
BuildRequires:  cargo-packaging
# Disable this line if you wish to support all platforms.

%description
Aardvark-dns is an authoritative dns server for A/AAAA container records.
It can forward other requests to configured resolvers.

%prep
%autosetup -a1

%build
%make_build

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}

%files
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}

%changelog
