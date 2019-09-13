#
# spec file for package dh-autoreconf
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


Name:           dh-autoreconf
Version:        10
Release:        0
Summary:        Add-on for debhelper to call autoreconf and clean up after the build
License:        GPL-2.0+
Group:          System/Packages
Url:            http://www.debian.org
Source0:        http://ftp.de.debian.org/debian/pool/main/d/dh-autoreconf/%{name}_%{version}.tar.xz
BuildRequires:  debhelper
BuildRequires:  xz
Requires:       debhelper
%if 0%{?suse_version}
Requires:       perl = %{perl_version}
%endif
Provides:       deb:%{_bindir}/dh_autoreconf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
dh-autoreconf provides a debhelper sequence addon named 'autoreconf' and
two commands, dh_autoreconf and dh_autoreconf_clean.

The dh_autoreconf command creates a list of the files and their checksums,
calls autoreconf and then creates a second list for the new files.
 
The dh_autoreconf_clean command compares these two lists and removes all
files which have been added or changed (files may be excluded if needed).

For CDBS users, a rule is provided to call the dh-autoreconf programs at
the right time.

%prep
%setup

%build
pod2man -r "dh-autoreconf v%{version}" -c dh-autoreconf --section=1 dh_autoreconf dh_autoreconf.1
pod2man -r "dh-autoreconf v%{version}" -c dh-autoreconf --section=1 dh_autoreconf_clean dh_autoreconf_clean.1
pod2man -r "dh-autoreconf v%{version}" -c dh-autoreconf --section=7 dh-autoreconf.pod dh-autoreconf.7

%install
install -d %{buildroot}%{_bindir}
install -m 755 dh_autoreconf %{buildroot}%{_bindir}
install -m 755 dh_autoreconf_clean %{buildroot}%{_bindir}
install -d %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Sequence
install -m 644 autoreconf.pm %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Sequence
install -d %{buildroot}%{_datadir}/cdbs/1/rules/
install -m 644 autoreconf.mk %{buildroot}%{_datadir}/cdbs/1/rules
install -d %{buildroot}%{_datadir}/dh-autoreconf/
install -m 644 ltmain-as-needed.diff %{buildroot}%{_datadir}/dh-autoreconf/
install -d %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/man7
install -m 644 *.1 %{buildroot}%{_mandir}/man1
install -m 644 *.7 %{buildroot}%{_mandir}/man7

%files
%defattr(-,root,root)
%doc debian/changelog debian/copyright debian/NEWS
%doc %{_mandir}/man*/*
%{_bindir}/*
%{perl_vendorlib}/Debian/Debhelper/Sequence/*
%{_datadir}/cdbs/
%{_datadir}/dh-autoreconf/

%changelog
