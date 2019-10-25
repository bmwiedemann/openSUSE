#
# spec file for package texinfo
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# perl modules are not installed in global path
%global __provides_exclude ^(libtool|perl)\\(
Name:           texinfo
Version:        6.6
Release:        0
Summary:        Tools for creating documentation from texinfo sources
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Texinfo
URL:            https://www.gnu.org/software/texinfo/
Source0:        https://ftp.gnu.org/pub/gnu/texinfo/texinfo-%{version}.tar.xz
Source1:        https://ftp.gnu.org/pub/gnu/texinfo/texinfo-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source42:       %{name}-rpmlintrc
Patch1:         texinfo-zlib.patch
Patch2:         install-info_exitcode.patch
BuildRequires:  automake
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
Group:          Productivity/Publishing/Texinfo
Requires:       gzip

%description -n info
Info is a terminal-based program for reading documentation of computer
programs in the Info format. The GNU Project distributes most of its
on-line manuals in the Info format, so you need a program called "Info
reader" to read the manuals.

%package     -n info-std
Summary:        The info pages of the Info Browser
Group:          Productivity/Publishing/Texinfo
Supplements:    packageand(info:patterns-base-documentation)
BuildArch:      noarch

%description -n info-std
Info is a terminal-based program for reading documentation of computer
programs in the Info format. The GNU Project distributes most of its
on-line manuals in the Info format, so you need a program called "Info
reader" to read the manuals.

%package     -n makeinfo
Summary:        Translator for converting texinfo documents to info format
# /usr/share/texinfo/Texinfo/Convert/NodeNameNormalization.pm uses Text::Unidecode
Group:          Productivity/Publishing/Texinfo
Requires:       perl(Text::Unidecode)
%requires_eq    perl
Suggests:       texinfo
Provides:       texinfo:%{_bindir}/makeinfo

%description -n makeinfo
Makeinfo translates Texinfo source documentation to various other
formats, by default Info files suitable for reading online with Emacs
or standalone GNU Info.

%prep
%setup -q
%patch1 -p1 -b .zio
%patch2 -p1

%build
LANG=en_GB.UTF-8
export LANG
%configure \
	--with-external-Text-Unidecode \
	--enable-perl-xs
make %{?_smp_mflags}

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
    ln -sf texi2pdf.1.gz %{buildroot}%{_mandir}/man1/pdftexi2dvi.1.gz
fi

mkdir -p %{buildroot}/sbin
mv %{buildroot}%{_bindir}/install-info %{buildroot}/sbin/
ln -sf ../../sbin/install-info %{buildroot}%{_bindir}/install-info

%find_lang %{name} %{name}.lang
%find_lang %{name}_document %{name}_document.lang

%check
LANG=en_GB.UTF-8
export LANG
make %{?_smp_mflags} check

%filetriggerin -n info -p <lua> -- %{_infodir}
-- TODO: replace with rpm.execute after rpm 4.15
function execute(path, ...)
  local pid = posix.fork()
  if pid == 0 then
     posix.exec(path, ...)
     io.write(path, ": exec failed: ", posix.errno(), "\n")
     os.exit(1)
  end
  if not pid then
     error(path .. ": fork failed: " .. posix.errno() .. "\n")
  end
  posix.wait(pid)
end
--
file = rpm.next_file()
while file do
    if string.match(file, "%%.info%%.gz$") then
	execute("/usr/bin/install-info", "--info-dir=%{_infodir}", file)
    end
    file = rpm.next_file()
end

%filetriggerun -n info -p <lua> -- %{_infodir}
-- TODO: replace with rpm.execute after rpm 4.15
function execute(path, ...)
  local pid = posix.fork()
  if pid == 0 then
     posix.exec(path, ...)
     io.write(path, ": exec failed: ", posix.errno(), "\n")
     os.exit(1)
  end
  if not pid then
     error(path .. ": fork failed: " .. posix.errno() .. "\n")
  end
  posix.wait(pid)
end
--
file = rpm.next_file()
while file do
    if string.match(file, "%%.info%%.gz$") then
	execute("/usr/bin/install-info", "--quiet", "--delete", "--info-dir=%{_infodir}", file)
    end
    file = rpm.next_file()
end

%files -f %{name}_document.lang
%defattr(-,root,root,0755)
%license COPYING
%doc ABOUT-NLS AUTHORS NEWS README TODO
%doc doc/texinfo.tex doc/txi-*.tex
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

%files -n makeinfo -f %{name}.lang
%defattr(-,root,root,0755)
%{_bindir}/makeinfo
%{_bindir}/texi2any
%{_mandir}/man1/makeinfo.1%{?ext_man}
%{_mandir}/man1/texi2any.1%{?ext_man}
%{_libdir}/texinfo
%exclude %{_datadir}/texinfo/texindex.awk
%{_datadir}/texinfo/

%files -n info
%defattr(-,root,root,0755)
%ghost %verify(not md5 size mtime) %{_infodir}/dir
/sbin/install-info
%{_bindir}/install-info
%{_bindir}/info
%{_mandir}/man1/info.1%{?ext_man}
%{_mandir}/man1/install-info.1%{?ext_man}
%{_mandir}/man5/info.5%{?ext_man}

%files -n info-std
%defattr(-,root,root,0755)
%{_infodir}/info-stnd.info%{?ext_info}

%changelog
