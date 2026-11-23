#
# spec file for package hurl
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


Name:           hurl
Version:        8.1.0
Release:        0
Summary:        Run and test HTTP requests with plain text
License:        Apache-2.0
URL:            https://github.com/Orange-OpenSource/hurl
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch0:         hurl-lower-rust-version-dependency.patch
BuildRequires:  cargo >= 1.98
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
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
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/hurlfmt %{buildroot}%{_bindir}/hurlfmt

install -D -m 0644 docs/manual/hurl.1 %{buildroot}%{_mandir}/man1/hurl.1
install -D -m 0644 docs/manual/hurlfmt.1 %{buildroot}%{_mandir}/man1/hurlfmt.1
install -D -m 0644 completions/hurl.bash %{buildroot}/%{_datadir}/bash-completion/completions/hurl
install -D -m 0644 completions/hurlfmt.bash %{buildroot}/%{_datadir}/bash-completion/completions/hurlfmt
install -D -m 0644 completions/hurl.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/hurl.fish
install -D -m 0644 completions/hurlfmt.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/hurlfmt.fish
install -D -m 0644 completions/_hurl %{buildroot}/%{_datadir}/zsh/site-functions/_hurl
install -D -m 0644 completions/_hurlfmt %{buildroot}/%{_datadir}/zsh/site-functions/_hurlfmt

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
%{cargo_test} -- --skip simple_sample --skip runner::hurl_file::run

%files
%doc README.md
%license LICENSE
%{_bindir}/hurl
%{_bindir}/hurlfmt
%{_mandir}/man1/hurl.1%{?ext_man}
%{_mandir}/man1/hurlfmt.1%{?ext_man}
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/hurl
%{_datadir}/bash-completion/completions/hurlfmt
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/hurl.fish
%{_datadir}/fish/vendor_completions.d/hurlfmt.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_hurl
%{_datadir}/zsh/site-functions/_hurlfmt

%changelog
