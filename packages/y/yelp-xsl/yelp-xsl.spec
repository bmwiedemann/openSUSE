#
# spec file for package yelp-xsl
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands.
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


Name:           yelp-xsl
Version:        42.1
Release:        0
Summary:        XSL stylesheets for the yelp help browser
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Yelp
Source0:        https://download.gnome.org/sources/yelp-xsl/42/%{name}-%{version}.tar.xz
Source99:       yelp-xsl-rpmlintrc

BuildRequires:  itstool >= 1.2.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildArch:      noarch

%description
This package contains XSL stylesheets that are used by the yelp help browser.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/yelp-xsl/
%{_datadir}/pkgconfig/yelp-xsl.pc

%changelog
