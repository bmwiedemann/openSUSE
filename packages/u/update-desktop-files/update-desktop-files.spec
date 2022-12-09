#
# spec file for package update-desktop-files
#
# Copyright (c) 2022 SUSE LLC
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


Name:           update-desktop-files
Version:        84.87
Release:        0
Summary:        A Build Tool to Update Desktop Files
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         suse_update_desktop_file.sh
Source1:        map-desktop-category.sh
Source2:        macro
Source4:        brp-trim-translations.sh
# This is not true technically, but we do that to make the rpm macros from
# desktop-file-utils available to most packages that ship a .desktop file
# (since they already have a update-desktop-files BuildRequires).
Requires:       desktop-file-utils
BuildArch:      noarch

%description
This package provides further translations and a shell script to update
desktop files. It is used by the %%suse_update_desktop_file rpm macro.

%package -n brp-trim-translations
Summary:        Trim translations from desktop files, polkit actions, mimetype descriptions and AppStream metainfo
Group:          Development/Tools/Building
Provides:       brp-trim-desktop = %{version}
Obsoletes:      brp-trim-desktop < %{version}
Requires:       awk
Requires:       libxslt-tools
Conflicts:      brp-extract-translations

%description -n brp-trim-translations
Extract and trim translations from all desktop files, polkit
actions, mimetype descriptions and AppStream metainfo found in
build root

%package -n brp-extract-translations
Summary:        Extract translations from desktop files, polkit actions, mimetype descriptions and AppStream metainfo
Group:          Development/Tools/Building
Provides:       brp-trim-desktop = %{version}
Obsoletes:      brp-trim-desktop < %{version}
Requires:       libxslt-tools
Conflicts:      brp-trim-translations

%description -n brp-extract-translations
Extract translations from all desktop files, polkit actions, mimetype descriptions
and AppStream metainfo found in build root

%prep
%setup -q -D -T 0 -c
# supi hack
sed -e '/awk/d' < %SOURCE4 > brp-extract-translations

%build

%install
mkdir -p $RPM_BUILD_ROOT%_rpmconfigdir
install -m0755 %SOURCE0 %SOURCE1 $RPM_BUILD_ROOT%_rpmconfigdir
install -m0644 -D %SOURCE2 $RPM_BUILD_ROOT%_rpmmacrodir/macros.%name
install -m0755 -D %SOURCE4 $RPM_BUILD_ROOT/usr/lib/rpm/brp-suse.d/brp-70-trim-translations
install -m0755 -D brp-extract-translations $RPM_BUILD_ROOT/usr/lib/rpm/brp-suse.d/brp-70-extract-translations

%files
%defattr(-,root,root)
%_rpmconfigdir/*
%exclude %_rpmconfigdir/brp-suse.d
%_rpmmacrodir/*

%files -n brp-trim-translations
%defattr(-,root,root)
%dir %_rpmconfigdir/brp-suse.d/
%_rpmconfigdir/brp-suse.d/brp-70-trim-translations

%files -n brp-extract-translations
%defattr(-,root,root)
%dir %_rpmconfigdir/brp-suse.d/
%_rpmconfigdir/brp-suse.d/brp-70-extract-translations

%changelog
