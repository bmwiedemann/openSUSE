#
# spec file for package yelp-xsl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.34.0
Release:        0
Summary:        XSL stylesheets for the yelp help browser
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Yelp
Source0:        https://download.gnome.org/sources/yelp-xsl/3.34/%{name}-%{version}.tar.xz

BuildRequires:  itstool >= 1.2.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
# The lang subpackage is obsoleted now that translationed are
# merged inline in xml file, since 3.1.1.
Obsoletes:      %{name}-lang < %{version}
BuildArch:      noarch

%description
This package contains XSL stylesheets that are used by the yelp help browser.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS
%{_datadir}/yelp-xsl/
# This needs to be observed. As long as it does not Require: anything
# we can probably leave it here without splitting a dummy -devel
# package for it.
%{_datadir}/pkgconfig/yelp-xsl.pc

%changelog
