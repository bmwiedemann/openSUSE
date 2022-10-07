#
# spec file for package ispell
#
# Copyright (c) 2022 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif
%if ! %{defined make_build}
  %define make_build make
%endif
%if ! %{defined make_install}
  %define make_install make
%endif

Name:           ispell
BuildRequires:  bison
BuildRequires:  ncurses-devel
BuildRequires:  words
URL:            https://www.cs.hmc.edu/~geoff/ispell.html
BuildRequires:  fdupes
Requires(post): %fillup_prereq
Provides:       spell
Requires:       ispell_dictionary
Requires:       ispell_english_dictionary
Requires:       words
Version:        3.4.05
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        A Spell Checker
License:        BSD-3-Clause
Group:          Productivity/Text/Spell
Source:         https://www.cs.hmc.edu/~geoff/tars/ispell-%{version}.tar.gz
Source1:        SuSEconfig.ispell
Source2:        sysconfig.ispell
Source3:        ispell-rpmlintrc
Patch0:         ispell-3.3.02.dif
Patch1:         ispell-3.3.02-config.patch
Patch2:         ispell-3.2.06-suse.patch
Patch3:         ispell-3.3.02-languages.patch
Patch4:         ispell-3.3.02-types.patch
Patch5:         ispell-3.3.02-terminal.patch
Patch6:         ispell-3.3.02-sq.patch
Patch7:         ispell-3.3.02-brkgcc.patch
Patch8:         ispell-3.3.02-mkdir.patch
Patch9:         ispell-3.3.02-strip.patch
# PATCH-FIX-OPENSUSE correct typo (boo#966124)
Patch10:        boo966124.dif

%description
Ispell is a fast, screen-oriented spell checker that shows you your
errors in the context of the original file and suggests possible
corrections when it can figure them out.  Compared to UNIX spell, it is
faster and much easier to use.	Ispell can also handle languages other
than English.  Ispell has a long history and many people have
contributed to the current version--some of the major contributors
include R. E. Gorin, Pace Willisson, Walt Buehring, and Geoff Kuenning.

You can find a short description in the directory
/usr/share/doc/packages/ispell/.



Authors:
--------
    R. E. Gorin
    Pace Willisson <pace@ai.mit.edu>
    Walt Buehring
    Goeff Kuenning <geoff@ITcorp.com>

%package     -n ispell-american
Summary:        American ispell dictionary
Group:          Productivity/Text/Spell
Provides:       iamerica
Provides:       ispell_dictionary
Provides:       ispell_english_dictionary
Provides:       locale(ispell:en)
Requires(post): bash
Requires(post): fileutils
Requires(postun):bash
Requires(postun):fileutils

%description -n ispell-american
This package includes a ready American dictionary for ispell. If you
install ispell-british too, check /etc/sysconfig/ispell to see which
one the default English dictionary will be. A short usage description
is given in /usr/share/doc/packages/ispell/README. The sources for this
dictionary are included in the source package of ispell.

%package     -n ispell-british
Summary:        British ispell dictionary
Group:          Productivity/Text/Spell
Provides:       ibritish
Provides:       ispell_dictionary
Provides:       ispell_english_dictionary
Provides:       locale(ispell:en_GB)
Requires(post): bash
Requires(post): fileutils
Requires(postun):bash
Requires(postun):fileutils

%description -n ispell-british
This packages includes a ready British dictionary for ispell. If you
install ispell-american too, check /etc/sysconfig/ispell to see which
one will be the default English dictionary. A short usage description
is given in /usr/share/doc/packages/ispell/README. The sources for this
dictionary are included in the source package of ispell.

%prep
%setup
%patch0  -p 0 -b .dif
%patch1  -p 0 -b .config
%patch2  -p 0 -b .suse
%patch3  -p 0 -b .languages
%patch4  -p 0 -b .types
%patch5  -p 0 -b .terminal
%patch6  -p 0 -b .sq
%patch7  -p 0 -b .brkgcc
%patch8  -p 0 -b .mkdir
%patch9  -p 0 -b .strip
%patch10 -p 0 -b .typo

%build
  PATH=$PATH:$PWD
  export PATH
  make local.h
  make config.sh
  %make_build -j1 all

