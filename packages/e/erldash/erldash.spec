#
# spec file for package erldash
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


Name:           erldash
Version:        0.1.2~0
Release:        0
Summary:        A simple, terminal-based Erlang dashboard
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/sile/erldash
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
Requires:       erlang >= 23.0
ExclusiveArch:  %{rust_tier1_arches}

%description
A simple, terminal-based Erlang dashboard.
erldash connects to an Erlang node using the dynamic node name feature (since OTP-23) to collect metrics.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%{_bindir}/erldash

%changelog
