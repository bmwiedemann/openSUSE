#
# spec file for package podlet
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


Name:           podlet
Version:        0.2.4~0
Release:	0
Summary:        Podman quadlet generator
License:        MPL-2.0
URL:            https://github.com/k9withabone/podlet/
Source0:        podlet-0.2.4~0.tar.zst
Source1:	vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Podlet generates podman quadlet files from a podman command, compose file, or existing object.


%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/podlet

%changelog

