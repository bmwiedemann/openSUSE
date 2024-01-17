#
# spec file for package asterisk-sounds-devel
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           asterisk-sounds-devel
Version:        3
Release:        0
Summary:        Build helpers for Asterisk sound packages
License:        SUSE-Public-Domain
Group:          Development/Tools/Building

Source1:        macros.asterisk-sounds
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains additional RPM macros to help build Asterisk
sound packages.

%prep

%build

%install
c="%buildroot/usr/lib/rpm/macros.d/"
mkdir -p "$c"
install -pm0644 "%{S:1}" "$c/"

%files
%defattr(-,root,root)
/usr/lib/rpm/macros.d/

%changelog
