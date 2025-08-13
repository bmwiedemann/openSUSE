#
# spec file for package libstrophe
#
# Copyright (c) 2024 SUSE LLC
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


%define sover 0
Name:           libstrophe
Version:        0.14.0
Release:        0
Summary:        A XMPP library for C
License:        GPL-3.0-or-later OR MIT
Group:          Development/Libraries/C and C++
URL:            https://strophe.im/libstrophe/
Source0:        https://github.com/strophe/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/strophe/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
# https://github.com/strophe/libstrophe/blob/0.14.0/README.markdown
# "Releases are signed with the GPG key with ID F8ADC1F9A68A7AFF0E2C89E4391A5EFC2D1709DE"
Source2:        %{name}.keyring
Patch0:         libstrophe-0.14.0-gcc15.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7
BuildRequires:  pkgconfig(zlib)

%description
Strophe is a collection of libraries for speaking the XMPP protocol.

While most XMPP libraries and implementations are focused on chat-based
applications, Strophe takes a grander view.

It has been used to implement real-time games, notification systems, search
engines, as well as traditional instant messaging.

The implementations are production ready, well documented, easy to use, and
easy to extend.

%package devel
Summary:        Development files for libstrophe
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
Development files and headers for libstrophe

%package -n %{name}%{sover}
Summary:        A XMPP library for C
Group:          System/Libraries

%description -n %{name}%{sover}
The libstrophe library is a XMPP library written in C.

%prep
%autosetup -p1

%build
%configure \
	--with-libxml2 \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING
%doc ChangeLog README
%{_libdir}/libstrophe.so.%{sover}{,.*}

%files devel
%license COPYING
%{_libdir}/libstrophe.so
%{_includedir}/strophe.h
%{_libdir}/pkgconfig/libstrophe.pc

%changelog
