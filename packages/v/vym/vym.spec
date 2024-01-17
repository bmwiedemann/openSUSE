#
# spec file for package vym
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.9.2
Release:        0
Summary:        Tool to generate and manipulate thought maps
License:        GPL-2.0-only
Group:          Productivity/Office/Other
URL:            http://www.insilmaril.de/vym/index.html
Source0:        %{name}-%{version}.tar.bz2
Source1:        debian.dirs
Source2:        debian.docs
Source3:        makedist.config

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)

BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Xml)

%if 0%{?suse_version}
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
%global cmake_options \\\
    -DCMAKE_INSTALL_DATAROOTDIR="share/vym" \\\
    -DCMAKE_INSTALL_MANDIR="%{_mandir}/man1" \\\
    -DCMAKE_INSTALL_DOCDIR="%{_defaultdocdir}/%{name}"

%cmake %{cmake_options}
%cmake_build

%install
%cmake_install

%if 0%{?suse_version}
%suse_update_desktop_file -i vym Office ProjectManagement
%endif

# Make scripts executable already installed with cmake above
chmod 755 %{buildroot}%{_datadir}/%{name}/scripts/vivym
chmod 755 %{buildroot}%{_datadir}/%{name}/scripts/vym-addmail.rb

%post
if test -x usr/bin/update-mime-database ; then
  usr/bin/update-mime-database usr/share/mime >/dev/null
fi

%files
%defattr(-,root,root)
%{_datadir}/applications/*

# Directories can be owned by multiple packages:
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps

%{_datadir}/icons/*/*/*/*.*
%{_bindir}/vym
%{_datadir}/vym

%doc %{_docdir}/%{name}
%{_mandir}/*/*
%{_datadir}/mime/packages/vym.xml

%changelog
