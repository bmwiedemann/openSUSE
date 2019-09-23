#
# spec file for package xorg-sgml-doctools
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           xorg-sgml-doctools
Version:        1.11
Release:        0
License:        MIT
Summary:        Set of SGML entities and XML/CSS style sheets for building X.org documentation
Url:            http://xorg.freedesktop.org/
Group:          Development/Tools/Building
Source0:        http://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
# This was part of the xorg-x11-util-devel package up to version 7.6
Conflicts:      xorg-x11-util-devel <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides a common set of SGML entities and XML/CSS style
sheets used in building/formatting the documentation provided in other
X.Org packages.

%prep
%setup -q

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING README
%{_datadir}/sgml/X11/
%{_datadir}/pkgconfig/xorg-sgml-doctools.pc

%changelog
