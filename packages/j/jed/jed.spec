#
# spec file for package jed
#
# Copyright (c) 2025 SUSE LLC
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
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


Name:           jed
BuildRequires:  slang-devel
Requires:       slang-slsh
Version:        0.99.19
Release:        0
URL:            http://www.jedsoft.org
License:        GPL-2.0-only
Summary:        Small editor
Source:         %{name}-0.99-19.tar.bz2
Patch0:         %{name}-0.99-19.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
JED text editor

%prep
%autosetup -p1 -n %{name}-0.99-19

%build
slanginc=/usr/include
%configure --prefix=/usr --datadir=%{_datadir} --with-slanglib=%{_libdir} --with-slanginc=$slanginc
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-script
%dir %{_datadir}/jed
%{_datadir}/jed
%{_mandir}/man?/*

%changelog
