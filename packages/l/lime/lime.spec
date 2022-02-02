#
# spec file for package lime
#
# Copyright (c) 2022 SUSE LLC
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


%define soname  liblime
%define sover   0
Name:           lime
Version:        5.0.67
Release:        0
Summary:        Instant Message End-to-End Encryption Library
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://linphone.org/technical-corner/lime/
Source:         https://gitlab.linphone.org/BC/public/lime/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  soci-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  pkgconfig(bctoolbox) >= 5.0.0
BuildRequires:  pkgconfig(belle-sip) >= 5.0.0

%description
LIME is an encryption library for one-to-one and group instant
messaging, allowing users to exchange messages privately and
asynchronously. It supports multiple devices per user and multiple
users per device.

LIME offers two major security benefits to instant messaging users:
  * End-to-end encryption, which means that only you and your
    contact (and not even the server) can decrypt the content that
    you shared.
  * Perfect forward secrecy, which ensures that encrypted messages
    cannot be decrypted by a third party, even if a key is
    compromised in the future.

%package -n %{soname}%{sover}
Summary:        Instant Message End-to-End Encryption Library
Group:          Productivity/Networking/Instant Messenger

%description -n %{soname}%{sover}
LIME is an encryption library for one-to-one and group instant
messaging, allowing users to exchange messages privately and
asynchronously. It supports multiple devices per user and multiple
users per device.

LIME offers two major security benefits to instant messaging users:
  * End-to-end encryption, which means that only you and your
    contact (and not even the server) can decrypt the content that
    you shared.
  * Perfect forward secrecy, which ensures that encrypted messages
    cannot be decrypted by a third party, even if a key is
    compromised in the future.

%package devel
Summary:        Development files for lime
Group:          Development/Languages/C and C++
Requires:       %{soname}%{sover} = %{version}
Requires:       soci-devel
Requires:       soci-sqlite3-devel

%description devel
LIME is an encryption library for one-to-one and group instant
messaging, allowing users to exchange messages privately and
asynchronously. It supports multiple devices per user and multiple
users per device.

The soci development package includes the header files, libraries,
development tools necessary for compiling and linking applications
which will use lime.

%prep
%setup -q

%build
%cmake \
  -DENABLE_STRICT=OFF     \
  -DENABLE_STATIC=OFF     \
  -DENABLE_C_INTERFACE=ON
%cmake_build

%install
%cmake_install
chmod -x %{buildroot}%{_datadir}/%{name}_tester/data/*.pem

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license LICENSE.txt
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%license LICENSE.txt
%doc AUTHORS.md CHANGELOG.md README.md
%{_bindir}/%{name}*
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_datadir}/%{name}/
%{_datadir}/%{name}_tester/

%changelog
