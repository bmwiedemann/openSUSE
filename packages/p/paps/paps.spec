#
# spec file for package paps
#
# Copyright (c) 2020 SUSE LLC
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


Name:           paps
Version:        0.7.1
Release:        0
Summary:        A text to postscript converter through pango 
License:        LGPL-2.0-only
Group:          System/Base
URL:            https://github.com/dov/%{name}
Source:         https://github.com/dov/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch1:         paps-cpi_scale_calculation.patch
Patch2:         paps-manpage_units.patch
Patch3:         paps-manpage_fixes.patch
Patch4:         paps-gutter-width.patch
Patch5:         paps-page_setup.patch
Patch6:         paps-layout.patch
Patch7:         paps-glib.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
paps is a command line program for converting Unicode text encoded in UTF-8 to postscript and pdf by using pango.

%prep
%setup -qT -b0 -n %{name}-%{version}
%patch1 -p0 -b .p1
%patch2 -p0 -b .p2
%patch3 -p0 -b .p3
%patch4 -p0 -b .p4
%patch5 -p0 -b .p5
%patch6 -p0 -b .p6
%patch7 -p0 -b .p7
mkdir -p config m4
for c in /usr/share/aclocal*/{codeset,gettext,glibc21,iconv,isc-posix,lcmessage}.m4
do
    test -e $c || continue
    cp -p $c m4/
done
for c in /usr/share/automake*/config.{guess,sub}
do
    test -e $c || continue
    cp -p $c .
done
unset c

%build
echo "no" | glib-gettextize --force --copy
intltoolize --copy --force --automake
autoreconf --force --install -I config -I m4
automake --copy --force-missing --add-missing
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%files
%defattr(-,root,root)
%license COPYING.LIB
%{_bindir}/*
%{_mandir}/*/*

%changelog
