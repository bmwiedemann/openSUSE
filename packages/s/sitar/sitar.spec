#
# spec file for package sitar
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           sitar
Url:            http://sitar.berlios.de/
Version:        1.0.6
Release:        0
Summary:        System InformaTion at Runtime
License:        GPL-2.0+
Group:          System/Monitoring
Source0:        sitar-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE fix-syntax-errors-with-newer-perl.patch boo#899992 wbauer@tmo.at -- fix syntax errors when run with the perl in openSUSE 13.1 and higher
Patch:          fix-syntax-errors-with-newer-perl.patch
Patch1:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  groff
BuildArch:      noarch
PreReq:         %fillup_prereq

%description 
Sitar prepares system information using perl and binary tools, and by
reading the /proc file system. Output is in HTML, LaTeX and (docbook)
XML, and can be converted to PS and PDF.

This program must be run as "root".

sitar.pl includes scsiinfo by Eric Youngdale, Michael Weller
<eowmob@exp-math.uni-essen.de> and ide_info by David A. Hinds
<dhinds@hyper.stanford.edu>.

The accompanying tool "cfg2scm" is supplied for checking configuration
changes into SCMs (like SVN, CVS, ...) or creating a tar-file with all
relevant files.

Comment: Sitar is an ancient Indian instrument as well.



Authors:
--------
    Matthias Eckermann  <mge@suse.de> 
    and contributors

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
: ${SOURCE_DATE_EPOCH:=1168904229}
export SOURCE_DATE_EPOCH
make

%install
make DESTDIR=${RPM_BUILD_ROOT} install
#
mkdir -p $RPM_BUILD_ROOT%{_fillupdir}
mv $RPM_BUILD_ROOT/etc/sysconfig/sitar   $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.sitar
mv $RPM_BUILD_ROOT/etc/sysconfig/cfg2scm $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.cfg2scm

%files
%defattr(-,root,root)
%attr(700, root, root) /usr/sbin/sitar.pl
%attr(700, root, root) /usr/sbin/sitar
%attr(700, root, root) /usr/sbin/cfg2scm.pl
%dir /usr/share/sitar
%dir /var/lib/support
%doc sitar.html sitar.ps cfg2scm.html cfg2scm.ps LICENSE
/usr/share/man/man1/sitar.1.gz
/usr/share/man/man1/cfg2scm.1.gz
/usr/share/sitar/proc.txt
%{_fillupdir}/sysconfig.sitar
%{_fillupdir}/sysconfig.cfg2scm

%post
%{fillup_only -n sitar}
%{fillup_only -n cfg2scm}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
