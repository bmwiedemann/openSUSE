#
# spec file for package steamtricks
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


Name:           steamtricks
Version:        0.3.1
Release:        0
Summary:        Workarounds for problems with Steam on Linux
License:        GPL-2.0-only
Group:          Amusements/Games/Other
URL:            https://steamtricks.github.io/steamtricks/
Source:         https://github.com/steamtricks/steamtricks/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  systemd-rpm-macros
# see https://github.com/steamtricks/steamtricks/issues/27
Requires:       coreutils
Requires:       findutils
Requires:       grep
Requires:       patch
Requires:       rpm
Requires:       sed
# steamtricksd.service file utilizes `script`
Requires:       util-linux
Requires:       which
Recommends:     ca-certificates-steamtricks
Recommends:     steamtricks-data
BuildArch:      noarch
%{?systemd_requires}

%description
steamtricks provides workarounds for problems with Steam on Linux.

Steam primarily targets Ubuntu and not the wider base of Linux distributions.
This has led to a number of suboptimal experiences for users not on an
officially supported distribution. The goal of this project is to
provide workarounds and solutions to those problems in an easy to use package.
Currently, workarounds exist in some distribution packages and in various forums
and the like. This project aims to be the upstream source for packaging Steam
fixes.

%prep
%autosetup

%build

%install
%make_install VERSION="%{version}"

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
# <= leap 42.1 does not provide _userunitdir
%if 0%{!?_userunitdir:1}
  %define _userunitdir %{_prefix}/lib/systemd/user
  %dir %{_prefix}/lib/systemd/user
%endif
%{_userunitdir}/%{name}d.service

%changelog
