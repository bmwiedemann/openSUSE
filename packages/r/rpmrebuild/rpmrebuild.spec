#
# spec file for package rpmrebuild
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


Name:           rpmrebuild
Version:        2.15
Release:        0
Summary:        A tool to build a rpm file from the rpm database
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            http://rpmrebuild.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Patch1:         gpl-license.patch
Patch2:         gpl-COPYRIGHT-address.patch
Patch3:         rpmrebuild-fix-bashisms.patch
Requires:       bash
Requires:       coreutils
Requires:       cpio
Requires:       rpm-build
Requires:       sed
BuildArch:      noarch

%description
rpmrebuild allows to build an rpm file from an installed rpm, or from
another rpm file, with or without changes (batch or interactive). It
can be extended by a plugin system. A typical use is to easy repackage
a software after some configuration's change.

%prep
%setup -q -c
%autopatch -p1

%build
make %{?_smp_mflags}
# Remove shebang on script that are sourced and not executed
find . -iname "*.src" -exec sed -i 's,^#!%{_bindir}/env bash,,g' {} \;
# As in 2.15 remove env usage to static path
find . -iname "*.sh" -exec sed -i 's,^#!%{_bindir}/env bash,#!%{_bindir}/sh,g' {} \;
# Same for those
find . -iname "*.sh" -exec sed -i 's,^#!%{_bindir}/env sh,#!%{_bindir}/sh,g' {} \;
# and last
sed -i 's,^#!%{_bindir}/env sh,#!%{_bindir}/sh,g' rpmrebuild

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mv %{buildroot}%{_mandir}/fr_FR.UTF-8/ %{buildroot}%{_mandir}/fr
rm -rf %{buildroot}%{_mandir}/fr_FR/
# chmod 0755 %%{buildroot}%%{_libexecdir}/rpmrebuild/*.sh

%files
%defattr(-,root,root,-)
%license COPYING COPYRIGHT
%doc AUTHORS Changelog News README Todo
%{_bindir}/rpmrebuild
%{_prefix}/lib/rpmrebuild
%{_mandir}/fr/man1/*
%{_mandir}/man1/*

%changelog
