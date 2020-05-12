#
# spec file for package impressive
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


%define dist_name Impressive
%define fileversion 0.13.0-beta1
Name:           impressive
Version:        0.13.0~beta1
Release:        0
Summary:        PDF and image viewer optimized for presentations
License:        GPL-2.0-only
Group:          Productivity/Office/Other
URL:            http://impressive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{dist_name}/%{fileversion}/%{dist_name}-%{fileversion}.tar.gz
Requires:       ghostscript
Requires:       python3-imaging
Requires:       python3-opengl
Requires:       python3-pygame
Recommends:     mupdf
BuildArch:      noarch

%description
A DRI accelerated PDF document viewer with 3D effects. Currently, it only
supports keyboard commands (not mouse) and a single 3D cube effect.

%prep
%setup -q -n %{dist_name}-%{fileversion}

sed -i 's/env python/python3/' impressive.py

%build

%install
cd %{_builddir}/%{dist_name}-%{fileversion}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 %{name}.py %{buildroot}%{_bindir}/%{name}

gzip -9c <%{name}.1 >%{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%license license.txt
%doc changelog.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
