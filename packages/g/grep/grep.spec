#
# spec file for package grep
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


Name:           grep
Version:        3.8
Release:        0
Summary:        Print lines matching a pattern
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.gnu.org/software/grep/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source2:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
# Taken from https://savannah.gnu.org/project/release-gpgkeys.php?group=grep&download=1
Source3:        %{name}.keyring
Source4:        profile.sh
Source5:        %{name}-rpmlintrc
Patch0:         efgrep-warning.patch
BuildRequires:  fdupes
BuildRequires:  glibc-locale
BuildRequires:  makeinfo
BuildRequires:  pkgconfig(libpcre2-8)
Provides:       base:%{_bindir}/grep

%description
The grep command searches one or more input files for lines containing a
match to a specified pattern.  By default, grep prints the matching lines.

%lang_package

%prep
%autosetup -p1

%build
%configure \
  --disable-silent-rules \
  %{nil}
%if 0%{?do_profiling}
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}"
  setarch -R sh %{SOURCE4} # profiling run
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build
%endif

%check
%if 0%{?qemu_user_space_build}
echo exit 77 > tests/stack-overflow
echo exit 77 > tests/pcre-jitstack
echo exit 77 > gnulib-tests/test-c-stack.sh
echo 'int main() { return 77; }' > gnulib-tests/test-sigsegv-catch-stackoverflow1.c
echo 'int main() { return 77; }' > gnulib-tests/test-sigsegv-catch-stackoverflow2.c
echo 'int main() { return 77; }' > gnulib-tests/test-free.c
%endif
%make_build check

%install
%make_install
%if 0%{?suse_version} < 1550
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
%if 0%{?suse_version} < 1550
/bin/egrep
/bin/fgrep
/bin/grep
%endif
%{_bindir}/egrep
%{_bindir}/fgrep
%{_bindir}/grep
%{_mandir}/man1/grep.1%{?ext_man}
%{_infodir}/grep.info%{?ext_info}

%files lang -f %{name}.lang

%changelog
