#
# spec file for package abi-monitor
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           abi-monitor
Version:        1.12
Release:        0
Summary:        A tool to monitor and build new versions of a software library
License:        GPL-2.0-or-later OR LGPL-2.1-or-later
Url:            https://github.com/lvc/abi-monitor
Source:         https://github.com/lvc/abi-monitor/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  help2man
Requires:       curl
Requires:       perl-base >= 5.8
Requires:       wget
# Recommends only, supports BuildScript configuration
Recommends:     automake
Recommends:     cmake
Recommends:     gcc
Recommends:     gcc-c++
BuildArch:      noarch

%description
Monitor new versions of a software library, try to build them
and create profiles for abi-tracker

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
%doc GPL-2.0 LGPL-2.1 LICENSE README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*

%changelog
