
%package -n libglycin-2-0
Summary:        Shared library for %{name}

%description -n libglycin-2-0
Sandboxed and extendable image decoding.

This package provides the shared library for %{name}

%package -n typelib-1_0-Gly_2
Summary:        Introspection bindings for %{name}

%description -n typelib-1_0-Gly_2
Sandboxed and extendable image decoding.

This package provides introspection bindings for %{name}

%package devel
Summary:        Development Files for %{name}
Requires:       libglycin-2-0 = %{version}
Requires:       typelib-1_0-Gly_2 = %{version}
Provides:       glycin-loaders-devel = %{version}
Obsoletes:      glycin-loaders-devel = %{version}

%description -n libglycin-devel
Sandboxed and extendable image decoding.

This package provides developments files for %{name}

%prep
%autosetup -p1 -a1 -n %{_name}-%{version}

%build
%meson \
    -Dlibglycin-gtk4=false \
    -Dglycin-thumbnailer=false \
    -Dglycin-loaders=false \
    %{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libglycin-2-0

%files -n libglycin-2-0
%{_libdir}/libglycin-2.so.0

%files -n typelib-1_0-Gly_2
%{_libdir}/girepository-1.0/Gly-2.typelib

%files devel
%dir %{_includedir}/glycin-2
%{_includedir}/glycin-2/glycin.h
%{_libdir}/libglycin-2.so
%{_libdir}/pkgconfig/glycin-2.pc
%{_datadir}/gir-1.0/Gly-2.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/glycin-2.deps
%{_datadir}/vala/vapi/glycin-2.vapi

