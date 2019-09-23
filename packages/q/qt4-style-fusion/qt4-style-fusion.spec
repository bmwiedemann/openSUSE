#
# spec file for package qt4-style-fusion
#
# Copyright (c) 2015,2017 <opensuse.lietuviu.kalba@gmail.com>.
# Copyright (c) 2015 Sandro Mani <manisandro@gmail.com>.
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


Name:           qt4-style-fusion
Version:        hg20151214
Release:        0
Summary:        Fusion widget style for Qt4

License:        LGPL-2.0+
URL:            https://code.google.com/p/fusion-qt4/
Source0:        qt4-style-fusion-%{version}.tar.xz
# Taken from Qt4 sources
Source1:        qstylehelper.cpp
# Fix build scripts
Patch0:         fusion-qt4_build.patch
Provides:       fusion-qt4 = hg20151214
Obsoletes:      fusion-qt4 <= hg20151112
BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:  libqt4-private-headers-devel
%requires_eq    libqt4
%endif
%if 0%{?fedora}
BuildRequires:  qt4-devel-private
%endif


%description
Qt4 backport of the Qt5 fusion widget style.


%prep
%setup -q -n %{name}
sed -i.bak -e 's/\r$//g' fusion.pro
%patch0 -p1
cp -a %{SOURCE1} .


%build
%if 0%{?suse_version}
qmake .
%endif

%if 0%{?fedora}
qmake-qt4 .
%endif

make %{?_smp_mflags}


%install
%make_install INSTALL_ROOT=%{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_libdir}/qt4/plugins/styles
%{_libdir}/qt4/plugins/styles/libfusion.so


%changelog

