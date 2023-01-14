#
# spec file for package dumpzilla
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           dumpzilla
Version:        0.0.0+git.20210311
Release:        0
Summary:        Firefox browser forensic tool
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://www.dumpzilla.org/
Source:         %{name}-%{version}.tar.xz
Source1:        http://www.dumpzilla.org/Manual_dumpzilla_en.txt
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-lz4
Requires:       python3-python-magic
BuildArch:      noarch

%description
Extract all forensic interesting information from Firefox,
Iceweasel and Seamonkey browsers.
Works in command line interface, so information dumps could be
redirected by pipes with tools such as grep, awk, cut, sed...
Dumpzilla allows to visualize following sections, search
customization and extract certain content.

Features:
 * Cookies + DOM Storage (HTML 5).
 * User preferences (Domain permissions, Proxy settings...).
 * Downloads.
 * Web forms (Searches, emails, comments..).
 * Historial.
 * Bookmarks.
 * Cache HTML5 Visualization / Extraction (Offline cache).
 * visited sites "thumbnails" Visualization / Extraction .
 * Addons / Extensions and used paths or urls.
 * Browser saved passwords.
 * SSL Certificates added as a exception.
 * Session data (Webs, reference URLs and text used in forms).
 * Visualize live user surfing, Url used in each tab or window
   and use of forms.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' dumpzilla.py
cp %{SOURCE1} .

%build

%install
install -Dpm 0755 dumpzilla.py %{buildroot}%{_bindir}/dumpzilla
install -Dpm 0644 dumpzilla %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%doc README.md Manual_dumpzilla_en.txt
%{_bindir}/dumpzilla

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
