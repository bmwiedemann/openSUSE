#
# spec file for package safeeyes
#
# Copyright (c) 2020 SUSE LLC
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


# get python versions
%global py3_ver %(if [ -f "%{__python3}" ]; then %{__python3} -c "import sys; sys.stdout.write(sys.version[:3])"; else echo 0; fi;)

Name:           safeeyes
Version:        2.0.9+git20201003
Release:        0
Summary:        Protect you from eye strain when working on the computer
License:        GPL-3.0-only
Group:          Productivity/Graphics/Visualization/Other
URL:            https://github.com/slgobinath/SafeEyes
Source0:        SafeEyes-%{version}.tar.xz
Source99:       safeeyes-rpmlintrc
#PATCH-FIX-OPENSUSE SafeEyes-fix-install-path.patch opensuse.lietuviu.kalba@gmail.com -- install in /usr/share, not in /home/abuild/.local/share
Patch0:         SafeEyes-fix-install-path.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-Babel
BuildRequires:  python3-devel
BuildRequires:  python3-psutil
BuildRequires:  python3-setuptools
%if 0%{?suse_version} > 1315 && 0%{?is_opensuse}
BuildRequires:  python3-python-xlib
%else
BuildRequires:  python3-xlib
%endif
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
# MANUAL BEGIN
Requires:       python3-Babel
Requires:       python3-cairo >= 1.11.1
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       typelib(AppIndicator3)
Requires:       typelib(Notify)
%if 0%{?suse_version} > 1315 && 0%{?is_opensuse}
Requires:       python3-python-xlib
%else
Requires:       python3-xlib
%endif
Recommends:     xprintidle
# MANUAL END
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Protect your eyes from eye strain using this continuous breaks reminder.
A Free and Open Source Linux alternative for EyeLeo.

%lang_package

%prep
%define TAR_TOP_FOLDER SafeEyes-%{version}
%setup -q -n %{TAR_TOP_FOLDER}
%autopatch -p1
#Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!/usr/bin/env python3][#\!%{_bindir}/python3]' {} \;
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!/usr/bin/env python][#\!%{_bindir}/python3]' {} \;

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%suse_update_desktop_file -r safeeyes Utility Clock

# localization
%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/safeeyes
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-2.0.9-py%{py3_ver}.egg-info
%exclude %{python3_sitelib}/%{name}/config/locale

%files lang -f %{name}.lang
%{python3_sitelib}/%{name}/config/locale

%changelog
