#
# spec file for package cosmic-ext-applet-emoji-selector
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


%define         appname dev.dominiccgeh.CosmicAppletEmojiSelector
Name:           cosmic-ext-applet-emoji-selector
Version:        0.1.5+git20240819.13c0a7e
Release:        0
Summary:        Emoji Selector for COSMIC DE
License:        MIT AND MPL-2.0
URL:            https://github.com/leb-kuchen/emoji-selector-applet-for-cosmic_tm
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%suse_update_desktop_file %{appname}

%check
%{cargo_test}

%files
%license LICENSE-MPL-2 LICENSE-MIT
%doc ATTRIBUTION.md README.md DEPENDENCIES.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/dev.dominiccgeh.{CosmicAppletEmojiSelector,black-flag-icon,emotion-satisfied,food-and-drink-icon,food,international-travel-and-tourism,objects-column,people-nearby,pets,symbols,walking,world-1}.svg
%{_datadir}/%{appname}

%changelog
