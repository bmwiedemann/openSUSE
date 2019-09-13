#
# spec file for package nfcutils
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


Name:           nfcutils
Summary:        Near Field Communication (NFC) utilities
License:        GPL-3.0+
Group:          Hardware/Other
Version:        0.3.2
Release:        0
Url:            http://code.google.com/p/nfc-tools/

#SVN-DL:	http://nfc-tools.googlecode.com/svn/trunk/nfcutils/
#DL-URL:	http://nfc-tools.googlecode.com/files/nfcutils-0.3.2.tar.gz
Source:         %name-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(libnfc) > 1.6.99

%description
This package contains one utility for listing NFC devices and
in-field tags or targets.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags};

%install
b="%buildroot";
make install DESTDIR="$b";

%files
%defattr(-,root,root)
%_bindir/lsnfc
%doc COPYING

%changelog
