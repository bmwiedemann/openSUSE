#
# spec file for package bonk
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           bonk
Version:        0.4.0+g0
Release:        0
Summary:        Touch with mkdir tool
License:        MIT
Group:          System/Console
URL:            https://github.com/elliot40404/bonk
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Bonk is a touch alternative with an added feature to
create directories.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/bonk

%changelog
