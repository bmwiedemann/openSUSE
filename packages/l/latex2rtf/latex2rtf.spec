#
# spec file for package latex2rtf
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


# Get the major version of makeinfo.
%define makeinfo_major_version %(MJ="`rpm -q --queryformat='%%{VERSION}' makeinfo | cut -c 1`"; echo $MJ)
%define mversion 2.3.18
Name:           latex2rtf
Version:        2.3.18a
Release:        0
Summary:        LaTeX to RTF Converter
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            http://latex2rtf.sourceforge.net/index.html
Source0:        http://downloads.sourceforge.net/project/latex2rtf/latex2rtf-unix/%{mversion}/latex2rtf-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix_latex2rtf_texi.patch ronisbr@gmail.com Fix info page of latex2rtf
Patch1:         fix_latex2rtf_texi.patch
BuildRequires:  gcc-c++
BuildRequires:  info
BuildRequires:  m4
BuildRequires:  makeinfo
BuildRequires:  texinfo
Requires:       ImageMagick
Requires:       netpbm
Requires:       texlive-scheme-basic
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
LaTeX2RTF is a translator program to convert LaTeX formatted text files into
“rich text format” (RTF) files. RTF is a published standard format by Microsoft.
This standard can be ambiguous in places, but RTF is supported by many text
editors. Specifically, it is supported by Microsoft Word. This means that the
conversion of a LaTeX document to RTF allows anyone with a copy of Word to
ponvert LaTeX files to Word .doc or .docx files.

%prep
%setup -q -n %{name}-%{mversion}

%patch1 -p1

%build

make DESTDIR=%{buildroot} \
     BINDIR=%{_bindir} \
     MANDIR=%{_mandir}/man1/ \
     INFODIR=%{_infodir}/ \
     SUPPORTDIR=%{_datadir}/latex2rtf \
     CFGDIR=%{_datadir}/latex2rtf/cfg \
     latex2rtf

make DESTDIR=%{buildroot} \
     BINDIR=%{_bindir} \
     MANDIR=%{_mandir}/man1/ \
     INFODIR=%{_infodir}/ \
     SUPPORTDIR=%{_datadir}/latex2rtf \
     CFGDIR=%{_datadir}/latex2rtf/cfg \
     doc

%install

make install DESTDIR=%{buildroot} \
             BINDIR=%{_bindir} \
             MANDIR=%{_mandir}/man1/ \
             INFODIR=%{_infodir}/ \
             SUPPORTDIR=%{_datadir}/latex2rtf \
             CFGDIR=%{_datadir}/latex2rtf/cfg

make install-info DESTDIR=%{buildroot} \
             BINDIR=%{_bindir} \
             MANDIR=%{_mandir}/man1/ \
             INFODIR=%{_infodir}/ \
             SUPPORTDIR=%{_datadir}/latex2rtf \
             CFGDIR=%{_datadir}/latex2rtf/cfg

# GZip man page.
gzip %{buildroot}/%{_mandir}/man1/latex2rtf.1
gzip %{buildroot}/%{_mandir}/man1/latex2png.1

# Fix permissions of docs.
chmod 644 ChangeLog HACKING README ToDo doc/credits doc/copying.txt

%files
%defattr(-,root,root)
%doc ChangeLog HACKING README ToDo doc/credits doc/copying.txt
%{_bindir}/latex2rtf
%attr(0755,root,root) %{_bindir}/latex2png
%dir %{_datadir}/latex2rtf
%attr(0644,root,root) %{_datadir}/latex2rtf/latex2rtf.*
%dir %{_datadir}/latex2rtf/cfg
%attr(0644,root,root) %{_datadir}/latex2rtf/cfg/*.cfg
%attr(0644,root,root) %{_mandir}/man1/latex2rtf.1.gz
%attr(0644,root,root) %{_mandir}/man1/latex2png.1.gz
%attr(0644,root,root) %{_infodir}/latex2rtf.info.gz

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info --delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%changelog
