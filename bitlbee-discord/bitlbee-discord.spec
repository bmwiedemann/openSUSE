#
# spec file for package bitlbee-discord
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           bitlbee-discord
Version:        0.4.2
Release:        0
Summary:        Bitlbee plugin for Discord
License:        GPL-2.0-only
Group:          Productivity/Networking/IRC
URL:            https://github.com/sm00th/bitlbee-discord
Source:         https://github.com/sm00th/bitlbee-discord/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bitlbee)

%description
Bitlbee plugin for Discord.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/bitlbee/discord.la

%files
%license LICENSE
%doc README
%dir %{_libdir}/bitlbee
%{_libdir}/bitlbee/discord.so
%{_datadir}/bitlbee/discord-help.txt

%changelog
