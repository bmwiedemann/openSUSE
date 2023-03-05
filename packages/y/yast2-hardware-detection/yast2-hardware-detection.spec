#
# spec file for package yast2-hardware-detection
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


Name:           yast2-hardware-detection
Version:        4.6.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Group:          System/YaST
License:        GPL-2.0-or-later
# obviously
BuildRequires:  gcc-c++
BuildRequires:  libtool
# needed for all yast packages
BuildRequires:  yast2-devtools >= 3.1.10
# autodocs
BuildRequires:  doxygen
# testsuite
BuildRequires:  dejagnu
# this is a yast plugin, needs core
BuildRequires:  yast2-core-devel
# da library
BuildRequires:  hwinfo-devel
# we check for hwinfo
BuildRequires:  pkg-config
Requires:       yast2-ruby-bindings >= 1.0.0

Summary:        YaST2 - Hardware Detection Interface
Requires:       hwinfo >= 21.5

%description
This package contains the hardware detection library for YaST2.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

rm $RPM_BUILD_ROOT/%{yast_plugindir}/libpy2ag_hwprobe.la

%files
%defattr(-,root,root)
%{yast_scrconfdir}/*.scr
%{yast_plugindir}/libpy2ag_hwprobe.so.*
%{yast_plugindir}/libpy2ag_hwprobe.so
%doc %{yast_docdir}
%license COPYING

%changelog
