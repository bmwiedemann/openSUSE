#
# spec file for package nginx-module-echo
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


%define project_name echo-nginx-module
%define so_name ngx_http_echo_module.so
Name:           nginx-module-echo
Version:        0.63
Release:        0
Summary:        NGINX echo module
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/openresty/%{project_name}
Source0:        https://github.com/openresty/%{project_name}/archive/refs/tags/v%{version}.tar.gz#/%{project_name}-%{version}.tar.gz
BuildRequires:  nginx-source
%{ngx_conditionals}
%{ngx_requires}

%description
Brings "echo", "sleep", "time", "exec" and more shell-style goodies to Nginx config file.

%prep
mkdir %{project_name}
tar -xzf %{SOURCE0} --strip-components=1 -C %{project_name}
cp -r %{_prefix}/src/nginx .

%build
cd nginx
%{ngx_configure} --add-dynamic-module=../%{project_name}
%make_build modules

%install
mkdir -p %{buildroot}%{ngx_module_dir}
install -Dpm0644 nginx/objs/%{so_name} %{buildroot}%{ngx_module_dir}

%files
%license %{project_name}/LICENSE
%doc %{project_name}/README.markdown
%{ngx_module_dir}/%{so_name}

%changelog
