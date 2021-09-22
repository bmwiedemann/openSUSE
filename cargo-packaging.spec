#
# spec file for package cargo-packaging
#
# Copyright (c) 2021 SUSE LLC
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



Name:           cargo-packaging
Version:        1.0.0~git3.e0b8dad
Release:        0
BuildArch:      noarch
Summary:        Some macros to assist with cargo and rust packaging
License:        MPL-2.0
URL:            https://github.com/Firstyear/cargo-packaging
Source0:        %{name}-%{version}.tar.xz
Requires: cargo

Conflicts: rust-packaging

%description
A set of macros to assist with cargo and rust packaging, written in a manner
that follows rust's best practices.

%prep
%autosetup

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmconfigdir}/macros.d %{_builddir}/%{name}-%{version}/macros.cargo

%files
%{_rpmconfigdir}/macros.d/macros.cargo

%changelog
