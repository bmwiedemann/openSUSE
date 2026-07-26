#
# spec file for package waylyrics
#
# Copyright (c) 2026 mantarimay
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_with test
Name:           waylyrics
Version:        0.4.0
Release:        0
Summary:        The furry way to show desktop lyrics
License:        MIT
URL:            https://github.com/waylyrics/waylyrics
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
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
# fix trait GTK for macro @implements
sed -i -E 's/gtk::Accessible, //g' src/app/search_window/mod.rs src/app/window/mod.rs
sed -i -E 's/gtk4::Buildable/gtk::Buildable/g' src/app/search_window/mod.rs src/app/window/mod.rs

%build
export WAYLYRICS_THEME_PRESETS_DIR=%{_datadir}/waylyrics/themes
%{cargo_build}

%install
export WAYLYRICS_THEME_PRESETS_DIR=%{_datadir}/waylyrics/themes
install -Dm755 target/release/waylyrics -t %{buildroot}%{_bindir}

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

%if %{with test}
%check
export WAYLYRICS_THEME_PRESETS_DIR=%{_datadir}/waylyrics/themes
%{cargo_test} --features=offline-test
%endif

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
