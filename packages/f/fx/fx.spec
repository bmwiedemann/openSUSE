#
# spec file for package fx
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2022-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           fx
Version:        35.0.0
Release:        0
Summary:        Terminal JSON viewer
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://fx.wtf/
#Git-Clone:     https://github.com/antonmedv/fx.git
Source:         https://github.com/antonmedv/fx/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go
BuildRequires:  golang-packaging
%{go_provides}

%description
Terminal JSON viewer.

%prep
%autosetup -p 1 -a 1

%build
%{goprep} github.com/antonmedv/fx
%{gobuild} -mod=vendor .

%install
%{goinstall}

%files
%license LICENSE
%doc README.md
%{_bindir}/fx

%changelog
