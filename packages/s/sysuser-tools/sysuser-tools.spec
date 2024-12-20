#
# spec file for package sysuser-tools
#
# Copyright (c) 2024 SUSE LLC
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


Name:           sysuser-tools
Version:        3.3
Release:        0
Summary:        Auto provides for system users
License:        MIT
Group:          System/Packages
Source:         sysusers.prov
Source1:        sysusers.attr
Source2:        sysusers-generate-pre
Source3:        macros.sysusers
Source4:        sysusers2shadow.sh
BuildArch:      noarch
Requires:       sysuser-shadow
#!BuildIgnore:  sysuser-shadow
#!BuildIgnore:  sysuser-tools
BuildRequires:  diffutils

%description
Generate auto provides for system users.

%package -n sysuser-shadow
Summary:        Tool to execute sysusers.d with shadow utilities
Group:          System/Packages
Requires(pre):  (/usr/sbin/useradd or busybox)
# prefer original shadow over busybox by default
Suggests:       shadow

%description -n sysuser-shadow
This package contians a tool, which expects as input a sysusers.d
configuration file and uses the shadow suite to create the users
and groups from it like systemd-sysusers would do.

%prep
%setup -qcT

%build

%install
install -D -m 755 %{SOURCE0} %{buildroot}%{_prefix}/lib/rpm/sysusers.prov
install -D -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/rpm/fileattrs/sysusers.attr
install -D -m 755 %{SOURCE2} %{buildroot}%{_prefix}/lib/rpm/sysusers-generate-pre
install -D -m 644 %{SOURCE3} %{buildroot}%{_rpmmacrodir}/macros.sysusers
install -D -m 755 %{SOURCE4} %{buildroot}%{_sbindir}/sysusers2shadow

%check
mkdir -p subdir
cat <<EOF > subdir/me.conf
# Type Name       ID     GECOS           [HOME]    Shell
  u   me   -     "myself" /dev/null
m   me  nogroup
# foobar
  g   asdf
 z     welp invalid
EOF

cat <<EOFF > expected-account-pre
/usr/sbin/sysusers2shadow me.conf <<"EOF"
u   me   -     "myself" /dev/null
m   me  nogroup
g   asdf
EOF
EOFF

# copy pasta from macros.sysusers because the script sysusers-generate-pre is not in /usr/lib/rpm yet
bash %{SOURCE2} $(pwd)/subdir/me.conf me.conf > account.pre

diff account.pre expected-account-pre

%files
%defattr(-,root,root)
%{_rpmmacrodir}/macros.sysusers
%{_prefix}/lib/rpm/sysusers.prov
%{_prefix}/lib/rpm/fileattrs/sysusers.attr
%{_prefix}/lib/rpm/sysusers-generate-pre

%files -n sysuser-shadow
%defattr(-,root,root)
%{_sbindir}/sysusers2shadow

%changelog
