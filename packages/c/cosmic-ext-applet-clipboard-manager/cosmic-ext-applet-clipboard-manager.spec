#
# spec file for package cosmic-ext-applet-clipboard-manager
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


%define         appname io.github.wiiznokes.cosmic-ext-applet-clipboard-manager
Name:           cosmic-ext-applet-clipboard-manager
Version:        0.1.0+git20241008.f349d15
Release:        0
Summary:        Clipboard manager for COSMIC
License:        GPL-3.0-only
URL:            https://github.com/wiiznokes/clipboard-manager
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xkbcommon)

%description
The goal is to make a simple yet fast clipboard history, with a focus on UX,
rapidity and security.

Currently support storing the history on disk, search, delete

%prep
%autosetup -a1

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%suse_update_desktop_file %{appname}

%if 0%{?suse_version} >= 1600
mkdir -p %{buildroot}%{_distconfdir}/profile.d
mv %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh \
   %{buildroot}%{_distconfdir}/profile.d/%{name}.sh
%endif

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}-symbolic.svg

%if 0%{?suse_version} >= 1600
%{_distconfdir}/profile.d/%{name}.sh
%else
%{_sysconfdir}/profile.d/%{name}.sh
%endif

%changelog
