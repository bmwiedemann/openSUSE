#
# spec file for package gzip
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


%define _buildshell /bin/bash
Name:           gzip
Version:        1.10
Release:        0
Summary:        GNU Zip Compression Utilities
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Compression
URL:            http://www.gnu.org/software/gzip/
Source:         http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source2:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source3:        %{name}.keyring
Patch0:         zgrep.diff
Patch2:         zmore.diff
Patch3:         non-exec-stack.diff
Patch6:         zdiff.diff
# PATCH FIX OPENSUSE BNC#799561 - zgrep silently fails on LZMA compressed files
Patch7:         xz_lzma.patch
Patch8:         manpage-no-date.patch
Patch9:         gzip-1.10-ibm_dfltcc_support.patch
Patch10:        gzip-1.10-fix_count_of_lines_to_skip.patch
# https://git.savannah.gnu.org/cgit/gzip.git/commit/?id=be0a534ba2b6e77da289de8da79e70843b1028cc
Patch11:        gzip-1.10-fix-DFLTCC-segfault.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  makeinfo
BuildRequires:  xz
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}

%description
Gzip reduces the size of the named files using Lempel-Ziv coding LZ77.
Whenever possible, each file is replaced by one with the extension .gz,
while keeping the same ownership modes and access and modification
times.

%prep
%setup -q
%patch0
%patch2 -p1
%patch3
%patch6
%patch7 -p1
%patch8 -p1
%ifarch s390x
%patch9 -p1
%endif
%patch10 -p1
%ifarch s390x
%patch11 -p1
%endif

%build
export CFLAGS="%{optflags} -fomit-frame-pointer \
-W -Wall -Wno-unused-parameter -Wstrict-prototypes -Wpointer-arith -fPIE"
export LDFLAGS="-pie"
# added because of gzip-1.10-ibm_dfltcc_support.patch [jsc#SLE-5818]
%ifarch s390x
autoreconf -f -i
export CFLAGS="$CFLAGS -DDFLTCC_LEVEL_MASK=0x7e"
%endif
%configure --disable-silent-rules \
  gl_cv_func_printf_directive_n=yes \
  gl_cv_func_printf_infinite_long_double=yes \
%ifarch s390x
  --enable-dfltcc \
%endif

profile_gzip()
{
  tmpfile=$(mktemp)
  trap "rm -f $tmpfile $tmpfile.gz" EXIT
  xz -cd %{SOURCE0} > $tmpfile
  time ./gzip < $tmpfile > $tmpfile.gz
  time ./gzip -d < $tmpfile.gz > /dev/null
}
%if %{do_profiling}
make %{?_smp_mflags} CFLAGS="$CFLAGS -fprofile-generate" LDFLAGS="-pie"
profile_gzip
make clean %{?_smp_mflags}
make %{?_smp_mflags} CFLAGS="$CFLAGS -fprofile-use" LDFLAGS="-pie"
%else
make %{?_smp_mflags} LDFLAGS="-pie"
%endif

%check
for i in {1..9}; do
  for f in build-aux/texinfo.tex /bin/bash; do
    basef=${f##*/}
    time ./gzip -$i < $f > $basef.gz
    ./gzip --test $basef.gz
    ./gzip -d < $basef.gz > $basef.test$i
    cmp $f $basef.test$i
  done
done

%install
%make_install
%if !0%{?usrmerged}
mkdir -p %{buildroot}/bin
ln -sf %{_bindir}/gzip %{_bindir}/gunzip %{_bindir}/zcat %{buildroot}/bin
%endif
ln -sf zmore %{buildroot}%{_bindir}/zless
ln -sf zmore.1 %{buildroot}%{_mandir}/man1/zless.1

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING
%doc README AUTHORS ChangeLog TODO NEWS THANKS
%if !0%{?usrmerged}
/bin/gunzip
/bin/gzip
/bin/zcat
%endif
%{_bindir}/gunzip
%{_bindir}/gzexe
%{_bindir}/gzip
%{_bindir}/uncompress
%{_bindir}/zcat
%{_bindir}/zcmp
%{_bindir}/zdiff
%{_bindir}/zegrep
%{_bindir}/zfgrep
%{_bindir}/zforce
%{_bindir}/zgrep
%{_bindir}/zless
%{_bindir}/zmore
%{_bindir}/znew
%{_infodir}/gzip.info%{?ext_info}
%{_mandir}/man1/gunzip.1%{?ext_man}
%{_mandir}/man1/gzexe.1%{?ext_man}
%{_mandir}/man1/gzip.1%{?ext_man}
%{_mandir}/man1/zcat.1%{?ext_man}
%{_mandir}/man1/zcmp.1%{?ext_man}
%{_mandir}/man1/zdiff.1%{?ext_man}
%{_mandir}/man1/zforce.1%{?ext_man}
%{_mandir}/man1/zgrep.1%{?ext_man}
%{_mandir}/man1/zless.1%{?ext_man}
%{_mandir}/man1/zmore.1%{?ext_man}
%{_mandir}/man1/znew.1%{?ext_man}

%changelog
