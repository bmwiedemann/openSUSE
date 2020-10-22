#
# spec file for package perl-Bootloader
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Bootloader
Version:        0.932
Release:        0
Requires:       coreutils
Requires:       perl-base = %{perl_version}
Recommends:     perl-gettext
Summary:        Library for Configuring Boot Loaders
License:        GPL-2.0-or-later
Group:          System/Boot
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
Conflicts:      multipath-tools < 0.4.8-40.25.1
#!BuildIgnore: mdadm e2fsprogs limal-bootloader

%description
Perl modules for configuring various boot loaders.



Authors:
--------
    Jiri Srain <jsrain@suse.cz>
    Joachim Plack <jplack@suse.de>
    Alexander Osthof <aosthof@suse.de>
    Josef Reidinger <jreidinger@suse.cz>

%package YAML
Requires:       %{name} = %{version}
Requires:       perl-YAML-LibYAML
Summary:        YAML interface for perl-Bootloader
Group:          System/Boot

%description YAML
A command line interface to perl-Bootloader using YAML files for input and output.


%prep
%setup -q

%build

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -d -m 700 $RPM_BUILD_ROOT/var/log/YaST2
touch $RPM_BUILD_ROOT/var/log/pbl.log
%perl_process_packlist
#install only needed files for bootloader for specific architecture
%ifarch %ix86 x86_64
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/Bootloader/Core/{ZIPL*,PowerLILO*}
rm -f $RPM_BUILD_ROOT/%{_mandir}/man?/{*ZIPL*,*PowerLILO*}
%if 0%{?suse_version} == 0 || 0%{?suse_version} <= 1130
sed -i '/ZIPL/D;/PowerLILO/D;' $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/Bootloader/.packlist
%endif
%endif
%ifarch ppc ppc64
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/Bootloader/Core/{ZIPL*,LILO*,ELILO*,GRUB.*}
%if 0%{?suse_version} == 0 || 0%{?suse_version} <= 1130
sed -i '/ZIPL/D;/ELILO/D;/\/LILO/D;/GRUB/D;' $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/Bootloader/.packlist
%endif
%endif
%ifarch s390 s390x
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/Bootloader/Core/{*LILO*,GRUB.*,GRUB2EFI.*}
%if 0%{?suse_version} == 0 || 0%{?suse_version} <= 1130
sed -i '/LILO/D;/GRUB/D;' $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/Bootloader/.packlist
%endif
%endif
%ifarch ia32 ia64
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/Bootloader/Core/{LILO*,GRUB*,ZIPL*,PowerLILO*}
%if 0%{?suse_version} == 0 || 0%{?suse_version} <= 1130
sed -i '/ZIPL/D;/PowerLILO/D;/\/LILO/D;/GRUB/D;' $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/Bootloader/.packlist
%endif
%endif

%post
echo -n >>/var/log/pbl.log
chmod 600 /var/log/pbl.log

%files
%defattr(-, root, root)
%license COPYING
%doc %{_mandir}/man?/*
%{perl_vendorarch}/auto/Bootloader
%{perl_vendorlib}/Bootloader
%if 0%{?suse_version} == 0 || 0%{?suse_version} <= 1130
/var/adm/perl-modules/perl-Bootloader
%endif
/sbin/update-bootloader
/sbin/pbl
/usr/lib/bootloader
/boot/boot.readme
/etc/logrotate.d/pbl
%dir %attr(0700,root,root) /var/log/YaST2
%ghost %attr(0600,root,root) /var/log/pbl.log

%files YAML
%defattr(-, root, root)
%{_sbindir}/pbl-yaml

%changelog
