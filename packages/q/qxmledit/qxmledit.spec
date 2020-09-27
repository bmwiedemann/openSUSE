#
# spec file for package qxmledit
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


%define major   0
Name:           qxmledit
Version:        0.9.16
Release:        0
Summary:        XML Editor and XSD Viewer
License:        LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:            http://qxmledit.org/
Source:         https://github.com/lbellonda/qxmledit/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Scxml)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(glu)

%description
QXmlEdit is a XML editor written in Qt. Its main features are
unusual data visualization modes, nice XML manipulation and presentation and
it is multi platform. It can split very big XML files into fragments, and
compare XML files. It can also few XSD files.

* Hierarchical customizable view of XML elements.
* XML hierarchy navigation.
* Splitting of big XML files.
* Search supporting XPath expressions.
* Base64 data handling.
* Custom visualization styles.
* XML Schema (XSD) viewer.
* Columnar view.
* Sessions handling.
* Graphical XML file view.
* Map view of an XML document.
* Split and fragment extraction of big XML files.
* Visual compare of XML Schema files.
* Visual compare of XML files.
* XML Snippets.
* XSL specialized mode.
* Element display via user customizable rules.

%package -n libqxmledit%{major}
Summary:        XML Editor Shared Libraries

%description -n libqxmledit%{major}
QXmlEdit is a XML editor written in Qt. It uses a tree-based
interface to ease the edit of long files.

This package includes QXmlEdit shared libraries.

%package devel
Summary:        XML Editor Development Files
Requires:       libqxmledit%{major} = %{version}

%description devel
QXmlEdit is a XML editor written in Qt. It uses a tree-based
interface to ease the edit of long files.

This package includes QXmlEdit development files.

%prep
%autosetup

%build
export QXMLEDIT_INST_DATA_DIR=%{_datadir}/%{name}/
export QXMLEDIT_INST_DIR=%{_bindir}/
export QXMLEDIT_INST_DOC_DIR=%{_defaultdocdir}/%{name}/
export QXMLEDIT_INST_INCLUDE_DIR=%{_includedir}/%{name}/
export QXMLEDIT_INST_LIB_DIR=%{_libdir}/
export QXMLEDIT_INST_TRANSLATIONSDIR=%{_datadir}/%{name}/translations/
export QXMLEDIT_INST_USE_C11=y
export QXMLEDIT_NO_QWTPLOT=y
%qmake5
%make_jobs

%install
%qmake5_install

# Install icons.
install -Dm 0644 install_scripts/environment/icon/qxmledit_48x48.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -Dm 0644 src/images/icon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Install an appdata file.
install -Dm 0644 install_scripts/environment/desktop/QXmlEdit.appdata.xml \
    %{buildroot}%{_datadir}/appdata/QXmlEdit.appdata.xml

# Install a desktop file.
install -Dm 0644 install_scripts/environment/desktop/QXmlEdit.desktop \
    %{buildroot}%{_datadir}/applications/QXmlEdit.desktop

# Install a manual page.
install -Dm 0644 install_scripts/environment/man/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1

# Remove redundant files.
rm -f \
    %{buildroot}%{_datadir}/%{name}/{QXmlEdit.appdata.xml,QXmlEdit.desktop}

%suse_update_desktop_file QXmlEdit TextEditor Development Documentation Qt

%post -n libqxmledit%{major} -p /sbin/ldconfig
%postun -n libqxmledit%{major} -p /sbin/ldconfig

%files
%license COPYING GPLV3.txt LGPLV3.txt
%doc AUTHORS NEWS README ROADMAP TODO
%doc doc/QXmlEdit_manual.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/QXmlEdit.appdata.xml
%{_datadir}/applications/QXmlEdit.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man?/*

%files -n libqxmledit%{major}
%{_libdir}/libQXmlEdit*.so.*

%files devel
%license COPYING GPLV3.txt LGPLV3.txt
%doc AUTHORS NEWS README ROADMAP TODO
%{_includedir}/%{name}/
%{_libdir}/libQXmlEdit*.so

%changelog
