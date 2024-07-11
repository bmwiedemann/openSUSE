#
# spec file for package cosmic-ext-bg-theme
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


Name:           cosmic-ext-bg-theme
Version:        0.1.0+git20240603.9945b3d
Release:        0
Summary:        COSMIC daemon for adapting theme to the wallpaper
License:        GPL-3.0-only
URL:            https://github.com/wash2/cosmic_bg_theme
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        %{name}.service
BuildRequires:  cargo-packaging
BuildRequires:  make

%description
Unofficial service for syncing COSMIC theme with the active wallpaper.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -Dm0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 %{SOURCE2} %{buildroot}%{_userunitdir}/%{name}.service

%preun %service_del_preun %{name}.service

%postun %service_del_postun %{name}.service

%pre %service_add_pre %{name}.service

%post %service_add_post %{name}.service

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
