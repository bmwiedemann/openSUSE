#
# spec file for package duply
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2011-2019 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           duply
Version:        2.4.1
Release:        0
Summary:        A frontend for the "duplicity" backup program
License:        GPL-2.0-only
URL:            https://duply.net/
Source0:        https://sourceforge.net/projects/ftplicity/files/duply%{20}%{28}simple%{20}duplicity%{29}/2.4.x/%{name}_%{version}.tgz
BuildArch:      noarch
# MANUAL BEGIN
Requires:       duplicity
# MANUAL END

%description
A shell front end to duplicity that simplifies the usage by managing
settings for backup jobs in profiles. It supports executing multiple
commands in a batch mode to enable single line cron entries and executes
pre/post backup scripts.

%prep
%setup -q -n %{name}_%{version}
#Fix env-script-interpreter rpmlint error
sed -i 's/\/usr\/bin\/env bash/\/bin\/bash/g' duply

%build

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc CHANGELOG.txt
%if ( 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100 ) || ! 0%{?is_opensuse}
# Needed if Leap 42.1 or SLE build targets
%doc gpl-2.0.txt
%else
%license gpl-2.0.txt
%endif
%{_bindir}/%{name}

%changelog
