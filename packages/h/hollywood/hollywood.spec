#
# spec file for package hollywood
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


#

Name:           hollywood
Version:        1.21
Release:        0
Summary:        Program to fill the console with Hollywood melodrama technobabble
License:        Apache-2.0 AND CC0-1.0
Group:          Amusements/Toys/Other
URL:            https://launchpad.net/hollywood
Source:         https://launchpad.net/hollywood/trunk/%{version}/+download/hollywood_%{version}.orig.tar.gz#/%{name}-%{version}.tar.gz
Recommends:     byobu
Recommends:     apg
Recommends:     bmon
# in debian: bsdmainutils
Recommends:     util-linux
Recommends:     coreutils
Recommends:     ccze
Recommends:     cmatrix
Recommends:     htop
Recommends:     jp2a
Recommends:     mlocate
Requires:       moreutils
Recommends:     mplayer
Recommends:     openssh-client
Recommends:     speedometer
Recommends:     tree
Requires:       %name-data
# for /usr/bin/pygmentize
Requires:       python3-Pygments
Requires:       tmux
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%package data
Summary:        Data files for hollywood
License:        CC0-1.0
Group:          Amusements/Toys/Other

%package -n wallstreet
Summary:        Program to fill the console with Wall Street-like news and stats
License:        Apache-2.0
Group:          Amusements/Toys/Other
Recommends:     byobu
Recommends:     caca-utils
Recommends:     newsbeuter
Requires:       perl-base
Recommends:     rsstail
# unavailable
Recommends:     ticker
Requires:       wget
Recommends:     w3m
# unavailable:
Recommends:     jp2a

%description
This utility will split the console into a multiple panes of genuine
technobabble, perfectly suitable for any Hollywood geek melodrama.
It is particularly suitable on any number of computer consoles in the
background of any excellent schlock technothriller.

%description data
Data files needed for the "hollywood" package.

%description -n wallstreet
This utility will split the console into a multiple panes of news
and statistics, like any good computer screen on Wall Street.

%prep
%setup -q

%build

%install
install -Dm 0755 -t %buildroot/%_bindir bin/hollywood
install -Dm 0755 -t %buildroot/%_libexecdir/hollywood/ lib/hollywood/*
install -Dm 0644 -t %buildroot/%_mandir/man1/ share/man/man1/hollywood.1
install -Dm 0644 -t %buildroot/%_datarootdir/hollywood/ share/hollywood/*

install -Dm 0755 bin/wallstreet %buildroot/%_bindir
install -Dm 0755 -t %buildroot/%_libexecdir/wallstreet/ lib/wallstreet/*
install -Dm 0644 -t %buildroot/%_datarootdir/wallstreet share/wallstreet/*

%files
%defattr(-,root,root)
%_bindir/hollywood
%_libexecdir/hollywood/
%_mandir/man1/hollywood.1*

%files data
%defattr(-,root,root)
%_datarootdir/hollywood

%files -n wallstreet
%defattr(-,root,root)
%_bindir/wallstreet
%_libexecdir/wallstreet/
%_datarootdir/wallstreet

%changelog
