#
# spec file for package debhelper
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           debhelper
Version:        9.20150101
Release:        0
Summary:        Helper programs for debian/rules
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            http://kitenet.net/~joey/code/debhelper/
# http://ftp.de.debian.org/debian/pool/main/d/debhelper/
Source0:        debhelper_%{version}.tar.gz
# PATCH-FIX-UPSTREAM not build translated-manpages.
Patch0:         debhelper-9.20150101-no-localized-manpages.patch
# PATCH-FIX-UPSTREAM remove --utf8 since we only build En manpages.
Patch1:         debhelper-pod2man-no-utf8.patch
Requires:       dpkg
%if 0%{?suse_version}
Requires:       perl = %{perl_version}
%endif
Provides:       deb:%{_bindir}/dh_install
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A collection of programs that can be used in a debian/rules file to
automate common tasks related to building debian packages. Programs
are included to install various files into your package, compress
files, fix file permissions, integrate your package with the debian
menu system, debconf, doc-base, etc. Most debian packages use debhelper
as part of their build process.

%prep
%setup -q -n %{name}

%patch0 -p1
%if 0%{?suse_version} && 0%{?suse_version} < 1130
%patch1 -p1
%endif

%build
make %{?_smp_mflags} VERSION='%{version}'

%install
# autoscripts
install -d -m 755 %{buildroot}%{_datadir}/debhelper/autoscripts
install -m 644 autoscripts/* %{buildroot}%{_datadir}/debhelper/autoscripts
# perl modules:
install -d -m 755 %{buildroot}%{perl_vendorlib}/Debian/Debhelper
install -d -m 755 %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Sequence
install -d -m 755 %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Buildsystem
install -m 644 Debian/Debhelper/Buildsystem/*.pm %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Buildsystem
install -m 644 Debian/Debhelper/Sequence/*.pm %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Sequence
install -m 644 Debian/Debhelper/*.pm %{buildroot}%{perl_vendorlib}/Debian/Debhelper
# man pages:
install -d -m 755 %{buildroot}%{_mandir}/man1
install -d -m 755 %{buildroot}%{_mandir}/man7
install -m 644 *.1 %{buildroot}%{_mandir}/man1
install -m 644 debhelper.7 %{buildroot}%{_mandir}/man7
# binaries:
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 dh_*[^1-9] %{buildroot}%{_bindir}
install -m 755 dh %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%doc doc/* examples/* debian/changelog debian/copyright
%doc %{_mandir}/man*/*
%{_bindir}/*
%{_datadir}/debhelper
%{perl_vendorlib}/Debian

%changelog
