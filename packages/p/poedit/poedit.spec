#
# spec file for package poedit
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without language_detection
%bcond_without crowdin_integration
%bcond_with bundled_deps
Name:           poedit
Version:        3.2.2
Release:        0
Summary:        Gettext Catalog Editing Tool
License:        MIT
Group:          Development/Tools/Other
URL:            https://poedit.net/
Source:         https://github.com/vslavik/poedit/releases/download/v%{version}-oss/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_iostreams-devel >= 1.60
BuildRequires:  libboost_regex-devel >= 1.60
BuildRequires:  libboost_system-devel >= 1.60
BuildRequires:  libboost_thread-devel >= 1.60
BuildRequires:  pkgconfig
BuildRequires:  wxGTK3-devel >= 3.1.4
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(liblucene++) >= 3.0.5
Requires:       gettext-tools
%if %{with language_detection}
BuildRequires:  cld2-devel
%endif
%if %{with crowdin_integration}
BuildRequires:  cpprest-devel >= 2.5.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
%endif
%if !%{with bundled_deps}
BuildRequires:  nlohmann_json-devel
BuildRequires:  pkgconfig(pugixml)
%endif

%description
Poedit is an editor for gettext catalogs (.po files). It is built
with the wxWidgets toolkit, providing a graphical approach to
editing catalogs over launching vi and editing the file by hand.

%lang_package

%prep
%autosetup -p1
%if !%{with bundled_deps}
# Remove bundled dependencies, use the ones provided by the distribution
rm -r deps
%endif

%build
%configure \
  %{!?with_language_detection: --without-cld2} \
  %{!?with_crowdin_integration: --without-cpprest}

%make_build

%install
%make_install
%fdupes -s %{buildroot}%{_datadir}
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/net.poedit.Poedit.desktop
%{_datadir}/applications/net.poedit.PoeditURI.desktop
%{_datadir}/metainfo/net.poedit.Poedit.appdata.xml
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man?/*

%files lang -f %{name}.lang

%changelog
