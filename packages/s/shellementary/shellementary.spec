#
# spec file for package shellementary
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           shellementary
Version:        0.2.0
Release:        0
Summary:        EFL GUI application similar to zenity/kdialog
License:        MIT
Group:          System/X11/Utilities
Url:            http://enlightenment.org
Source:         %{name}-%{version}.tar.bz2
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         printf.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
#elementary eina >= 1.0.0 evas >= 1.0.0 ecore >= 1.0.0 ecore-file >= 1.0.
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ecore) >= 1.0.0
BuildRequires:  pkgconfig(ecore-file) >= 1.0.
BuildRequires:  pkgconfig(eina) >= 1.0.0
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(evas) >= 1.0.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Application providing GUI to shell scripts, similar to zenity/kdialog.

%prep
%setup -q
%patch0 -p3

%build
# Devs refuse to add autogen.sh to make dist tarball
#./autogen.sh
autoreconf -ifv
automake --add-missing --copy --gnu
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
%find_lang %{name}

%clean
%{?buildroot:rm -rf %{buildroot}}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README COPYING
%dir %{_datadir}/shellementary/
%{_bindir}/*
%{_datadir}/shellementary/*

%changelog
