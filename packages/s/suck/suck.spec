#
# spec file for package suck
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           suck
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  inn-devel
BuildRequires:  openssl-devel
Version:        4.3.4
Release:        0
Url:            https://github.com/lazarus-pkgs/suck
Summary:        Reading News Offline
License:        SUSE-Public-Domain
Group:          Productivity/Networking/News/Utilities
%{?libperl_requires}
Source:         https://github.com/lazarus-pkgs/%{name}/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Suck is a program used to grab news from a remote NNTP news server and
bring it to a local machine, without having the remote server do
anything special.

%prep
%setup -q

%build
autoreconf -fi
%configure --with-inn-lib=/usr/lib/news/lib/ --with-inn-include=/usr/lib/news/include/
# parallel building doesnt work
make

%install
%make_install DESTDIR="%{?buildroot}"

%files
%defattr(-,root,root)
/usr/bin/*
%doc %{_mandir}/man1/*

%changelog
