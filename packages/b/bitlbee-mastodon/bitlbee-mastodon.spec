#
# spec file for package bitlbee-mastodon
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


Name:           bitlbee-mastodon
Version:        1.4.5
Release:        0
Summary:        A Mastodon plugin for Bitlbee
License:        GPL-2.0-only
Group:          Productivity/Networking/IRC
URL:            https://github.com/kensanata/bitlbee-mastodon
Source:         https://github.com/kensanata/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bitlbee)
BuildRequires:  pkgconfig(glib-2.0)

%description
This plugin allows Bitlbee to communicate with Mastodon instances.
Mastodon is a free, open-source, decentralized microblogging network.
Bitlbee is an IRC server connecting to various other text messaging
services. You run Bitlbee and connect to it using an IRC client, then
configure Bitlbee to connect to other services, such as a Mastodon
instance where you already have an account. The benefit is that you can
now use any IRC client you want to connect to Mastodon.

%prep
%setup -q

%build
sh ./autogen.sh
%configure
%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/bitlbee/mastodon.la

%files
%license LICENSE
%doc README.md RELEASE.md
%dir %{_libdir}/bitlbee
%{_libdir}/bitlbee/mastodon.so
%{_datadir}/bitlbee/mastodon-help.txt

%changelog
