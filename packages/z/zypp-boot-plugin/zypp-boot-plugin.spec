#
# spec file for package zypp-boot-plugin
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


Name:           zypp-boot-plugin
Version:        0.0.13
Release:        0
Summary:        Zypp plugin for checking if a reboot is needed
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/openSUSE/zypp-boot-plugin
Source:         zypp-boot-plugin-%{version}.tar.xz
# PATCH-FIX-UPSTREAM - remove system library which is headers only
Patch1:         https://github.com/openSUSE/zypp-boot-plugin/pull/8.patch
BuildRequires:  boost-devel > 1.69.0
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  grep
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libeconf-devel
BuildRequires:  libjson-c-devel
BuildRequires:  meson
BuildRequires:  xsltproc
BuildRequires:  libzypp(plugin:commit)

Requires:       libzypp(plugin:commit) = 1
Recommends:     grep

%description
This package contains a plugin for zypp that checks if a reboot is needed after
package installation/update.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%dir %{_distconfdir}/zypp
%{_distconfdir}/zypp/zypp-boot-plugin.conf
/usr/lib/zypp/plugins/commit/boot-plugin
%doc %{_mandir}/*/zypp-boot-plugin.8*

%changelog
