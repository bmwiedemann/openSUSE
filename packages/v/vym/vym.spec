#
# spec file for package vym
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


Name:           vym
Version:        2.7.0
Release:        0
Summary:        Tool to generate and manipulate thought maps
License:        GPL-2.0-only
Group:          Productivity/Office/Other
Url:            http://www.insilmaril.de/vym/index.html
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.xml
Source2:        %{name}.desktop
Source3:        x-%{name}.desktop
Source4:        debian.dirs
Source5:        debian.docs
Source6:        makedist.config
%if 0%{?fedora_version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
%else
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtscript-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  update-desktop-files
%endif

Requires:       unzip
Requires:       zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
VYM (View Your Mind) is a tool to generate and manipulate maps which
show thoughts. Such maps can help improve creativity and effectivity.
They can be used for time management, to organize tasks, to get an
overview over complex contexts, to sort ideas etc.

%prep
%setup -q

%build
lrelease-qt5 vym.pro
qmake-qt5 -o Makefile vym.pro PREFIX=%{_datadir} BINDIR=%{_bindir} CONFIG+=RELEASE
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/vym
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 icons/vym.png %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
install -m 0644 README.md LICENSE.txt INSTALL.txt %{buildroot}%{_defaultdocdir}/%{name}
install -m 0644 doc/*.pdf %{buildroot}%{_defaultdocdir}/%{name}
make %{?_smp_mflags} DESTDIR=%{buildroot} install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications

mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 doc/vym.1.gz %{buildroot}%{_mandir}/man1

mkdir -p %{buildroot}%{_datadir}/mime/packages
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/
%suse_update_desktop_file -i vym Office ProjectManagement

%post
if test -x usr/bin/update-mime-database ; then
  usr/bin/update-mime-database usr/share/mime >/dev/null
fi

%files
%defattr(-,root,root)
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_bindir}/vym
%{_datadir}/vym

%doc %{_docdir}/%{name}
%{_mandir}/*/*
%{_datadir}/mime/packages/vym.xml

%changelog
