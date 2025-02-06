#
# spec file for package distrobox
#
# Copyright (c) 2025 SUSE LLC
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


Name:           distrobox
Version:        1.8.1.2
Release:        0
Summary:        Use any linux distribution inside your terminal
License:        GPL-3.0-only
URL:            https://github.com/89luca89/distrobox
Source:         https://github.com/89luca89/distrobox/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        distrobox.conf
Requires:       %{_bindir}/basename
Requires:       %{_bindir}/find
Requires:       %{_bindir}/grep
Requires:       %{_bindir}/sed
Requires:       (%{_bindir}/podman or %{_bindir}/docker)
# Idea would be: if bash completion is already there, let's have it. If
# not, let's "only" recommend it...
Requires:       (%{name}-bash-completion if bash-completion)
# For distrobox-exec to work properly, we need flatpak helper services (bsc#1220037)
Requires:       flatpak
BuildRequires:  ImageMagick
BuildRequires:  hicolor-icon-theme
BuildArch:      noarch

%description
Use any Linux distribution inside your terminal.
Distrobox uses podman or docker to create containers using the Linux distribution of your choice.
The created container will be tightly integrated with the host,
allowing sharing of the HOME directory of the user, external storage,
external USB devices and graphical apps (X11/Wayland), and audio.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for distrobox.

%prep
%autosetup -p1 -n distrobox-%{version}

%build

%install
./install --prefix %{buildroot}/%{_prefix}

install -d -m0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 docs/*.md %{buildroot}%{_docdir}/%{name}

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/distrobox
install -m 0644 %{SOURCE1} %{buildroot}%{_distconfdir}/distrobox/distrobox.conf
%else
mkdir -p %{buildroot}%{_sysconfdir}/distrobox
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/distrobox/distrobox.conf
%endif

%files
%license COPYING.md
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/%{name}-*.1.gz
%if 0%{?suse_version} > 1500
%dir %{_distconfdir}/distrobox
%{_distconfdir}/distrobox/distrobox.conf
%else
%config %{_sysconfdir}/distrobox
%config(noreplace) %{_sysconfdir}/distrobox/distrobox.conf
%endif
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/*x*/
%dir %{_datadir}/icons/hicolor/*x*/apps/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/icons/hicolor/*/apps/terminal-distrobox-icon.png
%{_datadir}/icons/hicolor/scalable/apps/terminal-distrobox-icon.svg
%{_datadir}/zsh/site-functions/_%{name}*

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}*

%changelog
