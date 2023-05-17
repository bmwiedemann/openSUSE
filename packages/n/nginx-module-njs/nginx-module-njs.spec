#
# spec file for package nginx-module-njs
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


Name:           nginx-module-njs
Version:        0.7.12
Release:        0
Summary:        NGINX module for NGINX Javascript
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://nginx.org/en/docs/njs/
Source:         %name.tar.gz
BuildRequires:  nginx-source
%ngx_conditionals
%ngx_requires

%description
njs is a subset of the JavaScript language that allows extending
nginx functionality.

%prep
%autosetup -p1 -n %name
cp -r %_prefix/src/nginx .

%build
cd nginx
%ngx_configure --add-dynamic-module=.
%make_build modules

%install
mkdir -p %buildroot/%ngx_module_dir
install -Dpm0755 nginx/objs/ngx_http_js_module.so %buildroot/%ngx_module_dir
install -Dpm0755 nginx/objs/ngx_stream_js_module.so %buildroot/%ngx_module_dir

%files
%license LICENSE
%doc README CHANGES
%ngx_module_dir/ngx_http_js_module.so
%ngx_module_dir/ngx_stream_js_module.so

%changelog
