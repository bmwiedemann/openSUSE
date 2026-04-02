#
# spec file for package texinfo
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%global __provides_exclude ^perl\\(
Name:           texinfo
Version:        7.3
Release:        0
Summary:        Tools for creating documentation from texinfo sources
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/texinfo/
Source0:        https://ftp.gnu.org/pub/gnu/texinfo/texinfo-%{version}.tar.xz
Source1:        https://ftp.gnu.org/pub/gnu/texinfo/texinfo-%{version}.tar.xz.sig
# All GPG keys from the maintainers are available at https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=texinfo&download=1
Source2:        %{name}.keyring
Source42:       %{name}-rpmlintrc
Patch0:         texinfo-zlib.patch
Patch1:         install-info_exitcode.patch
BuildRequires:  gawk >= 4.0
BuildRequires:  glibc-locale
BuildRequires:  help2man
BuildRequires:  libbz2-devel
BuildRequires:  libzio-devel >= 1.09
BuildRequires:  ncurses-devel
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl-macros
BuildRequires:  zlib-devel
BuildRequires:  perl(Archive::Zip)
# Testing dependencies
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Test::Deep)
# Proxy for {,busybox-}gawk
Requires:       /usr/bin/awk
# Proxies for {,busybox-}coreutils
Requires:       /usr/bin/cat
Requires:       /usr/bin/uniq
# Proxies for {,busybox-}diffutils
Requires:       /usr/bin/cmp
Requires:       /usr/bin/diff
# Proxy for {,busybox-}grep
Requires:       /usr/bin/grep
# Proxy for {,busybox-}sed
Requires:       /usr/bin/sed
# Proxy for {bash,busybox}-sh
Requires:       /usr/bin/sh
# Proxy for {,busybox-}tar
Requires:       /usr/bin/tar
Requires:       makeinfo = %{version}
Requires:       perl >= 5.8.1
Requires:       texlive-biber
Requires:       texlive-bibtex
Requires:       texlive-dvipdfmx
Requires:       texlive-dvips
Requires:       texlive-latex
Requires:       texlive-makeindex
Requires:       texlive-pdftex
Requires:       texlive-tex
Requires:       texlive-texinfo
# Recommended as users are used to them being installed
Recommends:     texi2html
# Recommended as users are used to them being installed
Recommends:     texi2roff
Recommends:     texlive-thumbpdf

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
Recommends:     /usr/bin/man
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
# Keep in sync with perl-libintl-perl
Requires:       gettext-runtime >= 0.12.2
Recommends:     perl(Archive::Zip)
Recommends:     perl(File::ShareDir)
Requires:       perl
%perl_requires
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
%autosetup -p1

%build
%configure \
	--enable-additional-checks \
	--enable-perl-xs \
	--enable-t2a-tests
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/texi2any/*.a
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

# For SUSE systems pre 15.5, install to /sbin, otherwise install to /usr/sbin
%if 0%{?suse_version} < 1550
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
make %{?_smp_mflags} check

%post -n makeinfo -p /sbin/ldconfig

%postun -n makeinfo -p /sbin/ldconfig

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

%if 0%{?suse_version} >= 1699
%transfiletriggerin -n info -p <lua> -- %{_infodir}
%else
%filetriggerin -n info -p <lua> -- %{_infodir}
%endif
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

%if 0%{?suse_version} >= 1699
%transfiletriggerun -n info -p <lua> -- %{_infodir}
%else
%filetriggerun -n info -p <lua> -- %{_infodir}
%endif
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
%{_infodir}/texinfo.info*%{ext_info}
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
%{_infodir}/texi2any_api.info%{ext_info}
%{_infodir}/texi2any_internals.info%{ext_info}
%{_infodir}/texi2any_internals.info-1%{ext_info}
%{_infodir}/texi2any_internals.info-2%{ext_info}
%{_mandir}/man1/makeinfo.1%{?ext_man}
%{_mandir}/man1/texi2any.1%{?ext_man}
%{_libdir}/texi2any
%exclude %{_datadir}/texinfo/texindex.awk
%{_datadir}/texinfo
%{_datadir}/texi2any

%files -n info-lang -f %{name}.lang

%files -n info
%defattr(-,root,root,0755)
%ghost %verify(not mode md5 size mtime) %{_infodir}/dir
%if 0%{?suse_version} < 1550
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
