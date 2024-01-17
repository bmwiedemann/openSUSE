#
# spec file for package telepathy-rakia
#
# Copyright (c) 2020 SUSE LLC
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


Name:           telepathy-rakia
Version:        0.8.0
Release:        0
Summary:        SIP connection manager for Telepathy
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://telepathy.freedesktop.org/wiki/Components
Source:         http://telepathy.freedesktop.org/releases/telepathy-rakia/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 1.patch dimstar@opensuse.org -- Fix build with python3
Patch0:         https://patch-diff.githubusercontent.com/raw/TelepathyIM/telepathy-rakia/pull/1.patch
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  sofia-sip-devel >= 1.12.11
BuildRequires:  telepathy-glib-devel >= 0.17.7
BuildRequires:  pkgconfig(glib-2.0) >= 2.16
Obsoletes:      telepathy-sofiasip < %{version}
Provides:       telepathy-sofiasip = %{version}

%description
IETF SIP connection manager for Telepathy using the SofiaSIP protocol
stack; formerly known as telepathy-sofiasip

%package devel
Summary:        SIP connection manager for Telepathy - development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
IETF SIP connection manager for Telepathy using the SofiaSIP protocol
stack.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.sofiasip.service
%{_datadir}/telepathy/
%{_libexecdir}/telepathy-rakia
%{_mandir}/man8/telepathy-rakia.8%{?ext_man}

%files devel
%{_includedir}/%{name}-0.7/

%changelog
