#
# spec file for package hmaccalc
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


# at least from Red Hat Linux 9 through Fedora 11's development cycle.
%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	for length in 1 256 384 512 ; do \
		$RPM_BUILD_ROOT/%{_bindir}/sha${length}hmac -S > \\\
		$RPM_BUILD_ROOT/%{_libdir}/%{name}/sha${length}hmac.hmac \
	done \
	%{nil}

Name:           hmaccalc
Version:        0.9.14
Release:        0
Summary:        Tools for computing and checking HMAC values for files
License:        BSD-3-Clause
Group:          Productivity/Security
Url:            https://fedorahosted.org/hmaccalc/
Source0:        https://fedorahosted.org/released/hmaccalc/hmaccalc-%{version}.tar.gz
Source1:        https://fedorahosted.org/released/hmaccalc/hmaccalc-%{version}.tar.gz.sig
Source2:        %name.keyring
Patch1:         hmaccalc-susekey.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  mozilla-nss-devel
BuildRequires:  pkg-config

%description
The hmaccalc package contains tools which can calculate HMAC (hash-based
message authentication code) values for files.  The names and interfaces are
meant to mimic the sha*sum tools provided by the coreutils package.

%prep
%setup -q
%patch1 -p0

%build
%configure --enable-sum-directory=%{_libdir}/%{name}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%check
make check

%files
%defattr(-,root,root,-)
%doc README LICENSE
%{_bindir}/sha1hmac
%{_bindir}/sha256hmac
%{_bindir}/sha384hmac
%{_bindir}/sha512hmac
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/sha1hmac.hmac
%{_libdir}/%{name}/sha256hmac.hmac
%{_libdir}/%{name}/sha384hmac.hmac
%{_libdir}/%{name}/sha512hmac.hmac
%{_mandir}/*/*

%changelog
