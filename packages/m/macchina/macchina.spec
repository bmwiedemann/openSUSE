#
# spec file for package macchina
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


Name:           macchina
Version:        6.1.6
Release:        0
Summary:        Fast, minimal and customizable system information frontend
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/Macchina-CLI/macchina#macchina
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
Recommends:     wmctrl
ExcludeArch:    armv7l
ExcludeArch:    i586

%description
macchina lets you view system information, like your kernel version, uptime, memory usage, processor load and much more

%prep
%setup -q
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}
strip target/release/%{name}

%install
%{cargo_install}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m0644 -t %{buildroot}%{_datadir}/%{name} %{name}.toml

%check
%ifarch "x86_64"
%{cargo_test}
%else
true # Skipping tests on other archs than x86_64 due to SIGSEGV on arm64
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/%{name}/%{name}.toml
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
