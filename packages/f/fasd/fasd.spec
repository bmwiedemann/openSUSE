#
# spec file for package fasd
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Robin Roth <robin.roth@kit.edu>
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


Name:           fasd
Version:        1.0.1
Release:        0
Summary:        Command-line productivity booster, offers quick access to files and directories
License:        MIT
Group:          Productivity/File utilities
Url:            https://github.com/clvv/fasd
Source0:        https://github.com/clvv/fasd/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Fasd (pronounced similar to "fast") is a command-line productivity booster. Fasd offers quick access to files and directories for
POSIX shells. It is inspired by tools like autojump, z and v. Fasd keeps track of files and directories you have accessed, so that
you can quickly reference them in the command line.

The name fasd comes from the default suggested aliases f(files), a(files/directories), s(show/search/select), d(directories).

Fasd ranks files and directories by "frecency," that is, by both "frequency" and "recency." The term "frecency" was first coined
by Mozilla and used in Firefox.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix}

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_bindir}/fasd
%{_mandir}/man1/fasd.1*

%doc

%changelog
