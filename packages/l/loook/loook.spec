#
# spec file for package loook
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           loook
Version:        0.8.4
Release:        0
Summary:        Search strings in ODF documents
License:        GPL-2.0+
Group:          Productivity/Office/Other
Url:            http://mechtilde.de/Loook/
Source0:        http://mechtilde.de/Loook/Downloads/%{name}-%{version}-sources.zip
# PATCH-FEATURE-UPSTREAM loook-loook.desktop.patch (email)
Patch0:         %{name}-%{name}.desktop.patch
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  unzip
Requires:       python3-base
Requires:       python3-tk
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program is a program written in Python that searches for strings
in files created by OpenOffice.org, Apache OpenOffice, LibreOffice or
StarOffice 6.0 or higher. This is especially true for all documents
that were created in the Open Document Format. In addition, it can now
also search in documents created by Microsoft Word, Excel or PowerPoint
from the 2007 version in an OOXML format.

%prep
%setup -q
%patch0

%build

%install
# install executables and mans
install -Dm 0755 %{name}.py %{buildroot}%{_datadir}/%{name}/%{name}.py
install -Dm 0644 man/de/%{name}.1 %{buildroot}%{_mandir}/de/man1/%{name}.1
install -Dm 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# symlink executable
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/%{name}.py %{buildroot}%{_bindir}/%{name}

# install messages
for m in cs de en es fr it nl ; do
    msgfmt %{name}.${m}.po -o %{name}-%{version}.${m}.mo
    install -Dm 0644 %{name}-%{version}.${m}.mo %{buildroot}%{_datadir}/locale/${m}/LC_MESSAGES/%{name}-%{version}.mo
done
%find_lang %{name}-%{version} %{name}.lang

# install icon
install -Dm 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc Changelog Copyright
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/de/man1/%{name}.1%{ext_man}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/%{name}

%changelog
