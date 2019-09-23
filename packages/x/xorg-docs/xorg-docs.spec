#
# spec file for package xorg-docs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xorg-docs
Version:        1.7.1
Release:        0
Summary:        Miscellaneous documentation for the X Window System
License:        MIT
Group:          Documentation/Other
Url:            http://xorg.freedesktop.org/
Source:         %{name}-%{version}.tar.bz2
Patch0:         reproducable_build.patch
# For xmlto txt support
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xorg-sgml-doctools >= 1.11
# Can be used if we want ps/pdf output
#BuildRequires:  xmlgraphics-fop
BuildRequires:  xmlto >= 0.0.20
BuildRequires:  pkgconfig(xorg-macros) >= 1.10
# Package was named xorg-x11-doc until 12.2
# We use 7.7 for Provides/Obsoletes, since we're renaming the packages when
# X11R7.7 is in RC1, and xorg-x11-doc was version 7.6
Provides:       xorg-x11-doc = 7.7
Obsoletes:      xorg-x11-doc < 7.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides miscellaneous documentation for the X Window
System that doesn't better fit into other packages.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/xorg-docs/
%{_mandir}/man7/Consortium.7%{?ext_man}
%{_mandir}/man7/Standards.7%{?ext_man}
%{_mandir}/man7/X.7%{?ext_man}
%{_mandir}/man7/XOrgFoundation.7%{?ext_man}
%{_mandir}/man7/XProjectTeam.7%{?ext_man}
%{_mandir}/man7/Xsecurity.7%{?ext_man}

%changelog
