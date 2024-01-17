#
# spec file for package profile-sync-daemon
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2013-2020 Artem Polishchuk & Christopher Meng
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


%global shortname psd
Name:           profile-sync-daemon
Version:        6.48
Release:        0
Summary:        Symlinks and syncs browser profile dirs to RAM thus reducing HDD/SDD calls
License:        MIT
URL:            https://github.com/graysky2/profile-sync-daemon
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  rsync
BuildRequires:  systemd-rpm-macros
BuildRequires:  zsh
Requires:       rsync
BuildArch:      noarch

%description
Profile-sync-daemon (psd) is a tiny pseudo-daemon designed to manage your
browser's profile in tmpfs and to periodically sync it back to your physical
disc (HDD/SSD). This is accomplished via a symlinking step and an innovative
use of rsync to maintain back-up and synchronization between the two. One of
the major design goals of psd is a completely transparent user experience.

%package        zsh-completion
Summary:        zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)

%description    zsh-completion
zsh completion for %{name}.

%prep
%autosetup -p1


%build
%make_build


%install
%make_install
%fdupes %{buildroot}/%{_datadir}/%{shortname}/


%post
%{systemd_user_post %{shortname}.service}

%preun
%{systemd_user_preun %{shortname}.service}

%postun
%{systemd_user_postun_with_restart %{shortname}.service}

%files
%doc README.md
%license MIT LICENSE
%{_bindir}/%{name}
%{_bindir}/%{shortname}
%{_bindir}/%{shortname}-overlay-helper
%{_bindir}/%{shortname}-suspend-sync
%{_datadir}/%{shortname}/
%{_mandir}/man1/*.1%{?ext_man}
%{_userunitdir}/*.{service,timer}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{shortname}

%changelog
