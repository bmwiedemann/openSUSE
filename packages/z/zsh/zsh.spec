#
# spec file for package zsh
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


%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
%if 0%{?rhel_version} >= 700 || 0%{?centos_version} >= 700
%global __requires_exclude ^/bin/zsh$
%endif
BuildRequires:  libtermcap-devel
BuildRequires:  texi2html
BuildRequires:  texinfo
%endif
Name:           zsh
Version:        5.8
Release:        0%{?dist}
Summary:        Shell with comprehensive completion
License:        MIT
Group:          System/Shells
URL:            http://www.zsh.org
Source0:        https://downloads.sourceforge.net/project/zsh/zsh/%{version}/zsh-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/project/zsh/zsh/%{version}/zsh-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        zshrc
Source4:        zshenv
Source5:        zprofile
Patch1:         trim-unneeded-completions.patch
# PATCH-FIX-OPENSUSE zsh-osc-completion.patch -- Fix openSUSE versions in osc completion
Patch2:         zsh-osc-completion.patch
Patch3:         ncurses-fix.patch
BuildRequires:  groff
BuildRequires:  libcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
Source11:       zlogin.rhs
Source12:       zlogout.rhs
Source13:       zprofile.rhs
Source14:       zshrc.rhs
Source15:       zshenv.rhs
Source16:       dotzshrc.rh
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  yodl
Requires(pre):  %{install_info_prereq}
%if 0%{?suse_version} >= 1210
BuildRequires:  makeinfo
BuildRequires:  texi2html
%endif
%else
Requires(pre):  /sbin/install-info
Requires(pre):  fileutils
Requires(pre):  grep
%endif

