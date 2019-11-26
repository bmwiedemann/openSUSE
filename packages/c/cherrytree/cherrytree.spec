#
# spec file for package cherrytree
#
# Copyright (c) 2019 SUSE LLC
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
Version:        0.38.9
Release:        0
Summary:        A hierarchical note taking application
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://www.giuspen.com/cherrytree/
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
Requires:       python-xml
Recommends:     %{name}-lang
BuildArch:      noarch
# For password-protected format
%if 0%{?suse_version} > 1500
Recommends:     p7zip-full
%else
Recommends:     p7zip
%endif

%description
A hierarchical note taking application, featuring rich text and syntax
highlighting, storing all the data (including images) in a single xml
file with extension ".ctd".

%lang_package

%prep
%setup -q
# Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!/usr/bin/env python2][#\!%{_bindir}/python2]' {} \;

%build

%install
python setup.py install --prefix=%{_prefix} --exec-prefix=%{_prefix} --root=%{buildroot}
# Remove old mime registration files
rm %{buildroot}%{_datadir}/application-registry/cherrytree.*
rm %{buildroot}%{_datadir}/mime-info/cherrytree.*
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file -G "Hierarchical Notes Utility" cherrytree TextEditor

%files
%license license.txt
%doc changelog.txt
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
