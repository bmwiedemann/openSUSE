#
# spec file for package irc-otr
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


Name:           irc-otr
Version:        1.0.2
Release:        0
Summary:        Off-The-Record Messaging plugin for irssi
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/cryptodotis/irssi-otr
Source:         https://github.com/cryptodotis/irssi-otr/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.12
BuildRequires:  irssi-devel >= 0.8.15
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  libotr-devel >= 4.1.0
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides modules which implement Off-The-Record (OTR) Messaging
protocol for a number of popular IRC clients.

OTR allows you to have private conversations over IM by providing:

 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%package -n	irssi-otr
Summary:        Off-The-Record messaging plugin for irssi
Group:          Productivity/Networking/Instant Messenger
Requires:       irssi

%description -n	irssi-otr
This plugin adds Off-the-Record messaging support for the irssi IRC client.
Although primarily designed for use with the bitlbee IRC2IM gateway, it
works within any query window, provided that the conversation partner's IRC
client supports OTR.

OTR allows you to have private conversations over IM by providing:

 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%prep
%setup -q -n irssi-otr-%{version}

%build
./bootstrap
export CFLAGS="%{optflags}"
%configure \
	--with-irssi-module-dir=%{_libdir}/irssi/modules
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm %{buildroot}%{_datadir}/irssi/help/otr

%files -n irssi-otr
%defattr(-,root,root)
%doc README.md LICENSE ChangeLog help/otr
%{_libdir}/irssi/modules/libotr.so

%changelog
