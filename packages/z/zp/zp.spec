#
# spec file for package zp
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


Name:           zp
Version:        0.2.0
Release:        0
Summary:        Shorter command of zypper
License:        GPL-3.0
Group:          System/Packages
URL:            https://github.com/openSUSE-zh/zp
Source:         https://github.com/openSUSE-zh/zp/archive/v%version.tar.gz
BuildArch:      noarch
Requires:       zypper

%description
A set of alias definitions (actually implemented using sh functions)
for zypper:

- zp: sudo zypper
- zi: sudo zypper install
- zr: sudo zypper remove
- zu: sudo zypper update (Leap) or sudo zypper dup (Tumbleweed)
- zs: sudo zypper search

Have a lot of fun...

%prep
%setup -q

%build

%install
install -Dpm0755 shorten-zypper.sh %{buildroot}/%{_sysconfdir}/profile.d/shorten-zypper.sh

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/profile.d/shorten-zypper.sh

%changelog
