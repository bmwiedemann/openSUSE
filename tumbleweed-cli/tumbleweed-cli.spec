#
# spec file for package tumbleweed-cli
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           tumbleweed-cli
Version:        0.3.3
Release:        0
Summary:        Command line interface for interacting with tumbleweed snapshots
License:        GPL-2.0-only
Group:          System/Packages
Url:            https://github.com/boombatower/tumbleweed-cli
Source:         %{name}-%{version}.tar.xz
BuildArch:      noarch
# see https://github.com/steamtricks/steamtricks/issues/27
Requires:       coreutils
Requires:       curl
Requires:       grep
Requires:       sudo
Requires:       zypper
Requires:       libzypp(repovarexpand) >= 1

%description
tumbleweed-cli provides a command line interface for interacting with tumbleweed
snapshots.

%prep
%setup -q

%build

%install
%make_install VERSION="%{version}"

%files
%defattr(-,root,root,-)
%{_bindir}/tumbleweed
%{_sysconfdir}/bash_completion.d/tumbleweed-completion.bash

%changelog
