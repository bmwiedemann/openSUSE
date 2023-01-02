#
# spec file for package thonny
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019-2021 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define pythons python3
%define desktop_file_name thonny

Name:           thonny
Version:        4.0.1
Release:        0
Summary:        Python IDE for beginners
License:        MIT
URL:            https://thonny.org/
Source0:        https://github.com/thonny/%{name}/archive/v%{version}.tar.gz#/thonny-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  mypy
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Send2Trash
BuildRequires:  python3-astroid
BuildRequires:  python3-asttokens
BuildRequires:  python3-docutils
BuildRequires:  python3-jedi
BuildRequires:  python3-pylint
BuildRequires:  python3-pyserial
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-tk
BuildRequires:  update-desktop-files
## MANUAL BEGIN
Requires:       mypy
Requires:       python3-Send2Trash
Requires:       python3-astroid
Requires:       python3-asttokens
Requires:       python3-docutils
Requires:       python3-jedi
Requires:       python3-pylint
Requires:       python3-pyserial
Requires:       python3-tk
## MANUAL END
Requires(post): desktop-file-utils
Requires(postun):desktop-file-utils
Recommends:     %{name}-lang
BuildArch:      noarch

%description
Thonny is a Python IDE meant for learning programming.

%package        lang
Summary:        Translations for Thonny IDE
Requires:       thonny = %{version}
Requires:       python(abi) = %{python3_version}

%description    lang
Provides translations for Thonny IDE

%prep
%setup -q
# Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -name "*.py" -exec sed -i 's|#!%{_bindir}/env python3|#!%{_bindir}/python3|' {} ";"

%build
export LC_ALL=en_US.utf8
%python_build

%install
export LC_ALL=en_US.utf8
%python_install
# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
cp packaging/linux/org.thonny.Thonny.desktop %{buildroot}%{_datadir}/applications/%{desktop_file_name}.desktop
%suse_update_desktop_file %{desktop_file_name}
# appdata
mkdir -p %{buildroot}%{_datadir}/metainfo
sed -i "s|org.thonny.Thonny|%{desktop_file_name}|g" packaging/linux/org.thonny.Thonny.appdata.xml
cp packaging/linux/org.thonny.Thonny.appdata.xml %{buildroot}%{_datadir}/metainfo/%{desktop_file_name}.appdata.xml
# icons
for size in 16 22 32 48 64 128 192 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
  cp packaging/icons/thonny-${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/thonny.png
done
# find and mark locale files
%python_find_lang thonny
# fdupes
%fdupes %{buildroot}%{python3_sitelib}

%check
# Skip test as requires Display.
pytest_flags=(-k 'not test_locals_marker')
# failed to access /dev/ttyACM0
pytest_flags+=(--ignore misc/mp/threads_test.py)
%pytest "${pytest_flags[@]}"

%post
# update desktop database
%desktop_database_post
%icon_theme_cache_post
exit 0

%postun
%icon_theme_cache_postun
%desktop_database_postun
exit 0

%files
%exclude %{python3_sitelib}/thonny/locale/
%doc CHANGELOG.rst CONTRIBUTING.rst CREDITS.rst
%license LICENSE.txt
%{_bindir}/thonny
%{python3_sitelib}/thonny
%{python3_sitelib}/thonny-%{version}*-info
%{_datadir}/applications/%{desktop_file_name}.desktop
%{_datadir}/metainfo/%{desktop_file_name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/thonny.png

%files lang -f python3-thonny.lang
%dir %{python3_sitelib}/thonny/locale/
%dir %{python3_sitelib}/thonny/locale/*
%dir %{python3_sitelib}/thonny/locale/*/LC_MESSAGES

%changelog
