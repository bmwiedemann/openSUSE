#
# spec file for package enscript
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           enscript
Version:        1.6.6
Release:        0
Summary:        An ASCII to PostScript(tm) Converter
License:        GPL-3.0+
Group:          Productivity/Publishing/PS
Url:            http://git.savannah.gnu.org/cgit/enscript.git
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        enscript-gs-font.map
Source3:        enscript.sh
Patch1:         enscript-1.6.4-perl_parens.patch
Patch2:         enscript-1.6.4-sh_string.patch
Patch3:         enscript-automake.diff
# PATCH-ENHANCE-SUSE -- Add Euro and Baltic support
Patch4:         enscript-1.6.6-euro+baltic.patch
# PATCH-ENHANCE-SUSE -- Add better encoding and automatic paper size support
Patch5:         enscript-1.6.6-encoding+paper.patch
# PATCH-ENHANCE-SUSE -- Add mailto support with optional address
Patch6:         enscript-1.6.6-mailto.patch
# PATCH-ENHANCE-SUSE -- Mention helper app support to manual page
Patch7:         enscript-1.6.6-helper-apps.patch
# PATCH-ENHANCE-SUSE -- Silent the compiler warnings
Patch8:         enscript-1.6.6-silent-warns.patch
# PATCH-ENHANCE-SUSE -- To be able to map fonts from adobe to gs replacement
Patch9:         enscript-1.6.6-ghostscript.patch
BuildRequires:  automake
Requires:       %{_bindir}/file
Requires:       %{_bindir}/iconv
Requires:       /bin/sed
Requires:       ghostscript-fonts-std
PreReq:         %{install_info_prereq}
Provides:       genscript
Provides:       nenscrip
%if 0%{?suse_version} >= 1230
BuildRequires:  makeinfo
%endif

%description
Enscript converts ASCII files to PostScript and writes the generated
output to a file or sends it directly to the printer.

The Enscript configuration file is in /etc/enscript.cfg.

Warning: enscript is not able to convert complex unicode (UTF-8) text
to PostScript.	Only language text which can be converted from UTF-8 to
latin encodings are supported with the help of a wrapper script. ~ ~

%prep
%setup -q
%patch1 -p0 -b .perl
%patch2 -p0 -b .shell
%patch3 -p1
%patch4 -p0 -b .euro
%patch5 -p0 -b .paper
%patch6 -p0 -b .mailto
%patch7 -p0 -b .happ
%patch8 -p0 -b .nowarns
%patch9 -p0 -b .gs

%build
  CFLAGS="%{optflags} -DPROTOTYPES -D_GNU_SOURCE -funroll-loops -Wall -fno-strict-aliasing -pipe -fstack-protector"
  LDFLAGS=
  export CC CFLAGS LDFLAGS
  AUTOPOINT=true autoreconf --force --install
  test ! -f po/Makevars.template || mv po/Makevars.template po/Makevars
  %configure \
	--with-spooler=lpr \
	--with-media=LC_PAPER \
	--with-encoding=LC_CTYPE
  pushd lib/
    make -f Makefile-encodings %{?_smp_mflags}
  popd
  pushd afmlib/
    make -f Makefile-encodings %{?_smp_mflags}
  popd
  make CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" %{?_smp_mflags}

%install
%make_install
  ln -sf enscript   %{buildroot}%{_bindir}/genscript
  ln -sf enscript.1 %{buildroot}%{_mandir}/man1/genscript.1
  mkdir   -p -m 0755         %{buildroot}%{_datadir}/ghostscript/fonts
  install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/ghostscript/fonts/font.map
  mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.bin
  install -m 0755 %{SOURCE3}          %{buildroot}%{_bindir}/%{name}
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -f %{name}.lang
%doc docs/FAQ.html
%{_bindir}/diffpp
%{_bindir}/%{name}
%{_bindir}/%{name}.bin
%{_bindir}/genscript
%{_bindir}/mkafmmap
%{_bindir}/sliceprint
%{_bindir}/over
%{_bindir}/states
%config %{_sysconfdir}/%{name}.cfg
%{_mandir}/man1/diffpp.1%{ext_man}
%{_mandir}/man1/enscript.1%{ext_man}
%{_mandir}/man1/genscript.1%{ext_man}
%{_mandir}/man1/sliceprint.1%{ext_man}
%{_mandir}/man1/states.1%{ext_man}
%{_datadir}/enscript
%dir %{_datadir}/ghostscript
%dir %{_datadir}/ghostscript/fonts
%{_datadir}/ghostscript/fonts/font.map
%{_infodir}/%{name}.info%{ext_info}

%changelog
