#
# spec file for package nginx-module-rtmp
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


Name:           nginx-module-rtmp
Version:        1.2.2
Release:        0
Summary:        NGINX module for RTMP/HLS/DASH serving
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/arut/nginx-rtmp-module/
Source:         https://github.com/arut/nginx-rtmp-module/archive/refs/tags/v%version.tar.gz
BuildRequires:  nginx-source
%ngx_conditionals
%ngx_requires

%description

%prep
%autosetup -p1 -n nginx-rtmp-module-%version
cp -r %_prefix/src/nginx .

%build
cd nginx
export CFLAGS="-Wno-error"
%ngx_configure --add-dynamic-module=..
%make_build modules

%install
b="%buildroot"
mkdir -p "$b/%ngx_module_dir" "$b/%_datadir/nginx/modules"
install -Dpm0755 nginx/objs/ngx_rtmp_module.so "$b/%ngx_module_dir/"
cat >"$b/%_datadir/nginx/modules/mod-rtmp.conf" <<-EOF
	load_module %ngx_module_dir/ngx_rtmp_modules.so;
EOF

%files
%license LICENSE
%doc *.md
%ngx_module_dir/ngx*.so
%_datadir/nginx/

%changelog
