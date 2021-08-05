#
# spec file for package grep
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


Name:           grep
Version:        3.6
Release:        0
Summary:        Print lines matching a pattern
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.gnu.org/software/grep/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source2:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source3:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=grep&download=1#/%{name}.keyring
Source4:        profile.sh
Source5:        %{name}-rpmlintrc
Patch0:         werror-return-type.patch
Patch1:         gnulib-c-stack.patch
BuildRequires:  fdupes
BuildRequires:  makeinfo
BuildRequires:  pcre-devel
Provides:       base:%{_bindir}/grep

%description
The grep command searches one or more input files for lines containing a
match to a specified pattern.  By default, grep prints the matching lines.

%lang_package

%prep
%autosetup -p1

touch aclocal.m4 configure Makefile.in config.hin

%build
%configure \
  --disable-silent-rules \
  --without-included-regex \
  %{nil}
%if 0%{?do_profiling}
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}"
  sh %{SOURCE4} # profiling run
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build
%endif

%check
%make_build check

%install
%make_install
%if !0%{?usrmerged}
install -d %{buildroot}/bin
ln -sf %{_bindir}/egrep %{buildroot}/bin/egrep
ln -sf %{_bindir}/fgrep %{buildroot}/bin/fgrep
ln -sf %{_bindir}/grep %{buildroot}/bin/grep
%endif
%fdupes -s %{buildroot}
%find_lang %{name}

%files
%license COPYING
%doc README AUTHORS NEWS THANKS TODO ChangeLog*
%if !0%{?usrmerged}
/bin/egrep
/bin/fgrep
/bin/grep
%endif
%{_bindir}/egrep
%{_bindir}/fgrep
%{_bindir}/grep
%{_mandir}/man1/egrep.1%{?ext_man}
%{_mandir}/man1/fgrep.1%{?ext_man}
%{_mandir}/man1/grep.1%{?ext_man}
%{_infodir}/grep.info%{?ext_info}

%files lang -f %{name}.lang

%changelog
