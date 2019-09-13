#
# spec file for package neofetch
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           neofetch
Version:        6.1.0
Release:        0
Summary:        CLI system information tool written in BASH
License:        MIT
Group:          Productivity/Text/Utilities
Url:            https://github.com/dylanaraps/neofetch
Source0:        https://github.com/dylanaraps/%{name}/archive/%{version}.tar.gz
# PATCH-FIX-SUSE Fix E: env-script-interpreter
Patch0:         fix-shebang.patch
Recommends:     maim
Recommends:     w3m-inline-image
BuildArch:      noarch

%description
Displays information about the system next to an image, the OS logo, or any
ASCII file of choice. The main purpose of Neofetch is to be used in
screenshots to show other users what OS/Distro is running, what Theme/Icons
are being used, etc.

Customizable through the use of command line flags or the user config file.
There are over 50 config options to mess around with and there's the `print_info()
function and friends which let you add your own custom info.

%prep
%setup -q
%patch0 -p1

%build
# Placeholder, no build required.

%install
%make_install

%files
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
