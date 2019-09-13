#
# spec file for package when-command
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


%define _version 0.9.12-beta.5
Name:           when-command
Version:        0.9.12~beta5
Release:        0
Summary:        Configurable user task scheduler
License:        BSD-3-Clause
Group:          Productivity/Other
Url:            http://almostearthling.github.io/when-command
Source:         https://github.com/almostearthling/%{name}/archive/v%{_version}.tar.gz#/%{name}-%{_version}.tar.gz
Source1:        %{name}.appdata.xml
Source2:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libXss1
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-pyinotify
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       libXss1
Requires:       python3-gobject
Requires:       python3-pyinotify
Recommends:     %{name}-lang
BuildArch:      noarch
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
Requires:       python3-gobject-Gdk
%endif

%description
When is a configurable user task scheduler. It interacts with the
user through a GUI, where the user can define tasks and conditions,
as well as relationships of causality that bind conditions to
tasks. When a condition is bound to a task, it is said to trigger a
task.

%lang_package

%prep
%setup -q -n %{name}-%{_version}
cp -f %{SOURCE1} %{name}.appdata.xml
sed -i 's/^\(Exec=\).*$/\1%{name}/' share/applications/%{name}.desktop

%build
python3 setup.py build

%install
python3 setup.py install \
  --root=%{buildroot} --prefix=%{_prefix}

install -Dpm 0644 %{name}.appdata.xml \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

mkdir -p %{buildroot}%{_docdir}/
mv -f %{buildroot}%{_datadir}/doc/%{name}/ \
  %{buildroot}%{_docdir}/%{name}/

%suse_update_desktop_file -r -G "When scheduler" %{name} Utility TimeUtility

%fdupes %{buildroot}%{_prefix}/
%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man?/%{name}.?%{?ext_man}
%{python3_sitelib}/when_command-*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
