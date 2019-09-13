#
# spec file for package dssi
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           dssi
Version:        1.1.1
Release:        0
Summary:        Disposable Soft Synth Interface
License:        GPL-2.0+ and LGPL-2.1+ and SUSE-Public-Domain
Group:          Development/Libraries/C and C++
Url:            http://dssi.sf.net/
Source:         http://downloads.sourceforge.net/project/dssi/dssi/1.1.1/%{name}-%{version}.tar.gz
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         dssi-add-missing-closedir.diff
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         dssi-linking.patch
BuildRequires:  alsa-devel
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  libjack-devel
BuildRequires:  liblo-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Disposable Soft Synth Interface (DSSI, pronounced "dizzy") is a
proposal for a plug-in API for software instruments (soft synths) with
user interfaces, permitting them to be hosted in-process by Linux audio
applications. Think of it as LADSPA-for-instruments or something
comparable to a simpler version of VSTi.

%package devel
Summary:        Development Package for DSSI plugins
Group:          Development/Libraries/C and C++
# note: dssi-devel doesn't require dssi itself; this contains just
# a header and a pkgconfig file.
Requires:       glibc-devel
Requires:       ladspa-devel

%description devel
This package contains files to be needed for building DSSI plugins.

%prep
%setup -q
%patch0 -p1
%patch1

%build
mkdir m4
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/dssi/*.la
make -C examples clean
rm -rf examples/.deps
rm -f examples/.cvsignore

%files
%defattr(-,root,root)
%doc COPYING README
%doc examples
%dir %{_libdir}/dssi
%{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/dssi

%files devel
%defattr(-,root,root)
%{_includedir}/dssi.h
%{_libdir}/pkgconfig/*.pc

%changelog
