#
# spec file for package nomino
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


Name:           nomino
Version:        1.3.5
Release:        0
Summary:        Batch rename utility for developers
License:        Apache-2.0 OR MIT
URL:            https://github.com/yaa110/nomino
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
nomino is a batch rename utility for developers

%prep
%autosetup -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/%{name}

%changelog
