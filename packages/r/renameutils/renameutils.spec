#
# spec file for package renameutils
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


Name:           renameutils
Version:        0.12.0
Release:        0
Summary:        Programs to make file renaming easier
License:        GPL-3.0-or-later
URL:            https://www.nongnu.org/renameutils/
Source:         http://download.savannah.gnu.org/releases/renameutils/renameutils-%{version}.tar.gz
Patch0:         makefile-am-bindir.patch
BuildRequires:  fdupes
BuildRequires:  readline-devel
BuildRequires:  gettext
# Installs imv binary
Conflicts: imv

%description
The file renaming utilities (renameutils for short) are a set of programs
designed to make renaming of files faster and less cumbersome.

This package consists of five programs - qmv, imv, icp, qcp and deurlname:

qmv ("quick move") allows file names to be edited in a text editor. The
names of all files in a directory are written to a text file, which is
then edited by the user. The text file is read and parsed, and the changes
are applied to the files.

imv ("interactive move"), is trivial but useful when you are too lazy to
type (or even complete) the name of the file to rename twice. It allows a
file name to be edited in the terminal using the GNU Readline library.

icp and qcp are similar to imv and qmv but for copying using "cp".

deurlname removes URL encoded characters (such as %20 representing space)
from file names. Some programs such as w3m tend to keep those characters
encoded in saved files.

%prep
%setup -q renameutils-%{version}
%autopatch -p1

%build
%configure
%make_build

%install
%make_install
%fdupes %{buildroot}
%find_lang %{name}
%find_lang renameutils-gnulib

%files -f %{name}.lang -f renameutils-gnulib.lang
%license COPYING
%doc ChangeLog README NEWS
%{_bindir}/deurlname
%{_bindir}/icmd
%{_bindir}/icp
%{_bindir}/imv
%{_bindir}/qcmd
%{_bindir}/qcp
%{_bindir}/qmv
%{_mandir}/man1/deurlname.1%{?ext_man}
%{_mandir}/man1/icmd.1%{?ext_man}
%{_mandir}/man1/icp.1%{?ext_man}
%{_mandir}/man1/imv.1%{?ext_man}
%{_mandir}/man1/qcmd.1%{?ext_man}
%{_mandir}/man1/qcp.1%{?ext_man}
%{_mandir}/man1/qmv.1%{?ext_man}

%changelog

