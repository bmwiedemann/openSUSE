#
# spec file for package wdiff
#
# Copyright (c) 2025 SUSE LLC
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


Name:           wdiff
Version:        1.2.2
Release:        0
Summary:        Display Word Differences Between Text Files
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.gnu.org/software/wdiff/
Source0:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz.sig
Source2:        %{name}.keyring
# build with gcc15
Patch0:         wdiff-gcc15.patch
BuildRequires:  help2man
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
wdiff compares two files and finds which words have been deleted or
added to old_file to get new_file. A word is considered to be anything
between whitespace.

Xwdiff is a handy X Window System front-end, based on Tcl/Tk.

%lang_package

%prep
%autosetup -p1

%build
%configure \
  --enable-experimental="mdiff wdiff2 unify"
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}-gnulib
%find_lang %{name}

%check
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%license COPYING
%doc BACKLOG ChangeLog NEWS README* THANKS TODO ABOUT-NLS AUTHORS
%{_bindir}/mdiff
%{_bindir}/unify
%{_bindir}/wdiff
%{_bindir}/wdiff2
%{_infodir}/wdiff.info%{?ext_info}
%{_mandir}/man1/mdiff.1%{?ext_man}
%{_mandir}/man1/unify.1%{?ext_man}
%{_mandir}/man1/wdiff.1%{?ext_man}
%{_mandir}/man1/wdiff2.1%{?ext_man}

%files lang -f %{name}-gnulib.lang -f %{name}.lang

%changelog
