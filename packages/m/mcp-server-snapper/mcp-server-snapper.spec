#
# spec file for package mcp-server-snapper
#
# Copyright (c) 2026 SUSE LLC
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

Name:           mcp-server-snapper
Version:        0.3.0
Release:        0
Summary:        MCP Server for Snapper
License:        MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/aschnell/mcp-server-snapper
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.25
Requires:       snapper

%description
An MCP server for Snapper.

%prep
%setup -q -a 1
cp vendor/github.com/godbus/dbus/v5/LICENSE LICENSE-dbus
cp vendor/golang.org/x/sys/LICENSE LICENSE-sys
cp vendor/github.com/modelcontextprotocol/go-sdk/LICENSE LICENSE-mcp
cp vendor/github.com/google/jsonschema-go/LICENSE LICENSE-jsonschema
cp vendor/github.com/yosida95/uritemplate/v3/LICENSE LICENSE-uritemplate
cp vendor/github.com/segmentio/encoding/LICENSE LICENSE-encoding
cp vendor/github.com/segmentio/asm/LICENSE LICENSE-asm
cp vendor/golang.org/x/oauth2/LICENSE LICENSE-oauth2
cp vendor/golang.org/x/sync/LICENSE LICENSE-sync
cp vendor/golang.org/x/time/LICENSE LICENSE-time

%build
./build.sh

%check
for test in tools/tools ; do
    echo "Running $test..."
    MCPSERVER=src/mcp-server-snapper "testsuite/$test" || { echo "Test $test failed!" ; exit 1; }
done

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 src/mcp-server-snapper %{buildroot}%{_bindir}/mcp-server-snapper

install -d -m 0755 %{buildroot}%{_prefix}/lib/mcp-server-snapper/testsuite
install -m 0644 testsuite/README %{buildroot}%{_prefix}/lib/mcp-server-snapper/testsuite/README

for prog in create-snapshot-1 create-snapshot-2 create-snapshot-3 get-config list-configs list-snapshots rollback tools; do
    install -d -m 0755 %{buildroot}%{_prefix}/lib/mcp-server-snapper/testsuite/$prog
    install -m 0755 testsuite/$prog/$prog %{buildroot}%{_prefix}/lib/mcp-server-snapper/testsuite/$prog/$prog
    install -m 0644 testsuite/$prog/README %{buildroot}%{_prefix}/lib/mcp-server-snapper/testsuite/$prog/README
done

%files
%license LICENSE
%license LICENSE-dbus
%license LICENSE-sys
%license LICENSE-mcp
%license LICENSE-jsonschema
%license LICENSE-uritemplate
%license LICENSE-encoding
%license LICENSE-asm
%license LICENSE-oauth2
%license LICENSE-sync
%license LICENSE-time

%doc README.md
%{_bindir}/mcp-server-snapper

%package testsuite
Summary:        Testsuite for package %{name}
Requires:       %{name}

%description testsuite
Testsuite for package %{name}

Note: This package is for testing purposes only. It is intended for
use by quality assurance and requires a dedicated testing environment.

Do not install on a production system!

%files testsuite
%{_prefix}/lib/mcp-server-snapper/

%changelog
