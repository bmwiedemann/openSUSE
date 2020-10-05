#
# spec file for package discord-rpc
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           discord-rpc
Version:        3.4.0
Release:        0
Summary:        Discord rich presence library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/discordapp/discord-rpc
Source:         https://github.com/discordapp/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rapidjson-devel

%description
This is a library for interfacing your game with a locally running Discord
desktop client.

%package -n libdiscord-rpc
Summary:        Discord RPC library
Group:          System/Libraries
Recommends:     discord

%description -n libdiscord-rpc
Discord RPC shared library

%package devel
Summary:        Development files for libdiscord-rpc
Requires:       libdiscord-rpc = %{version}

%description devel
Header files for the discord-rpc library

%prep
%setup -q

%build
%cmake

%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/discord_register.h
%{_includedir}/discord_rpc.h

%files -n libdiscord-rpc
%{_libdir}/libdiscord-rpc.so

%changelog

