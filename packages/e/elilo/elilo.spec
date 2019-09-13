#
# spec file for package elilo
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


%ifarch x86_64
%if 0%{?suse_version} < 1100
BuildRequires:  binutils219
#!BuildIgnore: binutils
%endif
%endif
BuildRequires:  gnu-efi >= 3.0u
BuildRequires:  xz
BuildRequires:  perl(Pod::Man)

Name:           elilo
Summary:        EFI Linux Loader
License:        GPL-2.0+
Group:          System/Boot
Version:        3.16
Release:        0
ExclusiveArch:  ia64 %ix86 x86_64
PreReq:         /usr/bin/perl perl(Pod::Usage) perl(Getopt::Long)
# "perl" must be in place *before* any package's 'pre' or 'post' section
# can (directly or indirectly) run '/sbin/elilo'!  (bnc#842183)
%ifarch ia64
PreReq:         perl(File::Compare)
%endif
Url:            http://elilo.sourceforge.net/
#ource:         http://downloads.sourceforge.net/elilo/elilo-3.16-all.tar.gz
Source:         elilo-%{version}-source.tar.xz
Source1:        elilo.pl
Source2:        debian.eliloalt.man8
Source3:        elilo.conf.man5
Source4:        http://downloads.sourceforge.net/elilo/%{version}-release-notes.txt
Source9:        elilo-rpmlintrc
Patch0:         elilo-ipv6.diff
Patch1:         elilo-max-conf.diff
Patch2:         elilo-mac-conf.diff
Patch3:         elilo-auto-add_efi_memmap.diff
Patch4:         elilo-blocksize.diff
Patch5:         elilo-text-mode.diff
Patch6:         elilo-textmenu-disable-print-devices.diff
Patch7:         elilo-high_base_mem.diff
Patch10:        elilo-de-debianify.diff
Patch11:        eliloalt-no-date.diff

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The EFI Linux boot loader.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch10 -p1
%patch11 -p1
# work around b0rked 'Str'-ops in newer 'gnu-efi' ... :-(
find . -type f -name '*.[ch]' -print0 | xargs -0rn 1 \
  perl -pi -e 's{Str(Chr|n(X?Cpy|Cat))}{eliloStr$1}g'

%build
perl -pi -e 's{/usr/lib}{%{_libdir}}' Make.defaults
##################################################################
## DO NOT ADD RPM OPT FLAGS! THIS DOES NOT BUILD AGAINST GLIBC. ##
##################################################################
OPTFLAGS="-fmessage-length=0"
%ifnarch ia64
OPTFLAGS="$OPTFLAGS -mno-red-zone"
%endif
make OPTIMFLAGS="$OPTFLAGS"
perl -pe 's{\@EDITION\@}{%{version}};
	  s{\@LIBDIR\@}{%{_libdir}};
	  s{\@ARCH\@}{%{_target_cpu}};
	' < %{SOURCE1} > elilo.pl &&
chmod 555 elilo.pl && touch -r %{SOURCE1} elilo.pl
! grep -F '%%{version}' elilo.pl
pod2man -s 8 -c "System Boot" -r "SuSE Linux" \
    -n elilo -d "%{version}" elilo.pl elilo.8
touch -r elilo.pl elilo.8

%install
install -d $RPM_BUILD_ROOT%{_libdir}/efi $RPM_BUILD_ROOT/sbin
install -p -m 444 elilo.efi $RPM_BUILD_ROOT%{_libdir}/efi
install tools/eliloalt $RPM_BUILD_ROOT/sbin
install -p -m 555 elilo.pl $RPM_BUILD_ROOT/sbin/elilo
install -D -p -m 644 elilo.8 $RPM_BUILD_ROOT/usr/share/man/man8/elilo.8
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/usr/share/man/man8/eliloalt.8
install -D -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT/usr/share/man/man5/elilo.conf.5
install -p -m 644 %{SOURCE4} RELEASE-NOTES
diff -q docs/README.txt docs/elilo.txt && rm -f docs/README.txt

%post
if [ -r /etc/sysconfig/bootloader ]; then
  . /etc/sysconfig/bootloader
  if [ "$LOADER_TYPE" = "elilo" -a -r /etc/elilo.conf ]; then
    /sbin/elilo -v || :
  fi
fi

%files
%defattr(-, root, root)
%doc README README.* TODO docs/*.txt RELEASE-NOTES
%{_libdir}/efi
/sbin/elilo
/sbin/eliloalt
/usr/share/man/man5/*
/usr/share/man/man8/*

%changelog
