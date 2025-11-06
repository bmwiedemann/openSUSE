#
# spec file for package onedrive
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2018-2022 LISA GmbH, Bingen, Germany.
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


%{!?_userunitdir: %{expand: %%global _userunitdir %{_unitdir}/../user}}
%define docdir %{_defaultdocdir}/%{name}

# DMD is available only on x86*. Use LDC otherwise.
%ifarch %{ix86} x86_64
%bcond_without dcompiler_dmd
%else
%bcond_with dcompiler_dmd
%endif

Name:           onedrive
Version:        2.5.8
Release:        0
Summary:        Client for One Drive Service for Linux
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://github.com/abraunegg/onedrive/
Source0:        %{name}-%{version}.tar.xz
%if %{with dcompiler_dmd}
BuildRequires:  dmd >= 2.087.0
BuildRequires:  phobos-devel-static
%else
BuildRequires:  ldc >= 1.17.0
BuildRequires:  ldc-phobos-devel
%endif
BuildRequires:  help2man
BuildRequires:  libcurl-devel
BuildRequires:  libnotify-devel
BuildRequires:  sqlite3-devel
BuildRequires:  pkgconfig(dbus-1)
Requires:       libdbus-1-3
Requires:       libnotify4
Recommends:     logrotate
Suggests:       onedrive-completion-bash
Suggests:       onedrive-completion-zsh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package completion-bash
Summary:        OneDrive Bash completion
Group:          Productivity/Networking/Other
BuildRequires:  bash
BuildRequires:  bash-completion
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       bash
Requires:       bash-completion
Requires:       onedrive = %{version}
Supplements:    (%{name} and bash-completion)

%package completion-zsh
Summary:        OneDrive zsh completion
Group:          Productivity/Networking/Other
BuildRequires:  zsh
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)

%package completion-fish
Summary:        OneDrive fish completion
Group:          Productivity/Networking/Other
BuildRequires:  fish
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)

%description
OneDrive is a client for Microsoft file serving service

%description completion-bash
OneDrive shell completions for Bash.

%description completion-zsh
OneDrive shell completions for zsh.

%description completion-fish
OneDrive shell completions for fish.

%prep
%setup -q
sed -i 's/^docdir.*/docdir = @docdir@/g' Makefile.in

%build
%configure \
    --docdir=%{docdir} \
    --with-systemduserunitdir=%_userunitdir \
    --with-systemdsystemunitdir=%_unitdir \
    --enable-notifications \
    --enable-completions \
    --with-bash-completion-dir=%{_datarootdir}/bash-completion/completions/ \
    --with-zsh-completion-dir=%{_datarootdir}/zsh/site-functions/ \
    --with-fish-completion-dir=%{_datarootdir}/fish/vendor_completions.d/
make %{?_smp_mflags} %{name}

%install
%make_install
install -D -m 0644 config %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}
rm %{buildroot}%{_docdir}/%{name}/LICENSE

install -D -m 0644 readme.md %{buildroot}%{_docdir}/%{name}/readme.md
install -D -m 0644 changelog.md %{buildroot}%{_docdir}/%{name}/changelog.md

%pre
%service_add_pre %{name}@.service
%service_add_pre %{name}.service

%post
%service_add_post %{name}@.service
%service_add_post %{name}.service

%preun
%service_del_preun %{name}@.service
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}@.service
%service_del_postun %{name}.service

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/%{name}
%dir %{_userunitdir}
%{_userunitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%attr(0644, root, root) %{_mandir}/man1/%{name}.1*
%{_localstatedir}/log/%{name}
%dir %{_docdir}/%{name}
%{_docdir}/%{name}
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/places/
%{_datadir}/icons/hicolor/scalable/places/onedrive.svg

%files completion-bash
%{_datadir}/bash-completion/completions/

%files completion-zsh
%{_datarootdir}/zsh/site-functions/_onedrive

%files completion-fish
%{_datarootdir}/fish/vendor_completions.d/onedrive.fish

%changelog
