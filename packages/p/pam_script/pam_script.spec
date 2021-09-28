#
# spec file for package pam_script
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) specCURRENT_YEAR SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pam_script
Version:        1.1.9
Release:        0
License:        GPL-2.0-or-later
Summary:        PAM module which allows executing a script
URL:            https://github.com/jeroennijhof/pam_script
Group:          Productivity/Networking
Source0:        https://github.com/jeroennijhof/pam_script/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         pam_script-man-section.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if ! %{defined _pam_moduledir}
%define _pam_moduledir /%{_lib}/security
%endif

%description
This module will allow you to execute scripts during authorization,
password changes and sessions. This is very handy if your current
security application has no PAM support but is accessible with perl
or other scripts.

%prep
%setup -q -n %{name}-%{version}
%patch0
autoreconf -fis

%build
%configure --disable-static --with-gnu-ld --libdir=%{_pam_moduledir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} man7dir='$(mandir)/man8'
rm -vf %{buildroot}%{_pam_moduledir}/*.la
rm -vf %{buildroot}%{_sysconfdir}/README
for file in %{buildroot}%{_mandir}/man8/*.7*
do
    test -e "$file" || continue
    path=${file%%/*}
    mv "$file" "${path}/%{name}.8"
done

%files
%defattr(-,root,root)
%if %{defined license}
%license COPYING
%doc AUTHORS ChangeLog README NEWS etc/README.pam_script
%else
%doc AUTHORS COPYING ChangeLog README NEWS etc/README.pam_script
%endif
%config(noreplace) %dir %{_sysconfdir}/pam-script.d/
%config(noreplace) %{_sysconfdir}/pam_script*
%{_pam_moduledir}/*
%{_mandir}/man8/%{name}.8*

%changelog
