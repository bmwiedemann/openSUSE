#
# spec file for package qutebrowser
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


Name:           qutebrowser
Version:        3.2.0
Release:        0
Summary:        Keyboard-driven vim-like browser based on Qt6
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://qutebrowser.org/
Source:         https://github.com/The-Compiler/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/The-Compiler/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  Mesa-dri
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-Flask
BuildRequires:  python3-Jinja2
BuildRequires:  python3-MarkupSafe
BuildRequires:  python3-PyQt6-WebEngine
BuildRequires:  python3-PyQt6-sip
BuildRequires:  python3-PyYAML
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-cheroot
BuildRequires:  python3-devel >= 3.8
BuildRequires:  python3-hypothesis
BuildRequires:  python3-importlib-resources
BuildRequires:  python3-opengl
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-bdd
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-pytest-instafail
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-rerunfailures
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-setuptools
BuildRequires:  python3-tk
BuildRequires:  python3-tldextract
BuildRequires:  qt6-sql-sqlite
BuildRequires:  python(abi) >= 3.8
Requires:       python3-Jinja2
Requires:       python3-MarkupSafe
Requires:       python3-PyQt6-WebEngine
Requires:       python3-PyYAML
Requires:       python3-opengl
Requires:       qt6-sql-sqlite
Recommends:     python3-Pygments
Recommends:     python3-adblock
Obsoletes:      qutebrowser-git-qt6 < %{version}
Provides:       qutebrowser-git-qt6 = %{version}
BuildArch:      noarch

%description
qutebrowser is a keyboard-focused browser with a minimal GUI.
It's based on PyQt6 and QtWebEngine.

%prep
%setup -q
sed -i '1d' %{name}/__main__.py
sed -i 's,^#!%{_bindir}/env ,#!%{_bindir}/,' \
    misc/userscripts/* \
    scripts/*.py
sed -i 's,^#!%{_bindir}/bash,#!/bin/bash,' \
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

# NOTE: test suite disabled because the BDD tests are too unreliable
# %%check
# NOTE: test suite is slow but doesn’t run reliably with xdist
# PYTHONPATH=. pytest -v \
#     -k 'not importlib' \

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
