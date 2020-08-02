#
# spec file for package tei-roma (Version 2.11)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           tei-roma
Summary:        TEI Schema or DTD Generator
Version:        2.11
Release:        57
License:        GPL-2.0+
Group:          Productivity/Publishing/XML
Source0:        http://ftp1.sourceforge.net/sourceforge/tei/tei-roma-%{version}.zip
Patch:          roma-dir.diff
# PATCH-FIX-OPENSUSE tei-roma-2.11-fix-race.patch bmwiedemann@opensuse
Patch1:         tei-roma-2.11-fix-race.patch
Url:            http://www.tei-c.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       /usr/bin/xsltproc trang perl
BuildRequires:  unzip

%description
Roma is a shell script and XSL stylesheets for building a customized
TEI schema or DTD.  It uses xsltproc, trang, and Perl.



%define INSTALL install -m755 -s
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define xml_dir %{_datadir}/xml
%define xml_mod_dir %{xml_dir}/tei
%define xml_mod_style_dir %{xml_mod_dir}
%define xml_mod_style_prod_dir %{xml_mod_style_dir}/rahtz
%define xml_mod_style_prod_ver_dir %{xml_mod_style_prod_dir}/%{version}

%prep
%setup -q
# unzip -q -a %{SOURCE0}
%patch -p 1
%patch1 -p1
/bin/chmod -Rf a+rX,g-w,o-w .

%build

%install
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_mod_dir}
make release
(cd release; tar cf - . ) | (cd $RPM_BUILD_ROOT/%{xml_mod_dir}; tar xf - )
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
  $RPM_BUILD_ROOT%{_mandir}/man1
%{INSTALL_SCRIPT} roma.sh $RPM_BUILD_ROOT%{_bindir}/roma
cp -p roma.1 $RPM_BUILD_ROOT%{_mandir}/man1
# chmod 755 $RPM_BUILD_ROOT%{_bindir}/roma

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%dir %{xml_mod_dir}
%attr(755, root, root) %{xml_mod_dir}/%name/roma.sh
%attr(755, root, root) %{xml_mod_dir}/%name/roma/res/merge.pl
%{xml_mod_dir}/tei-roma
%attr(755, root, root) %{_bindir}/roma
%{_mandir}/man1/roma*

%changelog
* Thu Nov 29 2007 ke@suse.de
- Update to version 2.11.
* Mon Apr 02 2007 ke@suse.de
- Update to version 2.8.
- Install the roma man page.
* Thu Mar 29 2007 coolo@suse.de
- Fix BuildRequires
* Fri Jan 12 2007 ke@suse.de
- Remove /usr/share/xml from the files list.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Nov 16 2005 ke@suse.de
- New package: Version 1.7.10.
