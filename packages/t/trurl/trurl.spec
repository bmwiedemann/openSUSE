#
# spec file for package trurl
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2023-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           trurl
Version:        0.16.1
Release:        0
Summary:        Command line tool for URL parsing and manipulation
License:        curl
Group:          Productivity/Networking/Web/Utilities
#Git-Clone:     https://github.com/curl/trurl.git
URL:            https://curl.se/trurl
Source:         https://github.com/curl/trurl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM exclude tests with uppercase
Patch0:         trurl-395-exculdes-uppercase.patch
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(libcurl) >= 7.62.0

%description
A CLI tool that parses and manipulates URLs, designed to help
shell script authors everywhere.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup

%build
%make_build PREFIX=%{_prefix}
make completions

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
install -Dm 0644 completions/_trurl.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
make test

%files
%license COPYING
%doc README.md RELEASE-NOTES
%{_bindir}/trurl
%{_mandir}/man1/trurl.1%{?ext_man}

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
