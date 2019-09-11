#
# spec file for package pkgdiff
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pkgdiff
Version:        1.7.2
Release:        0
Summary:        Package Changes Analyzer
License:        GPL-2.0
Group:          Development/Tools/Other
Url:            https://github.com/lvc/pkgdiff
Source:         https://github.com/lvc/pkgdiff/archive/%{version}.tar.gz#/%{name}-%{version}.tar.xz
BuildRequires:  help2man
BuildRequires:  make
Requires:       awk
Requires:       binutils
Requires:       diff
Requires:       perl-base >= 5.8
Requires:       wdiff
Suggests:       abi-compliance-checker
Suggests:       abi-dumper
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A tool for visualizing changes in Linux software packages (RPM, DEB, TAR.GZ, etc).
The tool is intended for Linux maintainers who are interested in ensuring
compatibility of old and new versions of packages.

%prep
%setup -q

%build
chmod 0755 %{name}.pl

%install
mkdir -vp %{buildroot}%{_prefix}
env \
	"DESTDIR=%{buildroot}"  \
	perl Makefile.pl -install \
	--prefix=%{_prefix}
# Generate man page with help2man
mkdir -p %{buildroot}%{_mandir}/man1
ln -s %{name}.pl %{name}
help2man -N -o %{name}.1 ./%{name}
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc LICENSE README doc
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*

%changelog
