#
# spec file for package cosmic-session
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           cosmic-session
Version:        1.0.0+0
Release:        0
Summary:        Session manager for the COSMIC desktop environment
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-session
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        %{name}.dconf
BuildRequires:  cargo-packaging
BuildRequires:  dconf
BuildRequires:  just
Requires:       switcheroo-control

%description
%{summary}.

%prep
%autosetup -a1

%build
just build

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%check
%{cargo_test}

%files
%license LICENSE.md
%dir %{_datadir}/dconf
%dir %{_datadir}/dconf/profile
%dir %{_datadir}/wayland-sessions
%{_bindir}/%{name}
%{_bindir}/start-cosmic
%{_datadir}/applications/cosmic-mimeapps.list
%{_datadir}/dconf/profile/cosmic
%{_datadir}/wayland-sessions/cosmic.desktop
%{_prefix}/lib/systemd/user/cosmic-session.target

%changelog
