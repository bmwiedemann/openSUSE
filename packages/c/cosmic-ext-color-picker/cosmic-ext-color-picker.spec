#
# spec file for package cosmic-ext-color-picker
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


%define         appname me.pixeldoted.CosmicExtColorPicker
Name:           cosmic-ext-color-picker
Version:        0.1.0+git20240719.1e7eaff
Release:        0
Summary:        A Color Picker for COSMIC desktop
License:        GPL-3.0-only
# We use my fork, so we don't infringe on the trademark. I only change the name, rest is as is.
# https://github.com/rrahl0/cosmic-color-picker
URL:            https://github.com/PixelDoted/cosmic-color-picker
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary} Desktop Environment.

%prep
%autosetup -a1

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%suse_update_desktop_file %{appname}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{appname}.svg
%{_datadir}/icons/hicolor/???x???/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
