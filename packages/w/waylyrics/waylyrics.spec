#
# spec file for package waylyrics
#
# Copyright (c) 2024 SUSE LLC
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


Name:           waylyrics
Version:        0.3.13
Release:        0
Summary:        The furry way to show desktop lyrics
License:        MIT
URL:            https://github.com/waylyrics/waylyrics
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.76.0
BuildRequires:  cargo-packaging
BuildRequires:  dbus-1-devel
BuildRequires:  gettext
BuildRequires:  gtk4-devel
BuildRequires:  libgraphene-devel
BuildRequires:  mimalloc-devel
BuildRequires:  openssl-devel

%description
The furry way to show desktop lyrics, and simple universal desktop lyrics made with GTK4 and love.

%lang_package

%prep
%autosetup -a1 -p0

%build
export WAYLYRICS_THEME_PRESETS_DIR=%{_datadir}/waylyrics/themes
%{cargo_build} --locked

%install
export WAYLYRICS_THEME_PRESETS_DIR=%{_datadir}/waylyrics/themes
%{cargo_install} --locked

install -dm755 %{buildroot}%{_datadir}/waylyrics
cp -r themes %{buildroot}%{_datadir}/waylyrics/

install -Dm644 "metainfo/io.github.waylyrics.Waylyrics.desktop" -t %{buildroot}%{_datadir}/applications/
install -Dm644 "metainfo/io.github.waylyrics.Waylyrics.gschema.xml" -t %{buildroot}%{_datadir}/glib-2.0/schemas/
cp -r res/icons %{buildroot}%{_datadir}/icons

# Locale files
(
    cd locales
    for po in $(find . -type f -name '*.po')
    do
        mkdir -p %{buildroot}%{_datadir}"/locale/${po#/*}"
        msgfmt -o %{buildroot}%{_datadir}"/locale/${po%.po}.mo" ${po}
    done
)
%find_lang %{name} %{name}.lang

%check
export WAYLYRICS_THEME_PRESETS_DIR=%{_datadir}/waylyrics/themes
%{cargo_test} --locked --features=offline-test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/waylyrics/
%{_datadir}/applications/io.github.waylyrics.Waylyrics.desktop
%{_datadir}/glib-2.0/schemas/io.github.waylyrics.Waylyrics.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.github.waylyrics.Waylyrics.svg

%files lang -f %{name}.lang

%changelog
