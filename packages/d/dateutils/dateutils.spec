#
# spec file for package dateutils
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


Name:           dateutils
Version:        0.4.10
Release:        0
Summary:        Command line date and time utilities
License:        BSD-3-Clause
Group:          Productivity/Text/Utilities
URL:            https://github.com/hroptatyr/dateutils/
Source0:        https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.asc
Source2:        %{name}.keyring
Patch0:         https://github.com/hroptatyr/dateutils/commit/841c635b.patch
Patch1:         https://github.com/hroptatyr/dateutils/commit/35041f4d.patch
BuildRequires:  octave-devel
BuildRequires:  pkgconfig
BuildRequires:  timezone

%description
Dateutils are a bunch of tools that revolve around fiddling with dates
and times in the command line with a strong focus on use cases that
arise when dealing with large amounts of financial data. Their target
market is shell scripts that need date calculations or calendar
conversions, and as such they are highly pipe-able and modeled after
their well-known cousins (e.g. dtest vs. test, or dgrep vs. grep).

%package octave
Summary:        Dateutils functions for matlab and octave
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       octave

%description octave
Dateutils can be used from within matlab or ocatave.

%prep
%autosetup -p1

%build
%configure \
  --enable-contrib
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/dateutils
rm -rf %{buildroot}%{_libdir}/octave/site/oct/*/dateutils/tzconv.la

%check
%make_build check

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/dateutils/
%{_mandir}/man1/*
%{_infodir}/%{name}.info%{?ext_info}

%files octave
%dir %{_libdir}/octave/site/oct/*/dateutils/
%{_libdir}/octave/site/oct/*/dateutils/tzconv.m
%{_libdir}/octave/site/oct/*/dateutils/tzconv.mex

%changelog
