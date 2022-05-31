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
Version:        1.3.0
Release:        0
Summary:        Use any linux distribution inside your terminal
License:        GPL-3.0
URL:            https://github.com/89luca89/distrobox
Source:         distrobox-%{version}.tar.gz
Source1:        distrobox.conf
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
%setup -q -n distrobox-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/distrobox
mkdir -p %{buildroot}%{_docdir}/%{name}
./install --prefix %{buildroot}/%{_prefix}
install -m 0644 docs/*.md %{buildroot}%{_docdir}/%{name}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/distrobox/distrobox.conf

%files
%license COPYING.md
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/%{name}-*.1.gz
%config %{_sysconfdir}/distrobox
%config %{_sysconfdir}/distrobox/distrobox.conf

%changelog
