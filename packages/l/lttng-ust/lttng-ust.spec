#
# spec file for package lttng-ust
#
# Copyright (c) 2025 SUSE LLC
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


%define sover   1
%define sover_ctl 5
Name:           lttng-ust
Version:        2.13.6
Release:        0
Summary:        Linux Trace Toolkit Userspace Tracer library
License:        GPL-2.0-only
Group:          Development/Languages/C and C++
URL:            https://lttng.org/
Source:         https://lttng.org/files/lttng-ust/lttng-ust-%{version}.tar.bz2
Source1:        https://lttng.org/files/lttng-ust/lttng-ust-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  libnuma-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(liburcu) >= 0.12
BuildRequires:  pkgconfig(uuid)
ExclusiveArch:  %ix86 x86_64 armv7l aarch64 riscv64 ppc64 ppc64le

%description
This library may be used by user space applications to generate
tracepoints within the kernel LTT subsystem.

%package -n liblttng-ust%{sover}
Summary:        Linux Trace Toolkit Userspace Tracer library
Group:          System/Libraries

%description -n liblttng-ust%{sover}
This library may be used by user space applications to generate
tracepoints within the kernel LTT subsystem.

%package -n liblttng-ust-ctl%{sover_ctl}
Summary:        Linux Trace Toolkit Userspace Tracer library
Group:          System/Libraries

%description -n liblttng-ust-ctl%{sover_ctl}
This library may be used by user space applications to generate
tracepoints within the kernel LTT subsystem.

%package -n liblttng-ust-python-agent%{sover}
Summary:        Linux Trace Toolkit Userspace Tracer Python agent library
Group:          System/Libraries

%description -n liblttng-ust-python-agent%{sover}
This library may be used by user space applications to generate
tracepoints within the kernel LTT subsystem.

%package -n python3-lttngust
Summary:        Linux Trace Toolkit Userspace Tracer Python 3 agent
Group:          Development/Languages/Python
Requires:       liblttng-ust-python-agent%{sover} = %{version}

%description -n python3-lttngust
This library may be used by user space applications to generate
tracepoints within the kernel LTT subsystem.

This package provides the LLTng-UST Python 3 agent.

%package devel
Summary:        Linux Trace Toolkit Userspace Tracer library
Group:          Development/Languages/C and C++
Requires:       liblttng-ust%{sover} = %{version}
Requires:       liblttng-ust-ctl%{sover_ctl} = %{version}
Requires:       liblttng-ust-python-agent%{sover} = %{version}
Requires:       pkgconfig(liburcu)
# lttng-ust was last used in openSUSE Leap 42.3.
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description devel
This library provides support for developing programs using LTTng
userspace tracing.

%package doc
Summary:        Linux Trace Toolkit Userspace Tracer Documentation
Group:          Documentation/Other
Requires:       liblttng-ust%{sover} = %{version}
Requires:       liblttng-ust-ctl%{sover_ctl} = %{version}
Requires:       liblttng-ust-python-agent%{sover} = %{version}
# lttng-ust-docs was last used in openSUSE Leap 42.3.
Provides:       %{name}-docs = %{version}
Obsoletes:      %{name}-docs < %{version}
BuildArch:      noarch

%description -n %{name}-doc
This package includes documentation and examples for developing
applications using LTTng userspace tracing.

%prep
%autosetup -p1

%build
export PYTHON=python3
%configure \
  --disable-silent-rules \
  --docdir=%{_docdir}/%{name} \
  --disable-static            \
  --disable-maintainer-mode   \
  --enable-python-agent
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%python3_fix_shebang

%post -n liblttng-ust%{sover} -p /sbin/ldconfig

%postun -nliblttng-ust%{sover} -p /sbin/ldconfig

%post -n liblttng-ust-ctl%{sover_ctl} -p /sbin/ldconfig

%postun -nliblttng-ust-ctl%{sover_ctl} -p /sbin/ldconfig

%post -n liblttng-ust-python-agent%{sover} -p /sbin/ldconfig

%postun -n liblttng-ust-python-agent%{sover} -p /sbin/ldconfig

%files -n liblttng-ust%{sover}
%license LICENSE LICENSES/
%{_libdir}/liblttng-ust.so.%{sover}*
%{_libdir}/liblttng-ust-common.so.%{sover}*
%{_libdir}/liblttng-ust-cyg-profile*.so.%{sover}*
%{_libdir}/liblttng-ust-dl.so.%{sover}*
%{_libdir}/liblttng-ust-fd.so.%{sover}*
%{_libdir}/liblttng-ust-fork.so.%{sover}*
%{_libdir}/liblttng-ust-libc-wrapper.so.%{sover}*
%{_libdir}/liblttng-ust-pthread-wrapper.so.%{sover}*
%{_libdir}/liblttng-ust-tracepoint.so.%{sover}*

%files -n liblttng-ust-ctl%{sover_ctl}
%{_libdir}/liblttng-ust-ctl.so.%{sover_ctl}*

%files -n liblttng-ust-python-agent%{sover}
%{_libdir}/liblttng-ust-python-agent.so.%{sover}*

%files -n python3-lttngust
%{python3_sitelib}/lttngust/
%{python3_sitelib}/lttngust-*

%files devel
%{_includedir}/lttng/
%{_bindir}/lttng-gen-tp
%{_mandir}/man1/lttng-gen-tp.1%{?ext_man}
%{_libdir}/liblttng-ust*.so
%{_libdir}/pkgconfig/lttng-ust*.pc

%files doc
%doc %{_docdir}/%{name}/
%{_mandir}/man3/lttng-ust.3%{?ext_man}
%{_mandir}/man3/lttng-ust-cyg-profile.3%{?ext_man}
%{_mandir}/man3/lttng-ust-dl.3%{?ext_man}
%{_mandir}/man3/lttng_ust_do_tracepoint.3%{?ext_man}
%{_mandir}/man3/lttng_ust_tracef.3%{?ext_man}
%{_mandir}/man3/lttng_ust_tracelog.3%{?ext_man}
%{_mandir}/man3/lttng_ust_tracepoint.3%{?ext_man}
%{_mandir}/man3/lttng_ust_tracepoint_enabled.3%{?ext_man}
%{_mandir}/man3/lttng_ust_vtracef.3%{?ext_man}
%{_mandir}/man3/lttng_ust_vtracelog.3%{?ext_man}
%{_mandir}/man3/do_tracepoint.3%{?ext_man}
%{_mandir}/man3/tracef.3%{?ext_man}
%{_mandir}/man3/tracelog.3%{?ext_man}
%{_mandir}/man3/tracepoint.3%{?ext_man}
%{_mandir}/man3/tracepoint_enabled.3%{?ext_man}

%changelog
