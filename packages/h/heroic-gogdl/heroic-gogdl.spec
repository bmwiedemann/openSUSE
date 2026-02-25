#
# spec file for package heroic-gogdl
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           heroic-gogdl
Version:        1.2.1
Release:        0
Summary:        GOG download module for Heroic Games Launcher
License:        GPL-3.0-only
URL:            https://github.com/Heroic-Games-Launcher/heroic-gogdl
Source0:        %{name}-%{version}.tar.gz
Patch0:         use-system-xdelta3.patch
BuildRequires:  python3-PyInstaller
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests < 3.0
Requires:       xdelta3
%ifarch aarch64
ExclusiveArch: aarch64
%endif
%ifarch x86_64
ExclusiveArch: x86_64
%endif

%description
GOG Downloading module for Heroic Games Launcher

%prep
%autosetup -p1

%build
pyinstaller --onefile --name gogdl gogdl/cli.py

%install
install -Dm0755 dist/gogdl %{buildroot}/%{_bindir}/gogdl

%files
%license LICENSE*
%{_bindir}/gogdl

%changelog
