#
# spec file for package gti
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gti
Version:        1.9.1
Release:        0
Summary:        ASCII art punishment for misspelling git
License:        MIT
Group:          Amusements/Toys/Other
URL:            https://r-wos.org/hacks/gti
Source:         https://github.com/rwos/gti/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
Recommends:     git-core

%description
Program which will show you ASCII art car driving across the terminal when you
misspell git command. After animation it will perform git command as well.
Similar to sl (steam locomotive).

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags}" STRIP=false

%install
# Override INSTALL command as Makefile does not create directories otherwise
%make_install INSTALL="install -D"

%files
%doc README.md
%license LICENSE
%{_bindir}/gti
%{_datadir}/bash-completion/completions/gti
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_gti
%{_mandir}/man*/*

%changelog
