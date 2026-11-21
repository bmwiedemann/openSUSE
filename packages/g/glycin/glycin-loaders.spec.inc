

%prep
%autosetup -p1 -a1 -n %{_name}-%{version}

%build
%meson \
    -Dlibglycin=false \
    -Dlibglycin-gtk4=false \
    -Dtests=false
%meson_build

%install
%meson_install

%files
%{_bindir}/glycin-thumbnailer
%dir %{_datadir}/glycin-loaders
%dir %{_datadir}/glycin-loaders/2+
%dir %{_datadir}/glycin-loaders/2+/conf.d
%{_datadir}/glycin-loaders/2+/conf.d/glycin-heif.conf
%{_datadir}/glycin-loaders/2+/conf.d/glycin-image-rs.conf
%{_datadir}/glycin-loaders/2+/conf.d/glycin-jxl.conf
%{_datadir}/glycin-loaders/2+/conf.d/glycin-svg.conf
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/glycin-heif.thumbnailer
%{_datadir}/thumbnailers/glycin-image-rs.thumbnailer
%{_datadir}/thumbnailers/glycin-jxl.thumbnailer
%{_datadir}/thumbnailers/glycin-svg.thumbnailer
%dir %{_libexecdir}/glycin-loaders
%dir %{_libexecdir}/glycin-loaders/2+
%{_libexecdir}/glycin-loaders/2+/glycin-heif
%{_libexecdir}/glycin-loaders/2+/glycin-image-rs
%{_libexecdir}/glycin-loaders/2+/glycin-jxl
%{_libexecdir}/glycin-loaders/2+/glycin-svg

