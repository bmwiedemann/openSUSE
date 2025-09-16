#
# spec file for package pg_rrule
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Dominik George <nik@naturalnet.de>
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


%define         pg_name  @BUILD_FLAVOR@%{nil}
%define         ext_name   pg_rrule
%if "%{pg_name}" == ""
%global main_build 1
%else
%global main_build 0
%{pg_version_from_name}
%endif

%if %{main_build}
Name:           %{ext_name}
ExclusiveArch:      do_not_build
%else
Name:           %{pg_name}-%{ext_name}
BuildRequires:  %{pg_name}-server-devel
%pg_server_requires
%endif
BuildRequires:  libical-devel
Version:        0.2.0+git20211101.d7d10f2
Release:        0
Summary:        RULE data type for PostgreSQL
License:        MIT
Group:          Productivity/Databases/Tools
URL:            https://github.com/petropavel13/pg_rrule
Source:         https://deb.debian.org/debian/pool/main/p/pg-rrule/pg-rrule_0.2.0+git20211101.d7d10f2.orig.tar.gz
Patch0:         https://sources.debian.org/data/main/p/pg-rrule/0.2.0%2Bgit20211101.d7d10f2-3/debian/patches/fix_make_install.patch
Patch1:         https://sources.debian.org/data/main/p/pg-rrule/0.2.0%2Bgit20211101.d7d10f2-3/debian/patches/fix_regress_opts.patch
Patch2:         https://sources.debian.org/data/main/p/pg-rrule/0.2.0%2Bgit20211101.d7d10f2-3/debian/patches/fix_testsuite.patch
Patch3:         https://sources.debian.org/data/main/p/pg-rrule/0.2.0%2Bgit20211101.d7d10f2-3/debian/patches/test-create-extension.patch

%description
pg-rrule can expand recurrence rules (RRULE) as defined in the
iCalendar specification (RFC 5545). It allows expanding RRULEs
into concrete occurences as timestamps, which can then be queried
against.

%prep
%autosetup -p1 -n %{ext_name}-master

%build
%make_pgxs

%install
%make_install
rm -rv %{buildroot}/usr/share/doc/

%files
%license LICENSE
%doc README.md 
%{pg_config_pkglibdir}/pg_rrule*.so
%{pg_config_sharedir}/extension/pg_rrule*

%changelog

