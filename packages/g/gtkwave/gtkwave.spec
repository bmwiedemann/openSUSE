#
# spec file for package gtkwave
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gtkwave
Version:        3.3.126
Release:        0
Summary:        Waveform viewer for Ditital Signals
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://gtkwave.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-gtk3-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  gtk3-devel
BuildRequires:  judy-devel
BuildRequires:  libtirpc-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
Recommends:     %{name}-doc

%description
GTKWave is a waveform viewer that can view VCD files produced by most Verilog
simulation tools, as well as LXT files produced by certain Verilog simulation
tools.

%package        doc
Summary:        Documentation for GTKWave
Group:          Documentation/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    doc
GTKWave is a waveform viewer that can view VCD files produced by most Verilog
simulation tools, as well as LXT files produced by certain Verilog simulation
tools.

This package contains documentation for GTKWave

%package        examples
Summary:        Examples for GTKWave
Group:          Documentation/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    examples
GTKWave is a waveform viewer that can view VCD files produced by most Verilog
simulation tools, as well as LXT files produced by certain Verilog simulation
tools.

This package contains examples for GTKWave

%prep
%setup -q -n %{name}-gtk3-%{version}

%build
%configure \
        --disable-mime-update \
        --enable-gtk3 \
        --enable-judy \
        --with-gsettings \
        --with-tirpc
%make_build

%install
%make_install

install -D -m 644 share/icons/gnome/16x16/mimetypes/gtkwave.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gtkwave.png
install -D -m 644 share/icons/gnome/32x32/mimetypes/gtkwave.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gtkwave.png
install -D -m 644 share/icons/gnome/48x48/mimetypes/gtkwave.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gtkwave.png

# move documentation
install -d %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/%{name}-gtk3/gtkwave.odt %{buildroot}%{_docdir}/%{name}/
# move examples
mv %{buildroot}%{_datadir}/%{name}-gtk3/examples %{buildroot}%{_docdir}/%{name}/

%fdupes %{buildroot}/%{_datadir}/icons/

%files
%license COPYING LICENSE.TXT
%doc ChangeLog README.md
%exclude %{_docdir}/%{name}/gtkwave.odt
%exclude %{_docdir}/%{name}/examples/
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/gnome/
%dir %{_datadir}/icons/gnome/*x*/
%dir %{_datadir}/icons/gnome/*/mimetypes/
%{_datadir}/icons/gnome/*/mimetypes/*.png
%{_datadir}/icons/gtkwave*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/glib-2.0/schemas/com.geda.gtkwave.gschema.xml
%{_datadir}/mime/packages/x-gtkwave-extension*.xml

%files doc
%doc %{_docdir}/%{name}/gtkwave.odt

%files examples
%doc %{_docdir}/%{name}/examples/

%changelog
