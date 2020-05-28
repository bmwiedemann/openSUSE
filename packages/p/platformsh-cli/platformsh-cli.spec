#
# spec file for package platformsh-cli
#
# Copyright (c) 2020 SUSE LLC
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


Name:           platformsh-cli
Version:        3.56.4
Release:        0
Summary:        Tool for managing Platform.sh services from the command line
# See licenses.txt for dependency licenses.
License:        MIT
Group:          Productivity/Networking/Web/Servers
URL:            https://github.com/platformsh/platformsh-cli
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-vendor.tar.xz
Source10:       extensions.php
Source11:       extensions.txt
Source12:       licenses.txt
Source13:       update.sh
BuildRequires:  xz
Requires:       php >= 5.5.9
Suggests:       php-curl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Platform.sh CLI is the official command-line interface for Platform.sh.
Use this tool to interact with Platform.sh projects, and to build them
locally for development purposes.

%prep
# -a 1: unpack Source1 vendor tarball
%setup -q -a 1

%build
find . -name ".travis.yml" -delete
sed -i 's/@version-placeholder@/%{version}/' config.yaml

%install
# install drush source
install -d -m 0755 . %{buildroot}%{_datadir}/%{name}
cp -r * %{buildroot}%{_datadir}/%{name}

# link to executable in bindir
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/bin/platform %{buildroot}%{_bindir}/platform

# link to bash complete script
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
ln -s %{_datadir}/%{name}/shell-config.rc %{buildroot}%{_sysconfdir}/bash_completion.d/platform.sh.complete.sh

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}
%{_bindir}/platform
%{_sysconfdir}/bash_completion.d/platform.sh.complete.sh

%changelog
