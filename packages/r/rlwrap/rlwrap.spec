#
# spec file for package rlwrap
#
# Copyright (c) 2021 SUSE LLC
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


Name:           rlwrap
Version:        0.44
Release:        0
Summary:        A Readline Wrapper
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://github.com/hanslub42/rlwrap/
Source0:        https://github.com/hanslub42/rlwrap/releases/download/7c1e432/rlwrap-%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel

%description
rlwrap uses the GNU readline library to allow the editing of keyboard
input for any other command. The input history is remembered across
invocations, separately for each command;history completion and search
work as in bash and completion word lists can be specified on the
command line.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%make_install

%files
%doc AUTHORS BUGS ChangeLog NEWS README.md
%license COPYING
%{_bindir}/rlwrap
%{_mandir}/man1/rlwrap.1%{ext_man}
%{_mandir}/man3/RlwrapFilter.3pm%{ext_man}
%{_datadir}/rlwrap

%changelog
