#
# spec file for package scap-workbench
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


Name:           scap-workbench
Version:        1.2.1+git20221219.10c1929
Release:        0
Summary:        A SCAP scanner and SCAP content editor
License:        GPL-3.0-only
Group:          Productivity/Security
URL:            https://github.com/OpenSCAP/%{name}
Source:         %{version}/%{name}-%{version}.tar.gz
Patch0:         0001-pkexec-avoid-potential-local-root-exploit-by-using-P.patch
BuildRequires:  asciidoc
BuildRequires:  cmake >= 2.6
BuildRequires:  openscap-devel >= 1.3.7
# buildtime and runtime requires for remote scan detection
BuildRequires:  openssh
Recommends:     openssh
# SLE 11 SP3: libopenscap needs libxslt without requiring it
# libxslt needs pcre
%if 0%{?suse_version} < 1140
BuildRequires:  libxslt-devel
BuildRequires:  pcre-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# scap-security-guide provides 'content'
Recommends:     scap-security-guide

# openscap-utils provides 'oscap' to run profiles
Recommends:     openscap-utils

%description
The main goal of this application is to lower the initial barrier of
using SCAP. Therefore, the scope of very narrow - scap-workbench only
scans a single machine and only with XCCDF/SDS (no direct OVAL
evaluation). The assumption is that this is enough for users who want
to scan a few machines and users with huge amount of machines to scan
will just use scap-workbench to test or hand-tune their content before
deploying it with more advanced (and harder to use) tools like
spacewalk.

%package doc
Summary:        Documentation for scap-workbench
Group:          Documentation/HTML

%description doc
This package provides HTML documentation for scap-workbench.

%prep
%setup -q
%patch0 -p1

%build
%if 0%{?cmake}
%cmake -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} -DCMAKE_INSTALL_LIBEXECDIR=%{_libdir}/%{name}
%else
rm -rf build
mkdir build
pushd build
 cmake -DCMAKE_INSTALL_PREFIX=/usr\
   -DCMAKE_VERBOSE_MAKEFILE=TRUE\
   -DCMAKE_SKIP_RPATH=1\
   -DPACKAGE_ARCHITECTURE=`uname -m`\
   -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}\
   -DCMAKE_INSTALL_LIBEXECDIR=%{_libdir}/%{name}\
   ..
popd
%endif
pushd build
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
rm -rf %{buildroot}%{_docdir}/%{name}/COPYING
popd

%if 0%{?suse_version}
%suse_update_desktop_file -i -u org.open_scap.scap_workbench Utility DesktopUtility
%endif

%files
%defattr(-,root,root,0755)
%doc README.md
%license COPYING
%{_bindir}/%{name}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*.appdata.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.png
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/README
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}*
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/%{name}*
%{_mandir}/man8/%{name}*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*sh
%exclude %{_docdir}/%{name}/*.html
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files doc
%defattr(-,root,root,0755)
%doc %{_docdir}/%{name}/*.html

%changelog
