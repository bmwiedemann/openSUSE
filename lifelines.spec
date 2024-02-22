#
# spec file for package lifelines
#
# Copyright (c) 2024 SUSE LLC
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


Name:           lifelines
%global commit      4f417309
%global longcommit  4f417309c1f1c188f5c67b099b4686ab8ff572ff
Version:        3.1.1+%{commit}
Release:        0
Summary:        The Lifelines Genealogy Program
License:        MIT
Group:          Productivity/Scientific/Other
URL:            https://github.com/lifelines/lifelines
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-SUSE mainly to get paths correct if installed as system package
Patch0:         lifelines-%{commit}.dif
# PATCH-FIX-SUSE avoid memory leak as well as no initialized array
Patch1:         lifelines-%{commit}-array.dif
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  dblatex
BuildRequires:  docbook-utils
BuildRequires:  dos2unix
BuildRequires:  libjpeg-devel
BuildRequires:  libpng
BuildRequires:  libxslt-devel
BuildRequires:  lynx
BuildRequires:  ncurses-devel
BuildRequires:  perl-XML-DOM
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-SAX
BuildRequires:  perl-libwww-perl
BuildRequires:  texlive
BuildRequires:  texlive-babel
BuildRequires:  texlive-babel-swedish
BuildRequires:  texlive-cmap
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-fancybox
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-jknapltx
BuildRequires:  texlive-latex
BuildRequires:  texlive-times
BuildRequires:  texlive-xmltex
BuildRequires:  tidy
BuildRequires:  w3m
BuildRequires:  xmlto
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Lifelines is terminal-based program that allows the tracking of
genealogical information.  The lifelines reports are the power of the
system but requires knowledge in the ll format.

%prep
%setup -q -c -T -n %{name}-%{commit}
tar -x  --strip-components=1 -z -f %{SOURCE0}
%patch -P0 -p0 -b .p0
%patch -P1 -p0 -b .p1

%build
CFLAGS="%{optflags} -fno-strict-aliasing -pipe $(pkg-config ncursesw --cflags) $(getconf LFS_CFLAGS)"
CPPFLAGS="-D_GNU_SOURCE -D_XOPEN_CURSES"
LIBS="$(pkg-config ncursesw --libs)"
CC=gcc
export CC CFLAGS CPPFLAGS LIBS
autoreconf -fi
%configure  --disable-rpath			\
	    --with-gnu-ld			\
	    --with-docs				\
	    --with-libintl-prefix=%{_prefix}
make %{?_smp_mflags}
make -C docs/
dos2unix lines.cfg

%install
make DESTDIR=%{buildroot}		\
     docdir=%{_defaultdocdir}/%{name}	\
     pkgdatadir=%{_datadir}/%{name}	\
     install
make -C docs/ DESTDIR=%{buildroot}	\
     docdir=%{_defaultdocdir}/%{name}	\
     pkgdatadir=%{_datadir}/%{name}	\
     install
%find_lang %{name}
rm -vf %{buildroot}%{_defaultdocdir}/%{name}/INSTALL
mkdir -p %{buildroot}%{_sysconfdir}/skel
mv %{buildroot}%{_defaultdocdir}/%{name}/.linesrc \
   %{buildroot}%{_sysconfdir}/skel/
chmod 755 %{buildroot}%{_datadir}/%{name}/gen_index
rm -vf %{buildroot}%{_datadir}/%{name}/desc-tex2/tree.tex
rm -vf %{buildroot}%{_datadir}/%{name}/pedtex/tree.tex
ln -sf ../tree.tex %{buildroot}%{_datadir}/%{name}/desc-tex2/tree.tex
ln -sf ../tree.tex %{buildroot}%{_datadir}/%{name}/pedtex/tree.tex

%files -f %{name}.lang
%defattr(-,root,root)
%config %{_sysconfdir}/skel/.linesrc
%doc %{_defaultdocdir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}
%doc %{_mandir}/man1/*.gz

%changelog
