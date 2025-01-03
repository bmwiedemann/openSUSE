#
# spec file for package nginx-module-vts
#
# Copyright (c) 2025 SUSE LLC
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


%define project_name nginx-module-vts
Name:           nginx-module-vts
Version:        0.2.3
Release:        0
Summary:        Nginx virtual host traffic status module
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/vozlt/nginx-module-vts
Source:         https://github.com/vozlt/nginx-module-vts/archive/refs/tags/v%version.tar.gz
BuildRequires:  nginx-source
BuildRequires:  pcre-devel
%ngx_conditionals
%ngx_requires

%description
This is an Nginx module that provides access to virtual host status
information. It contains the current status such as servers, upstreams, caches.
This is similar to the live activity monitoring of nginx plus. The built-in html
is also taken from the demo page of old version.

%prep
%autosetup -p1
cp -r /usr/src/nginx .

%build
cd nginx
%ngx_configure --add-dynamic-module=..
%make_build modules

%install
mkdir -p %buildroot/%ngx_module_dir
install -D -m 0644 nginx/objs/ngx_http_vhost_traffic_status_module.so %buildroot/%ngx_module_dir

%files
%license LICENSE
%ngx_module_dir/*.so

%changelog
