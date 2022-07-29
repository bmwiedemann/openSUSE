#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.3.1
Release:        0
Summary:        Use any linux distribution inside your terminal
License:        GPL-3.0
URL:            https://github.com/89luca89/distrobox
Source:         distrobox-%{version}.tar.gz
Source1:        distrobox.conf
# Fix a problem with automatic rootful container creation (from upstream)
Patch1:         0001-enter-fix-automatic-container-creation-when-r-is-use.patch
# Fix a problem if man is there but actual manpages are stripped (from upstream PR)
Patch2:         0002-distrobox-handle-situations-with-weird-manpages-setu.patch
# Default to distrobox-enter when just distrobox is used
Patch3:         0003-distrobox-if-no-command-is-specified-default-to-ente.patch
# Read the config from vendor specific directory (/usr/etc/distrobox) too
Patch4:         0004-opensuse-check-for-the-config-file-in-usr-etc-too.patch
Requires:       %{_bindir}/basename
Requires:       %{_bindir}/find
Requires:       %{_bindir}/grep
Requires:       %{_bindir}/sed
Requires:       (%{_bindir}/podman or %{_bindir}/docker)
BuildArch:      noarch

%description
Use any Linux distribution inside your terminal.
Distrobox uses podman or docker to create containers using the Linux distribution of your choice.
The created container will be tightly integrated with the host,
allowing sharing of the HOME directory of the user, external storage,
external USB devices and graphical apps (X11/Wayland), and audio.

%prep
%autosetup -p1 -n distrobox-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}
./install --prefix %{buildroot}/%{_prefix}
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
%{_distconfdir}/distrobox
%else
%config %{_sysconfdir}/distrobox
%endif
%if 0%{?suse_version} > 1500
%{_distconfdir}/distrobox/distrobox.conf
%else
%config(noreplace) %{_sysconfdir}/distrobox/distrobox.conf
%endif
%changelog
