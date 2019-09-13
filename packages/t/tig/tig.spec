#
# spec file for package tig
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


Name:           tig
Version:        2.4.1
Release:        0
Summary:        An ncurses-based text-mode interface for git
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://jonas.github.io/tig/
Source0:        https://github.com/jonas/tig/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  readline-devel >= 6.3
BuildRequires:  pkgconfig(ncurses)
Requires:       bash-completion
Requires:       git-core

%description
Tig is a git repository browser that additionally can act as a pager
for output from various git commands.

When browsing repositories, it uses the underlying git commands to
present the user with various views, such as summarized revision log
and showing the commit with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.

%prep
%setup -q

%build
%configure \
	--with-ncurses \
	--docdir=%{_docdir}
make %{?_smp_mflags} V=1

%install
%make_install install-doc-man
install -Dpm 0644 contrib/tig-completion.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license COPYING
%doc NEWS.adoc README.adoc
%doc contrib/*.tigrc
%{_bindir}/tig
%config %{_sysconfdir}/tigrc
%{_mandir}/man1/tig.1%{?ext_man}
%{_mandir}/man5/tigrc.5%{?ext_man}
%{_mandir}/man7/tigmanual.7%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}

%changelog
