#
# spec file for package zypp-boot-plugin
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.0.6
Release:        0
Summary:        Zypp plugin for checking if a reboot is needed
License:        AGPL-3.0-or-later
Group:          System/Packages
URL:            https://github.com/openSUSE/zypp-boot-plugin
Source:         zypp-boot-plugin-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  libeconf-devel
BuildRequires:  libjson-c-devel
BuildRequires:  boost-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  grep
BuildRequires:  xsltproc
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  libzypp(plugin:commit)

Requires:       libzypp(plugin:commit) = 1
Recommends:     grep

%description
This package contains a plugin for zypp that checks if a reboot is needed after
package installation/update.

%prep
%setup -q

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
