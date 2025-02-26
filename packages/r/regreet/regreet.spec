#
# spec file for package regreet
#
# Copyright (c) 2025 SUSE LLC
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


Name:           regreet
Version:        0.2.0
Release:        0
Summary:        Customizable greeter for greetd
License:        CC0-1.0 AND GPL-3.0-or-later AND MIT
URL:            https://github.com/rharish101/ReGreet
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}.tmpfile
Source3:        %{name}.service
Source4:        %{name}.toml
BuildRequires:  cargo-packaging
BuildRequires:  greetd
BuildRequires:  rust >= 1.70
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(pango)
Requires:       greetd
Recommends:     adwaita-icon-theme
Recommends:     cantarell-fonts

%description
A customizable GTK-based greetd greeter written in Rust using Relm4.
This is meant to be run under a Wayland compositor (like Sway).

%prep
%autosetup -a1 -n ReGreet-%{version}

%build
%{cargo_build} --all-features

%install
install -Dm0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dm0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -Dm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/greetd/%{name}.toml

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%check
%{cargo_test}

%files
%license LICENSES/*
%doc README.md
%config(noreplace) %{_sysconfdir}/greetd/%{name}.toml
%{_bindir}/%{name}
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service

%changelog
