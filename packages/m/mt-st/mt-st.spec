#
# spec file for package mt-st
#
# Copyright (c) 2020 SUSE LLC
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


Name:           mt-st
Version:        1.4
Release:        0
Summary:        Utility for Controlling Magnetic Tape Drives
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://github.com/iustin/%{name}
Source0:        https://github.com/iustin/mt-st/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/iustin/mt-st/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        stinit.def
Source3:        61-storage-tape-init.rules
Source4:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
Requires:       udev
Requires(post): udev
Requires(post): update-alternatives
Requires(postun): udev
Requires(postun): update-alternatives
Provides:       mt

%description
mt-st tools contains two programs: mt and stinit, used for dealing
with Linux-specific tape-drive handling. mt program is tailored for
SCSI tape drives, but it can also be used with other Linux tape
drivers that use the same ioctls. The program stinit is meant for
initializing of SCSI tape drive modes at system startup, or when
new tape drivers are added.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags} -pipe" DEFTAPE=/dev/nst0

%install
%make_install EXEC_PREFIX=%{_prefix}
install -D -p -m 0644 %{SOURCE2} \
  %{buildroot}%{_sysconfdir}/stinit.def
install -D -p -m 0644 %{SOURCE3} \
  %{buildroot}%{_udevrulesdir}/61-storage-tape-init.rules
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
#For alternatives
mv %{buildroot}%{_bindir}/mt %{buildroot}%{_bindir}/mtst
mv %{buildroot}%{_mandir}/man1/mt.1 %{buildroot}%{_mandir}/man1/mtst.1
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/mt %{buildroot}%{_bindir}/mt
ln -s -f %{_sysconfdir}/alternatives/mt.1%{ext_man} %{buildroot}%{_mandir}/man1/mt.1%{ext_man}

%post
%{_sbindir}/update-alternatives --force \
    --install %{_bindir}/mt mt %{_bindir}/mtst 30 \
    --slave %{_mandir}/man1/mt.1%{ext_man}  mt.1%{ext_man}  %{_mandir}/man1/mtst.1%{ext_man}
%udev_rules_update

%postun
if [ "$1" = 0 ] ; then
   "%{_sbindir}/update-alternatives" --remove mt %{_bindir}/mtst
fi
%udev_rules_update

%files
%license COPYING
%doc README.md CHANGELOG.md stinit.def.examples
%ghost %{_bindir}/mt
%{_bindir}/mtst
%{_sbindir}/stinit
%ghost %{_mandir}/man1/mt.1%{ext_man}
%{_mandir}/man1/mtst.1%{?ext_man}
%{_mandir}/man8/stinit.8%{?ext_man}
%config(noreplace) %{_sysconfdir}/stinit.def
%{_udevrulesdir}/61-storage-tape-init.rules
%ghost %{_sysconfdir}/alternatives/mt
%ghost %{_sysconfdir}/alternatives/mt.1%{ext_man}
%{_datadir}/bash-completion/completions/%{name}

%changelog
