#
# spec file for package holodev
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           holodev
Version:        0.9
Release:        0
Summary:        Tool for creating Debian Linux containers
License:        GPL-2.0+
Group:          Development/Tools/Other
Url:            https://github.com/lappis-tools/holodev
Source0:        https://github.com/lappis-tools/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  bridge-utils
BuildRequires:  dnsmasq
BuildRequires:  ebtables
BuildRequires:  git
BuildRequires:  lxc
BuildRequires:  shunit2
BuildRequires:  sudo
Requires:       bash-completion
Requires:       debootstrap
Requires:       bridge-utils
Requires:       git
Requires:       libvirt >= 1.3.2
Requires:       lxc
Requires:       sudo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A tool to facilitate the creation of Linux containers for developing Debian
systems.

%prep
%autosetup -n %{name}-%{version}

%build

%check
make test-minimal

%install
# install holodev binary
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 holodev %{buildroot}%{_bindir}/holodev

# install holodev bash-completion
install -d -m 0755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 0644 -T debian/holodev.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/holodev.bash-completion

%post
holodev setup

%files
%defattr(-,root,root)
%doc README.md
%config %{_sysconfdir}/bash_completion.d/holodev.bash-completion
%{_bindir}/holodev

%changelog
