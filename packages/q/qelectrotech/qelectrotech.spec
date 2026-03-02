#
# spec file for package qelectrotech
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2021 Asterios Dramis <asterios.dramis@gmail.com>.
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


Name:           qelectrotech
Version:        0.100
Release:        0
Summary:        Application to Design Electric Diagrams
License:        CC-BY-3.0 AND GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://qelectrotech.org/
Source0:        https://github.com/qelectrotech/qelectrotech-source-mirror/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  kcoreaddons-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(sqlite3)
Requires:       %{name}-symbols = %{version}-%{release}
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
Recommends:     %{name}-examples = %{version}-%{release}
Recommends:     %{name}-lang = %{version}-%{release}

%description
QElectroTech is a Qt5 application to design electric diagrams. It uses XML
files for elements and diagrams, and includes both a diagram editor and an
element editor.

%package examples
Summary:        Examples for QElectroTech
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
This packages contains examples for the QElectroTech application.

%package symbols
Summary:        Elements collection for QElectroTech
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description symbols
This packages contains the elements collection for the electronic
components used in the QElectroTech application.

%lang_package

%prep
%autosetup

# Fix compilation and installation paths
sed -e s,%{_prefix}/local/,%{_prefix}/, \
    -e /QET_LICENSE_PATH/s,'doc/,'share/doc/packages/, \
    -e /QET_MIME/s,../,, \
    -e /QET_MAN_PATH/s,'man/','share/man/', \
    -e /DEFINES/s,GIT_COMMIT_SHA.*,GIT_COMMIT_SHA='\\\\\\"\\\\\\"', \
    -i %{name}.pro

rm -rf .github

%build
# Not needed for version 0.100
#%#global optflags ${optflags} -Wno-error=return-type
%qmake5
%make_build

%install
%qmake5_install
# Only install UTF-8 files
rm -rf %{buildroot}%{_defaultdocdir}/%{name} \
       %{buildroot}%{_mandir}/fr.ISO8859-1 \
       %{buildroot}%{_mandir}/fr
mv %{buildroot}%{_mandir}/fr.UTF-8 %{buildroot}%{_mandir}/fr
# It's not Belarusian
mv %{buildroot}%{_mandir}/be %{buildroot}%{_mandir}/nl_BE

%fdupes %{buildroot}/%{_prefix}
%find_lang %{name} --with-qt --with-man --all-name

%files
%doc CREDIT ChangeLog README README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_mandir}/man1/%{name}*.1%{?ext_man}
%{_datadir}/mime/packages/%{name}.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/lang
%dir %{_mandir}/nl_BE

%files examples
%defattr(0644,root,root)
%{_datadir}/%{name}/examples

%files symbols
%defattr(0644,root,root)
%license ELEMENTS.LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/elements
%{_datadir}/%{name}/titleblocks

%changelog
