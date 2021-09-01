#
# spec file for package streamlink
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


%define pythons python3
Name:           streamlink
Version:        2.3.0
Release:        0
Summary:        Program to pipe streams from services into a video player
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://streamlink.github.io/
Source:         https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
# Revert the increased requirements for now since we don't have
# python-requests 2.26 yet.
Patch0:         python-requests-version.patch

BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-requests >= 2.21
BuildRequires:  python3-setuptools

# TEST REQUIREMENTS
BuildRequires:  python3-pytest
BuildRequires:  python3-PySocks
BuildRequires:  python3-freezegun
BuildRequires:  python3-isodate
BuildRequires:  python3-pycountry
BuildRequires:  python3-pycryptodome
BuildRequires:  python3-requests-mock
BuildRequires:  python3-websocket-client

Requires:       python3-PySocks
Requires:       python3-isodate
Requires:       python3-pycountry
Requires:       python3-pycryptodome
Requires:       python3-requests >= 2.21
Requires:       python3-websocket-client >= 0.58

Recommends:     vlc
Suggests:       ffmpeg
Suggests:       rtmpdump
BuildArch:      noarch

%description
Streamlink is a CLI utility that pipes flash videos
from online streaming services to a variety of video players
such as MPV, or alternatively, a browser.
The main purpose of streamlink is to convert CPU-heavy
flash plugins to a less CPU-intensive format.
Streamlink is a fork of the livestreamer project.

%prep
%setup -q
%patch0 -p1

%build
%python3_build

%install
export STREAMLINK_USE_PYCOUNTRY="true"
%python3_install \
  --root=%{buildroot} \
  --prefix=%{_prefix}

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
%{python3_sitelib}/%{name}*/
%_mandir/man*/*

%changelog
