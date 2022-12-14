#
# spec file for package susepaste
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


Name:           susepaste
Version:        0.6
Release:        0
Summary:        Script for using openSUSE paste
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://susepaste.org
Source0:        susepaste-script-%{version}.tar.bz2
Patch0:         0001-susepaste-Fix-parsing-of-returned-Location-header.patch
# PATCH-FIX-OPENSUSE 0002-susepaste-add-image-paste-info.patch malcolmlewis@opensuse.org boo#1193400-- Add info on posting an image to susepaste in the man page.
Patch1:         0002-susepaste-add-image-paste-info.patch
Patch2:         0003-susepaste-use-paste-opensuse.org.patch
Requires:       bash
Requires:       curl
BuildArch:      noarch

%description
A script for using the openSUSE paste service.
You can paste either the file or input from stdin.

%package screenshot
Summary:        Script for pasting screenshots
Group:          Productivity/Other
Requires:       ImageMagick
Requires:       curl
Requires:       wmctrl
Recommends:     xclip
BuildArch:      noarch

%description screenshot
A script for using the openSUSE paste service.
You can paste screenshot of the window or whole desktop.

%prep
%setup -q -n susepaste-script-%{version}
%patch0 -p2
%patch1 -p1
%patch2 -p2
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
%license COPYING
%{_bindir}/%{name}
%{_datadir}/susepaste/lang-mappings.sed
%dir %{_datadir}/susepaste
%{_mandir}/man1/%{name}.1%{?ext_man}

%files screenshot
%license COPYING
%{_bindir}/%{name}-screenshot
%{_mandir}/man1/%{name}-screenshot.1%{?ext_man}

%changelog
