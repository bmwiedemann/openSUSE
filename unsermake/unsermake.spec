#
# spec file for package unsermake (Version 0.4_20070504)
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
# icecream 0


Name:           unsermake
BuildRequires:  docbook-xsl-stylesheets libxslt python-devel
License:        GPL-2.0+
Group:          Development/Tools/Building
Summary:        Replacement for make and automake
Version:        0.4_20070504
Release:        135
# svn export svn+ssh://svn.kde.org/home/kde/trunk/kdenonbeta/unsermake unsermake-%version
Source0:        %name-%version.tar.bz2
Source1:        %name.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires

%description
Developed for building KDE, Unsermake replaces the functionality of
automake and make.



Authors:
--------
    Stephan Kulow <coolo@kde.org>

%prep
%setup -q

%build
xsltproc /usr/share/xml/docbook/stylesheet/nwalsh/*/manpages/docbook.xsl %{SOURCE1}

%install
install -d $RPM_BUILD_ROOT%py_sitedir/unsermake
cp *.py *.um $RPM_BUILD_ROOT%py_sitedir/unsermake
install -d $RPM_BUILD_ROOT%_bindir
cat > $RPM_BUILD_ROOT%_bindir/unsermake << EOF
#! /bin/sh
exec /usr/bin/python -c 'import unsermake; unsermake.main()' --modules %py_sitedir/unsermake "\$@"
EOF
chmod 755 $RPM_BUILD_ROOT%_bindir/unsermake
pushd $RPM_BUILD_ROOT%py_sitedir/unsermake
python %py_libdir/py_compile.py *.py
PYTHONOPTIMIZE=1 python %py_libdir/py_compile.py *.py
popd
%if %suse_version > 920
install -m 644 -D unsermake.1 $RPM_BUILD_ROOT%_mandir/man1/unsermake.1
%endif

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc README
%py_sitedir/unsermake
%_bindir/unsermake
%if %suse_version > 920
%_mandir/man1/unsermake.1*
%endif

%changelog
* Fri May 11 2007 coolo@suse.de
- copy documentation that disappeared from SVN
* Fri May 04 2007 coolo@suse.de
- update to 20070504:
  - fix python's help modules (#258385)
* Tue Mar 07 2006 dmueller@suse.de
- update to 20060307:
  - ignore generated .ui4 files in Qt4 build environments
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Jan 11 2006 dmueller@suse.de
- update to 20060111
* Wed Dec 21 2005 dmueller@suse.de
- update to 20051221
* Tue Nov 01 2005 dmueller@suse.de
- update to 20051101
* Thu Oct 06 2005 coolo@suse.de
- fixed another error ;(
* Wed Oct 05 2005 coolo@suse.de
- fix syntax
* Wed Oct 05 2005 coolo@suse.de
- make command line handling way more complex to
  support VERBOSE=1 at random places
* Thu Sep 08 2005 coolo@suse.de
- fixing file permissions
* Wed Aug 03 2005 ro@suse.de
- fix requires
* Thu Jul 28 2005 coolo@suse.de
- add require to python
* Tue Jul 19 2005 coolo@suse.de
- update from svn
* Thu Apr 14 2005 coolo@suse.de
- another fix for man pages
* Tue Mar 15 2005 coolo@suse.de
- fix man page support
* Mon Mar 14 2005 coolo@suse.de
- fix assembler files (and reduce the tar size _slightly_)
* Wed Feb 23 2005 adrian@suse.de
- update to current CVS
* Mon Feb 14 2005 adrian@suse.de
- update from CVS
* Fri Feb 11 2005 adrian@suse.de
- update from CVS
* Mon Feb 07 2005 adrian@suse.de
- update from CVS
* Tue Feb 01 2005 adrian@suse.de
- update from CVS
* Mon Jan 31 2005 coolo@suse.de
- update from CVS
* Mon Jan 31 2005 adrian@suse.de
- fix build on released distributions
* Tue Jan 25 2005 coolo@suse.de
- new package
