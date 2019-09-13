#
# spec file for package live-add-yast-repos
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


Name:           live-add-yast-repos
Version:        1.0
Release:        0
Summary:        A script to add the repos from control.xml to the system
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://build.opensuse.org/package/show/system:install:head/live-add-yast-repos
Source1:        geturls.xsl
Source2:        gpl-2.0.txt
BuildRequires:  libxslt-tools
BuildRequires:  openSUSE-release

%description
This package contains a script which adds all defined repositories from
control.xml (using extra_url) to the system.

%prep
%setup -q -T -c
cp %{SOURCE2} .

%build
xsltproc %{SOURCE1} /etc/YaST2/control.xml > add-yast-repos.sh

%install
install -Dm 755 add-yast-repos.sh %{buildroot}/%{_sbindir}/add-yast-repos

%files
%license gpl-2.0.txt
%{_sbindir}/add-yast-repos

%changelog
