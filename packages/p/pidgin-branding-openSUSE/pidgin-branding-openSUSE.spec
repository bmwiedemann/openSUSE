#
# spec file for package pidgin-branding-openSUSE
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libpurple_version %(rpm -q --queryformat '%%{version}' libpurple)
Name:           pidgin-branding-openSUSE
Version:        42.2
Release:        0
Summary:        Multiprotocol Instant Messaging Client -- openSUSE Default Configuration
License:        BSD-3-Clause
Group:          Productivity/Networking/Instant Messenger
Url:            https://pidgin.im/
Source0:        %{name}-prefs.xml
Source1:        %{name}-COPYING
BuildRequires:  libpurple
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%else
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif

%description
Pidgin is a messaging application which lets you log in to accounts
on multiple chat networks simultaneously.

Pidgin is compatible with the following chat networks out of the
box: Jabber/XMPP, AIM, ICQ, Bonjour, Gadu-Gadu, IRC, SILC, SIMPLE,
Novell GroupWise Messenger, Lotus Sametime, MXit, MySpaceIM, and
Zephyr. It can support many more with plugins.

This package provides the openSUSE default configuration for Pidgin.

%package -n libpurple-branding-openSUSE
Summary:        GLib-based Instant Messenger Library -- openSUSE Default Configuration
Group:          System/Libraries
Requires:       libpurple = %{libpurple_version}
Supplements:    packageand(libpurple:branding-openSUSE)
Conflicts:      otherproviders(libpurple-branding)
Provides:       libpurple-branding = %{libpurple_version}
# pidgin-branding-openSUSE was last used in openSUSE 11.4.
Provides:       pidgin-branding-openSUSE = %{version}
Obsoletes:      pidgin-branding-openSUSE < %{version}

%description -n libpurple-branding-openSUSE
libpurple is a library intended to be used by programmers seeking
to write an IM client that connects to many IM networks.

libpurple is compatible with the following chat networks out of the
box: Jabber/XMPP, AIM, ICQ, Bonjour, Gadu-Gadu, IRC, SILC, SIMPLE,
Novell GroupWise Messenger, Lotus Sametime, MXit, MySpaceIM, and
Zephyr. It can support many more with plugins.

This package provides the openSUSE default configuration for libpurple.

%prep
%setup -q -T -c
cp -a %{SOURCE0} prefs.xml
cp -a %{SOURCE1} COPYING

%build
# Nothing to build.

%install
install -Dpm 0644 prefs.xml %{buildroot}%{_sysconfdir}/purple/prefs.xml

%files -n libpurple-branding-openSUSE
%defattr(-,root,root)
%doc COPYING
%config %{_sysconfdir}/purple/prefs.xml

%changelog
