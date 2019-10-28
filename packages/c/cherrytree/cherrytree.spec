#
# spec file for package cherrytree
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


Name:           cherrytree
Version:        0.38.8
Release:        0
Summary:        A hierarchical note taking application
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
Url:            http://www.giuspen.com/cherrytree/
Source:         http://www.giuspen.com/software/%{name}-%{version}.tar.xz
BuildRequires:  desktop-file-utils
BuildRequires:  python-enchant
BuildRequires:  python-gtk
BuildRequires:  python-gtksourceview
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
Requires:       python-gtk
Requires:       python-gtksourceview
Recommends:     %{name}-lang
# For password-protected format
%if 0%{?suse_version} > 1500
Recommends:     p7zip-full
%else
Recommends:     p7zip
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%py_requires

%description
A hierarchical note taking application, featuring rich text and syntax
highlighting, storing all the data (including images) in a single xml
file with extension ".ctd".

%lang_package
%prep
%setup -q

%build

%install
%{__python} setup.py install --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} --root=%{buildroot}
# Remove old mime registration files
rm %{buildroot}%{_datadir}/application-registry/cherrytree.*
rm %{buildroot}%{_datadir}/mime-info/cherrytree.*
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file -G "Hierarchical Notes Utility" cherrytree TextEditor

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%defattr(-,root,root)
%doc changelog.txt license.txt
%{_bindir}/cherrytree
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/cherrytree.appdata.xml
%{_datadir}/applications/cherrytree.desktop
%{_datadir}/cherrytree/
%{_datadir}/icons/hicolor/scalable/apps/cherrytree.svg
%{_datadir}/mime/packages/cherrytree.xml
%{_mandir}/man1/cherrytree.1%{?ext_man}
%{python_sitelib}/CherryTree-%{version}-py%{python_version}.egg-info

%files lang -f %{name}.lang

%changelog
