#
# spec file for package qutebrowser
#
# Copyright (c) 2021 SUSE LLC
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


Name:           qutebrowser
Version:        2.1.0
Release:        0
Summary:        Keyboard-driven vim-like browser based on Qt5
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://qutebrowser.org/
Source:         https://github.com/The-Compiler/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/The-Compiler/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python >= 3.6.1
BuildRequires:  python3-Jinja2
BuildRequires:  python3-MarkupSafe
BuildRequires:  python3-PyYAML
BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-qt5 >= 5.12
BuildRequires:  python3-setuptools
Requires:       libqt5-sql-sqlite
Requires:       python3-Jinja2
Requires:       python3-MarkupSafe
Requires:       python3-PyYAML
Requires:       python3-opengl
Requires:       python3-qt5 >= 5.12
Recommends:     python3-Pygments
Recommends:     python3-adblock
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
BuildRequires:  python3-qt5-sip
%else
BuildRequires:  python3-sip
%endif
%if 0%{?suse_version} > 1500
Requires:       python3-qtwebengine-qt5
%endif
%if 0%{?suse_version} >= 1550
Requires:       python3-qt5-sip
%else
Requires:       python3-sip
%endif
%if 0%{?suse_version} <= 1320
BuildRequires:  update-desktop-files
%endif
%if %{python3_version_nodots} <= 38
Requires:       python3-importlib-resources
%endif
%if %{python3_version_nodots} == 36
Requires:       python3-dataclasses
%endif

%description
qutebrowser is a keyboard-focused browser with a minimal GUI.
It's based on PyQt5 and can use either QtWebEngine or QtWebKit.

%prep
%setup -q
sed -i '1d' %{name}/__main__.py
sed -i 's,^#!/usr/bin/env ,#!%{_bindir}/,' \
    misc/userscripts/* \
    scripts/*.py
sed -i 's,^#!/usr/bin/bash,#!/bin/bash,' \
    misc/userscripts/*
mv misc/Makefile .

%build

%install
%make_install PREFIX=%{_prefix}

chmod -x %{buildroot}%{_datadir}/%{name}/scripts/cycle-inputs.js \
    %{buildroot}%{_datadir}/%{name}/scripts/utils.py \
    %{buildroot}%{_datadir}/%{name}/userscripts/README.md
rm %{buildroot}%{python3_sitelib}/%{name}/git-commit-id
%fdupes %{buildroot}%{python3_sitelib}/

%if 0%{?suse_version} <= 1320
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license LICENSE
%doc doc/changelog.asciidoc README.asciidoc
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*
%{_datadir}/applications/org.qutebrowser.qutebrowser.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/metainfo/org.qutebrowser.qutebrowser.appdata.xml
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
