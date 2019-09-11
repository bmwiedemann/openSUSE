#
# spec file for package lifelines
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lifelines
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  docbook-utils
BuildRequires:  dos2unix
BuildRequires:  libjpeg-devel
BuildRequires:  libpng
BuildRequires:  libxslt-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-XML-DOM
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-SAX
BuildRequires:  perl-libwww-perl
BuildRequires:  texlive
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-latex
BuildRequires:  texlive-xmltex
%if 0%{?suse_version} > 1220
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-times
%endif
Version:        3.0.62
Release:        0
Summary:        The Lifelines Genealogy Program
License:        MIT
Group:          Productivity/Scientific/Other
Url:            http://lifelines.sourceforge.net/
Source:         http://download.sourceforge.net/lifelines/lifelines-3.0.62.tar.bz2
Source1:        sh.rellink
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         lifelines-3.0.62.dif
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         lifelines-3.0.59-funcptr.dif
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch2:         lifelines-3.0.60-array.dif
# PATCH-FIX-UPSTREAM Fix conflicting declaration
Patch3:         lifelines-decl.patch
BuildRequires:  tidy
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         _sysconfdir /etc
%global         ncursesw_config %(set -- %{_bindir}/ncursesw*-config; echo ${@:$#})

%description
Lifelines is terminal-based program that allows the tracking of
genealogical information.  The lifelines reports are the power of the
system but requires knowledge in the ll format.

%prep
%setup -q
%patch0  -p 0
%patch1 -p 0
%patch2 -p 0
%patch3 -p1

%build
CFLAGS="%{optflags} -fno-strict-aliasing -pipe $(%{ncursesw_config} --cflags)"
CPPFLAGS="-D_GNU_SOURCE -D_XOPEN_CURSES"
LDFLAGS="$(%{ncursesw_config} --libs)"
CC=gcc
export CC CFLAGS CPPFLAGS LDFLAGS
autoreconf -fi
./configure --prefix=%{_prefix} -exec-prefix=%{_prefix}	\
	    --libexecdir=%{_libdir}		\
	    --sysconfdir=%{_sysconfdir}		\
	    --libdir=%{_libdir}			\
	    --mandir=%{_mandir}			\
	    --infodir=%{_infodir}		\
	    --disable-rpath			\
	    --with-gnu-ld			\
	    --with-docs				\
	    --without-included-gettex		\
	    --with-libintl-prefix=%{_prefix}	\
	    --with-included-gettext=%{_prefix}
make
#chmod 644 docs/*.1
rm -f docs/*.pdf
make -C docs/

%install
. %{SOURCE1}
make DESTDIR=%{buildroot}			\
     docdir=%{_defaultdocdir}/lifelines/doc	\
     pkgdatadir=%{_defaultdocdir}/lifelines/doc	\
     install
make -C docs/ DESTDIR=%{buildroot}		\
     docdir=%{_defaultdocdir}/lifelines/doc	\
     pkgdatadir=%{_defaultdocdir}/lifelines/doc	\
     install
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 docs/*.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_datadir}/lifelines/reports/st
install -m 644 reports/*.l[li]    %{buildroot}%{_datadir}/lifelines/reports/
install -m 644 reports/st/*.l[li] %{buildroot}%{_datadir}/lifelines/reports/st/
mkdir -p %{buildroot}%{_datadir}/lifelines/tt
install -m 644 tt/*.tt  %{buildroot}%{_datadir}/lifelines/tt/
mkdir -p %{buildroot}%{_defaultdocdir}/lifelines/reports
install -m 644 reports/CREDIT %{buildroot}%{_defaultdocdir}/lifelines/reports/
install -m 644 reports/index.html reports/boc.gif reports/ll.png %{buildroot}%{_defaultdocdir}/lifelines/reports/
install -m 644 README ChangeLog NEWS AUTHORS LICENSE %{buildroot}%{_defaultdocdir}/lifelines/
rm -f  %{buildroot}%{_defaultdocdir}/lifelines/doc/*.l[li]
path=$(relpath %{buildroot}%{_datadir}/lifelines/reports %{buildroot}%{_defaultdocdir}/lifelines/doc)
for l in %{buildroot}%{_datadir}/lifelines/reports/*.l[li] ; do
    ln -sf ${path}/${l##*/} %{buildroot}%{_defaultdocdir}/lifelines/doc/
done
rm -f  %{buildroot}%{_defaultdocdir}/lifelines/doc/{README,NEWS,LICENSE,CREDIT,AUTHORS}
rm -f  %{buildroot}%{_defaultdocdir}/lifelines/doc/{INSTALL,README.MAINTAINERS.win32}
if test -e %{buildroot}%{_defaultdocdir}/lifelines/doc/.linesrc ; then
    mv %{buildroot}%{_defaultdocdir}/lifelines/doc/.linesrc \
       %{buildroot}%{_defaultdocdir}/lifelines/doc/dot.linesrc
fi
if test -e %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg ; then
    mv %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg \
       %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg.tmp
    dos2unix -n %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg.tmp \
                %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg
    rm -f %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg.tmp
fi
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_defaultdocdir}/lifelines
%{_bindir}/*
%{_datadir}/lifelines
%doc %{_mandir}/man1/*.gz

%changelog
