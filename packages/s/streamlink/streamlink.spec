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

Name:           streamlink
Version:        5.3.1
Release:        0
Summary:        Program to pipe streams from services into a video player
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://streamlink.github.io/
Source:         https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc

BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx >= 4
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-pip >= 9
BuildRequires:  python3-requests >= 2.26
BuildRequires:  python3-versioningit >= 2.0.0
BuildRequires:  python3-wheel

# TEST REQUIREMENTS
BuildRequires:  python3-pytest >= 6.0.0
BuildRequires:  python3-PySocks >= 1.5.6
BuildRequires:  python3-certifi
BuildRequires:  python3-freezegun >= 1.0.0
BuildRequires:  python3-isodate
BuildRequires:  python3-lxml >= 4.6.4
BuildRequires:  python3-pycountry
BuildRequires:  python3-pycryptodome >= 3.4.3
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-requests-mock
BuildRequires:  python3-urllib3 >= 1.26.0
BuildRequires:  python3-websocket-client >= 1.2.1
BuildConflicts: python3-PySocks = 1.5.7

Requires:       python3-PySocks >= 1.5.6
Requires:       python3-certifi
Requires:       python3-isodate
Requires:       python3-lxml >= 4.6.4
Requires:       python3-pycountry
Requires:       python3-pycryptodome >= 3.4.3
Requires:       python3-requests >= 2.26
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
