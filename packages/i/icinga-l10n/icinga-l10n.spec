#
# spec file for package icinga-l10n
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


%define revision    1
%define basedir     %{_datadir}/icinga-L10n
%if 0%{?el5}%{?el6}%{?amzn}%{?suse_version}
%define use_selinux 0
%else
%define use_selinux 1
%define selinux_variants mls targeted
%endif
Name:           icinga-l10n
Version:        1.2.0
Release:        %{revision}%{?dist}
Summary:        Icinga L10n
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/L10n/archive/v%{version}/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildArch:      noarch

%prep
%setup -q -n L10n-%{version}
%if 0%{?use_selinux}
cp -r %{_topdir}/../selinux selinux
%endif

%build
%if 0%{?use_selinux}
cd selinux
for selinuxvariant in %{selinux_variants}
do
  %make_build NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile
  mv icinga-l10n.pp icinga-l10n.pp.${selinuxvariant}
  %make_build NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile clean
done
cd -
%endif

%install
mkdir -p %{buildroot}/%{basedir}
cp -prv locale %{buildroot}/%{basedir}
find %{buildroot}/%{basedir}/locale -name *.po -delete
%if 0%{?use_selinux}
cd selinux
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 icinga-l10n.pp.${selinuxvariant} %{buildroot}%{_datadir}/selinux/${selinuxvariant}/icinga-l10n.pp
done
cd -
%endif

# Main package
%description
L10n (short for Localization) provides all translations available for Icinga.

%files
%license COPYING
%doc README.md CONTRIBUTING.md
%{basedir}

# Selinux package
%if 0%{?use_selinux}
%package selinux
Summary:        SELinux policy for Icinga L10n
BuildRequires:  checkpolicy
BuildRequires:  selinux-policy-devel
Requires:       %{name} = %{version}-%{release}
Requires(post): policycoreutils
Requires(postun):policycoreutils

%description selinux
SELinux policy for Icinga L10n

%post selinux
for selinuxvariant in %{selinux_variants}
do
  %{_sbindir}/semodule -s ${selinuxvariant} -i %{_datadir}/selinux/${selinuxvariant}/icinga-l10n.pp &> /dev/null || :
done
%{_sbindir}/restorecon -R %{basedir} &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
     %{_sbindir}/semodule -s ${selinuxvariant} -r icinga-l10n &> /dev/null || :
  done
  [ -d %{basedir} ] && %{_sbindir}/restorecon -R %{basedir} &> /dev/null || :
fi

%files selinux
%defattr(-,root,root,0755)
%doc selinux/*
%{_datadir}/selinux/*/icinga-l10n.pp

%endif

%changelog
