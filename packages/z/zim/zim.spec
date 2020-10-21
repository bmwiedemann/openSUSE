#
# spec file for package zim
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Matthias Propst.
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


%define skip_python2 1

Name:           zim
Version:        0.73.2
Release:        0
Summary:        A Desktop Wiki
License:        GPL-2.0-or-later
Group:          Productivity/Office/Organizers
URL:            https://zim-wiki.org
Source:         https://zim-wiki.org/downloads/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
# For directory ownership
BuildRequires:  %{python_module gobject >= 3.2}
BuildRequires:  %{pythons}
BuildRequires:  hicolor-icon-theme
BuildRequires:  typelib-1_0-Gtk-3_0
# We need the %%mime_database_*, %%desktop_database_* and %%icon_theme_cache_*
# macros for old suse versions
%if 0%{?suse_version} < 1330
BuildRequires:  shared-mime-info
%endif
BuildRequires:  update-desktop-files
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       xdg-utils
# for the version control plugin
Suggests:       bzr
Suggests:       git-core
Suggests:       mercurial
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Zim is a graphical text editor used to maintain a collection of wiki
pages. Each page can contain links to other pages, simple formatting and
images. Pages are stored in a folder structure, like in an outliner, and
can have attachments. Creating a new page is as easy as linking to a
nonexistent page. All data is stored in plain text files with wiki
formatting. Various plugins provide additional functionality, like a
task list manager, an equation editor, a tray icon, and support for
version control.

%lang_package
%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%suse_update_desktop_file %{name}
# remove ubuntu-specific icons
rm -r %{buildroot}%{_datadir}/icons/{ubuntu-mono-dark,ubuntu-mono-light}
%find_lang %{name}

%fdupes -s %{buildroot}

%desktop_database_post

%desktop_database_postun

%files
%defattr(-,root,root)
%license LICENSE
%doc CHANGELOG.md PLUGIN_WRITING.md CONTRIBUTING.md
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-%{version}-py*.egg-info
%{_bindir}/%{name}
%{_datadir}/%{name}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.zim_wiki.Zim.appdata.xml
%{_datadir}/applications/zim.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/zim.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-zim-notebook.*
%{_datadir}/icons/hicolor/*/mimetypes/gnome-mime-application-x-zim-notebook.*
%{_datadir}/pixmaps/zim.png
%{_mandir}/man1/zim.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
