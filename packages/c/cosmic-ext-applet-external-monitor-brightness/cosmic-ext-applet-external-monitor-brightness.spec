#
# spec file for package cosmic-ext-applet-external-monitor-brightness
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


%define         appname io.github.maciekk64.CosmicExtAppletExternalMonitorBrightness
Name:           cosmic-ext-applet-external-monitor-brightness
Version:        0.1.0+git20240704.13b212d
Release:        0
Summary:        Applet for adjusting external monitors
License:        GPL-3.0-only
URL:            https://github.com/maciekk64/cosmic-ext-applet-external-monitor-brightness
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xkbcommon)

%description
A small applet for adjusting external monitors. Utilising the DDC/CI protocol.

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

%changelog
