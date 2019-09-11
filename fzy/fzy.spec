#
# spec file for package fzy
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


Name:           fzy
Version:        1.0
Release:        0
Summary:        A fuzzy text selector
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/jhawthorn/fzy
Source0:        https://github.com/jhawthorn/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/jhawthorn/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring

%description
fzy can be used to filter any list: files, command history, processes,
hostnames, bookmarks, git commits, etc. It's designed to be used both as an
editor plugin and on the command line. Rather than clearing the screen, fzy
displays its interface directly below the current cursor position, scrolling
the screen if necessary.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=%{?buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/fzy
%{_mandir}/man1/fzy.1%{?ext_man}

%changelog
