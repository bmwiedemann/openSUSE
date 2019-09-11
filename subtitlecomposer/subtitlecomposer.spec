#
# spec file for package subtitlecomposer
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


Name:           subtitlecomposer
Version:        0.7.0
Release:        0
Summary:        A text-based subtitle editor
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/maxrd2/subtitlecomposer/
Source0:        https://github.com/maxrd2/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.10
BuildRequires:  extra-cmake-modules
BuildRequires:  kauth-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kross-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  sonnet-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libxine)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(phonon4qt5)
Recommends:     %{name}-lang = %{version}
%if 0%{?suse_version} < 1500
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
%endif

%description
A text-based subtitles editor that supports basic operations. It supports
SubRip (SRT), MicroDVD, SSA/ASS, MPlayer, TMPlayer and YouTube captions, and
has speech Recognition using PocketSphinx.

%lang_package

%prep
%setup -q -n SubtitleComposer-%{version}

# Fix permissions
chmod 644 ChangeLog

# Fix shebang
sed -i '1s|%{_bindir}/env python|%{_bindir}/python|' \
       src/scripting/examples/*.py
sed -i '1s|%{_bindir}/env ruby|%{_bindir}/ruby|' \
       src/scripting/examples/*.rb

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

# Fix persissions
chmod 755 %{buildroot}%{_kf5_appsdir}/%{name}/scripts/*.py
chmod 755 %{buildroot}%{_kf5_appsdir}/%{name}/scripts/*.rb
# Fix rpmlint error (devel-file-in-non-devel-package) and install header files as doc (since they are installed just for help)
mkdir files_for_doc
cp -a %{buildroot}%{_kf5_appsdir}/%{name}/scripts/api/ files_for_doc/
rm -rf %{buildroot}%{_kf5_appsdir}/%{name}/scripts/api/
# Point to the correct path of the header files directory (doc)
perl -pi -e "s|'api'|'%{_docdir}/subtitlecomposer/api'|" %{buildroot}%{_kf5_appsdir}/%{name}/scripts/README

%suse_update_desktop_file -r %{name} Qt KDE AudioVideo AudioVideoEditing

%find_lang %{name}

%{kf5_post_install}

%if 0%{?suse_version} < 1500
%post
%mime_database_post

%postun
%mime_database_postun
%endif

%files
%doc ChangeLog README.md files_for_doc/api
%license LICENSE
%{_kf5_applicationsdir}/%{name}.desktop
%{_kf5_appsdir}/%{name}/
%{_kf5_bindir}/%{name}
%config(noreplace) %{_kf5_configdir}/%{name}rc
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_appstreamdir}/%{name}.desktop.appdata.xml
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/%{name}/
%{_kf5_libdir}/%{name}/
%{_datadir}/mime/packages/%{name}.xml

%files lang -f %{name}.lang

%changelog
