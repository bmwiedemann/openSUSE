#
# spec file for package mtx
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mtx
Version:        1.3.12
Release:        0
Summary:        A Program for Controlling the Robotic Mechanism in DDS Auto Loaders
License:        GPL-2.0+
Group:          Hardware/Other
Url:            https://sourceforge.net/projects/mtx/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}-stable/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.3.12-param_h.patch
Patch2:         %{name}-1.3.12-autoconf.patch
Patch3:         mtx-1.3.11-large-slots.patch
Patch4:         mtx-1.3.12-destdir.patch
BuildRequires:  autoconf
BuildRequires:  automake

%description
A program for controlling the robotic mechanism in DDS auto loaders and tape
libraries.

%prep
%setup -q
%patch0
%patch2
%patch3
%patch4 -p2

%build
autoreconf -fvi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc README TODO LICENSE CHANGES FAQ mtx.doc
%{_sbindir}/*
%{_mandir}/man1/*

%changelog
