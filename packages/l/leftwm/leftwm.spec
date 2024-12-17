#
# spec file for package leftwm
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


Name:           leftwm
Version:        0.5.3
Release:        0
Summary:        A tiling window manager for adventurers
License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR MPL-2.0) AND BSD-2-Clause AND BSD-3-Clause AND (MIT OR Unlicense)
Group:          System/GUI/Other
URL:            https://github.com/leftwm/leftwm
Source0:        https://github.com/leftwm/leftwm/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}-rpmlintrc
BuildRequires:  cargo >= 1.74
BuildRequires:  cargo-packaging
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  zstd
Recommends:     xorg-x11-server
Suggests:       polybar
Suggests:       lemonbar
Suggests:       rofi
Suggests:       dunst

%description
LeftWM is a tiling window manager written in Rust that aims to be stable and performant.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_datadir}
install -D -d -m 0755 %{buildroot}%{_datadir}/xsessions
install -D -d -m 0755 %{buildroot}%{_mandir}
install -D -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 %{name}/doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/xsessions/%{name}.desktop

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name}-worker %{buildroot}%{_bindir}/%{name}-worker
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name}-state %{buildroot}%{_bindir}/%{name}-state
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name}-command %{buildroot}%{_bindir}/%{name}-command
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name}-check %{buildroot}%{_bindir}/%{name}-check
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/lefthk-worker %{buildroot}%{_bindir}/lefthk-worker

%files
%license LICENSE.md
%doc README.md CONTRIBUTING.md CHANGELOG.md themes
%{_bindir}/leftwm
%{_bindir}/leftwm-worker
%{_bindir}/leftwm-state
%{_bindir}/leftwm-check
%{_bindir}/leftwm-command
%{_bindir}/lefthk-worker
%{_datadir}/xsessions/leftwm.desktop
%{_mandir}/man1/leftwm.1%{?ext_man}

%changelog