%description
Zsh is a UNIX command interpreter (shell) that resembles the Korn shell
(ksh). It is not completely compatible. It includes many enhancements,
notably in the command-line editor, options for customizing its
behavior, file name globbing, features to make C-shell (csh) users feel
at home, and extra features drawn from tcsh (another `custom' shell).
Zsh is well known for its command line completion.

%package htmldoc
Summary:        Zsh shell manual in HTML format
Group:          Documentation/HTML
Provides:       %{name}-html = %{version}
Obsoletes:      %{name}-html < %{version}

%description htmldoc
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

This package contains the Zsh manual in HTML format.

%prep
%setup -q
%if 0%{?suse_version}
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1

# Remove executable bit
chmod 0644 Etc/changelog2html.pl

# Fix bindir path in some files
perl -p -i -e 's|%{_prefix}/local/bin|%{_bindir}|' \
    Doc/intro.ms Misc/globtests.ksh Misc/globtests \
    Misc/lete2ctl Util/check_exports Util/helpfiles \
    Util/reporter

%build

%configure \
%if 0%{?suse_version}
    --with-term-lib="ncursesw" \
    --enable-cflags="%{optflags} -fPIE %(ncursesw6-config --cflags)" \
    --enable-ldflags="%(ncursesw6-config --libs) -pie -Wl,-z,relro" \
%endif
    --enable-fndir=%{_datadir}/%{name}/${version}/functions \
    --enable-site-fndir=%{_datadir}/%{name}/site-functions \
    --enable-function-subdirs \
    --enable-maildir-support \
    --with-tcsetpgrp \
    --enable-cap \
    --enable-multibyte \
    --enable-pcre \
    --enable-unicode9

# Copy _rpm completion from Redhat (bnc#900424)
%if 0%{?suse_version}
cp Completion/Redhat/Command/_rpm Completion/openSUSE/Command/_rpm
%endif

make %{?_smp_mflags} all info html

# generate intro.ps
groff -Tps -ms Doc/intro.ms > intro.ps

# better name for html documentation
install -d -m 0755 Doc/htmldoc/
mv Doc/*.html Doc/htmldoc

# remove some unwanted files in Etc/
rm -f Etc/Makefile* Etc/*.yo

%install
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
%endif

%if 0%{?suse_version}
%make_install install.info
%else
  make DESTDIR=%{buildroot} install install.info
%endif

install -m 0755 -Dd  %{buildroot}/{etc,bin}

%if 0%{?suse_version}
# install SUSE configuration
install -m 0644 %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}%{_sysconfdir}

# Create custom completion directory
mkdir %{buildroot}%{_sysconfdir}/zsh_completion.d
%endif

%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
# install RHEL || CentOS || Fedora configuration
for i in zlogin zlogout zprofile zshrc zshenv; do
  install -m 0644 $RPM_SOURCE_DIR/${i}.rhs %{buildroot}%{_sysconfdir}/$i
done
install -D -m 0644 %{SOURCE16} %{buildroot}%{_sysconfdir}/skel/.zshrc
%endif

# link zsh binary
%if 0%{?suse_version} || 0%{?rhel} <= 6
ln -sf %{_bindir}/zsh %{buildroot}/bin/zsh
%endif

# Remove versioned zsh binary
rm -f %{buildroot}%{_bindir}/zsh-*
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
rm -f %{buildroot}/%{_infodir}/dir
%endif

%if 0%{?suse_version} >= 1110
%fdupes %{buildroot}
%endif

%check
%if ! 0%{?qemu_user_space_build}
%if 0%{?suse_version}
make %{?_smp_mflags} check
%else
# FixMe: sometimes failing Test
#+ fn:echo:2: write error: broken pipe
#+ fn:2: write error: inappropriate ioctl for device
mv Test/E01options.ztst Test/E01options.ztst.mvd
%ifarch s390 s390x ppc ppc64
  ( cd Test
    mkdir skipped
    mv Y*.ztst skipped )
%endif
  ZTST_verbose=0 make test
%endif
%endif

%preun
%if 0%{?suse_version}
  :
%else
  if [ "$1" = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/zsh.info.gz %{_infodir}/dir \
      --entry="* zsh: (zsh).                  An enhanced bourne shell."
  fi
%endif

%post
%if 0%{?suse_version}
  %install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%else
if [ ! -f %{_sysconfdir}/shells ]; then
  echo "%{_bindir}/zsh" > %{_sysconfdir}/shells
else
  grep -q "^%{_bindir}/zsh$" %{_sysconfdir}/shells || echo "%{_bindir}/zsh" >> %{_sysconfdir}/shells
fi

/sbin/install-info %{_infodir}/zsh.info.gz %{_infodir}/dir \
  --entry="* zsh: (zsh).                  An enhanced bourne shell."
%endif

%postun
%if 0%{?suse_version}
  %install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%else
  if [ "$1" = 0 ] ; then
    if [ -f %{_sysconfdir}/shells ] ; then
      TmpFile=`%{_bindir}/mktemp /tmp/.zshrpmXXXXXX`
      grep -v '^%{_bindir}/zsh$' %{_sysconfdir}/shells > $TmpFile
      cp -f $TmpFile %{_sysconfdir}/shells
      rm -f $TmpFile
      chmod 644 %{_sysconfdir}/shells
    fi
  fi
%endif

%files
%doc ChangeLog FEATURES LICENCE MACHINES META-FAQ NEWS README
%doc Etc/* intro.ps Misc/compctl-examples
%config(noreplace) %{_sysconfdir}/zshrc
%config(noreplace) %{_sysconfdir}/zshenv
%config(noreplace) %{_sysconfdir}/zprofile
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
%config(noreplace) %{_sysconfdir}/zlogin
%config(noreplace) %{_sysconfdir}/zlogout
%config(noreplace) %{_sysconfdir}/skel/.zshrc
%endif

%if 0%{?suse_version}
%dir %{_sysconfdir}/zsh_completion.d
%endif

%{_bindir}/zsh
%if 0%{?suse_version} || 0%{?rhel} <= 6
/bin/zsh
%endif
%{_libdir}/zsh/
%{_datadir}/zsh/
%{_infodir}/zsh.info*%{ext_info}
%{_mandir}/man1/zsh*.1%{ext_man}

%files htmldoc
%doc Doc/htmldoc/*

%changelog
