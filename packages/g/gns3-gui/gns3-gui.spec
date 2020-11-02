#
# spec file for package gns3-gui
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


%if %{undefined suse_version}
# get python versions
%global py3_ver %(if [ -f "python3" ]; then python3 -c "import sys; sys.stdout.write(sys.version[:3])"; else echo 0; fi;)
%endif
Name:           gns3-gui
Version:        2.2.14
Release:        0
Summary:        GNS3 graphical interface for the GNS3 server
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            http://github.com/GNS3/%{name}
Source:         https://github.com/GNS3/gns3-gui/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}_fix_desktop_file.patch
Patch1:         gns3-gui-fix-requirements.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1500
Requires:       python3-jsonschema >= 3.2.0
%else
Requires:       python3-jsonschema < 3
Requires:       python3-jsonschema >= 2.4.0
%endif
Requires:       python3-psutil >= 2.2.1
Requires:       python3-qt5
Requires:       python3-sentry-sdk >= 0.14.4
Requires:       python3-sip

BuildArch:      noarch
# SECTION test requirements
#BuildRequires:  python3-jsonschema >= 2.4.0
#BuildRequires:  python3-jsonschema < 3
#BuildRequires:  python3-psutil >= 2.2.1
#BuildRequires:  python3-raven >= 5.23.0
#BuildRequires:  %%{python_module tox}
# /SECTION

%description
GNS3 is an excellent complementary tool to real labs for network engineers,
administrators and people wanting to study for certifications such as Cisco
CCNA, CCNP, CCIP and CCIE as well as Juniper JNCIA, JNCIS and JNCIE.

It can also be used to experiment features of Cisco IOS, Juniper JunOS or to
check configurations that need to be deployed later on real routers.

Thanks to VirtualBox integration, now even system engineers and administrators
can take advantage of GNS3 to study Redhat (RHCE, RHCT), Microsoft (MSCE,
MSCA), Novell (CLP) and many other vendor certifications.

%prep
%autosetup -p1
find . -type f -name "*\.py" -exec sed -i 's/^#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/' {} \;
find . -type f -name "*\.py" -exec sed -i 's/^#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' {} \;

%build
%if 0%{?suse_version} > 1315
%python3_build
%else
python3 setup.py build
%endif

%install
%if 0%{?suse_version} > 1315
%python3_install
%else
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
%endif

rm %{buildroot}/%{python3_sitelib}/gns3/static/.keep
#
find %{buildroot}/%{python3_sitelib}/gns3 -name "*.ui" -exec chmod -x {} \;
find %{buildroot}/%{python3_sitelib}/gns3  -type f -name "*\.py" -exec grep -Hl python3 {} \; | xargs chmod +x
find %{buildroot}/%{python3_sitelib}/gns3  -name "*.svg" -exec chmod -x {} \;
#
install -D -m0644 %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/gns3.appdata.xml
%fdupes %{buildroot}

%post
%{_bindir}/update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
%{_bindir}/update-desktop-database

%postun
%{_bindir}/update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
%{_bindir}/update-desktop-database

%files
%license LICENSE
%doc AUTHORS README.rst
%{_bindir}/gns3
%{python3_sitelib}/gns3*
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/gns3.desktop
%{_datadir}/mime/packages/gns3-gui.xml
%{_datadir}/appdata/gns3.appdata.xml

%changelog
