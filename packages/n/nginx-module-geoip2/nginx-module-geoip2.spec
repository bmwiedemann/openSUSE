#
# spec file for package nginx-module-geoip2
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


%define project_name ngx_http_geoip2_module
Name:           nginx-module-geoip2
Version:        3.4
Release:        0
Summary:        NGINX Maxmind GeoIP2 support
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/leev/%{project_name}
Source0:        https://github.com/leev/%{project_name}/archive/%{version}.tar.gz#/%{project_name}-%{version}.tar.gz
BuildRequires:  nginx-source
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmaxminddb)
Provides:       nginx:%{ngx_module_dir}/ngx_http_geoip2_module.so
Provides:       nginx:%{ngx_module_dir}/ngx_stream_geoip2_module.so
%{ngx_conditionals}
%{ngx_requires}

%description
Creates variables with values from the maxmind geoip2 databases based on the client IP (IPv4 or IPv6).

%prep
mkdir %{project_name}
tar -xzf %{SOURCE0} --strip-components=1 -C %{project_name}
cp -r %{_prefix}/src/nginx .

%build
cd nginx
%{ngx_configure} --add-dynamic-module=../%{project_name}
%make_build modules

%install
install -Dpm0755 nginx/objs/ngx_http_geoip2_module.so %{buildroot}%{ngx_module_dir}/ngx_http_geoip2_module.so
install -Dpm0755 nginx/objs/ngx_stream_geoip2_module.so %{buildroot}%{ngx_module_dir}/ngx_stream_geoip2_module.so

%files
%license %{project_name}/LICENSE
%doc %{project_name}/README.md
%{ngx_module_dir}/ngx_http_geoip2_module.so
%{ngx_module_dir}/ngx_stream_geoip2_module.so

%changelog
