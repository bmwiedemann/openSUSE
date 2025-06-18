#
# spec file for package gpodder
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%if 0%{?suse_version} > 1500
# Build only one time
%define pythons %{primary_python}
%else
# Build only with python 3.11
%{?sle15_python_module_pythons}
%endif
Name:           gpodder
Version:        3.11.5
Release:        0
Summary:        A free podcast aggregator for Linux
License:        GPL-3.0-or-later
URL:            https://gpodder.org
Source:         https://github.com/gpodder/gpodder/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module eyed3 >= 0.7}
BuildRequires:  %{python_module gobject >= 3.22.0}
BuildRequires:  %{python_module installer}
BuildRequires:  %{python_module mygpoclient >= 1.7}
BuildRequires:  %{python_module podcastparser >= 0.6.0}
BuildRequires:  %{python_module requests >= 2.24.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  update-desktop-files
BuildRequires:  typelib(Gtk) >= 3.16
# For runnung the tests
BuildRequires:  %{python_module MiniMock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module sqlite3}
Requires:       python3-dbus-python
Requires:       python3-eyed3 >= 0.7
Requires:       python3-gobject >= 3.22.0
Requires:       python3-mygpoclient >= 1.7
Requires:       python3-podcastparser >= 0.6.0
Requires:       python3-requests >= 2.24.0
Requires:       python3-sqlite3
Requires:       typelib(Gtk) >= 3.16
# On PackMan it is called gpodder3
Conflicts:      gpodder3 <= 3.11.0

%description
gPodder manages Podcasts for you and automatically downloads selected episodes
from as many channels as you like. Synchronization support is available for
iPods and filesystem-based MP3 players, but Podcasts can (of course) also be
played with any desktop player application.

%lang_package

%prep
%autosetup

%build
%make_build build

%install
%make_install PREFIX=%{_prefix}

# remove shebangs from .py files that are in sitelib:
find %{buildroot}%{python3_sitelib} -name '*.py' \
| while read f; do
    case $(head -1 "$f") in
        \#!*) %__sed -i '1d' "$f" ;;
    esac
done

rm -rf %{buildroot}%{_datadir}/icons/*/{26,40}x*

%fdupes %{buildroot}

%suse_update_desktop_file -r gpodder AudioVideo Player

%find_lang gpodder

%check
make unittest

%files
%license COPYING
%doc README.md
%{_bindir}/gpo
%{_bindir}/gpodder
%{_bindir}/gpodder-migrate2tres
%{python3_sitelib}/gpodder
%{python3_sitelib}/gpodder-%{version}.dist-info
%{_datadir}/gpodder
%{_datadir}/metainfo
%exclude %{_datadir}/gpodder/extensions/ubuntu_unity.*
%{_datadir}/applications/gpodder.desktop
%{_datadir}/applications/gpodder-url-handler.desktop
%{_datadir}/dbus-1/services/org.gpodder.service
%{_datadir}/icons/*/*/apps/gpodder.*
%{_mandir}/man1/gpo.1%{?ext_man}
%{_mandir}/man1/gpodder.1%{?ext_man}
%{_mandir}/man1/gpodder-migrate2tres.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
