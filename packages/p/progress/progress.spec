#
# spec file for package progress
#
# Copyright (c) 2023 SUSE LLC
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


Name:           progress
Version:        0.17
Release:        0
Summary:        Coreutils Viewer
License:        GPL-3.0-or-later
Group:          System/Console
URL:            https://github.com/Xfennec/progress
Source0:        https://github.com/Xfennec/progress/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(form)
BuildRequires:  pkgconfig(formw)
BuildRequires:  pkgconfig(menu)
BuildRequires:  pkgconfig(menuw)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncurses++)
BuildRequires:  pkgconfig(ncurses++w)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(panel)
BuildRequires:  pkgconfig(panelw)
BuildRequires:  pkgconfig(tic)
BuildRequires:  pkgconfig(tinfo)
Provides:       cv = %{version}
Obsoletes:      cv < %{version}

%description
This tool can be described as a Tiny Dirty Linux Only* C command that looks for coreutils basic
commands (cp, mv, dd, tar, gzip/gunzip, cat, ...) currently running on your system and displays
the percentage of copied data.

It can now also display an estimated throughput (using -w flag).

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
%if 0%{?suse_version} == 1315
Supplements:    packageand(progress:zsh)
%else
Supplements:    (progress and zsh)
%endif
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%prep
%autosetup

%build
%make_build CFLAGS="-g -Wall -D_FILE_OFFSET_BITS=64 %{optflags}"

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files zsh-completion
%{_datadir}/zsh/
%{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_progress

%changelog
