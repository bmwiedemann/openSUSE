#
# spec file for package deepin-gettext-tools
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


Name:           deepin-gettext-tools
Version:        1.0.10
Release:        0
License:        GPL-3.0-or-later
Summary:        Deepin wrapper for gettext
URL:            https://github.com/linuxdeepin/deepin-gettext-tools
Group:          Development/Tools/Other
Source:         https://github.com/linuxdeepin/deepin-gettext-tools/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         reproducible.patch
BuildArch:      noarch
Requires:       gettext
Requires:       python3
Requires:       perl(Config::Tiny)
Requires:       perl(Exporter::Tiny)
Requires:       perl(XML::LibXML)
Requires:       perl(XML::LibXML::PrettyPrint)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The tools of gettext function wrapper.

Currently supported languages: Python, QML, Go lang

%prep
%autosetup -p1
# fix shebang
find -iname "*.py" | xargs sed -i '1s|.*|#!%{_bindir}/python3|'
sed -i '1s|.*|#!%{__perl}|' src/desktop_ts_convert.pl
sed -i 's|sudo cp|cp|' src/generate_mo.py
sed -i 's|lconvert|lconvert-qt5|; s|deepin-lupdate|lupdate-qt5|' src/update_pot.py

%build
make %{?_smp_mflags}

%install
make install \
             DESTDIR=%{buildroot} \
             PREFIX=%{_prefix} \
             %{?_smp_mflags}

#Fix permission
chmod +x %{buildroot}%{_prefix}/lib/%{name}/*.py

%files
%defattr(-,root,root)
%doc README.md LICENSE debian/copyright debian/changelog
%{_bindir}/deepin-generate-mo
%{_bindir}/deepin-desktop-ts-convert
%{_bindir}/deepin-update-pot
%{_bindir}/deepin-policy-ts-convert
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/generate_mo.py
%{_prefix}/lib/%{name}/update_pot.py

%changelog
