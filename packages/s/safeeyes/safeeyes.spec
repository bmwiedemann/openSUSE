#
# spec file for package safeeyes
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017 Malcolm J Lewis <malcolmlewis@opensuse.org>
# Copyright (c) 2020 opensuse.lietuviu.kalba@gmail.com
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


Name:           safeeyes
Version:        2.2.2
Release:        0
Summary:        Tool for reminding the user to take breaks
License:        GPL-3.0-only
Group:          Productivity/Graphics/Visualization/Other
URL:            https://github.com/slgobinath/SafeEyes
Source0:        %{name}-%{version}.tar.xz
Source99:       safeeyes-rpmlintrc
%if 0%{?suse_version} == 1500
#PATCH-FIX-OPENSUSE SafeEyes-Python3.6-support.patch opensuse.lietuviu.kalba@gmail.com -- SafeEyes needs Python 3.10+, fix to use in Python 3.6
Patch0:         SafeEyes-Python3.6-compatibility.patch
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Babel
%if 0%{?suse_version} == 1500
BuildRequires:  python3-devel >= 3.6
%else
BuildRequires:  python3-devel >= 3.10
%endif
BuildRequires:  python3-psutil
BuildRequires:  python3-python-xlib
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
# MANUAL BEGIN
Requires:       python3-Babel
Requires:       python3-cairo >= 1.11.1
Requires:       python3-croniter
Requires:       python3-gobject
Requires:       python3-packaging
Requires:       python3-psutil
Requires:       python3-python-xlib
Requires:       typelib(AppIndicator3)
Requires:       typelib(Notify)
Recommends:     xprintidle
# MANUAL END
BuildArch:      noarch

%description
This utility reminds the user to take breaks whilst they are working
at the computer in an effort to alleviate eye strain (asthenopia).

%lang_package

%prep
%setup -q
#Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!/usr/bin/env python3][#\!%{_bindir}/python3]' {} \;
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!/usr/bin/env python][#\!%{_bindir}/python3]' {} \;
# SmartPause: Increase default idle time to pause SafeEyes
sed 's/"default": 5,/"default": 60,/' -i safeeyes/plugins/smartpause/config.json
%if 0%{?suse_version} == 1500
%autopatch -p1
%endif

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

# localization
%find_lang %{name}

%files
%doc README.md
%license LICENSES/GPL-3.0-or-later.txt
%{_bindir}/safeeyes
%{_datadir}/applications/io.github.slgobinath.SafeEyes.desktop
%{_datadir}/icons/hicolor/*/*/
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info
%exclude %{python3_sitelib}/%{name}/config/locale

%files lang -f %{name}.lang
%dir %{python3_sitelib}/%{name}/config/locale
%dir %{python3_sitelib}/%{name}/config/locale/*
%dir %{python3_sitelib}/%{name}/config/locale/*/LC_MESSAGES

%changelog
