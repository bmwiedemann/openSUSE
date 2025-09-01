#
# spec file for package gpg-tui
#
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


Name:           gpg-tui
Version:        0.11.1
Release:        0
Summary:        Terminal User Interface for GnuPG
License:        MIT
URL:            https://github.com/orhun/gpg-tui
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.82.0
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(gpgme) >= 1.12.0
Requires:       gpg2
ExclusiveArch:  %{rust_tier1_arches}

%description
gpg-tui is a Terminal User Interface for GnuPG. It aims to ease the key
management operations such as listing/exporting/signing by providing an
interface along with the command-line fallback for more complex operations. It
is not trying to be a full-fledged interface for all the features that gpg
provides but it tries to bring a more interactive approach to key management.

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
%doc CHANGELOG.md COMMANDS.md README.md RELEASE.md
%{_bindir}/gpg-tui
%{_bindir}/gpg-tui-completions

%changelog
