#
# spec file for package nbping
#
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


Name:           nbping
Version:        0.5.0
Release:        0
Summary:        A ping tool with real-time data and visualizations
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/hanshuaikang/Nping
Source:         Nping-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
A ping tool with real-time data and visualizations.

Features
 * Supports concurrent Ping for multiple addresses..
 * Supports visual latency display.
 * Real-time display of maximum, minimum, average latency, packet
   loss rate, and other metrics.
 * Support IPv4 and IPv6.
 * Supports concurrent pinging of n ip's under one address.
 * Support output results to files.

%prep
%autosetup -a 1 -n Nping-%{version}

%build
%{cargo_build}

%install
%{cargo_install}
# next version will be named "nbping"
#  https://github.com/hanshuaikang/Nping/issues/62#issuecomment-3483448009
mv %{buildroot}%{_bindir}/nping %{buildroot}%{_bindir}/nbping

%check
#%%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/nbping

%changelog
