#
# spec file for package dualsensectl
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


Name:           dualsensectl
Version:        0.7
Release:        3%{?dist}
Summary:        Tool for controlling PlayStation 5 DualSense controllers on Linux
License:        GPL-2.0
URL:            https://github.com/nowrep/%{name}
Source0:        https://github.com/nowrep/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/nowrep/%{name}/refs/heads/main/README.md
Source2:        https://raw.githubusercontent.com/nowrep/%{name}/refs/heads/main/LICENSE

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)

%description
DualSense Control [DualSenseCTL] is a tool for controlling Sony PlayStation 5 DualSense controllers on Linux.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

install -Dm644 "%{_builddir}/%{name}-%{version}/completion/%{name}" -t "%{buildroot}/%{_datadir}/bash-completion/completions/"
install -Dm644 "%{_builddir}/%{name}-%{version}/completion/_%{name}"   "%{buildroot}/%{_datadir}/zsh/site-functions/%{name}"

%files
%license "LICENSE"

%doc     "README.md"

      %{_bindir}/%{name}

%dir "%{_datadir}/bash-completion/"
%dir "%{_datadir}/bash-completion/completions/"
     "%{_datadir}/bash-completion/completions/%{name}"

%dir "%{_datadir}/zsh/"
%dir "%{_datadir}/zsh/site-functions/"
     "%{_datadir}/zsh/site-functions/%{name}"

%changelog
