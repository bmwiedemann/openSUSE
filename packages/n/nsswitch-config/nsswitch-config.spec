#
# spec file for package nsswitch-config
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

Name:           nsswitch-config
Version:        0.0.5
Release:        0
Summary:        Handling nsswitch.conf entries
License:        GPL-2.0-or-later
URL:            https://github.com/schubi2/nsswitch-config.git
Source:         nsswitch-config-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig(libeconf) >= 0.8.0

%description
Tool which merges different nsswitch configuration file snippets into one single
nsswitch.conf file, which is normally located in the /etc directory.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%{_bindir}/nsswitch-config
%{_mandir}/man8/*.8%{?ext_man}
%license COPYING

%changelog
