#
# spec file for package cc-tool
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cc-tool
Version:        0.26
Release:        0
Summary:        Programmer for Texas Instruments 8051-based System-On-Chip devices
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            http://sourceforge.net/projects/cctool/
Source0:        https://downloads.sourceforge.net/project/cctool/cc-tool-%{version}-src.tgz
Source1:        boost.m4
Patch1:         fix-flashing.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libboost_filesystem-devel >= 1.55
BuildRequires:  libboost_program_options-devel >= 1.55
BuildRequires:  libboost_regex-devel >= 1.55
BuildRequires:  libboost_system-devel >= 1.55
BuildRequires:  libtool
BuildRequires:  libusb-devel

%description
cc-tool provides support for Texas Instruments CC Debugger for Linux in order
to program 8051-based System-On-Chip devices: CC254x CC253x CC243x CC251x CC111x.

%prep
%setup -q -n %{name}
%patch1

%build
cp %{SOURCE1} m4/
autoreconf -vfi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/cc-tool
%{_mandir}/man1/cc-tool.1%{?ext_man}

%changelog
