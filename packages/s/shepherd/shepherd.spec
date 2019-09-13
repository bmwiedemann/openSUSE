#
# spec file for package shepherd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           shepherd
Version:        0.6.1
Release:        0
Summary:        Init and service manager
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://www.gnu.org/software/shepherd/
Source0:        https://ftp.gnu.org/gnu/shepherd/shepherd-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/shepherd/shepherd-%{version}.tar.gz.sig
Source2:        shepherd-rpmlintrc
BuildRequires:  guile-devel >= 2.0.13
BuildRequires:  pkg-config
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
The GNU Daemon Shepherd or GNU Shepherd, formerly known as GNU dmd, is
a service manager that looks after the herd of system services. It
provides a replacement for the service-managing capabilities of
SysV-init (or any other init). It is intended
for use on GNU/Hurd, but it is supposed to work on every POSIX-like
system where Guile is available. In particular, it is used as PID 1 by
GNU Guix.


%package bins
Summary:        Shepherd's init binaries
Group:          System/Base
Conflicts:      systemd-sysvinit

%description bins
Binaries of shepherd conflicting with other init systems.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -f %{name}.lang
%doc
%{_bindir}/herd
%{_bindir}/shepherd
%{_libdir}/guile
%{_datadir}/guile
%doc %{_infodir}/%{name}.info.gz
%doc %{_mandir}/man*/*
%exclude %{_mandir}/man8/reboot.8.*
%exclude %{_mandir}/man8/halt.8.*

%files bins
%{_sbindir}/*
%doc %{_mandir}/man8/reboot.8.*
%doc %{_mandir}/man8/halt.8.*

%changelog
