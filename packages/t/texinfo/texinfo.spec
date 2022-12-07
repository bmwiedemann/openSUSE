#
# spec file for package texinfo
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


# perl modules are not installed in global path
%global __provides_exclude ^(libtool|perl)\\(
Name:           texinfo
Version:        7.0.1
Release:        0
Summary:        Tools for creating documentation from texinfo sources
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/texinfo/
Source0:        https://ftp.gnu.org/pub/gnu/texinfo/texinfo-%{version}.tar.xz
Source1:        https://ftp.gnu.org/pub/gnu/texinfo/texinfo-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source42:       %{name}-rpmlintrc
Patch0:         texinfo-zlib.patch
Patch1:         install-info_exitcode.patch
BuildRequires:  automake
BuildRequires:  glibc-locale
BuildRequires:  help2man
BuildRequires:  libbz2-devel
BuildRequires:  libzio-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  perl-Text-Unidecode
BuildRequires:  perl-gettext
BuildRequires:  perl-macros
BuildRequires:  zlib-devel
Requires:       makeinfo = %{version}
Requires:       perl
Requires:       perl-Text-Unidecode
Requires:       perl-gettext
Requires:       texlive-bibtex
Requires:       texlive-latex
Requires:       texlive-makeindex
Requires:       texlive-pdftex
Requires:       texlive-tex
Requires:       texlive-texinfo
Recommends:     texi2html
Recommends:     texi2roff

%description
Texinfo is a documentation system that uses a single source file to
produce both online information and printed output.  Using Texinfo, you
can create a printed document with the normal features of a book,
including chapters, sections, cross-references, and indices.  From the
same Texinfo source file, you can create a menu-driven, online info
file with nodes, menus, cross-references, and indices using the included
makeinfo tool.

%package     -n info
Summary:        A Stand-Alone Terminal-Based Info Browser
Requires:       /usr/bin/gunzip
Requires:       /usr/bin/gzip
Recommends:     info-lang = %{version}

%description -n info
Info is a terminal-based program for reading documentation of computer
programs in the Info format. The GNU Project distributes most of its
on-line manuals in the Info format, so you need a program called "Info
reader" to read the manuals.

%package     -n info-std
Summary:        The info pages of the Info Browser
Supplements:    (info and patterns-base-documentation)
BuildArch:      noarch

%description -n info-std
Info is a terminal-based program for reading documentation of computer
programs in the Info format. The GNU Project distributes most of its
on-line manuals in the Info format, so you need a program called "Info
reader" to read the manuals.

%package     -n makeinfo
Summary:        Translator for converting texinfo documents to info format
# /usr/share/texinfo/Texinfo/Convert/NodeNameNormalization.pm uses Text::Unidecode
Requires:       perl(Text::Unidecode)
%requires_eq    perl
Suggests:       texinfo
Provides:       texinfo:%{_bindir}/makeinfo
Recommends:     info-lang = %{version}
Recommends:     makeinfo-lang = %{version}

%description -n makeinfo
Makeinfo translates Texinfo source documentation to various other
formats, by default Info files suitable for reading online with Emacs
or standalone GNU Info.

%lang_package -n info
%lang_package -n makeinfo

%prep
%setup -q
%autopatch -p1

%build
LANG=en_GB.UTF-8
export LANG
%configure \
	--with-external-Text-Unidecode \
	--enable-perl-xs
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/texinfo/*.a
if cmp  %{buildroot}%{_bindir}/pdftexi2dvi %{buildroot}%{_bindir}/texi2pdf
then
    rm -vf %{buildroot}%{_bindir}/pdftexi2dvi
    ln -sf texi2pdf %{buildroot}%{_bindir}/pdftexi2dvi
fi
if cmp  %{buildroot}%{_mandir}/man1/pdftexi2dvi.1 %{buildroot}%{_mandir}/man1/texi2pdf.1
then
    rm -vf %{buildroot}%{_mandir}/man1/pdftexi2dvi.1
    ln -sf texi2pdf.1%{?ext_man} %{buildroot}%{_mandir}/man1/pdftexi2dvi.1%{?ext_man}
fi

%if !0%{?usrmerged}
mkdir -p %{buildroot}/sbin
mv %{buildroot}%{_bindir}/install-info %{buildroot}/sbin/
ln -sf ../../sbin/install-info %{buildroot}%{_bindir}/install-info
%else
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/install-info %{buildroot}%{_sbindir}/
ln -sf ../sbin/install-info %{buildroot}%{_bindir}/install-info
%endif

%find_lang %{name} %{name}.lang
%find_lang %{name}_document %{name}_document.lang

%check
LANG=en_GB.UTF-8
export LANG
make %{?_smp_mflags} check

%global trigger_functions %{expand:
-- Check if rpm.execute() as function call is given
if type(rpm.execute) == "function" then
   execute = rpm.execute
else
  function execute(path, ...)
    local pid = posix.fork()
    if not pid then
       error(path .. ": fork failed: " .. posix.errno() .. "\n")
    elseif pid == 0 then
       assert(posix.exec(path, ...))
    else
       posix.wait(pid)
    end
  end
end
--
}

%filetriggerin -n info -p <lua> -- %{_infodir}
%trigger_functions
file = rpm.next_file()
while file do
    if string.match(file, "%%.info%%%{ext_info}$") then
	stat = posix.stat(file)
	if stat then
	    execute("%{_bindir}/install-info", "--info-dir=%{_infodir}", file)
	end
    end
    file = rpm.next_file()
end

%filetriggerun -n info -p <lua> -- %{_infodir}
%trigger_functions
file = rpm.next_file()
while file do
    if string.match(file, "%%.info%%%{ext_info}$") then
	stat = posix.stat(file)
	if not stat then
	    execute("%{_bindir}/install-info", "--quiet", "--delete", "--info-dir=%{_infodir}", file)
	end
    end
    file = rpm.next_file()
end

%files
%defattr(-,root,root,0755)
%license COPYING
%doc ABOUT-NLS AUTHORS NEWS README TODO
%doc doc/texinfo.tex doc/txi-*.tex doc/refcard/*.pdf
%{_bindir}/pod2texi
%{_bindir}/texi2dvi
%{_bindir}/texi2pdf
%{_bindir}/texindex
%{_bindir}/pdftexi2dvi
%{_infodir}/texinfo*%{ext_info}
%{_mandir}/man1/pod2texi.1%{?ext_man}
%{_mandir}/man1/texindex.1%{?ext_man}
%{_mandir}/man1/texi2dvi.1%{?ext_man}
%{_mandir}/man1/texi2pdf.1%{?ext_man}
%{_mandir}/man1/pdftexi2dvi.1%{?ext_man}
%{_mandir}/man5/texinfo.5%{?ext_man}
%attr(644,root,root) %{_datadir}/texinfo/texindex.awk

%files -n makeinfo-lang -f %{name}_document.lang

%files -n makeinfo
%defattr(-,root,root,0755)
%{_bindir}/makeinfo
%{_bindir}/texi2any
%{_infodir}/texi2any_*%{ext_info}
%{_mandir}/man1/makeinfo.1%{?ext_man}
%{_mandir}/man1/texi2any.1%{?ext_man}
%{_libdir}/texinfo
%exclude %{_datadir}/texinfo/texindex.awk
%{_datadir}/texinfo/

%files -n info-lang -f %{name}.lang

%files -n info
%defattr(-,root,root,0755)
%ghost %verify(not mode md5 size mtime) %{_infodir}/dir
%if !0%{?usrmerged}
/sbin/install-info
%else
%{_sbindir}/install-info
%endif
%{_bindir}/install-info
%{_bindir}/info
%{_mandir}/man1/info.1%{?ext_man}
%{_mandir}/man1/install-info.1%{?ext_man}
%{_mandir}/man5/info.5%{?ext_man}

%files -n info-std
%defattr(-,root,root,0755)
%{_infodir}/info-stnd.info%{?ext_info}

%changelog
