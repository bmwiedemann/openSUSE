#
# spec file for package git-merge-changelog
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2008 Ivan N. Zlatev <contact@i-nz.net>
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


Name:           git-merge-changelog
Version:        20120413
Release:        0
Url:            http://www.gnu.org/software/gnulib
Source:         %{name}-2008.tar.xz
Summary:        Git merge driver for ChangeLog files
License:        GPL-3.0+
Group:          Development/Tools/Version Control
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  xz

%description
Git merge driver for ChangeLog files.
1. It produces no conflict when ChangeLog entries have been inserted
at the top both in the public and in the private modification. It
puts the privately added entries above the publicly added entries.
2. It respects the structure of ChangeLog files: entries are not split
into lines but kept together.
3. It also handles the case of small modifications of past ChangeLog
entries, or of removed ChangeLog entries: they are merged as one
would expect it.
4. Conflicts are presented at the top of the file, rather than where
they occurred, so that the user will see them immediately. (Unlike
for source code written in some programming language, conflict markers
that are located several hundreds lines from the top will not cause
any syntax error and therefore would be likely to remain unnoticed.)

%if %suse_version <= 1020
%define _prefix /opt/gnome
%define _sysconfdir /etc/opt/gnome
%endif

%prep
%setup -q -n %{name}-2008

%build
%configure
make %{?_smp_mflags}

%install
%make_install
gzip -9 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
