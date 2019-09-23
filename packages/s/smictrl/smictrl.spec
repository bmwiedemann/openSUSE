#
# spec file for package smictrl
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

BuildRequires:  kernel-source pciutils-devel zlib-devel

Name:           smictrl
Url:            http://www.rts.uni-hannover.de/rtaddon/#smictrl
License:        GPL-2.0+
Group:          System/Monitoring
AutoReqProv:    on
Summary:        SMI Register Manipulation Tool
Version:        20070409
Release:        3
Source0:        %{name}.tar.bz2
Source1:        COPYING
Patch0:         makefile-modifications.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# smictrl is x86 specifc
ExclusiveArch:  %ix86 x86_64

%description
smictrl is able to manipulate various SMI registers on various chipsets
(by today only Intel chipsets).



Authors:
--------
    Jan Kiszka <kiszka@rts.uni-hannover.de>

%prep
%setup  -n smictrl
%patch0 -p1

%build
CFLAGS=$RPM_OPT_FLAGS make %{?jobs:-j%jobs}

%install
mkdir  -p $RPM_BUILD_ROOT%{_sbindir}
install -m 755 smictrl $RPM_BUILD_ROOT%{_sbindir}

%files
%defattr(-, root, root)
%{_sbindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
