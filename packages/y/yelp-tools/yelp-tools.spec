#
# spec file for package yelp-tools
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


Name:           yelp-tools
Version:        42.1
Release:        0
Summary:        Collection of utilities to help create documentation
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://projects.gnome.org/yelp/
Source:         https://download.gnome.org/sources/yelp-tools/42/%{name}-%{version}.tar.xz
BuildRequires:  itstool
BuildRequires:  libxml2-tools
BuildRequires:  libxslt
BuildRequires:  meson >= 0.51.0
BuildRequires:  pkgconfig
BuildRequires:  python3-lxml
BuildRequires:  pkgconfig(yelp-xsl) >= 3.38.0
Requires:       itstool
Requires:       libxml2-tools
Requires:       libxslt
BuildArch:      noarch

%description
yelp-tools is a collection of scripts and build utilities to help create,
manage, and publish documentation for Yelp and the web. Most of the heavy
lifting is done by packages like yelp-xsl and itstool. This package just
wraps things up in a developer-friendly way.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/yelp-build
%{_bindir}/yelp-check
%{_bindir}/yelp-new
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/yelp.m4
%{_datadir}/yelp-tools/

%changelog
