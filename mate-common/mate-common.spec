#
# spec file for package mate-common
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version 1.22
Name:           mate-common
Version:        1.22.0
Release:        0
Summary:        Common scripts and macros to develop with MATE
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         http://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
# Upstream source distribution requires execution of 'autogen.sh';
# mate-common is a requirement, while this doesn't change we pull
# all the necessary stuff from here so we won't polute other specs.
Requires:       autoconf
Requires:       automake
Requires:       gettext
Requires:       intltool >= 0.50.1
Requires:       libtool
Requires:       pkgconfig
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk-doc)
BuildArch:      noarch

%description
mate-common is an extension to autoconf, automake and libtool for
the MATE desktop environment and MATE applications. mate-autogen,
and several macros are included to help in MATE source trees.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%license COPYING
%doc AUTHORS
%{_bindir}/mate-doc-common
%{_bindir}/mate-autogen
%{_datadir}/aclocal/mate-code-coverage.m4
%{_datadir}/aclocal/mate-common.m4
%{_datadir}/aclocal/mate-compiler-flags.m4
%{_datadir}/mate-common/
%{_mandir}/man?/mate-autogen.?%{?ext_man}
%{_mandir}/man?/mate-doc-common.?%{?ext_man}

%changelog
