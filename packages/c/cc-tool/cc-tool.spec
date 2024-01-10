#
# spec file for package cc-tool
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.27
Release:        0
Summary:        Programmer for Texas Instruments 8051-based System-On-Chip devices
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            http://sourceforge.net/projects/cctool/
Source0:        https://github.com/dashesy/cc-tool/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        boost.m4
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
%setup -q

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
