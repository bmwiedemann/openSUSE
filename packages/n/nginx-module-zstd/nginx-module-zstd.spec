#
# spec file for package nginx-module-zstd
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


Name:           nginx-module-zstd
Version:        0~g23
Release:        0
Summary:        NGINX module for Zstandard compression
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/tokers/zstd-nginx-module
Source:         %name-%version.tar.xz
BuildRequires:  nginx-source
BuildRequires:  pkgconfig(libzstd)
%ngx_conditionals
%ngx_requires

%description
This is a nginx module to enable Zstd (de)compression on HTTP streams.

Zstd, short for Zstandard, is a lossless compression algorithm. Speed
vs. compression trade-off is configurable in small increments.

%prep
%autosetup -p1
cp -r %_prefix/src/nginx .

%build
cd nginx
export CFLAGS="-Wno-error"
%ngx_configure --add-dynamic-module=..
%make_build modules

%install
mkdir -p %buildroot/%ngx_module_dir
install -Dpm0755 nginx/objs/ngx_http_zstd*_module.so %buildroot%ngx_module_dir

%files
%license LICENSE
%doc *.md
%ngx_module_dir/ngx*.so

%changelog
