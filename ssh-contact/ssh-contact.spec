#
# spec file for package ssh-contact
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


Name:           ssh-contact
Version:        0.7
Release:        0
Summary:        Tool to connect to telepathy IM contacts via SSH
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            http://telepathy.freedesktop.org/wiki/SSH-Contact
Source0:        http://telepathy.freedesktop.org/releases/ssh-contact/%{name}-%{version}.tar.gz
Source1:        README.openSUSE
BuildRequires:  intltool
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(telepathy-glib) >= 0.15.5
Requires:       %{name}-client = %{version}
Requires:       %{name}-service = %{version}

%description
SSH-Contact is a client/service tool that makes it easy to connect to
your telepathy IM contacts via SSH. No need to care about dynamic IP,
NAT, port forwarding, or firewalls anymore; if you can chat with a
friend, you can also SSH to their machine.

%package client
Summary:        Tool to connect to telepathy IM contacts via SSH -- Client
Group:          Productivity/Networking/Instant Messenger

%description client
SSH-Contact is a client/service tool that makes it easy to connect to
your telepathy IM contacts via SSH. No need to care about dynamic IP,
NAT, port forwarding, or firewalls anymore; if you can chat with a
friend, you can also SSH to their machine.

%package service
Summary:        Tool to connect to telepathy IM contacts via SSH -- Server
Group:          Productivity/Networking/Instant Messenger

%description service
SSH-Contact is a client/service tool that makes it easy to connect to
your telepathy IM contacts via SSH. No need to care about dynamic IP,
NAT, port forwarding, or firewalls anymore; if you can chat with a
friend, you can also SSH to their machine.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-, root, root)
%doc README.openSUSE

%files client
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS
%{_bindir}/ssh-contact

%files service
%defattr(-, root, root)
%{_libexecdir}/ssh-contact-service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.SSHContact.service
%{_datadir}/telepathy/clients/SSHContact.client
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/clients

%changelog
