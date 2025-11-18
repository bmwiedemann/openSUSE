#
# spec file for package asciinema
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           asciinema
Version:        3.0.1
Release:        0
Summary:        Terminal session recorder
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://asciinema.org
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Record of terminal sessions and sharing them on the web.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/%{name}

%changelog
