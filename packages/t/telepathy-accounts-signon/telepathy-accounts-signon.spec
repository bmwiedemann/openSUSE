#
# spec file for package telepathy-accounts-signon
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           telepathy-accounts-signon
Version:        2.0
Release:        0
Summary:        A mission control plugin for Telepathy
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://gitlab.com/accounts-sso/telepathy-accounts-signon
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libsignon-glib-devel
BuildRequires:  meson
BuildRequires:  telepathy-mission-control-devel

%description
A mission control plugin for Telepathy, integrating with libaccounts and libsignon
to provide IM accounts and authentication. This code is based on Nemo Mobile's
fork of the plugin from Empathy's ubuntu-online-account support.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.LGPL
%doc README.md
%{_libdir}/mission-control-plugins.0/mcp-account-manager-accounts-sso.so

%changelog
