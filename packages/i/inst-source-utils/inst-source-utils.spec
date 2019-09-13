#
# spec file for package inst-source-utils
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           inst-source-utils
Summary:        Utilities for creating customized installation sources
License:        GPL-2.0-or-later
Group:          System/YaST
Version:        2018.12.10
Release:        0
Url:            http://en.opensuse.org/Inst-source-utils
BuildArch:      noarch
Requires:       gpg2
Obsoletes:      autoyast2-utils <= 2.14.10
Provides:       autoyast2-utils = 2.14.10
Recommends:     create-repo-utils
Requires:       perl-XML-Parser
Source:         %name-%version.tar.xz
Source1:        split.pl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Utilities supporting autoinstallation and creation of customized
installation  sources.

Have a look at http://en.opensuse.org/Inst-source-utils for a detailed
description of each script.



%prep
%setup -q

%build

%install
install -d -m 755 %{buildroot}/%{_prefix}

cp -a usr %{buildroot}/

%files
%doc COPYING
%defattr(755,root,root,755)
%_bindir/*
%defattr(644,root,root,755)
%_datadir/%name

%changelog
