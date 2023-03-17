#
# spec file for package lua-copas
#
# Copyright (c) 2023 SUSE LLC
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


%define flavor @BUILD_FLAVOR@
%define mod_name copas
%define upversion 2.0.2
Version:        2.0.2
Release:        0
Summary:        Coroutine Oriented Portable Asynchronous Services
License:        MIT
URL:            https://lunarmodules.github.io/copas
Source:         https://github.com/lunarmodules/%{mod_name}/archive/%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-coxpcall
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luasec
BuildRequires:  %{flavor}-luasocket
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-copas
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-copas
%endif

%description
Copas is a dispatcher based on coroutines that can be used by TCP/IP
servers. It uses LuaSocket as the interface with the TCP/IP stack.
A server registered with Copas should provide a handler for requests and
use Copas socket functions to send the response. Copas loops through
requests and invokes the corresponding handlers. For a full
implementation of a Copas HTTP server you can refer to Xavante as an
example.

%prep
%setup -q -n %{mod_name}-%{upversion}

%build
/bin/true

%install
%make_install PREFIX=%{_prefix} LUA_DIR=%{lua_noarchdir}

%check
# make %%{?_smp_mflags} test

%files
%license LICENSE
%doc README.md
%{lua_noarchdir}/%{mod_name}*

%changelog
