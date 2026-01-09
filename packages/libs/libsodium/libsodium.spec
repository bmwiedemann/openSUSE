#
# spec file for package libsodium
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover   26
%define lname   %{name}%{sover}
Name:           libsodium
Version:        1.0.21
Release:        0
Summary:        Portable NaCl-based crypto library
License:        ISC
Group:          System/Libraries
URL:            https://github.com/jedisct1/libsodium
Source0:        https://download.libsodium.org/libsodium/releases/%{name}-%{version}.tar.gz
Source1:        https://download.libsodium.org/libsodium/releases/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source99:       baselibs.conf
Patch0:         libsodium-Fix-compilation-with-GCC-on-aarch64.patch
BuildRequires:  pkgconfig

%description
NaCl (pronounced "salt") is a new easy-to-use high-speed software library
for network communication, encryption, decryption, signatures, etc.NaCl's goal
is to provide all of the core operations needed to build higher-level cryptographic tools.

Sodium is a portable, cross-compilable, installable, packageable fork of NaCl,
with a compatible API.

%package -n  %{lname}
Summary:        Portable NaCl-based crypto library
Group:          System/Libraries

%description -n %{lname}
NaCl (pronounced "salt") is a new easy-to-use high-speed software library
for network communication, encryption, decryption, signatures, etc. NaCl's goal
is to provide all of the core operations needed to build higher-level cryptographic tools.

Sodium is a portable, cross-compilable, installable, packageable fork of NaCl,
with a compatible API.

%package devel
Summary:        Portable NaCl-based crypto library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libsodium.

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
  --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSE
%{_libdir}/%{name}.so.%{sover}*

%files devel
%license LICENSE
%doc AUTHORS ChangeLog README.markdown THANKS
%{_includedir}/sodium.h
%{_includedir}/sodium
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
