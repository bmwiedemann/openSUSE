#
# spec file for package gns3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if %{undefined suse_version}

# get python versions
%global py3_ver %(if [ -f "%{__python3}" ]; then %{__python3} -c "import sys; sys.stdout.write(sys.version[:3])"; else echo 0; fi;)

%endif

Name:           gns3
Summary:        A graphical network simulator
License:        GPL-3.0+
Group:          Productivity/Networking/Other
Version:        2.0.3
Release:        0
Url:            http://www.gns3.net/
Source0:        %{name}-gui-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.xml
Source3:        %{name}.desktop
Source4:        application-x-%{name}.png
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel >= 3.3
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
%if %{defined suse_version}
BuildRequires:  update-desktop-files
%endif
Requires:       gns3-server = %{version}
Requires:       python3-configobj
Requires:       python3-jsonschema >= 2.4.0
Requires:       python3-psutil >= 3.0.0
Requires:       python3-qt5
Requires:       python3-raven >= 5.2.0
Requires:       python3-sip
Provides:       gns3-gui > %{version}
Obsoletes:      gns3-gui <= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GNS3 is a excellent complementary tool to real labs for administrators
of Cisco networks or people wanting to pass their CCNA,
CCNP, CCIP or CCIE certifications.

It can also be used to experiment features of Cisco IOS or to check configurations
that need to be deployed later on real routers.

Important notice: users must provide their own Cisco IOS to use GNS3.

%prep
%setup -q -n %{name}-gui-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
%__rm %{buildroot}/%{python3_sitelib}/%{name}/static/.keep
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/registry/registry.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/symbol.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/items/utils.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/main.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/local_server.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/utils/export_project_worker.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/utils/sudo.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/items/drawing_item.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/compute.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/utils/import_project_worker.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/dialogs/vm_with_images_wizard.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/application.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/controller.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/registry/config.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/dialogs/appliance_wizard.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/utils/__init__.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/compute_manager.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/utils/server_select.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/qt/qimage_svg_renderer.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/registry/appliance.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/__main__.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/logger.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/utils/http.py
chmod +x %{buildroot}/%{python3_sitelib}/%{name}/update_manager.py
find %{buildroot}/%{python3_sitelib}/%{name} -name "*.ui" -exec chmod -x {} \;

mkdir -p %buildroot/%{_datadir}/pixmaps
mkdir -p %buildroot/%{_datadir}/mime/packages
mkdir -p %buildroot/%{_datadir}/applications
mkdir -p %buildroot/%{_datadir}/icons/hicolor/48x48/mimetypes
%__cp %SOURCE1 %buildroot/%{_datadir}/pixmaps
%__cp %SOURCE2 %buildroot/%{_datadir}/mime/packages/
%__cp %SOURCE3 %buildroot/%{_datadir}/applications/
%__cp %SOURCE4 %buildroot/%{_datadir}/icons/hicolor/48x48/mimetypes/
rm -rf %{buildroot}/%{python3_sitelib}/tests

%post
/usr/bin/update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
/usr/bin/update-desktop-database

%postun
/usr/bin/update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
/usr/bin/update-desktop-database

%files
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE README.rst
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/mimetypes
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}_gui-%{version}-py%{py3_ver}.egg-info

%changelog
