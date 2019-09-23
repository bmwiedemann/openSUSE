#
# spec file for package impressive
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define dist_name Impressive
Name:           impressive
Version:        0.12.0
Release:        0
Summary:        A PDF and image viewer optimized for presentations
License:        GPL-2.0
Group:          Productivity/Office/Other
Url:            http://impressive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{dist_name}/%{version}/%{dist_name}-%{version}.tar.gz
Requires:       ghostscript
Requires:       python-imaging
Requires:       python-opengl
Requires:       python-pygame
Recommends:     mupdf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A DRI accelerated pdf documents viewer with 3D
effects. Currently, it only supports keyboard
commands (not mouse) and a single 3D cube effect.

%prep
%setup -q -n %{dist_name}-%{version}

%build

%install
cd %{_builddir}/%{dist_name}-%{version}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 %{name}.py %{buildroot}%{_bindir}/%{name}

gzip -9 %{name}.1 &&
install -m 644 %{name}.1.gz %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root,-)
%attr(0755,root,root)%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1.gz

%changelog
