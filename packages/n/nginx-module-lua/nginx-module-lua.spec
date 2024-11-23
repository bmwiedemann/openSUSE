#
# spec file for package nginx-module-lua
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


%define project_name lua-nginx-module
%define so_name ngx_http_lua_module.so
Name:           nginx-module-lua
Version:        0.10.27
Release:        0
Summary:        Embed the power of Lua into Nginx HTTP Servers
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/openresty/%{project_name}
Source0:        https://github.com/openresty/%{project_name}/archive/refs/tags/v%{version}.tar.gz#/%{project_name}-%{version}.tar.gz
BuildRequires:  nginx-source
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(luajit2)
Requires:       lua-resty-core
Requires:       lua-resty-lrucache
Recommends:     lua-resty-mysql
Recommends:     lua-resty-redis
Recommends:     lua51-cjson
Recommends:     luajit2
%{ngx_conditionals}
%{ngx_requires}

%description
This module embeds LuaJIT 2.1 into Nginx. It is a core component of OpenResty.
Used to handle requests to upstream services such as MySQL, Redis and other services.

%prep
mkdir %{project_name}
tar -xzf %{SOURCE0} --strip-components=1 -C %{project_name}
cp -r %{_prefix}/src/nginx .

%build
export LUAJIT_INC=%{_includedir}/luajit2-2.1
export LUAJIT_LIB=%{_libdir}
sed -i s/luajit-5.1/luajit2-5.1/g %{project_name}/config
cd nginx
%{ngx_configure} --add-dynamic-module=../%{project_name}
%make_build modules

%install
mkdir -p %{buildroot}%{ngx_module_dir}
install -Dpm0644 nginx/objs/%{so_name} %{buildroot}%{ngx_module_dir}

%files
%doc %{project_name}/README.markdown
%{ngx_module_dir}/%{so_name}

%changelog
