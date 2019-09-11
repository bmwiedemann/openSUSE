#
# spec file for package mfoc
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           mfoc
Summary:        Mifare Classic Offline Cracker: key recovery tool for MC cards
License:        GPL-2.0+
Group:          Hardware/Other
Version:        0.10.6
Release:        0
Url:            http://code.google.com/p/nfc-tools/

#Git-Clone:	http://code.google.com/p/mfoc/
Source:         %name-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
BuildRequires:  xz
%if 0%{?suse_version} >= 1140 || 0%{?fedora_version}
BuildRequires:  pkgconfig(libnfc) >= 1.7
%else
BuildRequires:  libnfc-devel >= 1.7
%endif

%description
MFOC is a tool to recover keys from Mifare Classic cards.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags};

%install
b="%buildroot";
make install DESTDIR="$b";
rm -f "$b/%_libdir"/*.la;

%files
%defattr(-,root,root)
%_bindir/mfoc
%_mandir/man1/mfoc.1*

%changelog