%install
  DESTDIR=%{buildroot}
  export DESTDIR
  mkdir -p %{buildroot}/usr/doc/packages/ispell
  mkdir -p %{buildroot}%{_prefix}/lib/ispell/emacs
  mkdir -p %{buildroot}%{_fillupdir}
  mkdir -p %{buildroot}/var/lib/dict
  %make_install -j1 DESTDIR=%{buildroot}
  rm -f %{buildroot}/usr/share/emacs/site-lisp/ispell.el*
  install -m 0444 suse/ispell-emacs-menu.el 	%{buildroot}%{_prefix}/lib/ispell/
  install -m 0444 suse/emacs/american.el	%{buildroot}%{_prefix}/lib/ispell/emacs/
  install -m 0444 suse/emacs/british.el		%{buildroot}%{_prefix}/lib/ispell/emacs/
  install -m 0444 suse/emacs/english.el		%{buildroot}%{_prefix}/lib/ispell/emacs/
  rm -f %{buildroot}%{_prefix}/lib/ispell/british.hash
  rm -f %{buildroot}%{_prefix}/lib/ispell/american.hash
  ln -sf britishxlg.hash  %{buildroot}%{_prefix}/lib/ispell/british.hash
  ln -sf americanxlg.hash %{buildroot}%{_prefix}/lib/ispell/american.hash
  mv %{buildroot}%{_prefix}/lib/ispell/english.aff %{buildroot}%{_prefix}/lib/ispell/american.aff
  cp -a %{buildroot}%{_prefix}/lib/ispell/american.aff %{buildroot}%{_prefix}/lib/ispell/british.aff
  install -m 755 %{S:1} %{buildroot}%{_prefix}/lib/ispell/update
  install -m 644 %{S:2} %{buildroot}%{_fillupdir}/
  mkdir -p %{buildroot}/var/lib/dict
  ln -sf %{_prefix}/lib/ispell/american.hash %{buildroot}/var/lib/dict/english.hash
  ln -sf %{_prefix}/lib/ispell/american.aff  %{buildroot}/var/lib/dict/english.aff
  rm -f  %{buildroot}%{_prefix}/lib/ispell/english.hash
  rm -f  %{buildroot}%{_prefix}/lib/ispell/english.aff
  ln -sf /var/lib/dict/english.hash    %{buildroot}%{_prefix}/lib/ispell/
  ln -sf /var/lib/dict/english.aff     %{buildroot}%{_prefix}/lib/ispell/
  rm -f %{buildroot}%{_bindir}/defmt-*
  for man in icombine ijoin
  do
    echo .so man1/ispell.1 > %{buildroot}%{_mandir}/man1/${man}.1
  done
  %fdupes %{buildroot}%{_mandir}

%post
%{fillup_only}

%post -n ispell-american
if test -z "$YAST_IS_RUNNING" -a -x %{_prefix}/lib/ispell/update ; then
    %{_prefix}/lib/ispell/update
fi

%postun -n ispell-american
if test -z "$YAST_IS_RUNNING" -a -x %{_prefix}/lib/ispell/update ; then
    %{_prefix}/lib/ispell/update
fi

%post -n ispell-british
if test -z "$YAST_IS_RUNNING" -a -x %{_prefix}/lib/ispell/update ; then
    %{_prefix}/lib/ispell/update
fi

%postun -n ispell-british
if test -z "$YAST_IS_RUNNING" -a -x %{_prefix}/lib/ispell/update ; then
    %{_prefix}/lib/ispell/update
fi

%files
%defattr(-, root, root)
%doc suse/LIESMICH suse/README
%dir %{_prefix}/lib/ispell
%{_bindir}/buildhash
%{_bindir}/findaffix
%{_bindir}/icombine
%{_bindir}/ijoin
%{_bindir}/ispell
%{_bindir}/munchlist
%{_bindir}/sq
%{_bindir}/tryaffix
%{_bindir}/unsq
%{_prefix}/lib/ispell/ispell-emacs-menu.el
%dir %{_prefix}/lib/ispell/emacs
%{_prefix}/lib/ispell/emacs/english.el
%{_prefix}/lib/ispell/english.hash
%{_prefix}/lib/ispell/english.aff
%attr(0755,root,root) %{_prefix}/lib/ispell/update
%{_fillupdir}/sysconfig.ispell
%ghost %verify(not link mtime) /var/lib/dict/english.hash
%ghost %verify(not link mtime) /var/lib/dict/english.aff
%doc %{_mandir}/man1/buildhash.1.gz
%doc %{_mandir}/man1/findaffix.1.gz
%doc %{_mandir}/man1/ispell.1.gz
%doc %{_mandir}/man1/icombine.1.gz
%doc %{_mandir}/man1/ijoin.1.gz
%doc %{_mandir}/man1/munchlist.1.gz
%doc %{_mandir}/man1/sq.1.gz
%doc %{_mandir}/man1/tryaffix.1.gz
%doc %{_mandir}/man1/unsq.1.gz
%doc %{_mandir}/man5/ispell.5.gz

%files -n ispell-american
%defattr(-, root, root)
%{_prefix}/lib/ispell/american.hash
%{_prefix}/lib/ispell/americanmed.hash
%{_prefix}/lib/ispell/americanxlg.hash
%{_prefix}/lib/ispell/emacs/american.el
%{_prefix}/lib/ispell/american.aff

%files -n ispell-british
%defattr(-, root, root)
%{_prefix}/lib/ispell/british.hash
%{_prefix}/lib/ispell/britishmed.hash
%{_prefix}/lib/ispell/britishxlg.hash
%{_prefix}/lib/ispell/emacs/british.el
%{_prefix}/lib/ispell/british.aff

%changelog
