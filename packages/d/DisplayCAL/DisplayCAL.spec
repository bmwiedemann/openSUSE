#
# spec file for package DisplayCAL (SUSE based distributions only)
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Florian Hoech
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


%define numpy_version 1.0
%define py_minversion 2.6
%define py_maxversion 2.7
%define wx_minversion 3.0

%define __python /usr/bin/python2

%global debug_package %{nil}

Summary:        Display calibration and profiling with a focus on accuracy and versatility
License:        GPL-3.0+
Group:          Productivity/Graphics/Other
Name:           DisplayCAL
Version:        3.8.7.1
Release:        0
Source0:        http://displaycal.net/download/%{name}-%version.tar.gz
Url:            https://displaycal.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Obsoletes:      DisplayCAL-0install
Provides:       dispcalGUI = %{version}
Obsoletes:      dispcalGUI < 3.1.0.0
Obsoletes:      dispcalGUI-0install < 3.1.0.0
BuildRequires:  gcc
BuildRequires:  python-devel
BuildRequires:  udev
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  python-xml
Requires:       argyllcms
Requires:       python2-numpy >= %{numpy_version}
Requires:       libSDL2_mixer-2_0-0
Requires:       python2-wxWidgets >= %{wx_minversion}
Requires:       python2-psutil
Requires:       python2-gobject
Requires:       python2-xml
%py_requires

%description
This utility calibrates and characterizes display devices using one
of many supported measurement instruments, with support for
multi-display setups and a variety of available options for advanced
users, such as verification and reporting functionality to evaluate
ICC profiles and display devices, creating video 3D LUTs, as well as
optional CIECAM02 gamut mapping to take into account varying viewing
conditions.

%prep
%setup
# Convert line endings in LICENSE.txt
%{__python} -c "f = open('LICENSE.txt', 'rb')
d = f.read().replace('\r\n', '\n').replace('\r', '\n')
f.close()
f = open('LICENSE.txt', 'wb')
f.write(d)
f.close()"

%build
%{__python} setup.py build --use-distutils

%install
install_lib=`%{__python} -c "from distutils.sysconfig import get_python_lib;print get_python_lib(True)"`
%{__python} setup.py install --use-distutils \
	--root=$RPM_BUILD_ROOT \
	--prefix=%_prefix \
	--exec-prefix=%_exec_prefix \
	--install-data=%_datadir \
    --install-lib=${install_lib} \
	--skip-instrument-configuration-files \
	--skip-postinstall \
	--record=INSTALLED_FILES

# Strip extensions
bits=`%{__python} -c "import platform;print platform.architecture()[0][:2]"`
python_shortversion=`%{__python} -c "import sys;print ''.join(map(str, sys.version_info[:2]))"`
strip --strip-unneeded %{buildroot}/${install_lib}/%{name}/lib${bits}/python${python_shortversion}/*.so

# Remove doc directory
if [ -e "%{buildroot}/%{_datadir}/doc/%{name}-%{version}" ]; then
	rm -rf "%{buildroot}/%{_datadir}/doc/%{name}-%{version}"
fi

# Update desktop files to prevent buildservice from complaining
desktopfilenames=`%{__python} -c "import glob
import os
print ' '.join([os.path.splitext(os.path.basename(path))[0] for path in
				glob.glob('misc/displaycal*.desktop')])"`
for desktopfilename in $desktopfilenames ; do
	%suse_update_desktop_file $desktopfilename 2DGraphics
done
%suse_update_desktop_file "%{buildroot}/etc/xdg/autostart/z-displaycal-apply-profiles.desktop"

# Prepare files list:
# - Remove traces of RPM_BUILD_ROOT
# - Remove unused files from list of installed files and add directories
#   as well as mark files as executable where needed
%{__python} -c "import os
f = open('INSTALLED_FILES')
paths = [chr(0x22) + path.replace('$RPM_BUILD_ROOT', '').strip() + chr(0x22) for path in 
		 filter(lambda path: not '/doc/' in path and not '/etc/' in path and
				not '/man/' in path, 
				f.readlines())]
f.close()
executables = ['Argyll'] + os.listdir('scripts')
for path in list(paths):
	path = path.strip(chr(0x22))
	if os.path.basename(path) in executables:
		paths.remove(chr(0x22) + path + chr(0x22))
		paths.append('%attr(755, root, root) ' + chr(0x22) + path + chr(0x22))
	while True:
		path = os.path.dirname(path)
		if os.path.isdir(path):
			break
		else:
			directory = '%dir ' + chr(0x22) + path + chr(0x22)
			if not directory in paths:
				paths.append(directory)
f = open('INSTALLED_FILES', 'w')
f.write('\n'.join(paths))
f.close()"

%files -f INSTALLED_FILES
%defattr(-,root,root)
%config /etc/xdg/autostart/z-displaycal-apply-profiles.desktop
%doc LICENSE.txt
%doc README.html
%doc README-fr.html
%doc screenshots
%doc theme
/usr/share/man/man1/*

%post
#!/bin/sh

# Update icon cache and menu
/bin/touch --no-create %{_datadir}/icons/hicolor >/dev/null 2>/dev/null || true
which xdg-icon-resource >/dev/null 2>/dev/null && xdg-icon-resource forceupdate || true
which xdg-desktop-menu >/dev/null 2>/dev/null && xdg-desktop-menu forceupdate || true

%postun
#!/bin/sh

# Update icon cache and menu
/bin/touch --no-create %{_datadir}/icons/hicolor >/dev/null 2>/dev/null || true
which xdg-desktop-menu >/dev/null 2>/dev/null && xdg-desktop-menu forceupdate || true
which xdg-icon-resource >/dev/null 2>/dev/null && xdg-icon-resource forceupdate || true

%changelog
