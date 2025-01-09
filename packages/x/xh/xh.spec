#
# spec file for package xh
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


Name:           xh
Version:        0.23.1
Release:        0
Summary:        Tool for sending HTTP requests
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/ducaale/xh
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  libopenssl-devel

%description
xh is a tool for sending HTTP requests. It reimplements as much as possible of HTTPie's design, with a focus on improved performance.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%{_bindir}/%{name}

%changelog
