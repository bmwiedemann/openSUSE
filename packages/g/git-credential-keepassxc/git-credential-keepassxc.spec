#
# spec file for package git-credential-keepassxc
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


Name:           git-credential-keepassxc
Version:        0.14.1~0
Release:        0
Summary:        Helper that allows Git (and shell scripts) to use KeePassXC as credential store 
License:        GPL-3.0-only
URL:            https://github.com/Frederick888/git-credential-keepassxc
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
A Git credential helper that allows Git (and shell scripts) to get/store logins from/to KeePassXC.

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
%{_bindir}/%{name}

%changelog
