#
# spec file for package vmtouch
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

Name:           vmtouch
Version:        1.3.0
Release:        0
License:        BSD-3-Clause
Summary:        Portable file system cache diagnostics and control
Url:            http://hoytech.com/vmtouch/
Group:          System/Utilities
Source:         https://github.com/hoytech/vmtouch/archive/v%{version}.tar.gz#/vmtouch-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  perl
BuildRequires:  make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A tool for learning about and controlling the file system
cache of unix and unix-like systems.

%prep
%setup -q

%build
make CFLAGS="%{optflags} -std=gnu99"

%install
b=%{buildroot}
make PREFIX="$b"%{_prefix} MANDIR="$b"%{_mandir}/man8 install

%files
%defattr(-,root,root)
%doc CHANGES README.md TODO
%{_bindir}/vmtouch
%{_mandir}/man8/vmtouch.8%{ext_man}
