#
# spec file for package lsb-release
#
# Copyright (c) 2022 SUSE LLC
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


Name:           lsb-release
Version:        3.2
Release:        0
Summary:        Linux Standard Base Release Tools
License:        GPL-2.0-or-later
Group:          System/Fhs
URL:            https://github.com/thkukuk/lsb-release_os-release
Source:         https://github.com/thkukuk/lsb-release_os-release/archive/refs/tags/v%{version}.tar.gz#/lsb-release-%{version}.tar.gz
BuildArch:      noarch

%description
Tools from the Linux Standard Base project to determine the used distribution

%prep
%setup -q -n lsb-release_os-release-%{version}

%build
make

%install
make install INSTALL_ROOT=%{buildroot}%{_prefix}

%files
%license COPYING
%{_bindir}/lsb?release
%{_mandir}/man1/lsb?release.1%{?ext_man}

%changelog
