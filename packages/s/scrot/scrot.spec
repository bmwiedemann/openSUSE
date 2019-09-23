#
# spec file for package scrot
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           scrot
Version:        0.8
Release:        0
Summary:        Screenshot Capture Utility
License:        SUSE-Scrot
Group:          Productivity/Graphics/Other
Url:            http://linuxbrit.co.uk/scrot/
Source:         http://linuxbrit.co.uk/downloads/scrot-%{version}.tar.gz
#Patch set from debian
Patch1:         01_manpagefix.patch
Patch2:         02_options.c.patch
Patch3:         003_descmanpage.patch
Patch4:         04-focused.patch
Patch5:         05-addfocusedmanpage.patch
Patch6:         06_manpagespace.patch
Patch7:         07_fix-formatstring.patch
Patch8:         08_fix-beeping.patch
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(giblib)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(zlib)
Requires:       imlib2-loaders
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A nice and straightforward screen capture utility implementing
the dynamic loaders of imlib2.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# SED-FIX-FIX-OPENSUSE -- Fix paths
sed -i -e 's|$(prefix)/doc/scrot|%{_defaultdocdir}/%{name}|' Makefile.in

# SED-FIX-FIX-OPENSUSE -- Fix includes
sed -i -e 's|/usr/X11R6/include|-I$(prefix)/include|' src/Makefile.in

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
