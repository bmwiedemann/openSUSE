#
# spec file for package gperf
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


Name:           gperf
Version:        3.1
Release:        0
Summary:        A Compiler Tool for Generating Perfect Hash Functions
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Url:            https://gnu.org/software/gperf/
Source0:        https://ftp.gnu.org/pub/gnu/gperf/gperf-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/gperf/gperf-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Patch0:         testsuite-race.patch
BuildRequires:  gcc-c++
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
A perfect hash function is simply: a hash function and a data structure
that allows recognition of a key word in a set of words using exactly
one probe into the data structure.

%prep
%setup -q
%patch0 -p1

%build
%configure	\
	--htmldir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
rm -f %{buildroot}%{_prefix}/doc/gperf/gperf.html
rm -f %{buildroot}%{_datadir}/doc/gperf/gperf.html

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%defattr (-,root,root)
%doc README NEWS AUTHORS COPYING ChangeLog doc/*.html
%{_bindir}/gperf
%{_infodir}/gperf.info%{ext_info}
%{_mandir}/man1/gperf.1%{ext_man}

%changelog
