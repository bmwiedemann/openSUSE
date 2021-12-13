#
# spec file for package libcacard
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


Name:           libcacard
URL:            https://gitlab.freedesktop.org/spice/libcacard
Summary:        Common Access Card (CAC) emulation
License:        LGPL-2.1-or-later
Group:          System/Emulators/PC
Version:        2.8.1
Release:        0
Source:         http://www.spice-space.org/download/libcacard/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  meson
BuildRequires:  mozilla-nss-devel
BuildRequires:  pkg-config

%description
This emulator is designed to provide emulation of actual smart cards to a
virtual card reader running in a guest virtual machine. The emulated smart
cards can be representations of real smart cards, where the necessary functions
such as signing, card removal/insertion, etc. are mapped to real, physical
cards which are shared with the client machine the emulator is running on, or
the cards could be pure software constructs.

%package -n libcacard0
Summary:        Common Access Card (CAC) emulation
Group:          System/Emulators/PC

%description -n libcacard0
This emulator is designed to provide emulation of actual smart cards to a
virtual card reader running in a guest virtual machine. The emulated smart
cards can be representations of real smart cards, where the necessary functions
such as signing, card removal/insertion, etc. are mapped to real, physical
cards which are shared with the client machine the emulator is running on, or
the cards could be pure software constructs.

%package devel
Summary:        Common Access Card (CAC) emulation -- Development files
Group:          Development/Languages/C and C++
Requires:       glib2-devel
Requires:       libcacard0 = %version
Requires:       mozilla-nspr
Requires:       mozilla-nss

%description devel
This emulator is designed to provide emulation of actual smart cards to a
virtual card reader running in a guest virtual machine. The emulated smart
cards can be representations of real smart cards, where the necessary functions
such as signing, card removal/insertion, etc. are mapped to real, physical
cards which are shared with the client machine the emulator is running on, or
the cards could be pure software constructs.

This sub-package contains development files for the Smartcard library.

%prep
%setup -q

%build
%meson -Dpcsc=disabled -Ddisable_tests=true
%meson_build

%install
%meson_install
rm -f %{buildroot}%{_libdir}/libcacard.a
rm -f %{buildroot}%{_libdir}/libcacard.la

%post   -n libcacard0 -p /sbin/ldconfig

%postun -n libcacard0 -p /sbin/ldconfig

%files -n libcacard0
%defattr(-, root, root)
%{_libdir}/libcacard.so.0*

%files devel
%defattr(-, root, root)
%dir %{_includedir}/cacard
%{_includedir}/cacard/*.h
%{_libdir}/libcacard.so
%{_libdir}/pkgconfig/libcacard.pc

%changelog
