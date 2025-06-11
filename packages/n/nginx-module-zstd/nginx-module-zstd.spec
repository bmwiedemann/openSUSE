#
# spec file for package nginx-module-zstd
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


Name:           nginx-module-zstd
Version:        0.1.1
Release:        0
Summary:        NGINX module for Zstandard compression
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/tokers/zstd-nginx-module
Source:         https://github.com/tokers/zstd-nginx-module/archive/refs/tags/%version.tar.gz
BuildRequires:  nginx-source
BuildRequires:  pkgconfig(libzstd)
%ngx_conditionals
%ngx_requires

%description
This is a nginx module to enable Zstd (de)compression on HTTP streams.

Zstd, short for Zstandard, is a lossless compression algorithm. Speed
vs. compression trade-off is configurable in small increments.

%prep
%autosetup -p1 -n zstd-nginx-module-%version
cp -r %_prefix/src/nginx .

%build
cd nginx
export CFLAGS="-Wno-error"
%ngx_configure --add-dynamic-module=..
%make_build modules

%install
b="%buildroot"
mkdir -p "$b/%ngx_module_dir" "$b/%_datadir/nginx/modules"
install -Dpm0755 nginx/objs/ngx_http_zstd*_module.so "$b/%ngx_module_dir/"
cat >"$b/%_datadir/nginx/modules/mod-zstd.conf" <<-EOF
	load_module %ngx_module_dir/ngx_http_zstd_filter_module.so;
	load_module %ngx_module_dir/ngx_http_zstd_static_module.so;
EOF

%files
%license LICENSE
%doc *.md
%ngx_module_dir/ngx*.so
%_datadir/nginx/

%changelog
