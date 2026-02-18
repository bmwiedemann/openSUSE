#
# spec file for package nginx-module-acme
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           nginx-module-acme
Version:        0.3.1
Release:        0
Summary:        NGINX module for automatic certificate management (ACMEv2)
License:        Apache-2.0
URL:            https://github.com/nginx/nginx-acme
Source0:        https://github.com/nginx/nginx-acme/releases/download/v%{version}/nginx-acme-%{version}.tar.gz
Source1:        https://github.com/nginx/nginx-acme/releases/download/v%{version}/nginx-acme-%{version}.tar.gz.asc
Source2:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  nginx-source
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(libpcre2-posix)
ExclusiveArch:  %{rust_tier1_arches}
%{ngx_conditionals}
%{ngx_requires}

%description
Nginx-acme is an NGINX module implementation of the automatic
certificate management (ACMEv2) protocol.

The module implements the following specifications:

* RFC8555 (Automatic Certificate Management Environment) with
  limitations: Only HTTP-01 challenge type is supported
* RFC8737 (ACME TLS Application-Layer Protocol Negotiation (ALPN)
  Challenge Extension)
* RFC8738 (ACME IP Identifier Validation Extension)

%prep
%autosetup -a2 -n nginx-acme-%{version}
cp -a %{_prefix}/src/nginx .

%build
cd nginx
%{ngx_configure}
%make_build
cd ..

export NGINX_BUILD_DIR=$(realpath nginx/objs)
%{cargo_build}

%install
mkdir -p %{buildroot}/%{ngx_module_dir}
install -m 0644 target/release/libnginx_acme.so %{buildroot}/%{ngx_module_dir}/ngx_http_acme_module.so

%files
%license LICENSE
%doc *.md
%{ngx_module_dir}/*.so

%changelog
