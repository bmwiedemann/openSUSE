#
# spec file for package libirman
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with     lirc_plugin
%define         sover 0
Name:           libirman
Version:        0.5.2
Release:        0
Summary:        Library for irman access
License:        GPL-2.0+
Group:          Hardware/Other
Url:            https://sourceforge.net/projects/libirman/
Source0:        https://downloads.sf.net/libirman/libirman-%{version}.tar.gz
BuildRequires:  pkgconfig
%if %{with lirc_plugin}
BuildRequires:  pkgconfig(lirc)
%endif

%description
libirman is a general purpose library for programs to use in order to
receive infrared signals via irman-compatible hardware.

%package -n %{name}%{sover}
Summary:        Library for irman access
License:        LGPL-2.0+
Group:          System/Libraries
Requires:       %{name}-common = %{version}

%description -n %{name}%{sover}
libirman is a general purpose library for programs to use in order to
receive infrared signals via irman-compatible hardware.

%package -n irman-common
Summary:        Common files for %{name}
License:        LGPL-2.0+
Group:          Development/Languages/C and C++
Conflicts:      %{name}%{sover} < %{version}
Provides:       libirman-common = %{version}-%{release}
Obsoletes:      libirman-common < %{version}-%{release}

%description -n irman-common
Common files for %{name}.

%package -n irman-utils
Summary:        Library for irman access
License:        GPL-2.0+
Group:          Hardware/Other
Requires:       irman-common = %{version}
Provides:       libirman-utils = %{version}
Obsoletes:      libirman-utils < %{version}

%description -n irman-utils
Utilities from %{name} from the lirc project.

%if %{with lirc_plugin}
%package -n lirc-irman
Summary:        Lirc plugin for irman
License:        GPL-2.0+
Group:          Hardware/Other
Requires:       irman-common = %{version}

%description -n lirc-irman
Lirc plugin for irman.
%endif

%package devel
Summary:        Development files for %{name}
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
libirman is a general purpose library for programs to use in order to
receive infrared signals via irman-compatible hardware.

Devel files for %{name} from the lirc project.

%prep
%setup -q

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n irman-utils
%defattr(-,root,root)
%doc COPYING
%{_bindir}/test_func
%{_bindir}/test_io
%{_bindir}/test_name
%{_bindir}/workmanir

%files -n %{name}%{sover}
%defattr(-,root,root)
%doc COPYING.lib
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.%{sover}*

%files -n irman-common
%defattr(-,root,root)
%config %{_sysconfdir}/irman.conf

%if %{with lirc_plugin}
%files -n lirc-irman
%defattr(-,root,root)
%dir %{_libdir}/lirc
%dir %{_libdir}/lirc/plugins
%{_libdir}/lirc/plugins/irman.so
%endif

%files devel
%defattr(-,root,root)
%doc COPYING COPYING.lib NEWS README
%defattr(-,root,root,-)
%{_includedir}/irman.h
%{_libdir}/libirman.so
%{_libdir}/pkgconfig/libirman.pc

%changelog
