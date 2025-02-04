#
# spec file for package spectcl
#
# Copyright (c) 2025 SUSE LLC
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


Name:           spectcl
Version:        1.2.1.9
Release:        0
Summary:        Interface Builder for Tcl/Tk and Java
License:        SUSE-Sun-Laboratories
Group:          Development/Tools/GUI Builders
URL:            http://spectcl.sourceforge.net/
Source:         http://optimate.dl.sourceforge.net/project/spectcl/SpecTcl/1.2.2a/SpecTcl.tar.gz
Patch0:         SpecTcl1.1-dir.patch
Patch1:         SpecTcl1.1-tk8.4.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       SpecTcl1.1
Requires:       tk

%description
An interface builder for Tcl/Tk and Java.

Main Features of SpecTcl: * Easy to Learn:SpecTcl's drag & drop
   interface along with a powerful toolbar and on-line help that
   make it easy to start building GUI applications.

* Tcl and Java Support: SpecTcl generates both Tcl and Java code.
   Note: this generates code for the old JDK 1.0

* Platform Independent: SpecTcl runs on all major platforms:
   Solaris, SunOS, Linux, Windows 95, Windows NT, MacOS, and Irix.

* Constraint Based Geometry Manager: Alignment and resizing of widgets
(buttons, check boxes, and more.) is automatic. This makes creating
dynamic UIs and cross platform UIs a snap!



Authors:
--------
    Raymond Johnson <spectcl@tcl.eng.sun.com>
    Ioi Lam
    Allan Pratt

%prep
%setup -q -n SpecTcl
#%%patch -P 0
#%%patch -P 1

%build

%install
#touch /lastinit
INSTALLDIR="install -m 755 -d"
INSTALLEXE="install -m 755"
INSTALLFIL="install -m 644"
export SPECTCL_LIB=/usr/share/SpecTcl
export DOCDIR=%{_defaultdocdir}/spectcl
${INSTALLDIR} $RPM_BUILD_ROOT/usr/bin
${INSTALLDIR} $RPM_BUILD_ROOT/${SPECTCL_LIB}/bin
${INSTALLDIR} $RPM_BUILD_ROOT/${SPECTCL_LIB}/demo/images
${INSTALLDIR} $RPM_BUILD_ROOT/${SPECTCL_LIB}/examples
${INSTALLDIR} $RPM_BUILD_ROOT/${SPECTCL_LIB}/SpecTcl/help
${INSTALLDIR} $RPM_BUILD_ROOT/${SPECTCL_LIB}/SpecTcl/images
${INSTALLDIR} $RPM_BUILD_ROOT/${DOCDIR}
( cd bin && ${INSTALLEXE} specTcl specJava $RPM_BUILD_ROOT/${SPECTCL_LIB}/bin )
for i in `find SpecTcl -type f`
do
    ${INSTALLFIL} $i $RPM_BUILD_ROOT/${SPECTCL_LIB}/$i
done
for i in `find demo -type f`
do
    ${INSTALLFIL} $i $RPM_BUILD_ROOT/${SPECTCL_LIB}/$i
done
for i in `find examples -type f`
do
    ${INSTALLFIL} $i $RPM_BUILD_ROOT/${SPECTCL_LIB}/$i
done
(
    cd $RPM_BUILD_ROOT/usr/bin && \
    rm -f specTcl  && ln -s ${SPECTCL_LIB}/bin/specTcl && \
    rm -f specJava && ln -s ${SPECTCL_LIB}/bin/specJava
)
#fix executable permissions for tcl scripts
cd $RPM_BUILD_ROOT/${SPECTCL_LIB}/SpecTcl
chmod ugo+x *tcl

%files
%defattr(-,root,root)
%doc license.terms changes README README.JAVA INSTALL.JAVA
%docdir /usr/share/SpecTcl/SpecTcl/help
/usr/bin/specTcl
/usr/bin/specJava
/usr/share/SpecTcl

%changelog
