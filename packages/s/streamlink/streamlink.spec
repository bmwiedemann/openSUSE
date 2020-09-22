#
# spec file for package streamlink
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           streamlink
Version:        1.5.0
Release:        0
Summary:        Program to pipe streams from services into a video player
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://streamlink.github.io/
Source:         https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Recommends:     mpv
BuildArch:      noarch
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests >= 1.0
BuildRequires:  fdupes
Requires:       python3-pycountry
Requires:       python3-pycryptodome
Requires:       python3-requests >= 1.0
Requires:       python3-websocket-client
Requires:       python3-isodate
Requires:       python3-PySocks

%description
Streamlink is a CLI utility that pipes flash videos
from online streaming services to a variety of video players
such as MPV, or alternatively, a browser.
The main purpose of streamlink is to convert CPU-heavy
flash plugins to a less CPU-intensive format.
Streamlink is a fork of the livestreamer project.

%prep
%setup -q

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

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md MANIFEST.in README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}*/

%changelog
