#
# spec file for package virtui-manager
#
# Copyright (c) 2026 SUSE LLC
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

%{?!python_module:%define python_module() python3-%{**}}
%define pythons python3

Name:           virtui-manager
Version:        1.9.4
Release:        0
Summary:        Terminal-based interface to manage virtual machines using libvirt
License:        GPL-3.0-or-later
URL:            https://aginies.github.io/virtui-manager/
Source:         %{name}-%{version}.tar.gz
Group: 		System/Monitoring
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
# Runtime dependencies
Requires:       python3-libvirt-python
Requires:       python3-textual >= 0.40.0
Requires:       python3-PyYAML
Requires:       python3-markdown-it-py
BuildArch:      noarch

%description
Virtui-manager is a terminal-based interface to manage virtual machines using libvirt.
It allows you to view VM status, start/stop/pause VMs, and access consoles.

%package doc
Summary:        Documentation for virtui-manager
Group:          Documentation/HTML

%description doc
This package contains the HTML documentation for virtui-manager.

%package -n virtui-remote-viewer
Summary:        Simple remote viewer for virtui-manager
Requires:       %{name} = %{version}
Requires:       python3-gobject
Requires:       python3-libvirt-python
Requires:       gtk3
#Requires:       libgtk-vnc-2_0-0
#Requires:       libvirt-glib-1_0-0
# Spice support (optional but good to have)
Recommends:     typelib(SpiceClientGtk) = 3.0

%description -n virtui-remote-viewer
A simple remote viewer application bundled with virtui-manager.
It supports VNC and SPICE protocols.

%lang_package

%prep
%setup -q

%build
# Compile translations
bash src/vmanager/manage_translation.sh compile-mo
%python3_pyproject_wheel

%install
%python3_pyproject_install
rm %{buildroot}%{python3_sitelib}/vmanager/remote_viewer_gtk4.py
chmod 755 %{buildroot}%{python3_sitelib}/vmanager/remote_viewer.py
chmod 755 %{buildroot}%{python3_sitelib}/vmanager/gui_wrapper.py
chmod 755 %{buildroot}%{python3_sitelib}/vmanager/virtui_dev.py

# Install docs
mkdir -p %{buildroot}%{_docdir}/%{name}/html
if [ -d docs ]; then
    cp -r docs/* %{buildroot}%{_docdir}/%{name}/html/
fi
# Install other docs
cp README.md %{buildroot}%{_docdir}/%{name}/

# Deduplicate files
%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/virtui-manager
%{_bindir}/virtui-manager-cmd
%{_bindir}/virtui-gui
%{python3_sitelib}/vmanager
%exclude %{python3_sitelib}/vmanager/locale
%{python3_sitelib}/virtui_manager-*-info

%files lang -f %{name}.lang
%defattr(-,root,root,-)
%{python3_sitelib}/vmanager/locale

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

%files -n virtui-remote-viewer
%{_bindir}/virtui-remote-viewer

%changelog
