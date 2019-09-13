#
# spec file for package pidgin-otr
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


Name:           pidgin-otr
Version:        4.0.2
Release:        0
Summary:        "Off The Record" end-to-end encryption plugin for Pidgin
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://otr.cypherpunks.ca/
Source:         https://otr.cypherpunks.ca/%{name}-%{version}.tar.gz
Source2:        https://otr.cypherpunks.ca/%{name}-%{version}.tar.gz.asc
Source3:        https://otr.cypherpunks.ca/gpgkey.asc#/pidgin-otr.keyring
# PATCH-FEATURE-UPSTREAM https://bugs.otr.im/plugins/pidgin-otr/issues/127
Source4:        pidgin-otr.metainfo.xml
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libotr) >= 4.0.0
BuildRequires:  pkgconfig(pidgin)

%description
This is a Pidgin plugin which implements Off-the-Record (OTR)
Messaging. OTR allows you to have private conversations over IM by
providing:
 * Encryption.
 * No one else can read your instant messages.
 * Authentication.
 * You are assured the correspondent is who you think it is.
 * Deniability.
 * The messages you send do not have digital signatures that are
   checkable by a third party. Anyone can forge messages after a
   conversation to make them look like they came from you.
   However, during a conversation, your correspondent is assured
   the messages he sees are authentic and unmodified.
 * Perfect forward secrecy.
 * If you lose control of your private keys, no previous
   conversation is compromised.

%package -n pidgin-plugin-otr
Summary:        "Off The Record" end-to-end encryption plugin for Pidgin
Group:          Productivity/Networking/Instant Messenger
Recommends:     pidgin-plugin-otr-lang
# pidgin-otr was last used in openSUSE Leap 42.2.
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
%requires_ge    pidgin

%description -n pidgin-plugin-otr
This is a Pidgin plugin which implements Off-the-Record (OTR)
Messaging. OTR allows you to have private conversations over IM by
providing:
 * Encryption.
 * No one else can read your instant messages.
 * Authentication.
 * You are assured the correspondent is who you think it is.
 * Deniability.
 * The messages you send do not have digital signatures that are
   checkable by a third party. Anyone can forge messages after a
   conversation to make them look like they came from you.
   However, during a conversation, your correspondent is assured
   the messages he sees are authentic and unmodified.
 * Perfect forward secrecy.
 * If you lose control of your private keys, no previous
   conversation is compromised.

%lang_package -n pidgin-plugin-otr

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install -Dm0644 %{SOURCE4} %{buildroot}%{_datadir}/appdata/pidgin-otr.metainfo.xml
%find_lang pidgin-otr

%post -n pidgin-plugin-otr -p /sbin/ldconfig

%postun -n pidgin-plugin-otr -p /sbin/ldconfig

%files -n pidgin-plugin-otr
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/pidgin/%{name}.so
%dir %{_datadir}/appdata/
%{_datadir}/appdata/pidgin-otr.metainfo.xml

%files -n pidgin-plugin-otr-lang -f %{name}.lang
%defattr(-,root,root)

%changelog
