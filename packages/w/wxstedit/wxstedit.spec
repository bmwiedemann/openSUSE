#
# spec file for package wxstedit
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wxstedit
Version:        1.6.0.r3180
Release:        0
Summary:        Sample program for wxWidgets's wxStyledTextCtrl Scintilla wrapper
License:        SUSE-wxWidgets-3.1
Group:          Productivity/Text/Editors
Url:            http://wxcode.sourceforge.net/showcomp.php?name=wxStEdit
Source:         %{name}-%{version}.tar.bz2
Source1:        wxStEdit.desktop
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  cppcheck
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  ImageMagick

%description
wxStEdit is a library and sample program for the wxWidgets's wxStyledTextCtrl
wrapper around the Scintilla text editor widget. It provides a number of
convenience functions and added capabilities, including the necessary
prefs/styles/language management, menu creation and updating, a splitter,
notebook, and frame component. Additionally it provides a find/replace, editor
settings, and property dialogs. It is designed to be easily integrated into a
larger program and while it tries to manage as much as possible, it's fairly
extensible as well. Individual features and &quot;helper&quot; functionality
can be turned off or overridden if desired. The bottom line, this editor
builds upon the wxStyledTextCtrl by adding all the necessary code to ease the
burden of providing a full featured editor or a set of identically styled
editors in a notebook or frame.

%package -n libwxstedit-wx30gtk2u-1_6_0
Summary:        Library for the wxWidgets's Scintilla wrapper
Group:          System/Libraries

%description -n libwxstedit-wx30gtk2u-1_6_0
wxStEdit is a library and sample program for the wxWidgets's wxStyledTextCtrl
wrapper around the Scintilla text editor widget. It provides a number of
convenience functions and added capabilities, including the necessary
prefs/styles/language management, menu creation and updating, a splitter,
notebook, and frame component. Additionally it provides a find/replace, editor
settings, and property dialogs. It is designed to be easily integrated into a
larger program and while it tries to manage as much as possible, it's fairly
extensible as well. Individual features and &quot;helper&quot; functionality
can be turned off or overridden if desired. The bottom line, this editor
builds upon the wxStyledTextCtrl by adding all the necessary code to ease the
burden of providing a full featured editor or a set of identically styled
editors in a notebook or frame.

%package devel
Summary:        Development files of libwxstedit
Group:          Development/Languages/C and C++
Requires:       libwxstedit-wx30gtk2u-1_6_0 = %{version}

%description devel
libwxstedit is a library for the wxWidgets's wxStyledTextCtrl wrapper around
the Scintilla text editor widget.

%prep
%setup -q
sed -r -i 's|LIBRARY DESTINATION .*$|LIBRARY DESTINATION %{_lib}|' \
	CMakeLists.txt

%build
%cmake -DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-config \
	-DBUILD_SHARED_LIBS=TRUE -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags}

%install
%cmake_install

mkdir -p %{buildroot}%{_bindir}
install -p -m 755 build/bin/RelWithDebInfo/wxStEdit %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications/
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

convert -strip art/pencil.ico wxStEdit.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -p -m 644 wxStEdit-1.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/wxStEdit.png

pushd %{buildroot}%{_libdir}/
ln -s libwxstedit*.so libwxStEditLib.so
popd

%post -n libwxstedit-wx30gtk2u-1_6_0 -p /sbin/ldconfig
%postun -n libwxstedit-wx30gtk2u-1_6_0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/wxStEdit
%{_datadir}/wxStEdit/
%{_datadir}/applications/wxStEdit.desktop
%{_datadir}/icons/hicolor/32x32/apps/wxStEdit.png

%files -n libwxstedit-wx30gtk2u-1_6_0
%defattr(-,root,root)
%{_libdir}/libwxstedit-wx30gtk2u-1.6.0.so

%files devel
%defattr(-,root,root)
%dir %{_includedir}/wx/
%{_includedir}/wx/stedit
%{_libdir}/libwxStEditLib.so
%dir %{_datadir}/wxstedit/
%{_datadir}/wxstedit/*.cmake

%changelog
