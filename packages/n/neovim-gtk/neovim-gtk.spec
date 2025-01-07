#
# spec file for package neovim-gtk
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


%define         _name nvim-gtk
%define         appid com.github.Lyude.neovim-gtk
Name:           neovim-gtk
Version:        1.0.1+196
Release:        0
Summary:        GTK UI for Neovim
License:        GPL-3.0-only
URL:            https://github.com/Lyude/neovim-gtk
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(pango)

%description
GTK UI for Neovim written in Rust using gtk-rs bindings. With ligatures
support.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -Dm0755 ./target/release/%{_name} %{buildroot}%{_bindir}/%{_name}
%make_build DESTDIR=%{buildroot} PREFIX=%{_prefix} install-resources

%check
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/%{_name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/{128x128,48x48}/apps/%{appid}.png
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/%{_name}

%changelog
