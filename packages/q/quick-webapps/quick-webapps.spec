#
# spec file for package quick-webapps
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


%define         appname io.github.elevenhsoft.WebApps
Name:           quick-webapps
Version:        0.5.4a+2
Release:        0
Summary:        Web App Manager written with love and libcosmic
License:        GPL-3.0-only
URL:            https://github.com/cosmic-utils/web-apps
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       papirus-icon-theme

%description
Web App Manager for the COSMIC DE written with love and libcosmic.
Allows you to simply create web applications from given url working
inside separate window of your browser of choice.

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
%{_datadir}/icons/hicolor/??x??/apps/%{appname}.png
%{_datadir}/icons/hicolor/???x???/apps/%{appname}.png
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
