#
# spec file for package exfatprogs
#
# Copyright (c) 2020 SUSE LLC
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


Name:           exfatprogs
Version:        1.0.2
Release:        0
Summary:        Utilities for exFAT file system maintenance
License:        GPL-2.0-or-later
URL:            https://github.com/exfatprogs/exfatprogs
Source0:        https://github.com/exfatprogs/exfatprogs/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
Conflicts:      exfat-utils
ExclusiveArch:  aarch64 x86_64

%description
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

%package -n libexfat0
Summary:        Utilities for exFAT file system maintenance

%description -n libexfat0
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

This package contains the shared library.

%prep
%setup -q
chmod -x COPYING

%build
autoreconf -fi
%configure --disable-static

%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

# There is no header yet, so this is unusable for now.
rm %{buildroot}%{_libdir}/libexfat.so

%post -n libexfat0 -p /sbin/ldconfig
%postun -n  libexfat0 -p /sbin/ldconfig

%files -n libexfat0
%license COPYING
%{_libdir}/libexfat.so.0*

%files
%license COPYING
%doc README.md
%{_sbindir}/fsck.exfat
%{_sbindir}/label.exfat
%{_sbindir}/mkfs.exfat

%changelog
