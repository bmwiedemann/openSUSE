#
# spec file for package sequoia-pgp-octopus
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

Name:           sequoia-octopus-librnp
Version:        1.9.0
Release:        0
Summary:        librnp drop-in replacement using sequoia-pgp
License:        LGPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://gitlab.com/sequoia-pgp/sequoia-octopus-librnp
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
Requires:       MozillaThunderbird
Provides:       MozillaThunderbird-openpgp
Conflicts:      MozillaThunderbird-openpgp

%description
Sequoia Octopus' librnp is an alternative OpenPGP implementation for Mozilla Thunderbird.
If installed it will replace the upstream Thunderbird OpenPGP backend based on Botan.

%prep
%autosetup -a1 -p1

%build
%cargo_build

%install
mkdir  -p %{buildroot}%{_libdir}/thunderbird
install -m 755 target/release/libsequoia_octopus_librnp.so %{buildroot}%{_libdir}/thunderbird/librnp.so

%files
%dir %{_libdir}/thunderbird/
%{_libdir}/thunderbird/librnp.so

%changelog
