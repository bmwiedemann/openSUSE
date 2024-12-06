#
# spec file for package hurl
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


Name:           hurl
Version:        6.0.0
Release:        0
Summary:        Run and test HTTP requests with plain text
License:        Apache-2.0
URL:            https://github.com/Orange-OpenSource/hurl
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.77.2
BuildRequires:  cargo-packaging
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  zstd

# Test depdencies
BuildRequires:  python3-base
BuildRequires:  python3-Flask

ExcludeArch:    i586

%description
Hurl is a command line tool that runs HTTP requests defined in a simple plain
text format.

It can perform requests, capture values and evaluate queries on headers and
body response. Hurl is very versatile: it can be used for both fetching data
and testing HTTP sessions.

%prep
%autosetup -a 1 -p 1
mkdir -p .cargo

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
# start a local HTTP server for the tests
cd integration/hurl
mkdir -p build

echo -e "\n------------------ Starting server.py"
python3 server.py > build/server.log 2>&1 &

echo -e "\n------------------ Starting ssl/server.py (Self-signed certificate)"
python3 ssl/server.py 8001 ssl/server/cert.selfsigned.pem false > build/server-ssl-selfsigned.log 2>&1 &

echo -e "\n------------------ Starting ssl/server.py (Signed by CA)"
python3 ssl/server.py 8002 ssl/server/cert.pem false > build/server-ssl-signedbyca.log 2>&1 &

echo -e "\n------------------ Starting ssl/server.py (Self-signed certificate + Client certificate authentication)"
python3 ssl/server.py 8003 ssl/server/cert.selfsigned.pem true > build/server-ssl-client-authent.log 2>&1 &

echo -e "\n------------------ Starting unix_socket/server.py"
python3 unix_socket/server.py > build/server-unix-socket.log 2>&1 &

# run the tests
%{cargo_test}

%files
%doc README.md
%license LICENSE
%{_bindir}/hurl

%changelog
