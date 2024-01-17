#
# spec file for package dh-make
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


Name:           dh-make
Version:        1.20140617
Release:        0
Summary:        Tool that converts source archives into Debian package source
License:        SUSE-GPL-3.0-with-template-exception
Group:          System/Packages
Url:            http://www.debian.org
Source0:        http://ftp.de.debian.org/debian/pool/main/d/dh-make/dh-make_%{version}.tar.xz
Source99:       dh-make-rpmlintrc
BuildRequires:  debhelper
Requires:       debhelper
Requires:       dpkg
Requires:       perl
Provides:       deb:%{_bindir}/dh_make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package allows you to take a standard (or upstream) source package
and convert it into a format that will allow you to build Debian packages.

After answering a few questions, dh_make will then provide a set of
templates that, after some small editing, will allow you to create a
Debian package.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_bindir}
install -m 755 dh_make %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/debhelper/dh_make
mv lib/* %{buildroot}%{_datadir}/debhelper/dh_make/
install -d %{buildroot}%{_mandir}/man1
install -m 644 dh_make.1 %{buildroot}%{_mandir}/man1/

%files
%defattr(-,root,root)
%doc debian/changelog debian/copyright
%{_bindir}/dh_make
%{_datadir}/debhelper/dh_make
%{_mandir}/man1/dh_make.1.gz

%changelog
