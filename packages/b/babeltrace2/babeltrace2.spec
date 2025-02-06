#
# spec file for package babeltrace2
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


%define soname  libbabeltrace2
%define sover   0
Name:           babeltrace2
Version:        2.1.0
Release:        0
Summary:        Common Trace Format Babel Tower
License:        GPL-2.0-only AND MIT
URL:            https://babeltrace.org/
Source:         https://efficios.com/files/babeltrace/%{name}-%{version}.tar.bz2
Source1:        https://efficios.com/files/babeltrace/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdw) >= 0.154
BuildRequires:  pkgconfig(libelf) >= 0.154
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(uuid)
ExclusiveArch:  %ix86 x86_64 aarch64 ppc64le ppc64 riscv64 s390x

%description
This project provides trace read and write libraries, as well as a
trace converter. A plugin can be created for any trace format to
allow its conversion to/from another trace format.

The main format expected to be converted to/from is the
Common Trace Format (CTF).

%package -n python3-%{name}
Summary:        Python Bindings for babeltrace2

%description -n python3-%{name}
This project provides trace read and write libraries, as well as a
trace converter. A plugin can be created for any trace format to
allow its conversion to/from another trace format.

Python Bindings for the babeltrace2 package.

%package -n %{name}-devel
Summary:        Common Trace Format Babel Tower
Requires:       %{name} = %{version}

%description -n %{name}-devel
This project provides trace read and write libraries, as well as a
trace converter. A plugin can be created for any trace format to
allow its conversion to/from another trace format.

The main format expected to be converted to/from is the
Common Trace Format (CTF).

%prep
%setup -q

%build
export PYTHON="python3"
export PYTHON_CONFIG="$PYTHON-config"
%configure \
  --disable-static            \
  --disable-Werror            \
  --docdir=%{_docdir}/%{name} \
  --enable-python-bindings
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Remove licences from doc.
rm %{buildroot}%{_docdir}/%{name}/LICENSE

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc %{_docdir}/%{name}/
%license LICENSE LICENSES/*
%{_bindir}/%{name}*
%{_libdir}/%{name}/
%{_libdir}/%{soname}*.so.%{sover}*
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man7/*.7%{?ext_man}

%files -n python3-%{name}
%{python3_sitearch}/bt2/
%{python3_sitearch}/bt2-*

%files -n %{name}-devel
%{_includedir}/%{name}/
%{_includedir}/%{name}-ctf-writer/
%{_libdir}/%{soname}*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-ctf-writer.pc

%changelog
