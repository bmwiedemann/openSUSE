#
# spec file for package nfc-eventd
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


Name:           nfc-eventd
Summary:        NFC event daemon
License:        GPL-3.0+
Group:          Hardware/Other
Version:        0.1.7
Release:        0
Url:            http://code.google.com/p/nfc-tools/

#SVN-DL:	http://nfc-tools.googlecode.com/svn/trunk/nfc-eventd/
#DL-URL:	http://nfc-tools.googlecode.com/files/nfc-eventd-0.1.7.tar.gz
Source:         %name-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
BuildRequires:  xz
%if 0%{?suse_version} >= 1140 || 0%{?fedora_version}
BuildRequires:  pkgconfig(libnfc) > 1.6.99
%else
BuildRequires:  libnfc-devel > 1.6.99
%endif

%description
nfc-eventd is a daemon that looks for tags insertions/removes from
NFC device. It is provided with two NEM (Nfc Eventd Modules) which
allow many kind of usage of theses events.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags};

%install
b="%buildroot";
make install DESTDIR="$b";
find "$b" -type f -name "*.la" -delete;

%files
%defattr(-,root,root)
%config %_sysconfdir/nfc-eventd.conf
%_bindir/nfc-eventd
%_libdir/%name

%changelog
