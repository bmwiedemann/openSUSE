#
# spec file for package nginx-module-brotli
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


Name:           nginx-module-brotli
Version:        1.0.0~rc+git9
Release:        0
Summary:        NGINX module for Brotli compression
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/google/ngx_brotli
Source:         %name-%version.tar.xz
BuildRequires:  libbrotli-devel
BuildRequires:  nginx-source
%ngx_conditionals
%ngx_requires

%description
ngx_brotli is a set of two nginx modules:

* ngx_brotli filter module - used to compress responses on-the-fly,
* ngx_brotli static module - used to serve pre-compressed files.

Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling.

%prep
%autosetup -p1
cp -r %_prefix/src/nginx .

%build
mkdir -p deps/brotli/c/include
ln -s /usr/include/brotli deps/brotli/c/include/

cd nginx
%ngx_configure --add-dynamic-module=..
%make_build modules

%install
b="%buildroot"
mkdir -p "$b/%ngx_module_dir" "$b/%_datadir/nginx/modules"
install -Dpm0755 nginx/objs/ngx_http_brotli*_module.so "$b/%ngx_module_dir/"
cat >"$b/%_datadir/nginx/modules/mod-brotli.conf" <<-EOF
	load_module %ngx_module_dir/ngx_http_brotli_filter_module.so;
	load_module %ngx_module_dir/ngx_http_brotli_static_module.so;
EOF

%files
%license LICENSE
%doc *.md
%ngx_module_dir/ngx_http_brotli_filter_module.so
%ngx_module_dir/ngx_http_brotli_static_module.so
%_datadir/nginx/

%changelog
