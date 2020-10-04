#
# spec file for package grep
#
# Copyright (c) 2020 SUSE LLC
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
Version:        3.5
Release:        0
Summary:        Print lines matching a pattern
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.gnu.org/software/grep/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source2:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source3:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=grep&download=1#/%{name}.keyring
Source4:        profile.sh
BuildRequires:  fdupes
BuildRequires:  makeinfo
BuildRequires:  pcre-devel
Requires(pre):  %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Provides:       base:%{_bindir}/grep

%description
The grep command searches one or more input files for lines containing a
match to a specified pattern.  By default, grep prints the matching lines.

%lang_package

%prep
%setup -q

%build
%configure \
  --disable-silent-rules \
  --without-included-regex \
  %{nil}
%if 0%{?do_profiling}
  make %{?_smp_mflags} CFLAGS="%{optflags} %{cflags_profile_generate}"
  sh %{SOURCE4} # profiling run
  make clean
  make %{?_smp_mflags} CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  make %{?_smp_mflags} CFLAGS="%{optflags}"
%endif

%check
make %{?_smp_mflags} check

%install
%make_install
#UsrMerge
install -d %{buildroot}/bin
ln -sf %{_bindir}/egrep %{buildroot}/bin/egrep
ln -sf %{_bindir}/fgrep %{buildroot}/bin/fgrep
ln -sf %{_bindir}/grep %{buildroot}/bin/grep
#EndUsrMerge
%fdupes -s %{buildroot}
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/grep.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/grep.info%{ext_info}

%files
%defattr(-,root,root)
%license COPYING
%doc README AUTHORS NEWS THANKS TODO ChangeLog*
#UsrMerge
/bin/egrep
/bin/fgrep
/bin/grep
#EndUsrMerge
%{_bindir}/egrep
%{_bindir}/fgrep
%{_bindir}/grep
%{_mandir}/man1/egrep.1%{ext_man}
%{_mandir}/man1/fgrep.1%{ext_man}
%{_mandir}/man1/grep.1%{ext_man}
%{_infodir}/grep.info%{ext_info}

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
