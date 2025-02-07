#
# spec file for package babeltrace
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


%define soname  libbabeltrace
%define sover   1
Name:           babeltrace
Version:        1.5.8
Release:        0
Summary:        Common Trace Format Babel Tower
License:        GPL-2.0-only AND MIT
URL:            https://diamon.org/babeltrace
Source:         https://efficios.com/files/babeltrace/%{name}-%{version}.tar.bz2
Source1:        https://efficios.com/files/babeltrace/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  python3-setuptools
BuildRequires:  swig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdw) >= 0.154
BuildRequires:  pkgconfig(libelf) >= 0.154
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(uuid)
ExcludeArch:    s390 ppc

%description
This project provides trace read and write libraries, as well as a
trace converter. A plugin can be created for any trace format to
allow its conversion to/from another trace format.

The main format expected to be converted to/from is the
Common Trace Format (CTF).

%package -n python3-%{name}
Summary:        Python Bindings for babeltrace

%description -n python3-%{name}
This project provides trace read and write libraries, as well as a
trace converter. A plugin can be created for any trace format to
allow its conversion to/from another trace format.

Python Bindings for the babeltrace package.

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
  --docdir=%{_docdir}/%{name} \
  --enable-python-bindings
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Remove licences from doc.
rm %{buildroot}%{_docdir}/%{name}/{LICENSE,mit-license.txt,gpl-2.0.txt}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc %{_docdir}/%{name}/
%license LICENSE mit-license.txt gpl-2.0.txt
%{_bindir}/%{name}*
%{_libdir}/%{soname}*.so.%{sover}*
%{_mandir}/man1/*.1%{?ext_man}

%files -n python3-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-*

%files -n %{name}-devel
%{_includedir}/%{name}/
%{_libdir}/%{soname}*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-ctf.pc

%changelog
