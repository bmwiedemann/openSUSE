#
# spec file for package xfr
#
# Copyright (c) 2026, Martin Hauke <mardnh@gmx.de>
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


Name:           xfr
Version:        0.9.3
Release:        0
Summary:        Network bandwidth testing tool with TUI
License:        Apache-2.0 OR MIT
URL:            https://github.com/lance0/xfr
#Git-Clone:     https://github.com/lance0/xfr.git
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
A fast, modern network bandwidth testing tool with TUI.

Features:
- Live TUI with real-time throughput graphs and per-stream stats
- Server dashboard - xfr serve --tui for monitoring active tests
- Multi-client server - handle multiple simultaneous tests
- TCP and UDP with configurable bitrate and parallel streams
- Bidirectional testing - measure upload and download simultaneously
- Multiple output formats - plain text, JSON, JSON streaming, CSV
- Result comparison - xfr diff to detect performance regressions
- LAN discovery - find xfr servers with mDNS (xfr discover)
- Prometheus metrics - export stats for monitoring dashboards
- Config file - save defaults in ~/.config/xfr/config.toml
- Environment variables - XFR_PORT, XFR_DURATION overrides

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{_bindir}/xfr

%changelog
