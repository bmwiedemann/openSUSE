#
# spec file for package qt4-qtscript
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


%define date 20111225

Name:           qt4-qtscript
Version:        0.2.0
Release:        0
Summary:        Qt bindings generator for Qt Script
License:        SUSE-LGPL-2.1-with-nokia-exception-1.1
Group:          Development/Libraries/KDE
Url:            http://code.google.com/p/qtscriptgenerator/
Source0:        qtscriptgenerator-src-%{version}.tar.gz
Patch0:         qtscript-qt-no_phonon.diff
Patch1:         gcc-44.diff
Patch3:         fix-arm-build.diff
# PATCH-FIX-UPSTREAM https://github.com/qt-labs/qtscriptgenerator/pull/1
Patch4:         reproducible.patch
# PATCH-FIX-OPENSUSE
Patch5:         qtscript-qt-no_webkit.patch
BuildRequires:  libqt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%requires_eq    libqt4

%description
Qt Script Generator is a tool that generates Qt bindings for Qt Script.
With the generated bindings you get access to substantial portions of
the Qt API from within Qt Script.

%package doc
Summary:        Qt bindings generator for Qt Script
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description doc
Qt Script Generator is a tool that generates Qt bindings for Qt Script.
With the generated bindings you get access to substantial portions of
the Qt API from within Qt Script.

%prep
%setup -q -n qtscriptgenerator-src-%{version}
%patch0
%patch1
%ifarch %arm
%patch3
%endif
%patch4 -p1
%patch5 -p1

%build
export QTDIR=/usr
cd generator
qmake QMAKE_CXXFLAGS="%{optflags}"
make %{?_smp_mflags}
./generator
cd ../qtbindings
qmake QMAKE_CXXFLAGS="%{optflags}"
make %{?_smp_mflags}
cd ..

%install
# copying generated library files
# install doesn't do symlinks
mkdir -p %{buildroot}%{_libdir}/qt4/plugins/script/
cp -a plugins/script/libqtscript* %{buildroot}%{_libdir}/qt4/plugins/script/
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
install -c -m 644 README       %{buildroot}%{_defaultdocdir}/%{name}/README
install -c -m 644 LICENSE.LGPL  %{buildroot}%{_defaultdocdir}/%{name}/LICENSE.LGPL
# Copy generated docs in doc/ to doc directory
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/doc-html
cp -a doc/* %{buildroot}%{_defaultdocdir}/%{name}/doc-html/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/LICENSE.LGPL
%{_libdir}/qt4/plugins/script/libqtscript*

%files doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/doc-html

%changelog
