#
# spec file for package debhelper
#
# Copyright (c) 2025 SUSE LLC
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


Name:           debhelper
Version:        13.23
Release:        0
Summary:        Helper programs for debian/rules
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://salsa.debian.org/debian/debhelper
Source0:        https://salsa.debian.org/debian/debhelper/-/archive/debian/%{version}/%{name}-debian-%{version}.tar.gz
# PATCH-FIX-UPSTREAM not build translated-manpages.
Patch0:         debhelper-no-localized-manpages.patch
# PATCH-FIX-UPSTREAM remove --utf8 since we only build En manpages.
Patch1:         debhelper-pod2man-no-utf8.patch
# PATCH-FIX-UPSTREAM debhelper-fix-perl-version-requirement.patch https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1001403
Patch2:         debhelper-fix-perl-version-requirement.patch
BuildRequires:  dpkg-devel >= 1.18
BuildRequires:  perl-Test-Pod
Requires:       dh-autoreconf >= 17
Requires:       dpkg >= 1.18
Requires:       strip-nondeterminism
Provides:       deb:%{_bindir}/dh_install
BuildArch:      noarch
%if 0%{?suse_version}
Requires:       perl = %{perl_version}
%endif

%description
A collection of programs that can be used in a debian/rules file to
automate common tasks related to building debian packages. Programs
are included to install various files into your package, compress
files, fix file permissions, integrate your package with the debian
menu system, debconf, doc-base, etc. Most debian packages use debhelper
as part of their build process.

%prep
%setup -q -n %{name}-debian-%{version}

%patch -P 0 -p1
%if 0%{?suse_version} && 0%{?suse_version} < 1130
%patch -P 1 -p1
%endif
%if 0%{?suse_version} < 1600
%patch -P 2 -p0
%endif

%build
%make_build VERSION='%{version}'

%check
%make_build test

%install
%make_install

# man pages:
install -d -m 755 %{buildroot}%{_mandir}/man1
install -d -m 755 %{buildroot}%{_mandir}/man7
install -m 644 *.1 %{buildroot}%{_mandir}/man1
install -m 644 debhelper.7 %{buildroot}%{_mandir}/man7

%files
%doc doc/* examples/* debian/changelog debian/copyright
%{_mandir}/man*/*
%{_bindir}/*
%{_datadir}/debhelper
%{perl_vendorlib}/Debian

%changelog
