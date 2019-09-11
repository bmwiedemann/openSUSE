#
# spec file for package pidgin-xmpp-receipts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname  xmpp-receipts
Name:           pidgin-xmpp-receipts
Version:        0.8
Release:        0
Summary:        Implementation of XMPP message delivery receipts for Pidgin
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/noonien-d/pidgin-xmpp-receipts
Source:         https://github.com/noonien-d/pidgin-xmpp-receipts/archive/release_%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(pidgin)

%description
This plugin for Pidgin implements XMPP message delivery receipts (XEP-0184).

%package -n pidgin-plugin-xmpp-receipts
Summary:        Implementation of XMPP message delivery receipts for Pidgin
Group:          Productivity/Networking/Instant Messenger
%requires_ge    pidgin
# pidgin-xmpp-receipts was last used in openSUSE Leap 42.2.
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n pidgin-plugin-xmpp-receipts
This plugin for Pidgin implements XMPP message delivery receipts (XEP-0184).

%prep
%setup -q -n %{name}-release_%{version}

%build
make %{?_smp_mflags} V=1

%install
%make_install \
  PLUGINDIR="%{_libdir}/pidgin"

%files -n pidgin-plugin-xmpp-receipts
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc README
%{_libdir}/pidgin/%{soname}.so

%changelog
