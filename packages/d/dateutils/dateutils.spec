#
# spec file for package dateutils
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dateutils
Version:        0.4.6
Release:        0
Summary:        Command line date and time utilities
License:        BSD-3-Clause
Group:          Productivity/Text/Utilities
URL:            https://github.com/hroptatyr/dateutils/
Source0:        https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.asc
BuildRequires:  octave-devel
BuildRequires:  pkgconfig
BuildRequires:  timezone
Requires(post): info
Requires(pre):  info

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
%setup -q

%build
%configure \
  --enable-contrib
make %{?_smp_mflags} V=1

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/dateutils
rm -rf %{buildroot}%{_libdir}/octave/site/oct/*/dateutils/tzconv.la

%check
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info*

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info*

%files
%license LICENSE
%doc README.md
%{_bindir}/dadd
%{_bindir}/dconv
%{_bindir}/ddiff
%{_bindir}/dgrep
%{_bindir}/dround
%{_bindir}/dseq
%{_bindir}/dsort
%{_bindir}/dtest
%{_bindir}/dzone
%{_bindir}/dateadd
%{_bindir}/dateconv
%{_bindir}/datediff
%{_bindir}/dategrep
%{_bindir}/dateround
%{_bindir}/dateseq
%{_bindir}/datesort
%{_bindir}/datetest
%{_bindir}/datezone
%{_bindir}/strptime
%dir %{_datadir}/dateutils/
%{_datadir}/dateutils/locale
%{_datadir}/dateutils/*.tzmcc
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/dadd.1%{?ext_man}
%{_mandir}/man1/dconv.1%{?ext_man}
%{_mandir}/man1/ddiff.1%{?ext_man}
%{_mandir}/man1/dgrep.1%{?ext_man}
%{_mandir}/man1/dround.1%{?ext_man}
%{_mandir}/man1/dseq.1%{?ext_man}
%{_mandir}/man1/dsort.1%{?ext_man}
%{_mandir}/man1/dtest.1%{?ext_man}
%{_mandir}/man1/dzone.1%{?ext_man}
%{_mandir}/man1/dateadd.1%{?ext_man}
%{_mandir}/man1/dateconv.1%{?ext_man}
%{_mandir}/man1/datediff.1%{?ext_man}
%{_mandir}/man1/dategrep.1%{?ext_man}
%{_mandir}/man1/dateround.1%{?ext_man}
%{_mandir}/man1/dateseq.1%{?ext_man}
%{_mandir}/man1/datesort.1%{?ext_man}
%{_mandir}/man1/datetest.1%{?ext_man}
%{_mandir}/man1/datezone.1%{?ext_man}
%{_mandir}/man1/strptime.1%{?ext_man}

%files octave
%dir %{_libdir}/octave/site/oct/*/dateutils/
%{_libdir}/octave/site/oct/*/dateutils/tzconv.m
%{_libdir}/octave/site/oct/*/dateutils/tzconv.mex

%changelog
