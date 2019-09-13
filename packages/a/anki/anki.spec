#
# spec file for package anki
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without tests
Name:           anki
Version:        2.1.13
Release:        0
Summary:        Spaced-Repetition Memory Training Program
License:        AGPL-3.0-only
Group:          Productivity/Text/Utilities
URL:            https://apps.ankiweb.net/
Source0:        https://apps.ankiweb.net/downloads/current/%{name}-%{version}-source.tgz
Source1:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE - anki-aqt___init__.py.patch -- Load Qt4 translations from the right place
Patch1:         %{name}-aqt___init__.py.patch
# PATCH-FIX-OPENSUSE - anki-anki_lang.py.patch -- Load Anki translations from the right place
Patch2:         %{name}-anki_lang.py.patch
BuildRequires:  python3-Markdown
BuildRequires:  python3-PyAudio
BuildRequires:  python3-Send2Trash
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-decorator
BuildRequires:  python3-jsonschema
BuildRequires:  python3-mock
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-qtwebengine-qt5
BuildRequires:  python3-requests
Requires:       python3-Markdown
Requires:       python3-PyAudio
Requires:       python3-Send2Trash
Requires:       python3-beautifulsoup4
Requires:       python3-decorator
Requires:       python3-jsonschema
Requires:       python3-qt5
Requires:       python3-qtwebengine-qt5
Requires:       python3-requests
Suggests:       lame
Suggests:       mpv
Suggests:       sox
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
Requires:       python3-qtwebengine-qt5
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
%if %{with tests}
BuildRequires:  python3-nose
%endif

%description
Anki is a spaced repetition system (SRS). It helps the user remember things by
scheduling reviews, so that the user can learn a lot of information
with the minimum amount of effort.
Anki is content-agnostic and supports images, audio,
videos and scientific markup (via LaTeX).

Anki stores data in ~/.local/share/Anki2, or $XDG_DATA_HOME/Anki2
if the user has set a custom data path.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

# SED-FIX-OPENSUSE -- Don't check for new updates.
sed -i -e 's|updates=True|updates=False|;
           s|suppressUpdate=False|suppressUpdate=True|' aqt/profiles.py

# Use dependencies instead of bundled stuff
rm -rf thirdparty

# Remove not needed files
rm -f anki/anki

%build
./tools/build_ui.sh
python3 -m compileall .
python3 -O -m compileall .

%install
%make_install

# install appdata
mkdir -p %{buildroot}%{_datadir}/appdata
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

# install mime data
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -m 0644 %{name}.xml %{buildroot}%{_datadir}/mime/packages/

# Remove duplicate and unneeded doc files
rm %{buildroot}%{_datadir}/doc/anki/LICENSE
rm %{buildroot}%{_datadir}/doc/anki/LICENSE.logo
rm %{buildroot}%{_datadir}/doc/anki/README.contributing
rm %{buildroot}%{_datadir}/doc/anki/README.development
rm %{buildroot}%{_datadir}/doc/anki/README.md

%find_lang %{name} %{name}.lang

%if 0%{?suse_version}
    %suse_update_desktop_file -r %{name} Education Languages
    %fdupes -s %{buildroot}%{_prefix}
%endif

# Fix rpmlint issues
find %{buildroot}%{_datadir}/%{name}/web/ -name '*.js' -exec chmod a-x {} +
sed -i 's|/usr/bin/env python3|/usr/bin/python3|' %{buildroot}%{_bindir}/%{name}

%check
%if %{with tests}
# to prevent Exception("Anki requires a UTF-8 locale.")
export LC_ALL=en_US.UTF-8
./tools/tests.sh
%endif

%post
update-mime-database %{_datadir}/mime

%postun
update-mime-database %{_datadir}/mime

%files -f %{name}.lang
%doc README.md
%license LICENSE LICENSE.logo
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/%{name}

%changelog
