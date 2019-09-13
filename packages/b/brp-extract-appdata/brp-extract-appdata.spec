#
# spec file for package brp-extract-appdata
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


Name:           brp-extract-appdata
Version:        2016.05.04
Release:        0
Summary:        Extract appdata.xml
License:        MIT
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/brp-extract-appdata
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

%description
Extract appdata.xml from all .deskop files found in build root

%package -n extract-appdata-icons
Summary:        A little perl script to split appdata.xml
Group:          Development/Tools/Building
Requires:       perl(XML::Simple)

%description -n extract-appdata-icons
OBS generated appdata.xml contains all icons and this little tool splits
the XML into the format expected from software center

%prep
%setup -q

%build

%install
install -m0755 -D brp-extract-appdata.pl %{buildroot}%{_rpmconfigdir}/brp-suse.d/brp-72-extract-appdata
install -m0755 -D create-appdata-xml.pl %{buildroot}%{_prefix}/lib/build/checks/72-translate-appdata
install -m0755 -D extract-icons.pl %{buildroot}%{_bindir}/extract-appdata-icons

%files
%{_rpmconfigdir}/brp-suse.d
%{_prefix}/lib/build

%files -n extract-appdata-icons
%{_bindir}/extract-appdata-icons

%changelog
