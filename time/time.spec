#
# spec file for package time
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


Name:           time
Version:        1.9
Release:        0
Summary:        Run Programs And Summarize System Resource Usage
License:        GPL-3.0+
Group:          System/Base
Url:            http://www.gnu.org/software/time/
Source:         http://ftp.gnu.org/gnu/time/%{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
Source2:        http://ftp.gnu.org/gnu/time/%{name}-%{version}.tar.gz.sig
Source3:        https://savannah.gnu.org/people/viewgpg.php?user_id=94790#/%{name}.keyring
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
The "time" command runs another program, then displays information
about the resources used by that program, collected by the system
while the program was running.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}%{_mandir}/man1

%check
make %{?_smp_mflags} check

%post
%install_info --entry="* time: (time). summarizing used system resources" --info-dir="%{_infodir}" "%{_infodir}/time.info.gz"

%postun
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/time.info.gz"

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/time
%{_infodir}/time.info*%{ext_info}

%changelog
