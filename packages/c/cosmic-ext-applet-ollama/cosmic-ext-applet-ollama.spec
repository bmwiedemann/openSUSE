#
# spec file for package cosmic-ext-applet-ollama
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


%define         appname io.github.elevenhsoft.CosmicExtAppletOllama
Name:           cosmic-ext-applet-ollama
Version:        0.1.0+git20240923.45bc56d
Release:        0
Summary:        Ollama applet for COSMIC Desktop
License:        GPL-3.0-only
URL:            https://github.com/elevenhsoft/cosmic-ext-applet-ollama
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       ollama

%description
This software integrates ollama into a small neat applet for easier access
on the COSMIC Desktop Environment

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
%{_datadir}/icons/hicolor/scalable/apps/%{appname}-symbolic.svg

%changelog
