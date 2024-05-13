#
# spec file for package lua-resty-websocket
#
# Copyright (c) 2024 SUSE LLC
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


%define lua_version 5.1
Name:           lua-resty-websocket
Version:        0.11
Release:        0
Summary:        Lua WebSocket implementation for the ngx_lua module
License:        BSD-2-Clause
URL:            https://github.com/openresty/lua-resty-websocket
Source0:        https://github.com/openresty/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  lua-macros
BuildArch:      noarch

%description
This Lua library implements a WebSocket server and client libraries based on the ngx_lua module.

%prep
%autosetup -p1

%build

%install
%make_install LUA_LIB_DIR=%{lua_noarchdir}

%files
%defattr(0644,root,root,-)
%doc README.markdown
%dir %{lua_noarchdir}
%{lua_noarchdir}/resty

%changelog
