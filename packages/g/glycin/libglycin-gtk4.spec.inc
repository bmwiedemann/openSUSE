
%package -n libglycin-gtk4-2-0
Summary:        Shared library for %{name}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk4)

%description -n libglycin-gtk4-2-0
Sandboxed and extendable image decoding.

This package provides the shared library for %{name}

%package -n typelib-1_0-GlyGtk-2
Summary:        Introspection bindings for %{name}

%description -n typelib-1_0-GlyGtk-2

%package devel
Summary:        Development Files for %{name}
Requires:       libglycin-gtk4-2-0 = %{version}
Requires:       typelib-1_0-GlyGtk-2 = %{version}

%description devel
Sandboxed and extendable image decoding.

This package provides developments files for %{name}

%prep
%autosetup -p1 -a1 -n %{_name}-%{version}

%build
%meson \
    -Dlibglycin-gtk4=true \
    -Dlibglycin=false \
    -Dglycin-thumbnailer=false \
    -Dglycin-loaders=false \
    %{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libglycin-gtk4-2-0

%files -n libglycin-gtk4-2-0
%{_libdir}/libglycin-gtk4-2.so.0

%files -n typelib-1_0-GlyGtk-2
%{_libdir}/girepository-1.0/GlyGtk4-2.typelib

%files devel
%{_includedir}/glycin-gtk4-2/
%{_libdir}/libglycin-gtk4-2.so
%{_libdir}/pkgconfig/glycin-gtk4-2.pc
%{_datadir}/gir-1.0/GlyGtk4-2.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/glycin-gtk4-2.deps
%{_datadir}/vala/vapi/glycin-gtk4-2.vapi

%changelog
