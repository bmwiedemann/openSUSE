#
# spec file for package lilypond
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define fontdir %{_datadir}/fonts
%define ttfdir  %{fontdir}/truetype
Name:           lilypond
Version:        2.18.2
Release:        0
Summary:        A typesetting system for music notation
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Other
Url:            http://www.lilypond.org
Source0:        http://download.linuxaudio.org/lilypond/sources/v2.18/lilypond-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://savannah.gnu.org/patch/index.php?9370
Patch0:         reproducible.patch
# PATCH-FIX-UPSTREAM j.mairboeck@gmail.com -- https://sourceforge.net/p/testlilyissues/issues/4814/
Patch1:         Avoid-segfault-in-grob.cc-with-gcc-6.patch
# Patches taken from Debian, see headers for info.
Patch2:         0101-read_relocation_dir-in-lilypond_datadir-too.patch
Patch3:         add_dircategories_to_documentation.patch
Patch4:         add_set-global-fonts_function.patch
Patch5:         hurd_file_name_support.patch
Patch6:         Issue-5243-1-editor-scm-Add-shell-quote-argument-function.diff
Patch7:         Issue-5243-2-Let-get-editor-use-shell-quote-argument.diff
Patch8:         Issue-5243-3-More-conservative-parsing-of-textedit-URIs.diff
Patch9:         use_cstring_and_ctype_includes.patch
Patch10:        use_system_correctly.patch
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  dblatex
BuildRequires:  flex
BuildRequires:  fontforge
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ghostscript >= 8.15
BuildRequires:  ghostscript-fonts-std
BuildRequires:  libguile1-devel >= 1.8
BuildRequires:  makeinfo
BuildRequires:  mftrace >= 1.1.19
BuildRequires:  potrace-devel
# Needed for pngtopnm
BuildRequires:  netpbm
BuildRequires:  pkgconfig
BuildRequires:  python-devel >= 2.4.0
BuildRequires:  rsync
BuildRequires:  t1utils
BuildRequires:  texinfo >= 4.8
BuildRequires:  texlive-extratools
BuildRequires:  texlive-latex
BuildRequires:  texlive-lh
BuildRequires:  texlive-metafont
BuildRequires:  texlive-metapost
BuildRequires:  vim-base
BuildRequires:  zip
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pango) >= 1.12.0
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
Requires:       ghostscript >= 8.15
Requires:       lilypond-century-schoolbook-l-fonts = %{version}
Requires:       lilypond-emmentaler-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Package texi2html was split off from texinfo in current Factory.
%if 0%{?suse_version} > 1320
BuildRequires:  texi2html
%else
BuildRequires:  texlive-filesystem
%endif

%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

%package century-schoolbook-l-fonts
Summary:        Lilypond Century Schoolbook L fonts
Group:          System/X11/Fonts
Requires:       lilypond-fonts-common = %{version}
BuildArch:      noarch

%description century-schoolbook-l-fonts
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

These are the Century Schoolbook L fonts included in the package.

%package emmentaler-fonts
Summary:        Lilypond emmentaler fonts
Group:          System/X11/Fonts
Requires:       lilypond-fonts-common = %{version}
BuildArch:      noarch

%description emmentaler-fonts
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

These are the emmentaler fonts included in the package.

%package fonts-common
Summary:        Lilypond fonts common dir
Group:          System/X11/Fonts
BuildArch:      noarch

%description fonts-common
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

This contains the directory common to all lilypond fonts.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10

%build
export LIBS="$LIBS  -lglib-2.0 -lgobject-2.0"
%configure --without-kpathsea \
	--disable-checking \
	--with-ncsb-dir=%{_datadir}/ghostscript/fonts/
# Build sometimes fails with multiple threads.
make %{_smp_mflags} || make -j1

%install
vimver=$(vim --version | head -n1 | grep -Po "\d\.\d" | sed 's|\.||')
%make_install package_infodir=%{_infodir} \
	vimdir="%{_datadir}/vim/vim$vimver"

chmod +x %{buildroot}%{_libdir}/%{name}/%{version}/python/midi.so

# Symlink lilypond-init.el in emacs' site-start.d directory
pushd %{buildroot}%{_datadir}/emacs/site-lisp
mkdir site-start.d
ln -s ../lilypond-init.el site-start.d
popd

# Change encoding to UTF8
pushd %{buildroot}%{_infodir}
iconv -f iso-8859-1 -t utf-8 music-glossary.info > music-glossary.info.utf8
mv music-glossary.info.utf8 music-glossary.info
sed -e s,lilypond/,, -i *.info
popd

rm -f %{buildroot}%{_infodir}/dir

%find_lang %{name}

mkdir -p %{buildroot}%{ttfdir}
mv %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf/*.otf %{buildroot}%{ttfdir}
rmdir %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf
ln -s %{ttfdir} %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf

%post
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-changes.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-contributor.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-essay.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-extending.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-internals.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-learning.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-notation.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-usage.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-web.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-changes.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-contributor.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-essay.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-extending.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-internals.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-learning.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-notation.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-usage.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-web.info.gz

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS.txt COPYING DEDICATION HACKING LICENSE*
%doc NEWS.txt README.txt ROADMAP VERSION
%{_bindir}/*
%{_libdir}/lilypond
%{_datadir}/lilypond
%{_datadir}/emacs/site-lisp
%{_datadir}/vim/vim*
%{_infodir}/*%{ext_info}
%{_mandir}/man1/*

%files century-schoolbook-l-fonts
%defattr(-,root,root,-)
%{ttfdir}/CenturySchL*otf

%files emmentaler-fonts
%defattr(-,root,root,-)
%{ttfdir}/emmentaler*otf

%files fonts-common
%defattr(-,root,root,-)
%doc COPYING
%defattr(0644,root,root,0755)
%dir %{ttfdir}

%changelog
