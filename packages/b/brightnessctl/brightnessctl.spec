#
# spec file for package brightnessctl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 R Tyler Croy <rtyler@brokenco.de>
# Copyright (c) 2016 Fabio Alessandro Locati <fale@fedoraproject.org>
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


Name:           brightnessctl
Version:        0.4
Release:        0
Summary:        Tool to read and control device brightness
License:        MIT
Group:          System/Management
URL:            https://github.com/Hummer12007/%{name}
Source:         https://github.com/Hummer12007/brightnessctl/archive/%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

%description
A utility to read and control the display brightness.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
export MODE="4755"
%make_build

%install
%make_install UDEVDIR=%{_udevrulesdir}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_udevrulesdir}/90-brightnessctl.rules
%{_mandir}/man1/brightnessctl.1%{?ext_man}

%changelog
