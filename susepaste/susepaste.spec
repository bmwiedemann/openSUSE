#
# spec file for package susepaste
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           susepaste
Version:        0.6
Release:        0
Summary:        Simple script for using openSUSE paste easily
License:        GPL-3.0-only
Group:          Productivity/Other
Url:            http://susepaste.org
Source0:        susepaste-script-%{version}.tar.bz2
Requires:       bash
Requires:       curl
BuildArch:      noarch

%description
Simple script for using openSUSE paste easily.
You can paste either the file or input from stdin.

http://susepaste.org

%package screenshot
Summary:        Simple script for pasting screenshots easily
Group:          Productivity/Other
Requires:       ImageMagick
Requires:       curl
Requires:       wmctrl
Recommends:     xclip
BuildArch:      noarch

%description screenshot
Simple script for using openSUSE paste easily.
You can paste screenshot of the window or whole desktop.

http://susepaste.org

%prep
%setup -q -n susepaste-script-%{version}
mv gpl-3.0.txt COPYING

%build

%install
install -Dpm 0755 susepaste \
  %{buildroot}%{_bindir}/susepaste
install -Dpm 0755 susepaste-screenshot \
  %{buildroot}%{_bindir}/susepaste-screenshot
install -Dpm 0644 susepaste.1 \
  %{buildroot}%{_mandir}/man1/susepaste.1
install -Dpm 0644 susepaste-screenshot.1 \
  %{buildroot}%{_mandir}/man1/susepaste-screenshot.1
install -Dpm 0644 lang-mappings.sed \
  %{buildroot}%{_datadir}/susepaste/lang-mappings.sed

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/susepaste/lang-mappings.sed
%dir %{_datadir}/susepaste
%{_mandir}/man1/%{name}.1%{ext_man}

%files screenshot
%doc COPYING
%{_bindir}/%{name}-screenshot
%{_mandir}/man1/%{name}-screenshot.1%{ext_man}

%changelog
