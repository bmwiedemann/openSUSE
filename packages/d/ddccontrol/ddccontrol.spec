#
# spec file for package ddccontrol
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ddccontrol
URL:            http://ddccontrol.sourceforge.net/
Version:        0.4.2+20140105+git9d89d8c
Release:        0
Summary:        A tool to configure monitor settings via DDC/CI
License:        GPL-2.0-or-later
Group:          Hardware/Other
Recommends:     ddccontrol-db
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
Source2:        90-ddccontrol-i2c.rules
Patch50:        0002_cerrors.patch
Patch51:        gcc10.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  tidy
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.4
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang = %version

%description
ddccontrol allows to change monitor settings, such as brightness and
contrast, without using the monitor's hardware buttons.


%lang_package


%package gtk
Summary:        A GTK+2 front-end for ddccontrol
Group:          Hardware/Other

%description gtk
This is a graphical tool to configure monitor settings such as brightness
and contrast via DDC/CI. It is based on ddccontrol.


%package -n libddccontrol0
Summary:        Back-end library for ddccontrol
Group:          Hardware/Other
Requires:       ddccontrol-db
Requires:       udev

%description -n libddccontrol0
The back-end library enabling DDC/CI access in ddccontrol/gddccontrol.


%package devel
Summary:        Development files for libddcontrol
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libddccontrol0 = %{version}

%description devel
ddccontrol allows to change monitor settings, such as brightness and
contrast, without using the monitor's hardware buttons.


%package doc
Summary:        Documentation for ddccontrol
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This is the HTML documentation for ddccontrol.


%prep
%setup -q
%patch50 -p1
%patch51 -p1

%build
./autogen.sh
%configure --disable-static \
           --enable-doc \
           --enable-gnome \
           --disable-gnome-panel \
           --disable-ddcpci
make %{?_smp_mflags} htmldir=%{_docdir}/%{name}/html

%install
make install DESTDIR=%buildroot htmldir=%{_docdir}/%{name}/html
%find_lang %{name}
%suse_update_desktop_file -r gddccontrol GTK Settings HardwareSettings
mkdir -p $RPM_BUILD_ROOT%{_udevrulesdir}/
cp -a %{_sourcedir}/90-ddccontrol-i2c.rules %buildroot/%{_udevrulesdir}/
rm -f %buildroot/%_libdir/*.la

%files
%defattr(-,root,root)
%{_bindir}/ddccontrol
%doc %{_mandir}/man1/ddccontrol.1.gz
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%exclude %{_docdir}/%{name}/html

%files gtk
%defattr(-,root,root)
%{_bindir}/gddccontrol
%{_datadir}/applications/gddccontrol.desktop
%{_datadir}/icons/hicolor/48x48/apps/gddccontrol.png
%dir %{_datadir}/icons/Bluecurve
%dir %{_datadir}/icons/Bluecurve/48x48
%dir %{_datadir}/icons/Bluecurve/48x48/apps
%{_datadir}/icons/Bluecurve/48x48/apps/gddccontrol.png
%doc %{_mandir}/man1/gddccontrol.1.gz

%files -n libddccontrol0
%defattr(-,root,root)
%{_libdir}/libddccontrol.so.0
%{_libdir}/libddccontrol.so.0.0.0
%{_udevrulesdir}/90-ddccontrol-i2c.rules

%files devel
%defattr(-,root,root)
%{_includedir}/ddccontrol
%{_libdir}/libddccontrol.so
%{_libdir}/pkgconfig/ddccontrol.pc

%files doc
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

%files lang -f ddccontrol.lang
%defattr(-,root,root)

%post -n libddccontrol0 -p /sbin/ldconfig

%postun -n libddccontrol0 -p /sbin/ldconfig

%changelog
