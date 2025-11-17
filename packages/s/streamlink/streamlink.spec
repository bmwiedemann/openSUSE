#
# spec file for package streamlink
#
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


%global         flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == "test"
%define         psuffix -test
%else
%define         psuffix %nil
%endif
%{?sle15_python_module_pythons}%{!?sle15_python_module_pythons:%define pythons python3}
Name:           streamlink%{psuffix}
Version:        8.0.0
Release:        0
Summary:        Program to pipe streams from services into a video player
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://streamlink.github.io/
Source:         https://github.com/%{name}/%{name}/releases/download/%{version}/streamlink-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/%{version}/streamlink-%{version}.tar.gz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xcdac41b9122470faf357a9d344448a298d5c3618#/streamlink.keyring
BuildRequires:  %{python_module PySocks >= 1.5.6}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module lxml >= 4.6.4}
BuildRequires:  %{python_module myst-parser >= 1.0.0}
BuildRequires:  %{python_module pip >= 21.0.0}
BuildRequires:  %{python_module pycountry}
BuildRequires:  %{python_module pycryptodome >= 3.4.3}
BuildRequires:  %{python_module requests >= 2.30}
BuildRequires:  %{python_module setuptools >= 77.0}
BuildRequires:  %{python_module sphinx-design >= 0.5.0}
BuildRequires:  %{python_module trio >= 0.25.0}
BuildRequires:  %{python_module trio-websocket >= 0.9.0}
BuildRequires:  %{python_module urllib3 >= 2.0.0}
BuildRequires:  %{python_module versioningit >= 2.0.0}
BuildRequires:  %{python_module websocket-client >= 1.2.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes

%if "%{flavor}" == "test"
BuildRequires:  %{python_module freezegun >= 1.5.0}
BuildRequires:  %{python_module pytest >= 8.4.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  streamlink = %{version}
%endif

Requires:       %{pythons}-PySocks >= 1.5.6
Requires:       %{pythons}-certifi
Requires:       %{pythons}-isodate
Requires:       %{pythons}-lxml >= 4.6.4
Requires:       %{pythons}-pycountry
Requires:       %{pythons}-pycryptodome >= 3.4.3
Requires:       %{pythons}-requests >= 2.26
Requires:       %{pythons}-trio >= 0.25.0
Requires:       %{pythons}-trio-websocket >= 0.9.0
Requires:       %{pythons}-urllib3 >= 1.26.0
Requires:       %{pythons}-websocket-client >= 1.2.1
Conflicts:      %{pythons}-PySocks = 1.5.7
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
%pyproject_wheel

%if "%{flavor}" != "test"
%install
%pyproject_install
%fdupes -s %{buildroot}
%endif

%if "%{flavor}" == "test"
%check
%pytest
%endif

%if "%{flavor}" != "test"
%files
%license LICENSE
%doc AUTHORS CHANGELOG.md MANIFEST.in README.md
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info
%{python3_sitelib}/%{name}_cli
%endif

%changelog
