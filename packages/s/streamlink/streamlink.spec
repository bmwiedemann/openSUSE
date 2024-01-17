#
# spec file for package streamlink
#
# Copyright (c) 2023 SUSE LLC
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
%{?sle15_python_module_pythons}

Name:           streamlink
Version:        6.4.2
Release:        0
Summary:        Program to pipe streams from services into a video player
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://streamlink.github.io/
Source:         https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc

BuildRequires:  %{python_module Sphinx >= 4}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip >= 9}
BuildRequires:  %{python_module requests >= 2.26}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#BuildRequires:  %#{python_module versioningit >= 2.0.0}
BuildRequires:  %{python_module wheel}

# SECTION TEST REQUIREMENTS
BuildRequires:  %{python_module pytest >= 6.0.0}
BuildRequires:  %{python_module freezegun >= 1.0.0}
BuildRequires:  %{python_module pytest >= 6.0.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module requests-mock}
# /SECTION

BuildRequires:  %{python_module PySocks >= 1.5.6}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module lxml >= 4.6.4}
BuildRequires:  %{python_module pycountry}
BuildRequires:  %{python_module pycryptodome >= 3.4.3}
BuildRequires:  %{python_module trio >= 0.22.0}
BuildRequires:  %{python_module trio-websocket >= 0.9.0}
BuildRequires:  %{python_module typing-extensions >= 4.0.0}
BuildRequires:  %{python_module urllib3 >= 1.26.0}
BuildRequires:  %{python_module websocket-client >= 1.2.1}
BuildConflicts: %{python_module PySocks = 1.5.7}

Requires:       python3-PySocks >= 1.5.6
Requires:       python3-certifi
Requires:       python3-isodate
Requires:       python3-lxml >= 4.6.4
Requires:       python3-pycountry
Requires:       python3-pycryptodome >= 3.4.3
Requires:       python3-requests >= 2.26
Requires:       python3-trio >= 0.22.0
Requires:       python3-trio-websocket >= 0.9.0
Requires:       python3-typing-extensions >= 4.0.0
Requires:       python3-urllib3 >= 1.26.0
Requires:       python3-websocket-client >= 1.2.1
Conflicts:      python3-PySocks = 1.5.7

Recommends:     vlc
Suggests:       ffmpeg
BuildArch:      noarch

%description
Streamlink is a command-line utility which pipes video streams from various
services into a video player, such as VLC. The main purpose of Streamlink is to
avoid resource-heavy and unoptimized websites, while still allowing the user to
enjoy various streamed content.

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install

find %{buildroot}{%{python3_sitelib},%{python_sitelib}} -type f -name '*.py' | while read py; do
    if [[ "$(head -c2 "$py"; echo)" == "#!" ]]; then
        chmod a+x "$py"
    else
        chmod a-x "$py"
    fi
done
%fdupes -s %{buildroot}

%check
%pytest

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md MANIFEST.in README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}_cli
%{python3_sitelib}/%{name}-%{version}*-info
%_mandir/man*/*
%{_datadir}/bash-completion/completions/streamlink
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_streamlink

%changelog
