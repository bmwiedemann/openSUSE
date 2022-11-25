#
# spec file for package rt-tests
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


Name:           rt-tests
Version:        2.4
Release:        0
Summary:        Realtime Kernel Testsuite
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git
Source0:        https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git/snapshot/rt-tests-%{version}.tar.gz
Patch1:         0001-cyclictest-Fix-threads-being-affined-even-when-a-isn.patch
Patch2:         0002-rt-tests-Remove-arbitrary-num-of-threads-limits.patch
Patch3:         0003-rt-tests-hackbench-Add-error-checking-to-connect-and.patch
Patch4:         0004-rt-tests-hwlatdetect-Update-to-integer-division.patch
BuildRequires:  libnuma-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
Conflicts:      hackbench

%description
The Realtime Kernel Testsuite measures real-time attributes of the kernel,
specifically timer and signal latency and the functionality of Priority
Inheritance Mutexes.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%make_build

%install
%make_install prefix=%{_prefix}
rm -rf %{buildroot}%{_prefix}/src/backfire

%files
%license COPYING
%doc MAINTAINERS README.markdown
%{_bindir}/cyclicdeadline
%{_bindir}/cyclictest
%{_bindir}/get_cyclictest_snapshot
%{_bindir}/deadline_test
%{_bindir}/hackbench
%{_bindir}/hwlatdetect
%{_bindir}/pi_stress
%{_bindir}/pip_stress
%{_bindir}/pmqtest
%{_bindir}/ptsematest
%{_bindir}/queuelat
%{_bindir}/rt-migrate-test
%{_bindir}/signaltest
%{_bindir}/sigwaittest
%{_bindir}/svsematest
%{_bindir}/ssdd
%{_bindir}/oslat
%{_bindir}/determine_maximum_mpps.sh
%{python3_sitelib}/hwlatdetect.py
%{python3_sitelib}/get_cyclictest_snapshot.py
%{_mandir}/man8/cyclictest.8%{?ext_man}
%{_mandir}/man8/hackbench.8%{?ext_man}
%{_mandir}/man8/hwlatdetect.8%{?ext_man}
%{_mandir}/man8/pi_stress.8%{?ext_man}
%{_mandir}/man8/pmqtest.8%{?ext_man}
%{_mandir}/man8/ptsematest.8%{?ext_man}
%{_mandir}/man8/rt-migrate-test.8%{?ext_man}
%{_mandir}/man8/signaltest.8%{?ext_man}
%{_mandir}/man8/sigwaittest.8%{?ext_man}
%{_mandir}/man8/svsematest.8%{?ext_man}
%{_mandir}/man8/ssdd.8%{?ext_man}
%{_mandir}/man8/queuelat.8%{?ext_man}
%{_mandir}/man8/pip_stress.8%{?ext_man}
%{_mandir}/man8/deadline_test.8%{?ext_man}
%{_mandir}/man8/cyclicdeadline.8%{?ext_man}
%{_mandir}/man8/get_cyclictest_snapshot.8%{?ext_man}
%{_mandir}/man8/oslat.8%{?ext_man}
%{_mandir}/man8/determine_maximum_mpps.8%{?ext_man}

%changelog
