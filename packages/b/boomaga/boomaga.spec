#
# spec file for package boomaga
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


Name:           boomaga
Version:        3.0.0
Release:        0
Summary:        Virtual Printer for Viewing a Document before Printing
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Productivity/Publishing/Other
URL:            https://www.boomaga.org/
Source0:        https://github.com/Boomaga/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
# SLE12 needs special BuildRequires.
# For suse_version values see https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
%if 0%{?suse_version} == 1315 && 0%{?is_opensuse} != 1
# For SLE12 by default CUPS 1.7.5 is provided and alternatively CUPS 1.5.4 is provided in the "legacy" module.
# For SLE12 build it with traditional CUPS 1.5.4 to ensure it works on SLE12 both with CUPS 1.7.5 and CUPS 1.5.4
# because libcups and libcupsimage in CUPS 1.7.5 are backward compatible with CUPS 1.5.4 so that applications
# that have been built with CUPS 1.5.4 also work under CUPS 1.7.5 but the libraries in CUPS 1.7.5 provide
# some additional functions so that applications that have been built with CUPS 1.7.5 and use those
# additional functions would not work under CUPS 1.7.5.
# Only in the Printing project for SLE12 use cups154-ddk (a sub package of the cups154-SLE12 source package):
BuildRequires:  cups154
BuildRequires:  cups154-devel
%else
# Anything what is not SLE12 (i.e. SLE11 and all openSUSE versions) have "normal" BuildRequires:
BuildRequires:  cups
BuildRequires:  cups-devel
%endif
BuildRequires:  hicolor-icon-theme
# There was a bug in the libpoppler-devel package (bnc#864299). Fixed in
# the "Update" repository.
%if 0%{?suse_version} && 0%{?suse_version} < 1320
BuildRequires:  libpoppler-cpp0
%endif
#
BuildRequires:  snappy-devel
BuildRequires:  update-desktop-files
%if 0%{?suse_version} >= 1315
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
%else
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtXml)
%endif
BuildRequires:  pkgconfig(poppler) >= 0.18
BuildRequires:  pkgconfig(poppler-cpp)
Requires:       ghostscript
Requires(post): %{_sbindir}/lpadmin
Requires(postun): %{_sbindir}/lpadmin
Requires(pre):  shared-mime-info
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Boomaga (BOOklet MAnager) is a virtual printer for viewing a document
before printing it out using the physical printer.
Select the "Boomaga" printer in any program and the Boomaga window
opens in several seconds (CUPS takes some time to respond).
If you print out one more document, it gets added to the previous one,
and you can also print them out as one.
Regardless of whether your printer supports duplex printing or not, you
would be able to easily print on both sides of the sheet.

%lang_package

%prep
%setup -q

%build
%cmake \
    -DCUPS_PPD_DIR=%{_datadir}/cups/model/
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install
%find_lang %{name} --with-qt
%suse_update_desktop_file -r %{name} Office Presentation

%post
if [ "$1" -eq 1 ] ; then
    %{_sbindir}/lpadmin -h localhost -p "Boomaga" -v "boomaga:/" -E -m "boomaga.ppd" -o printer-is-shared=no -o PageSize=A4
fi
%icon_theme_cache_post
%mime_database_post

%postun
if [ "$1" -eq 0 ] ; then
     %{_sbindir}/lpadmin -h localhost -x "Boomaga"
fi
%icon_theme_cache_postun
%mime_database_postun

%files
%defattr(-,root,root,-)
%license COPYING GPL LGPL
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/cups/model/*.ppd
%{_datadir}/dbus-1/services/org.boomaga.service
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_libexecdir}/cups/backend/%{name}
%{_mandir}/man?/*

%files lang -f %{name}.lang
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/

%changelog
