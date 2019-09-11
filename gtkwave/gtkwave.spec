#
# spec file for package gtkwave
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


Name:           gtkwave
Version:        3.3.101
Release:        0
Summary:        Waveform viewer for Ditital Signals
License:        GPL-2.0+
Group:          Productivity/Scientific/Electronics
Url:            http://gtkwave.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  gtk2-devel
BuildRequires:  judy-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q

%build
%configure \
        --disable-mime-update \
        --enable-judy
make %{?_smp_mflags}

%install
%make_install

install -D -m 644 share/icons/gnome/16x16/mimetypes/gtkwave.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gtkwave.png
install -D -m 644 share/icons/gnome/32x32/mimetypes/gtkwave.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gtkwave.png
install -D -m 644 share/icons/gnome/48x48/mimetypes/gtkwave.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gtkwave.png

%suse_update_desktop_file -i -r %{name} Education Engineering

# non OSI compliant files [bnc#783166]
rm -r %{buildroot}%{_datadir}/%{name}/examples/des*

# move documentation
install -d %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/%{name}/gtkwave.odt %{buildroot}%{_docdir}/%{name}/
# move examples
mv %{buildroot}%{_datadir}/%{name}/examples %{buildroot}%{_docdir}/%{name}/

%fdupes %{buildroot}/%{_datadir}/icons/

%files
%defattr(-,root,root,-)
%doc ChangeLog README COPYING LICENSE.TXT
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
%{_datadir}/mime/packages/x-gtkwave-extension*.xml

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/gtkwave.odt

%files examples
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/examples/

%changelog
