#
# spec file for package libotr
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libotr
Version:        4.1.1
Release:        0
Summary:        "Off The Record" messaging library toolkit
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://www.cypherpunks.ca/otr/
Source:         https://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
Source1:        https://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz.asc
Source2:        http://www.cypherpunks.ca/otr/gpgkey.asc#/libotr.keyring
Patch0:         libotr-4.1.1-fix-base64-tests.patch
Patch1:         libotr-test-underrun.patch
Patch2:         libotr-test-uninitialized.patch
Patch3:         libotr-4.1.1-include-socket.h.patch
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Off-the-Record (OTR) Messaging allows you to have private conversations
over instant messaging by providing: Encryption No one else can read
your instant messages. Authentication You are assured the correspondent
is who you think it is. Deniability The messages you send do not have
digital signatures that are checkable by a third party. Anyone can
forge messages after a conversation to make them look like they came
from you. However, during a conversation, your correspondent is assured
the messages he sees are authentic and unmodified. Perfect forward
secrecy If you lose control of your private keys, no previous
conversation is compromised.

%package -n libotr5
Summary:        "Off The Record" messaging library toolkit
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
#openSUSE 10.3
Provides:       %{name} = %{version}
Obsoletes:      %{name} <= 3.0.0

%description -n libotr5
Off-the-Record (OTR) Messaging allows you to have private conversations
over instant messaging by providing: Encryption No one else can read
your instant messages. Authentication You are assured the correspondent
is who you think it is. Deniability The messages you send do not have
digital signatures that are checkable by a third party. Anyone can
forge messages after a conversation to make them look like they came
from you. However, during a conversation, your correspondent is assured
the messages he sees are authentic and unmodified. Perfect forward
secrecy If you lose control of your private keys, no previous
conversation is compromised.

%package devel
Summary:        Include files and development libraries
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Libraries/C and C++
Requires:       libgcrypt-devel
Requires:       libotr5 = %{version}

%description devel
Headers and development libraries for libotr

%package tools
Summary:        "Off The Record" messaging library toolkit
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++

%description tools
Off-the-Record (OTR) Messaging allows you to have private conversations
over instant messaging by providing: Encryption No one else can read
your instant messages. Authentication You are assured the correspondent
is who you think it is. Deniability The messages you send do not have
digital signatures that are checkable by a third party. Anyone can
forge messages after a conversation to make them look like they came
from you. However, during a conversation, your correspondent is assured
the messages he sees are authentic and unmodified. Perfect forward
secrecy If you lose control of your private keys, no previous
conversation is compromised.

%prep
%autosetup -p1

%build
%ifarch %arm
export CFLAGS="%{optflags} -O1"
%else
export CFLAGS="%{optflags}"
%endif
%configure --disable-static --with-pic
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/libotr.la

%files tools
%defattr (-, root, root)
%license COPYING
%{_bindir}/otr*
%{_mandir}/man1/otr*

%files -n libotr5
%defattr (-, root, root)
%license COPYING.LIB
%{_libdir}/libotr.so.5*

%files devel
%defattr (-, root, root)
%doc README AUTHORS NEWS ChangeLog
%license COPYING
%dir %{_includedir}/libotr
%{_includedir}/libotr/*.h
%{_libdir}/libotr.so
%{_datadir}/aclocal/libotr.m4
%{_libdir}/pkgconfig/libotr.pc

%post -n libotr5 -p /sbin/ldconfig
%postun -n libotr5 -p /sbin/ldconfig

%changelog
