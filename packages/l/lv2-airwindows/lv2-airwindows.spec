# spec file for package lv2-airwindows
#
# Copyright (c) 2022 Fabio Pesari
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/

Name:          lv2-airwindows
Version:       18.0
Release:       0
Summary:       LV2 port of the Airwindows plugins
License:       MIT
Group:         Productivity/Multimedia/Sound/Editors and Convertors
URL:           https://github.com/hannesbraun/airwindows-lv2
Source0:       %{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(lv2)

%description

This is an LV2 port (by Hannes Braun) of the Airwindows plugins 
originally developed by Chris Johnson. 

Right now, only 84 plugins (out of 329) have been ported to LV2.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md NOTES.md
%license LICENSE
%dir %{_libdir}/lv2
%{_libdir}/lv2/*

%changelog
