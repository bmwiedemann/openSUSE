#
# spec file for package html2ps
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


Name:           html2ps
Version:        1.0b7
Release:        0
URL:            http://user.it.uu.se/~jan/html2ps.html
Summary:        HTML to PostScript Converter
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/HTML/Tools
Source0:        http://user.it.uu.se/~jan/%name-%version.tar.gz
Source1:        html2psrc
Patch0:         %{name}-1.0b5-open.diff
Patch1:         %{name}-1.0b5-opt.diff
Patch2:         document_dsc_option.patch
Patch3:         remove_latin1_char.patch
Patch4:         xhtml2ps_defaults.patch
Patch5:         default_paper_size.patch
Patch6:         proper_variable_escaping.patch
Patch7:         shell_tricks_removed.patch
Patch8:         large_eps_fix.patch
Patch9:         DSC_to_dsc.patch
Patch10:        fix_ps.patch
Patch11:        checker_warning.patch
Patch12:        upstream_changelog.patch
Patch13:        perl-deprecations.patch
Patch14:        html2ps-1.0b7-tmpname.patch
BuildRequires:  ImageMagick
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-x11
BuildRequires:  jpeg
BuildRequires:  netpbm
BuildRequires:  perl-libwww-perl
BuildRequires:  texlive-latex
Requires:       ImageMagick
Requires:       ghostscript_any
Requires:       gv
Requires:       netpbm
Requires:       perl
Requires:       perl-libwww-perl
BuildArch:      noarch

%description
An HTML to PostScript converter written in Perl.  Html2ps understands
many of the HTML 4.0 features.	From the home page
(http://www.tdb.uu.se/~jan/html2ps.html):

* Many ways to control the appearance; this is mostly done using
   configuration files.
* Support for processing multiple documents, can be done
   automatically by recursively following links.
* A table of contents can be generated, either from the links in a
   document or automatically from document headings.
* Configurable page headers and footers that can, for example,
   contain document title, URL, page number, current heading, and
   date.
* Automatic hyphenation and text justification can be selected.

%prep
%autosetup -p1

%build

%install
install -d -m755 %{buildroot}/%{_bindir}/
install -d -m755 %{buildroot}/%{_sysconfdir}/
install -d -m755 %{buildroot}/%{_prefix}/lib/html2ps/
install -d -m755 %{buildroot}/%{_mandir}/man{1,5}/
install -m755 html2ps %{buildroot}/%{_bindir}/
install -m755 contrib/xhtml2ps/xhtml2ps %{buildroot}/%{_bindir}/
install -m644 %{S:1} %{buildroot}/%{_sysconfdir}/
install -m644 hyphen.tex %{buildroot}/%{_prefix}/lib/html2ps/
install -m644 html2ps.1 %{buildroot}/%{_mandir}/man1/
install -m644 html2psrc.5 %{buildroot}/%{_mandir}/man5/

%files
%defattr(-, root, root)
%license COPYING
%doc README html2ps.html
%config %{_sysconfdir}/html2psrc
%doc %{_mandir}/man?/*
%{_bindir}/html2ps
%{_bindir}/xhtml2ps
%{_prefix}/lib/html2ps/

%changelog
