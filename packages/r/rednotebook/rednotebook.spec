#
# spec file for package rednotebook
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


Name:           rednotebook
Version:        2.16
Release:        0
Summary:        Graphical diary and journal
# See note at the end of README: code is using some LGPL-3.0+ module, so the resulting work is GPL-3.0+.
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            http://rednotebook.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/rednotebook/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       python3-PyYAML
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang
Recommends:     python3-chardet
Recommends:     python3-pyenchant
BuildArch:      noarch

%description
RedNotebook is a graphical journal to keep track of notes and thoughts.
It includes a calendar navigation, customizable templates, export
functionality and word clouds. You can also format, tag and search your
entries.

%lang_package

%prep
%setup -q

%build

%install
python3 setup.py install --prefix=%{_prefix} --exec-prefix=%{_prefix} --root=%{buildroot}
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name} Calendar
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/rednotebook.appdata.xml

%files lang -f %{name}.lang

%changelog
