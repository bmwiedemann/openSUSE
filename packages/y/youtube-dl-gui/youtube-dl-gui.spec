#
# spec file for package youtube-dl-gui
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


Name:           youtube-dl-gui
Version:        0.4
Release:        0
Summary:        GUI for youtube-dl
# The Unlicense
License:        SUSE-Public-Domain
Group:          Productivity/Networking/Web/Utilities
Url:            https://github.com/MrS0m30n3/youtube-dl-gui
Source0:        https://github.com/MrS0m30n3/youtube-dl-gui/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE youtube-dl-gui-use_system_exe.patch
Patch0:         %{name}-use_system_exe.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python-wxWidgets-3_0-devel
BuildRequires:  python2-devel
BuildRequires:  python2-twodict
BuildRequires:  update-desktop-files
Requires:       python-wxWidgets-3_0
Requires:       python2-twodict
Requires:       youtube-dl
Recommends:     ffmpeg
Enhances:       youtube-dl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A front-end GUI for the popular youtube-dl written in wxPython.

%lang_package

%prep
%setup -q
%patch0 -p1
sed -e 's|__BINDIR__|%{_bindir}|' -i youtube_dl_gui/optionsmanager.py
items=(
       'downloaders' 'downloadmanager' '__init__' 'logmanager'
       'mainframe' '__main__' 'optionsframe' 'optionsmanager'
       'parsers' 'updatemanager' 'utils' 'widgets'
      )
for i in "${items[@]}"; do
    sed -i -e "1d" "youtube_dl_gui/$i.py"
done

%build
%__python2 setup.py build

%install
%__python2 setup.py install --root %{buildroot}
%find_lang youtube_dl_gui
sed -e '1i \#!%__python2' -i %{buildroot}%{_bindir}/%{name}
%suse_update_desktop_file -c youtube-dl-gui youtube-dl-gui "Video downloader" youtube-dl-gui youtube-dl-gui "AudioVideo Recorder Network FileTransfer"

%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%exclude %{python2_sitelib}/youtube_dl_gui/locale
%{python2_sitelib}/youtube_dl_gui
%{python2_sitelib}/Youtube_DLG-%{version}-py%{python2_version}.egg-info

%files lang -f youtube_dl_gui.lang
%defattr(-,root,root)
%doc LICENSE
%dir %{python2_sitelib}/youtube_dl_gui/locale
%dir %{python2_sitelib}/youtube_dl_gui/locale/*
%dir %{python2_sitelib}/youtube_dl_gui/locale/*/*

%changelog
