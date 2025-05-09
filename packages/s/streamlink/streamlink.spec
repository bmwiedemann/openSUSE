#
# spec file for package streamlink
#
# Copyright (c) 2025 SUSE LLC
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


%global         flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == "test"
%define         psuffix -test
%else
%define         psuffix %nil
%endif
Name:           streamlink%{psuffix}
Version:        7.3.0
Release:        0
Summary:        Program to pipe streams from services into a video player
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://streamlink.github.io/
Source:         https://github.com/%{name}/%{name}/releases/download/%{version}/streamlink-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/%{version}/streamlink-%{version}.tar.gz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xcdac41b9122470faf357a9d344448a298d5c3618#/streamlink.keyring
BuildRequires:  fdupes
BuildRequires:  python3-PySocks >= 1.5.6
BuildRequires:  python3-Sphinx >= 4
BuildRequires:  python3-certifi
BuildRequires:  python3-devel >= 3.9
BuildRequires:  python3-isodate
BuildRequires:  python3-lxml >= 4.6.4
BuildRequires:  python3-mypy
BuildRequires:  python3-pip >= 9
BuildRequires:  python3-pycountry
BuildRequires:  python3-pycryptodome >= 3.4.3
BuildRequires:  python3-requests >= 2.26
BuildRequires:  python3-setuptools >= 77.0
BuildRequires:  python3-trio >= 0.25.0
BuildRequires:  python3-trio-typing
BuildRequires:  python3-trio-websocket >= 0.9.0
BuildRequires:  python3-urllib3 >= 1.26.0
BuildRequires:  python3-versioningit >= 2.0.0
BuildRequires:  python3-websocket-client >= 1.2.1
BuildRequires:  python3-wheel

%if "%{flavor}" == "test"
BuildRequires:  python3-freezegun >= 1.0.0
BuildRequires:  python3-pytest >= 8.0.0
BuildRequires:  python3-pytest-trio
BuildRequires:  python3-requests-mock
BuildRequires:  streamlink = %{version}
%endif

Requires:       python3-PySocks >= 1.5.6
Requires:       python3-certifi
Requires:       python3-isodate
Requires:       python3-lxml >= 4.6.4
Requires:       python3-pycountry
Requires:       python3-pycryptodome >= 3.4.3
Requires:       python3-requests >= 2.26
Requires:       python3-trio >= 0.22.0
Requires:       python3-trio-websocket >= 0.9.0
Requires:       python3-urllib3 >= 1.26.0
Requires:       python3-websocket-client >= 1.2.1
Conflicts:      python3-PySocks = 1.5.7
# the behaviour of libsolv changed, so we now have to suggest the one we actually want
# if no player is preinstalled or in the same install command
Recommends:     (vlc or mpv)
Suggests:       vlc
Suggests:       ffmpeg
BuildArch:      noarch

%description
Streamlink is a command-line utility which pipes video streams from various
services into a video player, such as VLC. The main purpose of Streamlink is to
avoid resource-heavy and unoptimized websites, while still allowing the user to
enjoy various streamed content.

%prep
%autosetup -n streamlink-%{version}

%build
%python3_build

%if "%{flavor}" != "test"
%install
%python3_install --root %{buildroot}
%fdupes -s %{buildroot}
%endif

%if "%{flavor}" == "test"
%check
pytest
%endif

%if "%{flavor}" != "test"
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
%endif

%changelog
